# The Wednesday Run

This is the map of the weekly digest job. Read this to understand what happens
and in what order. Every detail lives in a separate document, listed against the
step that uses it.

The job runs unattended every Wednesday, in a Claude Code cloud session. It never
sends email and never goes live by itself: it proposes the edition as a preview
and tells Jamie it is ready for review. His merge puts it live.

## Why this exists

There is a lot of rubbish content in the recruiting world. The point of this job
is to be the opposite: one place that reliably delivers high quality, practical,
useful content and cuts through the noise. That is the primary goal, and
everything else serves it.

The library is what makes it possible. Every week the job adds to a growing
archive of what the recruiting world is actually saying, in Jamie's own hands,
searchable and quotable, rather than scattered across podcast apps and inboxes.
That archive feeds client work, workshop material and content long after any
single edition has been forgotten.

The digest is the weekly proof of it. It gives recruiting and talent people
something genuinely worth their time, keeps The Rec Lab visible without Jamie
spending a day on it, and builds the subscriber list.

When there is a judgement call to make, that order settles it. Quality over
volume, every time. A short, honest edition beats a padded one. Never publish
something the archive cannot back up, and never include an item that does not
earn its place.

---

## The short version

1. **Refresh the library.** Pull in the week's new podcasts, newsletters, reports
   and tech episodes. Save them, summarise them, write down what was found.
2. **Build and publish the digest.** Pick the best new items, write the copy,
   fact-check it, propose it as a preview of thereclab.ai/digest.
3. **Save and report back.** Push the week's record to GitHub, then send a health
   check to Slack so Jamie knows what happened and can review the preview.

Each phase writes a small file when it finishes. The next phase reads that file.
That way, if something goes wrong halfway through, the work already done is not
lost and the run can be picked back up.

---

## Phase 1: Refresh the library

**Reads:** `config/sources.yaml` (every podcast, newsletter and vendor we track)
**Follows:** `REFRESH.md` (how each collection works and what to do when it misbehaves)
**Writes:** the new library files, plus `run-report.json`

Four collections get refreshed:

- **Recruiting podcasts.** Fetch new episodes, save the transcripts, write a
  summary of each one into the library.
- **Newsletters.** Pull the week's issues out of Gmail, save each one as a clean
  file, tag it.
- **Reports.** Anything sitting in the inbox folder first, then check the target
  publishers and the watchlist, then a wider search for anything good we missed.
- **Tech archive.** Lenny's, How I AI, AI & I, AI For Humans. Saved and indexed
  automatically,
  kept separate from the recruiting library.

- **Product launches.** Sweep the tracked vendors for genuinely material releases.
  Not saved to the library unless one gets featured, but gathered here with
  everything else.

Then a quick search for the week's biggest AI news story.

**The file it leaves behind (`run-report.json`) records:** how many new items per
source, anything that returned nothing, which reports came back complete versus
partial, whether the launch sweep actually ran, and the key points pulled from
each new item ready for Phase 2.

> This file is new. Right now these counts are held in the agent's head and passed
> along by memory, which is why the Slack report can drift. Writing them down fixes
> that and means Phase 2 can tell the difference between "no new episode this week"
> and "the fetch broke".

---

## Phase 2: Build and publish

**Reads:** `run-report.json`, plus `READER.md` (who this is for)
**Follows:** `SELECTION.md` (which items make the cut), `STYLE.md` (how it is
written), `PUBLISH.md` (getting it live)
**Writes:** the dated digest file, the live page, `publish-report.json`

In order:

1. **Check the template** is intact, then copy it to a new dated file.
2. **Pick the items.** Nothing older than 8 weeks, nothing featured before. A
   source with nothing new simply does not appear. Short weeks are fine.
3. **Write it.** Three bullets per item, five standout picks, a short preview of
   the issue. This is the part that makes the digest worth reading, so it is done
   properly and not rushed.
4. **Fact-check it.** Every number, tool name, date and quote gets checked back
   against the original source by a separate reviewer. Nothing publishes with an
   unresolved error.
5. **Run the checks.** No leftover placeholders, no dashes, correct headings, and
   between one and four sections, because empty ones are dropped rather than
   left showing a heading with nothing under it.
