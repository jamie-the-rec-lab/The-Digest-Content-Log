# CHANGELOG

What changed, when, and why. Newest first. One line each.

Add an entry every time you change a document or a script. When the digest reads
oddly in three weeks, this is how you find out what you changed.

Format: date, what changed, why.

---

## 2026-11-04

- 2026-11-04, `CLAUDE.md`: Resend tools are set to need Jamie's approval in the connector settings, a second gate on top of the rule. A Resend approval prompt during a weekly run is treated as a fault and reported. In send sessions, approving a tool call is not the broadcast green light.
- 2026-11-04, `CLAUDE.md`: the "never touch Resend" rule now applies to the weekly run only, and a new "Sending the newsletter" section covers the human-gated send (test, then a second green light for the broadcast). Why: every session reads CLAUDE.md, so the old wording would have stopped Jamie's own send sessions. Jamie keeps the Resend connector on the scheduled task by choice, so the rule, not a missing connector, is what stops the weekly run sending.
- 2026-11-04, edition date is now the Monday after the Sunday run (Jamie's call), in the edition line and page title. The 8 week window still ends on the run date. Changed in `CLAUDE.md`, `PUBLISH.md` step 3 and `RUN.md`. Not applied to Version 8 (PR #6, dated 4th November).
- 2026-11-04, run day moved to Sunday 14:20 UK (Jamie's call). `CLAUDE.md` says to read every "Wednesday" in the docs as the run date; `config.yaml` records the day and time.
- 2026-11-04, fixes from the first cloud dry run: `health_report.py` now speaks the review flow (preview link, pull request link, "ready for review, not live", last week's edition still waiting, DRY RUN labels) instead of "live for your review" and Cowork chat. `PUBLISH.md` step 7 checks the review branch really changes `digest/index.html` before and after pushing, because the dry run's first push went up identical to `main`. Offer Accepted's undated Loop Earplugs episode dated 3 Nov 2026 from the show's official feed and renamed, so selection can see it.
- 2026-11-04, `config/sources.yaml`: added Gem Newsletter (Jamie's call), with a new optional `search` line so only issues sent as "Gem Newsletter" are collected, not Gem's webinar and promo emails from the same address. `REFRESH.md` reads the `search` line. Its "View in browser" link is a personal tracking link and is never published.
- 2026-11-04, `scripts/cloud_setup.sh`: record copy of the cloud environment's setup script (beautifulsoup4 for the email builder; tesseract and poppler for scanned PDFs, optional). The live copy is in the environment settings; change both together.
- 2026-11-04, `scripts/fetch_transcripts.py` rewritten for the cloud: episode lists from each show's official YouTube RSS feed (Videos or Live tab only, so no Shorts), transcripts from TranscriptAPI, a new paragraph at each change of speaker. Same arguments and log events, so nothing else changed. New outcomes: `upcoming` (live stream not aired), `pending` (released under 12 hours ago, captions not ready, Jamie's call), `failed`/`gone`. `health_report.py` reports failed and pending episodes. `sources.yaml` uses channel ids, since an @handle has no feed. Why: YouTube bot-checks cloud machines, and the job does not get round bot checks.
- 2026-11-04, library: renamed `Lenny_s Podcast` back to `Lenny's Podcast`. Why: the Drive zip download swapped the apostrophe for an underscore, which broke every featured-log path and made the fetcher treat all 57 episodes as new.
- 2026-11-04, moved from Cowork on the laptop to a Claude Code cloud session. New `CLAUDE.md` holds the standing rules (replaces `SCHEDULE_PROMPT.md`, kept for history). Why: the laptop run stopped for weeks; the cloud runs without it.
- 2026-11-04, `PUBLISH.md`, `RUN.md`, `config/config.yaml`: the job no longer commits to the live site. It pushes to the `digest-review` branch, opens a pull request, and Jamie's merge puts it live; Vercel's preview is the review page. New step 0 reconciles last week's pull request (merged keeps the record, unmerged un-burns the items). Why: on 17 Oct the direct publish was blocked by a safety check as a production deploy, so Version 8 never went live; and Jamie wants to review on his phone before anything goes out.
- 2026-11-04, review rules, Jamie's call: the job never merges, closes or replaces a review pull request. If last week's is still open, this week refreshes the library but builds no new edition, and the report flags it. No Gemini fallback for transcripts: a TranscriptAPI failure is a recorded gap, retried next week.
- 2026-11-04, `RUN.md` "Before you start": dropped laptop-only notes (two filesystems, 45-second shell cap, installing yt-dlp each run). `_to_delete/` retired: git history now keeps every old version. Why: none of it applies in the cloud.

## 2026-10-09

- 2026-10-09, docs/RUN.md and scripts/fetch_transcripts.py: install the curl-cffi add-on (yt-dlp[default,curl-cffi]) at the start of every run, and have the fetcher install it itself if missing. Why: the 7 Oct impersonation fix needs it, and the workspace starts fresh each run. Approved by Jamie 9 Oct.

## 2026-10-07

- 2026-10-07, scripts/fetch_transcripts.py: added --impersonate chrome, --sleep-subtitles 3 and an en-orig-only retry (with --write-info-json) when no caption file lands. Why: YouTube returns HTTP 429 on the "en" track for many videos while "en-orig" works, the 429 aborted the call, and the script reported it as "nosubs", so weeks of episodes looked caption-less. Needs curl_cffi (installed via yt-dlp[default,curl-cffi]).

## 2026-09-30
- SEND_NEWSLETTER.md: reply-to for test and broadcast is now jamie@thereclab.ai (Jamie's call), with a note to check it survives on the broadcast before scheduling. Subject lines use a comma instead of a dash.
- build_email.py: stopped deleting the space before decimals (".42" became "of.42").

## 2026-09-10

- **AI news and AI regulation items moved from Section 3 to Section 4**, at
  Jamie's instruction. Section 3 is now strictly recruiting: reports, curve
  balls, events, product launches, essays. Section 4 is where the AI material
  lives, holding the four tech shows' episodes plus any standalone AI news or
  regulation item after them. Changed in `SELECTION.md` (Section 3 ordering,
  Section 4 definition, the subject gate now scoped to episodes only, and the AI
  pick standout rule) and `STYLE.md` (the `news` type removed from the Section 3
  type list and moved to Section 4).
  The AI pick standout is still an episode, never a news item: the row is for
  something worth an hour, not a headline. That was the previous intent and it
  survives the move.
  Not applied retroactively. Version 3, live from the 10 September run, has the
  OpenAI GPT-6 Astra item in Section 3 under the old rule.

- **Data Driven Recruiter sender corrected** in `config/sources.yaml`, from
  `luke-eaton@b.kajabimail.net` to `data-driven-recruiter@mail.beehiiv.com`.
  The newsletter migrated from Kajabi to beehiiv about ten weeks ago, so the
  Gmail search had matched nothing since and the source was reported as a quiet
  feed rather than as a stale matching rule. Issue DDR78, 3 September, was
  missed by the Version 3 edition as a result. It is inside the 8 week window,
  so it stays eligible for the next run.

---

## 2026-09-04

- **AI For Humans added to the tech collection**, effective from the 9 September
  run onward, not applied retroactively to the 2 September edition. Added to
  `config/sources.yaml`, to `RECURRING["tech"]` in `health_report.py` so a quiet
  feed is noticed, and named in `SELECTION.md` Section 4.
  First fetch run deliberately with `--backfill` (50 episodes, cutoff 20260101)
  so Wednesday sees a warm source and behaves like a normal weekly run instead of
  hitting the new scan-limit clamp.

- **Graded as tech, same bar as the others.** A source-specific warning was
  briefly added telling the run to apply the subject gate harder to this one,
  and then removed the same day at Jamie's instruction. It is judged on the
  standard Section 4 gate like Lenny's, How I AI and AI & I, with no extra
  hurdle. Consequence worth knowing: it publishes weekly and is always about AI,
  so it will clear the gate most weeks and the tech section will usually run
  three or four items rather than two.

- **`fetch_transcripts.py`: writing a summary block could get that summary
  destroyed.** The "already saved, skip it" check read only the first 4000 bytes
  of an existing file looking for a timecode link. A SUMMARY_SPEC block is 250 to
  450 words and sits ABOVE the title, which pushes the first timecode past that
  window, so the file looked un-fetched and was re-downloaded over the top. The
  better and longer the summary, the likelier it was to be destroyed. Six were
  lost on 4 September before it was spotted, and they were only spotted because
  the same run happened to re-fetch them minutes after they were written. On a
  normal week this would have quietly eaten archive work with nothing reporting
  it, which is the exact failure mode of the misfiled-fetch bug the day before.
  Two fixes: the check now reads the whole file, and a rewrite lifts out any
  existing summary block and puts it back on top. Both tested by injecting a
  3,171 byte block and confirming the fetcher skips rather than saves.

- **`fetch_transcripts.py` now records a `missing_date` event**, and
  `health_report.py` surfaces it under "Needs attention". A record with no date
  used to be written silently as `0000-<slug>.md`, which is invisible to
  selection, to the 8 week window and to the no-going-backwards rule.

- **Three malformed records repaired during that fetch.** Three episodes saved
  with an empty date, channel, duration and URL, and filenames beginning `0000-`.
  Dates were recovered from YouTube (2026-02-13, 2026-07-17, 2026-07-29), the
  headers filled from verified metadata and the files renamed. The originals are
  in `_to_delete/`. Nothing was invented. Worth watching: the fetcher wrote a
  record with a blank date rather than failing, and `build_index.py` accepted it,
  so a `0000-` file is currently invisible to date-based selection with nothing
  flagging it.

---

## 2026-09-03 (later)

- **The preview label is now "This week in the world of recruiting"**, replacing
  "In this issue". Changed in `digest/template.html` and its backup so it carries
  into every future edition, in the 2 September edition itself, and in
  `STYLE.md`, `GLOSSARY.md`, `PUBLISH.md`, `TOKEN_RULES.md` and
  `SEND_NEWSLETTER.md`. `build_email.py` needed no change: it reads the label out
  of the page rather than hardcoding it, so the email follows automatically.

- **`build_email.py` no longer puts an em dash in the plain text header.** It
  built `f"{kicker} — {date}"`, and the later safety pass swapped the dash for a
  comma while leaving its spaces, so the text version read "TheRecLab Weekly
  Digest ,  Version 2". Now a comma at source. The safety pass stays as a
  backstop, it just no longer has to clean up after the builder.

---

## 2026-09-03

Written after the 2 September edition had to be corrected twice, live. Two
faults, both selection working exactly as written on a library that was wrong
underneath it.

- **`SELECTION.md`: "never go backwards through a dated series" now covers every
  dated series**, podcasts and tech included, not just reports and newsletters.
  Restated positively: a pick must be NEWER than the newest item already featured
  from that source. Being unfeatured and inside the 8 week window is the floor,
  not the test. Why: a deep backfill dropped months-old episodes into the library,
  they arrived unfeatured and in window, and six of them were published as that
  week's picks, including episode 819 the week after episode 820.

- **`fetch_transcripts.py` now refuses an invalid destination.** It must resolve
  to `<collection>/transcripts` for one of the six known collections. A bad one
  exits non-zero, writes nothing, and records a `bad_destination` event. Why: 177
  episodes were written to bare top-level folders such as `library/Brainfood/`.
  The script reported success, selection never found them, and `build_index.py`
  never saw them because it only walks the six collections. Three episodes that
  belonged in the edition were missing from it, and nothing in the pipeline
  noticed. Only Jamie asking why the week looked so quiet caught it.

- **`fetch_transcripts.py` now caps the scan limit at 50** unless `--backfill` is
  passed. Above the ceiling it clamps and records a `scan_limit_clamped` event.
  Why: `REFRESH.md` told the run to rerun with a bigger limit whenever every
  listed episode was new, which is right, but had no ceiling. One weekly run
  escalated to 100 and pulled 50 Brainfood and 61 Recruiting Future episodes.
  Escalating past 50 is now a deliberate backfill job, not part of a weekly run.
  The existing "there may be more beyond this limit" warning is unchanged, and is
  now distinguished in the events from a clamp, because they need different
  responses.

- **`health_report.py` reports both new events.** A refused destination is
  `blocked` severity and appears under "Needs attention"; a clamp is recorded as a
  decision. Why: a guard nothing reports is a guard nobody acts on.

- **`publish_check.py` no longer flags section 3 for date order.** The rule is now
  stated positively: only Recruiting Podcasts, Recruiting Newsletters and AI &
  Tech Picks are genuinely date-ordered. Why: section 3 is ordered by TYPE per
  `SELECTION.md`, so the rule fired every week including on the published v1. A
  check that always fails trains everyone to skim past it. Note for anyone
  editing it: the section labels in that script are HTML-escaped, so the tech one
  is `AI &amp; Tech Picks`. Getting that wrong silently stops checking a section
  while still reporting clean, so there is now an assert against `SECTIONS`.

- **`READER.md` and `STYLE.md`: the digest is a way into good content, not a
  substitute for it.** `READER.md` now says each item does two jobs, giving
  something usable on the page AND telling the reader honestly what they get by
  clicking through. `STYLE.md` adds the two failure modes, over-summarised so
  there is no reason to click, and under-sold so the reader cannot tell what they
  would get. Explicitly not permission to tease: rule 2 still stands, and a vague
  bullet is just a worse bullet.

---

## 2026-08-27

- **The run is now a live scheduled task**, Wednesdays 08:00 UK, bound to Jamie's
  Mac. Cron is stored in UTC as `0 7 * * 3`, which is 08:00 during BST. **When the
  clocks go back in late October this must change to `0 8 * * 3`** or the run
  fires at 07:00. Times across the docs updated from 06:00 to 08:00 to match.
- **Tech cutoff set to 1 January 2026.** 458 transcripts older than that moved to
  `_to_delete/tech-pre-2026/`, and all three tech shows now carry
  `cutoff: '20260101'` in `sources.yaml`. Tech went from 584 files to 136. The
  digest only ever looks 8 weeks back, so a 2022 episode could never be selected.
  This also cut the summary backfill from 1,556 to 695.
- **yt-dlp is now resolved, not assumed.** `fetch_transcripts.py` finds it via the
  command, then `python3 -m yt_dlp`, then installs it. The machine does not keep
  packages between runs and pip puts the binary somewhere off PATH, so the old
  bare `"yt-dlp"` call would have failed the first unattended run.
- **The pipeline stays local, and now for a tested reason.** yt-dlp from a cloud
  IP gets "Sign in to confirm you're not a bot" on the first request; the same
  command locally works. Recorded in `TROUBLESHOOTING.md`. A fully cloud-hosted
  run is not possible without YouTube cookies or a residential proxy.
- **Agency collection removed.** Elite Recruiter and Recruitment Mentors, 383
  transcripts, moved to `_to_delete/library-agency`. They were never going to
  reach the digest, and maintaining a second body of content that nothing
  consumed was complexity for its own sake. Removed from `config/sources.yaml`,
  the scripts, and every document.
- **Nothing in this job ever deletes a file.** `PUBLISH.md` used to open with
  `rm -f` on the old build. It now moves it to `_to_delete/`, matching the rule
  in the schedule prompt. Deleting needs a permission prompt nobody sees at 8am.
- **Four contradictions fixed**, found by auditing the documents against each
  other: `config/config.yaml` still pointed at the pre-rename filenames,
  `RUN.md` still required exactly four sections, `SUMMARY_SPEC.md` still called
  agency frozen and optional, and `RUN.md` still described publishing and record
  keeping as an unsolved problem.

- **Library moved into `library/`**, every collection the same shape, core
  podcasts no longer loose at the top level. Scripts, config and documents
  updated to match, all six indexes verified clean.
- **Fetch now lists only the newest 10 episodes** by default, with `all`
  available for backfills. Brainfood and Recruitment Mentors went from about 220
  seconds and five shell calls each to under a second. It warns if every listed
  episode was new, which is the only way the limit could lose anything.
- **A failed listing is no longer reported as an empty source.** It retries with
  a growing wait, then says "LISTING FAILED" with the real error. Found during
  the trial run, where a rate limit made a working feed look broken.
- **`scripts/build_index.py` now reports summary block coverage.** It was only counting
  index lines, so a run could skip every written summary and look healthy.
  Actual coverage: 81 of 688 podcasts, 0 of tech and agency.

- **Rebuilt the whole job as separate documents.** It was one instruction of
  about 7,000 words holding orchestration, configuration, writing rules and bug
  workarounds all in one place. Now: `RUN.md` as the map, with `config/sources.yaml`,
  `config/config.yaml`, `READER.md`, `REFRESH.md`, `SELECTION.md`, `STYLE.md`,
  `PUBLISH.md`, `TOKEN_RULES.md`, `TROUBLESHOOTING.md`, `GLOSSARY.md` and
  `SEND_NEWSLETTER.md` underneath it.
- **Run day is Wednesday**, and the edition line now carries the Wednesday date
  rather than the Monday.
- **Audience widened to the UK, US and English-speaking Europe.** Every figure
  now names its market. British English stays.
- **Tech and agency shows now get full written summaries**, same as the core
  podcasts, so the whole archive is searchable by what was said. Creates a
  backlog of 1,550 transcripts, see `NEXT_STEPS.md`.
- **Agency is no longer frozen.** It is fetched and saved like everything else,
  and excluded from the digest only.
- **Vendor takeover episodes are no longer skipped** at fetch time. They are
  saved, and the selection rules decide whether they earn a place.
- **Empty sections are deleted** rather than showing a "nothing new this week"
  line. The pre-publish check now allows one to four sections instead of exactly
  four.
- **Publishing and record keeping are one action**, so the site cannot go live
  with the featured log left wrong.
- **Added an edit path and a rollback path** to `PUBLISH.md`, which did not
  exist before.
- **The featured log is never pruned.** The old instruction suggested pruning
  after ten weeks. It is the only record of what earns a place.
- **Handover files** in `_state/`, date stamped and emptied after the newsletter
  goes out, so a failed run can never hand stale material to the next one.
- **`_state/RUN_LOG.tsv` added**, every problem from every run, with a three strikes
  rule for turning patterns into fixes.
- **Publishing halved in cost**, by reading the live page's version marker from
  a folder listing rather than fetching all 49KB of the file.
- **New writing rules:** every bullet must work on a blank page, cite numbers
  exactly as the source gives them and never convert, launches must not read
  like press releases, and no framing is repeated across items.
