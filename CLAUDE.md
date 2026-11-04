# TheRecLab weekly digest: standing rules

Every session in this repo reads this file first. It replaces the old Cowork
schedule prompt (`docs/SCHEDULE_PROMPT.md`, kept for history).

This repo is the whole job: the guides (`docs/`), the settings (`config/`), the
tools (`scripts/`), the library (`library/`), the digest record (`digest/`) and
the run state (`_state/`). The website lives in a second repo,
`jamie-the-rec-lab/thereclab-site`, which this job only ever proposes changes to.

## The weekly run

**Run day: Sunday afternoon** (since November 2026; it used to be Wednesday).
Two dates, and they are different on purpose (Jamie's call, November 2026):

- **The edition date is the Monday after the run.** The edition line reads
  `Version <N> (<Monday date>)`, e.g. `Version 9 (16th November 2026)` for a run
  on Sunday 15 November, and the page title uses the same Monday. Readers get it
  in the new week, so it is dated for the new week.
- **The 8 week freshness window ends on the run date itself**, never the Monday:
  nothing can be selected from a day that has not happened yet.

Wherever the documents say "the Wednesday the job runs", read the edition date
as the Monday after the run and the window end as the run date.

Start with `docs/RUN.md`, the map of the whole job, then follow it, reading the
document each phase points you at when you reach it. Read `docs/TOKEN_RULES.md`
before you start. It governs every phase.

Run the phases in order, each as its own subagent so the heavy reading never
reaches the main thread. Helpers run on Sonnet, including the ones that read
transcripts. The fact-check runs on the strongest model available.

0. **RECONCILE** last week's review, per `docs/PUBLISH.md` step 0.
1. **REFRESH**, per `docs/REFRESH.md`. Writes `_state/run-report.json`.
2. **BUILD AND PROPOSE**, per `docs/SELECTION.md`, `docs/STYLE.md` and
   `docs/PUBLISH.md`. Reads the run report, writes `_state/publish-report.json`.
3. **SAVE**, per "Saving the run" below. Always, even if an earlier phase stopped.
   It comes before the report so the report can say whether the save worked.
4. **REPORT**, by running `scripts/health_report.py`. Send the printed message to
   Slack, then run it again with `--format email` and send that to
   jamie@thereclab.ai via Gmail. Include the review link and the pull request
   link from `_state/publish-report.json`.

## Non-negotiable

- **Never go live directly, and never merge.** The run pushes the new edition to
  the `digest-review` branch of the site repo and opens a pull request. Vercel
  builds a preview. Only Jamie decides when it goes live: he merges it himself,
  or explicitly says "merge" in a session. Never push to `main` of the site repo,
  and never merge, close or replace a review pull request without his say-so.
- **Never touch Resend, and never send anything to the subscriber list.** The
  newsletter is human-gated and separate (`docs/SEND_NEWSLETTER.md`).
- **Never invent a number, title, date, guest or company.** A recorded gap is fine.
- **Nothing is proposed with an unresolved fact-check mismatch.**
- **Never use a browser.** Fetching pages and feeds is fine and expected; driving
  a browser is not.
- **Never get round a bot check, rate limit or paywall.** A source that refuses
  is a recorded gap. YouTube transcripts come from TranscriptAPI
  (`docs/REFRESH.md`); never fetch YouTube captions directly. If TranscriptAPI
  fails on an episode, that episode is a recorded gap and is tried again next
  week.
- **Never force-push, never rewrite history, and push only to this repo and to
  the `digest-review` branch of the site repo.**
- **Secrets live in the environment settings, never in a file.** Never print,
  log or commit an API key.

## Nobody is awake, so never wait for an answer

Do not pause to ask. Decide, then record what you decided and why in
`_state/RUN_LOG.tsv` so it reaches the health report under "Decisions I made".

Use your judgement on editorial calls: what goes in, what it is worth, how it
reads, what a thin week is best filled with. `docs/READER.md`,
`docs/SELECTION.md` and `docs/STYLE.md` give you the audience and the purpose.
An educated call beats dropping a good item because no rule covered it exactly.

Never use judgement to supply a fact, to resolve a fact-check mismatch, or to
take an action that cannot be undone. A number, date, title, guest or company
you cannot verify is a gap, and a recorded gap is fine. Filling it is not.

Three things stop that part of the run rather than being decided:
- the featured log looking wiped or wrong
- a pre-publish check that cannot be fixed
- anything that would replace an edition already emailed to subscribers

For those, stop and do not propose, but still run the health report so the
problem reaches Slack, and still save the run. Stopping is fine. Waiting is not.

## When to give up on something

- A source that fails: park it, carry on with the others, then sweep the parked
  ones once more at the end of the refresh. Still failing, leave it for next
  week. The digest looks back 8 weeks, so nothing is lost.
- A permanent failure (bot check, private, unavailable, members-only): do not
  retry at all.
- An item whose fact-check still fails after two attempts to fix it: drop it.
- A phase that cannot complete at all: stop that phase, run the health report
  so the failure reaches Slack, save the run, and do not propose.

Never loop on the same failure more than twice. If something breaks, read
`docs/TROUBLESHOOTING.md`. Log every problem in `_state/RUN_LOG.tsv`.

## Saving the run

The cloud machine is wiped when the session ends. Anything not pushed is gone,
including the featured log, which is what stops items repeating.

At the end of every run, whatever happened, commit this repo's changes
(`library/`, `digest/`, `_state/`) with the message
`run: <YYYY-MM-DD> <one-line outcome>` and push them to `main` of this repo.
It must be `main`, not a side branch: next week's run starts from `main`, so
state saved anywhere else is state lost. This is the one standing exception to
working on a side branch, and it applies to the weekly run only, never to code
or document changes, which go through a pull request.

If the push fails, retry up to four times, then say so loudly in the Slack
message: an unsaved run means next week starts from stale state.

Deleting files is fine here: git history keeps everything, so `_to_delete/` is
no longer needed. Remove unwanted files with `git rm`.

## The output

The Slack message and the email are the output of the run. There is no need to
summarise anything back to the terminal.
