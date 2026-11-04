# TOKEN RULES: how the work is split up

Read this first, every run. It applies to every phase.

Two things are at stake: cost, and accuracy. They mostly pull in the same
direction, because the habits that keep the job affordable are the same ones
that keep it honest.

Where they conflict, accuracy wins. Saving tokens on the model that reads a
source is a false economy: the archive exists to be quoted in paid work.

---

## 1. Heavy reading happens in a helper, never in the main job

Transcripts, email bodies, PDFs and report pages are enormous. Anything the main
job reads stays in its memory and gets carried through every step that follows,
again and again. That is the single biggest cost in the whole pipeline.

So the main job never opens them. It hands over a file path or a URL, a helper
reads it in its own space, and only the key points come back.

**Never in the main job:**
- opening a transcript
- fetching a report page or PDF
- pulling a full email body
- reading anything long, for any reason

**Fine in the main job**, because they are small:
- search results
- what the index scripts print
- short lookups like an episode date
- error messages and file paths

If you are about to read something long "just to check", hand it to a helper
instead.

---

## 2. Read each source once

A source is opened once and everything needed comes out of that single pass. The
helper that reads a transcript writes its summary AND returns the key points in
one go, rather than being sent back for more.

If you find yourself going back to a source for one more detail, that is a sign
the first pass asked for too little.

## 3. Reopening is fine, but not in the main job

Sources do get reopened. The fact-check exists to do exactly that. The rule is
about where it happens, not whether: reopening happens in a helper, so the bulk
never lands in the main job.

If something is missing when the digest is being written, send a helper for it.
Do not open the transcript yourself.

## 4. The handover goes to a file, not to memory

At the end of gathering, the key points must be written to disk, not carried in
the running conversation.

Three reasons. A crash or an interruption costs nothing already done. The
building phase starts clean instead of dragging everything the gathering phase
ever saw. And after a bad run you can open the file and see what was actually
found, rather than guessing.

Three files live in `_state/`, with three different jobs:

- `run-events.jsonl`, written by the SCRIPTS as they run. Raw facts, one line
  each. Cleared at the start of every run.
- `run-report.json` and `publish-report.json`, written by the AGENT. One summary
  per phase, the handover between them. Cleared at the start of every run and
  again after the newsletter goes out.
- `RUN_LOG.tsv`, written by the health report. Problems only, appended forever,
  never pruned.

Tools record facts. The agent records conclusions. Problems go in the permanent
record.

**Each is overwritten every week, not accumulated.** Two files, forever.

**Each carries the date it was written, and the phase that reads it must check
that date.** A report that is not from today's run is stale and must not be
used. This is what stops a failed gathering phase quietly handing last week's
material to this week's digest.

**Both are emptied once the newsletter has gone out**, so the next run starts
from nothing. See `SEND_NEWSLETTER.md`.

## 5. Ask for what you need, not what is available

Most services will hand over everything if you do not say otherwise, and it
costs nothing to send and plenty to receive.

The example worth remembering: fetching the live page to get its version marker
returns all 49,000 characters. Listing the folder and asking for two fields
returns about 100. Same information, five hundred times smaller.

Before any call to an outside service, check whether it lets you narrow what
comes back.

---

## 6. Match the model to the job

**Sonnet for everything that reads a source.** Pulling facts out of a transcript,
writing the library summaries, tagging, returning key points. This was tested on
27 August 2026: a smaller model got the figures right but missed the judgement
that makes an archive worth having. It did not flag that a guest was the vendor
behind the product being praised, it repeated a statistic without attributing it,
and it labelled a comfortable prediction as a contrarian take.

None of those are accuracy failures. They are the difference between evidence
you can take to a client and marketing you have accidentally repeated.

**Sonnet or better for the writing.** The bullets, the "This week in the world of recruiting" preview
and the standouts are the product. The main job writes these itself.

**Strongest available for the fact-check.** Never anything less, under any
circumstances. This is the last thing standing between a mistake and the live
page.

If a model is unavailable on a given run, fall back to the default rather than
failing. Except the fact-check, which never falls below strong.

## 7. Every fact comes back with its evidence

A helper that reads a source must return each key point **with the exact figure,
tool name or date, and a short quote showing where it came from.**

Not "they talked about AI reducing screening time". Instead: "screening time
down 40%", with the line from the transcript that says it.

Two reasons. A summary without its source quietly drifts into something the
source never said, and nobody can tell afterwards. And the fact-check later
needs to confirm the claim without reopening the whole source.

**A vague gist is not acceptable.** Send it back.

---

## 8. A helper's own report is not evidence

A helper that says "40 done, 0 failed" is telling you it finished, not that the
work is good. It cannot judge its own output, and it will report success on
work that is below spec every time.

On 27 August every backfill batch reported clean. A quarter of the blocks were
too short, and one batch of 40 had been built from episode descriptions rather
than transcripts. Nothing in any report hinted at either.

**So verify with a check, never with a summary.** `check_summaries.py` after a
batch, `build_index.py` after anything that touches a library, the fact-check
before publishing. If there is no check for something, the honest position is
that you do not know whether it worked.

## 9. One job per helper

Both times the index was damaged on 27 August, it was a helper doing two things
at once, and the second one wrote to a file shared with other helpers.

Give a helper one job. Where two jobs both touch the same shared file, do the
second one yourself afterwards, in a single careful pass.

## 10. Say what could not be read

A helper that hits a truncated PDF, a login wall, garbled text or a page that
will not load must say so plainly. Never paper over it, and never fill the gap
with something plausible.

A recorded gap is fine. An invented fact is not, and by the time anyone notices
it is on the live page.

---

## 11. One writer at a time

Each collection has a single shared summary file. Two helpers appending to it at
once corrupts it. So summarising runs one after another within a collection,
never in parallel.

Different collections do not share a file, so they do not have this problem.

---

## The short version

The main job orchestrates. It sends work out, writes the digest from what comes
back, runs the fact-check, and publishes. It should never be carrying raw source
text at any point.

If it is, something has gone into the wrong place.
