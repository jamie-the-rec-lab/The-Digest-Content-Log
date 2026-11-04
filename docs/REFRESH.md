# REFRESH: how the library is gathered

Phase 1. What gets gathered is in `config/sources.yaml`. This file is how.

**Where things live.** Every collection sits under `library/`: `library/podcasts`,
`library/tech`, `library/newsletters`, `library/reports`, `library/news`,
`library/adhoc`. Each holds its own `transcripts/` folder, `INDEX.md`,
`TAXONOMY.md` and `episode_summaries.tsv`. Destinations in `config/sources.yaml` are
relative to `library/`.

**Start by clearing last week's working files**, so nothing from the previous
run can be mistaken for this one:

```
: > _state/run-events.jsonl
: > _state/run-report.json
: > _state/publish-report.json
```

The output is the library itself, plus a `run-report.json` that Phase 2 and
Phase 3 both read. Write that file as you go, do not reconstruct it from memory
at the end.

**The scripts record themselves.** `build_index.py` and `fetch_transcripts.py`
write what they did to `_state/run-events.jsonl` as they run: counts, missing
summaries, warnings, what saved, what failed, whether a scan limit was hit. The
health report reads that, so those facts never depend on being written down by
hand.

What still has to be recorded by the agent is what only the agent knows: which
reports came back full, partial or blocked, which launches were featured, and
what the fact-check said.

---

## The rules that apply everywhere

**Every helper that reads a source runs on sonnet.** Not because a smaller model
gets figures wrong, but because it misses the judgement: flagging that a guest is
the vendor behind the product they are praising, attributing a statistic to its
source, knowing the difference between a contrarian take and a comfortable
prediction. See `TOKEN_RULES.md`.

**Heavy reading happens in a helper, never in the main thread.** Transcripts,
emails and reports are long. Hand over the file path or the URL, get back key
points with a quote behind each one. See `TOKEN_RULES.md`.

**One writer at a time per collection.** Each collection has a single shared
`episode_summaries.tsv`. Two helpers appending to it at once corrupts it, so
summarising runs one after another, never in parallel.

**Never invent.** If a source could not be read, say so in the run report. A
gap that is recorded is fine. A gap that is papered over is not.

**A failed fetch does not stop the run.** Note it and carry on. Phase 2 goes
ahead with whatever is genuinely available.

**Each shell call is short-lived.** Long jobs get split into steps. A fetch loop
that gets cut off is rerun rather than abandoned.

---

## The two scripts

**`scripts/fetch_transcripts.py <url> <show name> [destination] [cutoff] [scan limit] [--backfill]`**

Saves any episode not already saved, with a timecoded transcript. Run it again
and it only picks up what is new, so it is safe to rerun until it stops saving.

**Where it gets things (since 4 Nov 2026).** The episode list comes from the
show's official YouTube RSS feed (a `/videos` URL reads the Videos tab only, so
no Shorts; a `/streams` URL reads the Live tab). The transcript comes from
TranscriptAPI. Nothing talks to YouTube's video or caption servers, which
bot-check cloud machines. Each episode ends in one of:

- `saved` / `skip` / `teaser`: as before
- `upcoming`: a scheduled live stream that has not aired. Normal, not logged as a problem
- `pending`: released in the last 12 hours with no captions yet. Captions often
  lag a new upload; it is picked up next week and noted, not counted as a failure
- `failed`: TranscriptAPI had nothing (no captions, or a service error). A
  recorded gap, retried next week
- `gone`: private or removed. Not retried

- destination is relative to `library/` and must be `<collection>/transcripts`
  for one of the six known collections: `podcasts`, `tech`, `newsletters`,
  `reports`, `news`, `adhoc`. So `tech/transcripts`. Defaults to
  `podcasts/transcripts`
- cutoff is a date like `20240101`, only for the shows that carry one
- scan limit is how many of the newest episodes to look at, default 10. The feed
  only ever shows the newest 15, so that is the ceiling
- `--backfill` is accepted but cannot go past 15 in the cloud: a deeper backfill
  needs a different source and is a deliberate job

**The destination is validated, and a bad one stops the run.** Anything that is
not `<collection>/transcripts` is refused: the script exits non-zero, writes no
file, and does not fall back to the default. It records a `bad_destination`
event to `_state/run-events.jsonl` so the health report sees it. This is the
3 September 2026 fault: a show name was passed where the destination belongs,
177 episodes landed at the top of `library/`, `build_index.py` never saw them
because it only walks the six collections, and three episodes went missing from
that week's digest. Passing a bare show name now fails loudly instead.

