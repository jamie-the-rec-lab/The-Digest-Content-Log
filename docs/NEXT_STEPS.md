# Next steps

Things agreed but not yet done. Delete a line once it is finished.

---

## 1. BIG SUMMARY BACKFILL (do this once the restructure is finished)

**Decision:** every podcast gets the full written summary added to its
transcript. Podcasts, tech and adhoc. This is what makes the archive
searchable by what was actually said, rather than only by title.

**Going forward:** on by default for all collections, roughly 15 to 25 new
episodes a week, on sonnet. No decision needed.

**Tech cutoff:** tech transcripts start at 1 January 2026. Everything older was
moved to `_to_delete/tech-pre-2026/` on 27 August 2026 and all three tech shows
now carry `cutoff: '20260101'` in sources.yaml, so nothing older comes back.

**The backlog, measured 27 August 2026** (run `build_index.py <collection>` and
read its "Summary blocks" line, which now reports this):

| Collection | Has a block | Total | Missing |
|---|---|---|---|
| Podcasts | 108 | 688 | 580 |
| Tech | 23 | 136 | 113 |
| Adhoc | 0 | 2 | 2 |
| **Total** | | | **695** |

Newsletters and reports are not included. They keep the full issue or the key
figures instead, so a summary block is not expected for them.

Average transcript is around 7,500 words, so the backfill means reading roughly
5 million words. Hours of processing and a real chunk of spend. It cannot be
done in one sitting.

**Roughly 40 existing blocks also need redoing.** Of the 82 written by earlier
runs before today, 40 do not match `docs/SUMMARY_SPEC.md`: some are missing the Guest line,
several are missing every section, and one is not at the top of its file. Find
them with the checker below and regenerate them alongside the missing ones.

```
python3 - <<'EOF'
import glob,re
need=["## Actionable summary","**Guest:**","**Show:**","**Tags:**",
      "**When to use this:**","**Big idea:**","**Steal this"]
for f in glob.glob("library/*/transcripts/*/*.md"):
    s=open(f,encoding="utf-8").read()
    if "<!--SUMMARY-->" not in s: continue
    b=s[s.index("<!--SUMMARY-->"):s.index("<!--/SUMMARY-->")]
    bad=[n for n in need if n not in b] or re.findall(r"[—–]",b) or not s.startswith("<!--SUMMARY-->")
    if bad: print(f)
EOF
```

**How to run it:**
- **On sonnet, always.** Tested 27 August: a smaller model produced accurate but
  shallow blocks, missing vendor conflicts, attribution and what actually counts
  as a contrarian take. The archive exists to be quoted in paid work, so the
  saving is a false economy.
- **Follow the two step method in `docs/SUMMARY_SPEC.md`**: gather quoted
  evidence first, then turn each one into something a stranger could use. Writing
  it in one pass produced usable blocks about 4 times in 10.
- **Backfill agents write the summary block ONLY. They never touch the TSV.**
  Almost every transcript already has its index line, so that step is nearly
  always wrong and never necessary. On 27 August two batches damaged the index:
  one added 23 duplicate lines, the other wrote folder names with the spaces
  stripped, creating 20 lines pointing at files that do not exist. Both were
  caught by `build_index.py`, both cost a repair. One job per agent removes the
  whole class of error.
- **If any index lines are genuinely missing** after a batch, `build_index.py`
  lists them. Add those separately, in one careful pass, not as part of
  summarising.
- **Rerun `build_index.py <collection>` after every batch** and fix any warning
  before starting the next. Invented tags and duplicate lines both show up there.
- **Never build the block from the episode description.** The description's
  "what you'll learn" list is topic labels, not methods. A summary built from it
  tells you what an episode is about rather than what was said in it, which is
  the whole difference this archive exists for. On 27 August a batch of 40 was
  scraped this way and had to be thrown away. `check_summaries.py` now detects it.
- **250 to 450 words, and it is enforced.** 107 blocks were stripped and
  requeued on 27 August for coming in around 180 words. A short block reads like
  a synopsis, which is what the index line is already for.