6. **Propose.** Swap the newsletter links to public ones, push to the site's
   `digest-review` branch and open a pull request. Vercel builds a preview in a
   couple of minutes; Jamie's merge puts it live. The edition line on the page reads
   `Version <N> (<Wednesday date>)`, using the Wednesday the job runs, written out
   in full, e.g. `26th August 2026`. The 8 week freshness window and the date in
   the page title both end on that same Wednesday.
7. **Record it.** Bump the edition number, log every item featured so it never
   appears again, save a permanent copy of exactly what was proposed. Next week's
   run checks whether it was merged and undoes the record if not (`PUBLISH.md`
   step 0).

---

## Phase 3: Report back

**Reads:** `run-report.json` and `publish-report.json`
**Follows:** `scripts/health_report.py` (the script that writes and sends the message)
**Writes:** a Slack DM and an email to Jamie, plus a row in `_state/RUN_LOG.tsv` for every problem

The message covers: what went live and the link, what was added to the library
this week, whether every report was reachable, any feed that has gone quiet, and
whether anything needs attention.

It goes to two places. Slack, as a DM. And email, to jamie@thereclab.ai via
Gmail, plain text, with the status in the subject line so it can be read from a
phone without opening it.

Those two use deliberately separate machinery. The subscriber newsletter goes
through Resend, and **this job never touches Resend**. That keeps "this job
cannot email the list" a wall rather than a judgement call: a note to Jamie's
own inbox cannot become a broadcast, because it is not using the thing that
broadcasts.

Then a nudge: the edition is live for review. Every mechanical check has
already passed by this point, so the only thing being asked for is judgement.

Jamie's green light on the page sends the TEST email to his own inboxes
straight away, with no further instruction needed. The broadcast to the list
needs a second, separate green light on that test. See `SEND_NEWSLETTER.md`.

Every problem also gets a row in `_state/RUN_LOG.tsv`, appended and never pruned. The
Slack message is read once and forgotten; the log is what shows a source has
failed six weeks running rather than once. Anything appearing three times gets
fixed properly or written up in `TROUBLESHOOTING.md`.

> This whole phase is mechanical. Given the two files above, there is only one
> correct message. So it should be a script rather than instructions, which makes
> it free to run and impossible to get wrong.

---

## Sending the newsletter

Not part of this job. Ever.

It is human-gated with two approvals: Jamie reads the live page and gives a
green light, a test email then goes to his own inboxes only, and the broadcast
goes out only after he approves that too. No approval of the test means no email
that week, though the site still updates.

The runbook is `SEND_NEWSLETTER.md`.

## What a good run looks like

When the job finishes, all of these should be true. If any is not, something went
wrong and `TROUBLESHOOTING.md` is the next stop.

- The live page shows a new version number and the correct Wednesday date.
- The Slack health report arrived, with a link to the live page.
- Every item featured this week was added to the featured log, so it can never
  appear again.
- The fact-check came back clean, or every problem it found was fixed before
  publishing.
- A copy of exactly what went live was saved to the published archive.
- The library grew: the new items are saved, summarised and indexed with nothing
  missing.
- `python3 scripts/run_check.py` comes back clean. That is the single command
  that answers "did the run actually do what a run does".

## If it stops halfway

Each phase writes its work to a file before handing over, so a failed run does not
mean starting again.

- **Phase 1 failed partway.** Rerun it. Anything already saved is skipped, so it
  picks up where it left off.
- **Phase 2 failed.** Phase 1's work is still on disk. Rerun Phase 2 on its own.
- **It published but the record keeping did not finish.** Do not republish. Just
  update the version number, the featured log and the archive copy by hand. The
  featured log is the one that matters, because a missing row means an item gets
  repeated next week.

## Before you start

**The machine.** Each run is a fresh cloud machine with this repo cloned. The
environment's setup script installs the Python packages the scripts need, so
nothing needs installing by hand. Only what is pushed to GitHub survives the run,
which is why saving is a phase of its own (`CLAUDE.md`).

**Secrets.** API keys (TranscriptAPI) live in the environment's network
secrets. They are added to requests automatically; no script reads or prints
them.

