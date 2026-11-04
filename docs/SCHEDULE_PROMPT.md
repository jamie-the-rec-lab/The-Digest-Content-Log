# The schedule prompt

This is what goes in the Wednesday scheduled task, replacing the old 7,000 word
instruction. Everything else lives in the project folder.

Keep it short. If you find yourself adding a rule here, it belongs in one of the
documents instead.

---

```
Run the weekly TheRecLab digest pipeline.

The project folder is "Podcast Project" in the connected folders. Everything you
need is in it. Start by reading docs/RUN.md, the map of the whole job, then
follow it, reading the document each phase points you at when you reach it.

Read docs/TOKEN_RULES.md before you start. It governs every phase.

Run the three phases in order, each as its own subagent so the heavy reading
never reaches this thread. Spawn every helper on sonnet, including the ones that
read transcripts, and the fact-check on the strongest model available:

1. REFRESH, per docs/REFRESH.md. Writes _state/run-report.json.
2. BUILD AND PUBLISH, per docs/SELECTION.md, docs/STYLE.md and docs/PUBLISH.md.
   Reads the run report, writes _state/publish-report.json.
3. REPORT, by running scripts/health_report.py. Send the printed message to
   Slack, then run it again with --format email and send that to
   jamie@thereclab.ai via Gmail.

NON-NEGOTIABLE
- Never use a browser. Nobody is watching.
- Never touch Resend, and never send anything to the subscriber list. The
  newsletter is human-gated and separate.
- Never delete a file on this machine. Deleting needs Jamie to approve a prompt
  he will not see at 8am. Move anything unwanted to _to_delete/ instead.
- Never invent a number, title, date, guest or company. A recorded gap is fine.
- Nothing publishes with an unresolved fact-check mismatch.

NOBODY IS AWAKE, SO NEVER WAIT FOR AN ANSWER
Do not pause to ask. Decide, then record what you decided and why in
_state/RUN_LOG.tsv so it reaches the health report under "Decisions I made".

Use your judgement on editorial calls: what goes in, what it is worth, how it
reads, what a thin week is best filled with. You have docs/READER.md,
docs/SELECTION.md and docs/STYLE.md, and between them they give you the audience
and the purpose. An educated call beats dropping a good item because no rule
covered it exactly.

Never use judgement to supply a fact, to resolve a fact-check mismatch, or to
take an action that cannot be undone. A number, date, title, guest or company
you cannot verify is a gap, and a recorded gap is fine. Filling it is not.

Three things stop that part of the run rather than being decided:
- the featured log looking wiped or wrong
- a pre-publish check that cannot be fixed
- anything that would republish over an edition already emailed to subscribers
For those, stop and do not publish, but still run the health report so the
problem reaches Slack. Stopping is fine. Waiting is not.

WHEN TO GIVE UP ON SOMETHING
- A source that fails: park it, carry on with the others, then sweep the parked
  ones once more at the end of the refresh. Still failing, leave it for next
  week. Nothing is lost: the digest looks back 8 weeks, so a missed source is
  picked up next Wednesday and is still eligible.
- A permanent failure, meaning a bot check, private, unavailable or
  members-only: do not retry at all. Waiting cannot fix those.
- An item whose fact-check still fails after two attempts to fix it: drop the
  item, do not keep trying.
- A phase that cannot complete at all: stop that phase, run the health report
  anyway so the failure reaches Slack, and do not publish.
Never loop on the same failure more than twice.

If something breaks, read docs/TROUBLESHOOTING.md. A failed fetch does not stop
the run: carry on with whatever is genuinely available. Log every problem in
_state/RUN_LOG.tsv.

The Slack message and the email are the output of this run. There is no need to
summarise anything back to the terminal.
```

---

## Why it is this short

Everything that used to be in the prompt is now in a document, and each document
is read only by the phase that needs it. The prompt's only job is to say what
order things happen in and what must never happen.

Five things are stated here rather than in a document, deliberately:

- **The phases as subagents, and which model each runs on.** Both are decisions
  made at the moment a helper is created, which is orchestration.
- **The non-negotiables.** Short, absolute, and they matter most when something
  has gone wrong and the documents are being skimmed.
- **Never wait for an answer, and what to do instead.** An earlier version told
  the job to ask when a rule was missing. There is nobody to ask at 8am, so that
  either hung the run or was quietly ignored. The version after that said "take
  the conservative option", which was too blunt: it threw away good items
  whenever a rule did not quite cover them. It now splits by what kind of
  decision it is. Editorial judgement is encouraged, because the reader profile
  and the selection rules give it enough to judge with. Supplying a fact,
  resolving a mismatch or doing anything irreversible is never a judgement call,
  because a confident wrong answer there is worse than a gap and nobody sees it
  until it is public. Everything decided gets logged and reaches the health
  report.
- **When to give up.** Without a stop rule, a stubborn fact-check or a failing
  fetch can grind for hours. Nothing loops on the same failure more than twice.
- **Where to start.** Without `docs/RUN.md` named explicitly, nothing else is
  reachable.

## If it stops working

The usual cause is a document being edited into disagreement with another one.
Check `docs/CHANGELOG.md` for what changed recently, then read the two documents that
cover whatever went wrong.

Do not fix it by adding rules back into this prompt. That is how the old
instruction reached 7,000 words.