- **Run `python3 scripts/check_summaries.py` after every batch**, then `--fix`,
  then rebuild the queue. It catches short blocks, dashes, missing sections and
  descriptions scraped instead of transcripts read.
- Newest first, so the most likely searches work soonest.
- In batches, checkpointing as it goes, so a stopped run picks back up.
- Skip anything that already has a summary block, and skip teasers.
- Follow `docs/SUMMARY_SPEC.md` exactly, same format for every collection.
- Never run it in the same session as the weekly digest.

---

## 2. Decided, 27 August

- **The two slow newsletters stay.** Data Driven Recruiter and Remade.md publish
  rarely, and that is fine. They keep their slot.
- **No US source is being added.** The tracked list stays as it is.
- **Edition 1's published copy is left as it was.** It was archived before the
  nine edits made on the morning of 27 August, so it records the first published
  version rather than the final one. That edition has already gone to
  subscribers, so it stays untouched. From edition 2 onward the rule in
  `docs/PUBLISH.md` keeps the archive matching the live page.

## 3. Waiting on the backfill

- **Delete `scripts/_retired_build_tech_index.py`.** It rewrites the whole tech summary file
  mechanically, so once tech episodes carry real summaries it would wipe every
  one. `REFRESH.md` already marks it do-not-run. Delete it once the backfill is
  finished, so nobody runs it out of habit.

## 4. Housekeeping

- **`_to_delete/` is empty and can stay that way.** It was emptied on 27 August:
  383 agency transcripts, 16 old digest drafts, backups, caches and stray files,
  417 files in total. The folder itself stays, because the weekly run moves
  unwanted files there rather than deleting them.
- **Do not prune the featured log.** It is the only record of what earns a place.

## 5. Decide later: where this runs

Today it runs on Jamie's Mac, so it only fires when the Mac is awake at 8am
Wednesday, and nothing tells him when it does not.

Three options, discussed 27 August:

1. **Leave it local.** No work. Silently skips a week whenever the Mac is off.
2. **Cloud session reaching into the Mac.** Needs everything option 1 needs plus
   a live bridge to the computer. Strictly worse. Ruled out.
3. **Move `library/` to a private GitHub repo and run fully in the cloud.** The
   only option that runs without Jamie. Text files are exactly what GitHub is
   for, and it brings version history and an offsite backup with it. The
   connectors already work from the cloud, as proved on 27 August.

**Recommendation:** option 3, but only after the new flow has run locally for
two or three weeks and proved itself.

A lighter variant exists if a full pull turns out slow: the weekly run only
needs the index files and this week's new episodes, not all 1,800 transcripts.
The archive is not the working set.

---

## Done on 27 August

The restructure itself, plus these fixes found along the way:

- **The TSV line-number bug** is fixed in `scripts/build_index.py`, verified by
  deliberately corrupting a copy of the file.
- **A failed listing is no longer reported as an empty source.** A rate limit
  made a working feed look broken during the trial. It now retries with a
  growing wait, then says "LISTING FAILED" with the real error.
- **Fetching only lists the newest 10 episodes.** Brainfood and Recruitment
  Mentors went from about 220 seconds and five shell calls each to under a
  second. It warns if every listed episode was new, which is the only way the
  limit could lose anything.
- **`build_index.py` now reports summary block coverage.** It was only counting
  index lines, so a run could skip every written summary and look healthy.
- **The health report flags unsummarised transcripts.** Same reason: a skipped
  summarising step used to produce a green report.
- **`scripts/check_duplicates.py` added**, comparing names rather than keys,
  which catches a repeat linked from a different URL.
- **A new selection rule:** never feature an older edition of a dated series
  after a newer one has gone out.
- **Web items are saved to `library/news`**, so they get fact-checked against a
  real page rather than against notes the job wrote itself.
- **The template comment** cut from 67 lines to 12 and pointing at the real
  documents.
- **The glossary** trimmed to 22 terms, each one line plus a pointer.
- **The whole folder reorganised**: `docs/`, `config/`, `scripts/`, `library/`,
  `digest/`, `_state/`, with a README at the top.