**Connectors.** Slack (the report), Gmail (newsletters in, the email report out)
and GitHub (the site repo) are attached to the scheduled task.

**YouTube.** Never fetch from YouTube's video or caption servers directly: cloud
addresses are bot-checked. Episode lists come from each channel's public RSS
feed, and transcripts from TranscriptAPI. An episode TranscriptAPI cannot
return is a recorded gap, tried again next week. See `REFRESH.md`.

**Tools that need loading first.** WebSearch and WebFetch are not available until
they are loaded. Load them before the reports discovery and the AI news scan.

**Scanned PDFs.** A report PDF with almost no extractable text is an image. It
needs `pdftoppm -r 150 -png` then `tesseract`, run inside the helper, never in
the main job.

## Rules that apply throughout

**Never use a browser.** This runs with nobody watching. That rule is about
driving a browser, not about the network: fetching pages and feeds with WebFetch
is how the reports, the vendor sweep and the news scan are meant to work. On
10 September a helper read "no browser" as "no fetching" and silently dropped the
whole launch sweep, so say which tool to use, not only which one not to.

**Do the heavy reading elsewhere.** Transcripts, emails and reports are long. They
get read by a helper working in its own space, which hands back only the key
points with a quote to back each one. The main job never carries the raw text.
See `TOKEN_RULES.md`.

**Never invent anything.** No made up numbers, titles, dates or guests. If a
source could not be read properly, say so rather than paper over it.

**If a fetch fails, keep going.** Phase 1 hiccuping does not stop Phase 2. The
digest goes out with whatever is genuinely available.

---

## Where everything lives

```
Podcast Project/
  README.md         start here

  docs/             every guide
    RUN.md          this file, the map of the job
    READER.md  SELECTION.md  STYLE.md  PUBLISH.md  REFRESH.md
    TOKEN_RULES.md  TROUBLESHOOTING.md  GLOSSARY.md  CHANGELOG.md
    SEND_NEWSLETTER.md  SCHEDULE_PROMPT.md  NEXT_STEPS.md
    SUMMARY_SPEC.md  HOW_TO_QUERY.md

  config/
    sources.yaml    every podcast, newsletter and vendor tracked
    config.yaml     where it publishes, where Slack goes

  scripts/
    fetch_transcripts.py    saves new episodes
    build_index.py          rebuilds a collection's index
    check_duplicates.py     the pre-publish repeat sweep
    health_report.py        the Slack and email report
    build_email.py          turns the live page into an email

  library/          the archive, and the point of the whole thing
    podcasts/  tech/  newsletters/  reports/  news/  adhoc/
    each holds: transcripts/, INDEX.md, TAXONOMY.md, episode_summaries.tsv

  digest/           the output
    template.html  template.backup.html
    version.txt  featured-log.tsv
    builds/         the dated build copies, with Gmail links
    published/      every edition exactly as it went live

  _state/           what the job writes as it goes
    run-report.json  publish-report.json   overwritten weekly
    RUN_LOG.tsv                            every problem, appended forever

```

Every collection has the same shape, so anything true of one is true of the
others. Destinations in `config/sources.yaml` are relative to `library/`.

## I want to change something

| What you want to do | Open this |
|---|---|
| Add or remove a podcast, newsletter or vendor | `config/sources.yaml` |
| Change how the digest is written: voice, bullets, standouts | `STYLE.md` |
| Change which items make the cut, or the no-repeats rule | `SELECTION.md` |
| Change who the digest is written for | `READER.md` |
| Change what the Slack message says | `scripts/health_report.py` |
| Change how the page is published or archived | `PUBLISH.md` |
| Change how the library is gathered or tagged | `REFRESH.md` |
| Change how the work is split up, or which model does what | `TOKEN_RULES.md` |
| Change the subscriber email | `SEND_NEWSLETTER.md` |
| Work out why something broke | `TROUBLESHOOTING.md` |
| Look up what a term means | `GLOSSARY.md` |
| See what changed and when | `CHANGELOG.md` |

Change one document at a time, and note it in `CHANGELOG.md`. If the digest reads
oddly in three weeks, that log is how you find out why.