**The scan limit is capped at 15** (the feed's own length). A request above it,
`all` or `--backfill` is clamped to 15, and the clamp is recorded to
`_state/run-events.jsonl` as `scan_limit_clamped`. Escalating past the ceiling
is a deliberate backfill job, run by hand and on purpose, never part of a
weekly run. On 3 September 2026 a weekly run escalated to 50 and then 100 and
pulled 50 Brainfood and 61 Recruiting Future episodes, most of them months old.

The limit changes only how many episodes are LISTED. Each one is still checked
against what is already saved and skipped if you have it, exactly as before, so
nothing can be fetched twice.

**If the fetch warns that all listed episodes were new**, the list ran out
before reaching the ones you already had, and there may be more beyond it. Rerun
that show with a bigger limit, `50`, or `all --backfill` if 50 is not enough.
This is the one way a scan limit could lose episodes, so never ignore the
warning. It is recorded as `more_beyond_limit`, which is a different thing from
`clamped`: `more_beyond_limit` means episodes may have been missed and the show
needs a rerun; `clamped` means this run asked for more than the ceiling allows
and got 50. Going past the ceiling means dropping out of the weekly run and
doing a backfill deliberately.

**Pause a few seconds between shows.** Nothing here is urgent, it runs in the
background, and running a dozen fetches back to back gets you rate limited. If a
listing does fail, the script waits and retries by itself before giving up.

**Park what fails, then sweep once at the end.** When a source fails, do not
stop and do not keep hammering it. Note it and move to the next one. When every
other source is done, come back and try the parked ones one more time.

By then several minutes have passed, which is the point: the script's own
retries are 20 and 40 seconds apart and all hit the same conditions. A genuine
blip will have cleared by the end of the phase. Anything still failing on the
second sweep is left for next week.

**One exception. Do not sweep a permanent failure.** If the error says "sign in
to confirm you're not a bot", or the video is private, unavailable or
members-only, waiting changes nothing. The script recognises these and stops
retrying by itself. Record it and move on.

**Giving up on a source costs one week, not the episodes.** The digest looks
back 8 weeks, so anything missed this Wednesday is still eligible next
Wednesday and gets picked up then. That is what makes it safe to stop trying. A
run that grinds for an hour on a dead feed costs far more than a source arriving
seven days late.

**"LISTING FAILED" is not "found 0 videos".** The first means the call broke,
almost always temporarily. The second means the source really is empty, which is
a genuine problem. Only the second belongs in the health report as a break.

It also routes trailers, previews and anything under about 700 words into a
`_teasers` folder automatically. Nothing in a folder starting with an underscore
is indexed, summarised or featured, so teasers need no manual handling.

**`build_index.py [collection]`**

Rebuilds the index for a collection and prints what still needs a summary, plus
a CHECK line covering invalid tags, duplicate lines, orphaned entries and
near-duplicate folder names. Run with no argument for the podcasts, or with
`newsletters`, `reports`, `tech`, `news` or `adhoc`.

Aim for zero missing and a clean CHECK. Record any warnings in the run report.

---

## The TSV line

Every item gets one line in its collection's `episode_summaries.tsv`, four
fields separated by three pipes:

```
Folder/file.md|||one-line summary|||Company|||tag, tag, tag
```

- **Path** is `Folder/file.md`, always the library folder name, never a display
  name, and never with a `transcripts/` prefix
- **Company** is the guest, product or show name
- **Tags** are 6 to 10, drawn only from that collection's `TAXONOMY.md`. Prefer
  specific AI tags over a generic umbrella.

---

## Collection 1: recruiting podcasts

Fetch every show in `config/sources.yaml`, rerunning each until nothing new saves.

If a fetch reports "found 0 videos", the feed is probably broken, most likely a
renamed channel or playlist. Record it in the run report.

Then `scripts/build_index.py` to list what needs a summary. Hand that list to one
helper, working through it in order. For each transcript it:

1. Reads the transcript and `TAXONOMY.md`, and appends the TSV line
2. Adds the full written summary to the top of the transcript file, above the
   title, wrapped in `<!--SUMMARY-->` markers, following `docs/SUMMARY_SPEC.md`
   exactly
3. Returns the show, a clean title with episode numbers stripped, the date, the
   guest line from the episode description, and three or four key points, each
   with the verbatim quote it came from

**Key points come from the transcript body, never from the episode
description.** Every file carries a "## Episode description" section near the
top. It is marketing copy: a "what you'll learn" list of topic labels. A key
point built from it describes what an episode is about, which is not the same as
what was said in it, and it cannot carry a real quote because nobody said it.

This is the difference the whole archive exists for. On 27 August a batch of 40
summaries was built this way and had to be thrown away. It is an easy mistake
because the output looks fine.

Those key points are raw material for Phase 2, not finished bullets.

**The summary block is the durable asset.** It is what makes the archive
searchable by what was actually said. Skip a file that already has one, so
reruns never write a second.

Then rebuild the index and confirm it is clean.

---

## Collection 2: newsletters

For each sender in `config/sources.yaml`, search Gmail for messages from the last 14
days. The run is weekly, so 7 days would do, but the extra week costs nothing
and covers a missed run. Anything already saved is skipped. Skip welcome and confirmation emails, keep only real issues.

For anything not already in the library, pull the full thread. The result is
large and gets saved to a file. Note the path and hand it over. Do not read it
in the main thread.

The helper works from the **plain text body only**. It is complete for every one
of these senders, and the HTML version is six to thirteen times larger and is
pure packaging. Only fall back to the HTML if the plain text is nearly empty or
is an obvious "view in browser" stub.

It then strips the header line, the unsubscribe and sponsor boilerplate,
tracking links and email addresses, and writes:

`library/newsletters/transcripts/<Newsletter Name>/<YYYY-MM-DD>-<slug>.md`

with a header carrying the subject, source, date, fetched date, and the public
archive link if the email has one. Ashby Community has no per-issue public link,
so it never gets one.

**Folder names use real spaces, never `%20`.** If the index reports a
URL-encoded near-duplicate folder, move the files into the correct one and
rerun.

It returns the thread id, subject, date, public URL and three or four
quote-backed key points per issue.

---

## Collection 3: reports

Read `library/reports/SOURCES.md`, `library/reports/WATCHLIST.md` and
`library/reports/FORMAT.md` first.
Only take reports published or refreshed in the last 8 weeks, and skip anything
already in the library.

**The inbox comes first.** Anything sitting in `library/reports/_inbox/` gets extracted,
matched to its publisher, written up in full and tagged. A PDF with almost no
extractable text is a scan, so it needs converting to images and reading that
way. If it is a fuller version of a report already held, overwrite the existing
record and mark it complete. Remove it from `library/reports/_TO_GRAB.md`.

The sandbox may refuse to delete the inbox file. Leave it and note it.

**Then find candidates** from three places: the target pages in `SOURCES.md`,
the recurring editions in `WATCHLIST.md`, and the discovery searches. Searching
for titles and dates in the main thread is fine, the results are small.

Apply the quality bar in `library/reports/SOURCES.md` strictly. A credible publisher, a real
stated method and sample, primary research. Not a listicle or a press release
rewrite.

**One report at a time**, each handed to its own helper, which fetches the
source itself, writes the file per `library/reports/FORMAT.md` with a key figures section of
real numbers, appends the TSV line, and returns the figures with their quotes,
the real publish date, and whether it got the whole report or only a public
summary.

- **Complete** means the full report or PDF was captured.
- **Partial** means only a public summary was readable because the full data is
  gated. That is acceptable. Mark it partial and add it to `library/reports/_TO_GRAB.md` so it
  stays on the list to upgrade.
- **Blocked** means even a summary was unreadable. Store nothing. Add the title
  and link to `library/reports/_TO_GRAB.md` for a human to fetch.

Update a watchlist item's last-seen date when a newer edition lands.

---

## Collection 4: tech archive

Fetch the three shows in `config/sources.yaml` into `tech/transcripts`.

These get the same full written summary treatment as everything else, following
`docs/SUMMARY_SPEC.md`. They are kept out of everyday recruiting recall, but the
archive is only worth having if it is searchable by what was said.

Rebuild with `build_index.py tech`, exactly like the core podcasts.

**Do not run `scripts/_retired_build_tech_index.py`.** It rewrites the whole TSV
mechanically from episode descriptions, so it would wipe every real summary and
tag. It was built for when tech was indexed without summaries, and it is now
obsolete.

---

## Collection 5: adhoc

Anything found or sent manually, outside the tracked sources. A one-off report
someone emails over, a podcast episode worth keeping, a newsletter from a
publication not on the list.

Nothing is fetched here. Items are dropped in by hand, into
`library/adhoc/transcripts/Podcasts`, `Reports` or `Newsletters`.

Each run, summarise and tag anything new the same way as everywhere else, then
`build_index.py adhoc`. Adhoc items are eligible for the digest like anything
else, and follow the same two gates in `SELECTION.md`. A report lands in section
3, a podcast in section 1, a newsletter in section 2.

---

## If a run was missed

Most of this heals itself. Just run the job as normal.

- **Podcasts and tech** fetch incrementally, so a missed week means more
  episodes this time. Nothing to do.
- **Reports** look back 8 weeks anyway. Nothing to do.
- **The edition number, the featured log and the archive** all read from files,
  so they carry on from wherever they were.
- **Newsletters** are the one weak point, which is why the search covers 14 days
  rather than 7. Two missed runs in a row would lose issues, so widen the search
  by hand that week.

**A missed week does not mean a double edition.** Publish one edition as
normal, picking the best of a bigger pool. Anything not picked stays eligible,
because only featured items get logged. Quality over volume still holds, and a
catch-up issue that crams two weeks in is exactly the padding the whole thing is
meant to avoid.

---

## Collection 6: product launches

**This is Phase 1's job.** It used to be described as Phase 2's, in a passing
line in the Vendor quirks section below and nowhere else. The result on
10 September 2026 was that neither phase did it: Phase 1 read "not here", Phase 2
never read this document at all, and the edition went out with no product updates
because nobody had looked. A step that lives only in the document belonging to the
phase that does NOT do it is invisible. So it lives here now, with the rest of the
gathering.

Sweep the `vendors:` list in `config/sources.yaml`, tier A first. Use WebFetch on
each vendor's `feed`, falling back to its `backup`. **No browser, ever**: a page
that comes back nearly empty is built by JavaScript, so fall through to a
WebSearch for that vendor's recent releases rather than trying to render it.

Curate hard on the way in. `SELECTION.md` section 5 decides what survives: only a
net-new product, a major AI capability or a notable acquisition, never a minor
tweak, integration or UI change. Most weeks most vendors produce nothing that
qualifies, and that is the normal result, not a failed sweep.

Each candidate comes back with vendor, release name, date, URL, one factual line
and a verbatim quote. **A release whose date you cannot establish from the source
is a gap, not an estimate.** Say so and leave it out.

Launches are not saved to the library on the way in, only when one is actually
featured, per the rule at the end of this document.

---

## Vendor quirks

The quirks for the launch sweep above, one per vendor:

- **Greenhouse**: monthly articles titled "Release Notes"
- **Teamtailor**: a very large page, take only the top dated entries
- **Gem**: use the blog, the "what's new" widget does not load
- **iCIMS**: a seasonal page, a changed release name is the signal
- **Jack & Jill**: no changelog, the blog is the only signal
- **A page that comes back nearly empty** is built by JavaScript. Do not try a
  browser. Fall through to a search instead.

---

## The AI news scan

One or two searches for the week's biggest AI development relevant to a
recruiter. Pick the single item worth their attention, not generic tech news,
and not something already covered by a launch or a report.

If nothing clears the bar, record that and drop the item. Do not force one.

**Save it to the library, like a report.** Once you have picked the item, hand
the URL to a helper and have it write the page into
`library/news/transcripts/<Source>/<YYYY-MM-DD>-<slug>.md`, with the full text
and the source link, then append its TSV line using `library/news/TAXONOMY.md`.

`library/news` is the collection for the weekly AI news item and for any product
launch that gets featured. Source is the vendor or the publication, so
`Greenhouse/` or `EU AI Act/`. Rebuild it with `build_index.py news`.

This is not filing for the sake of it. Everything else in the digest is checked
against a saved file, and anything without one has to be checked against a
summary the main job wrote itself, which only proves the wording matches the
summary. Saving the page removes that special case: the fact-check reads the
same page you read.

**For anything consequential, use two independent sources.** A saved page can
still be out of date. Regulation, legal changes and anything with a date on it
should be confirmed against a second source before it goes in. A single
explainer article is not enough on its own.

Product launches follow the same rule when a release is featured: save the
release note into `library/news`, do not rely on a summary. Launches that were
looked at and not featured are not saved.

---

## What goes in the run report

Written as you go, not reconstructed at the end.

- New items saved, per source
- Any source that returned nothing, or reported "found 0 videos"
- Each report ingested, with complete, partial or blocked
- Index totals and any warnings, per collection
- The key points from every new item, ready for Phase 2
- The AI news item, or a note that there wasn't one
- The launch sweep: **whether it ran at all**, which vendors were read, which
  could not be read, and the material releases found. "No launches this week" and
  "nobody swept" must be different answers in this file. They looked identical in
  the 10 September run and an empty section shipped as though it were a quiet week.
