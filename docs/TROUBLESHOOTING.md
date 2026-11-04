# TROUBLESHOOTING

Open this when something has gone wrong. Each entry is the symptom, what it
actually means, and what to do.

Log every problem in `_state/RUN_LOG.tsv`, even the ones that fix themselves.

---

## A check that only reports gets ignored

Worth remembering when adding any new check. On 27 August `build_index.py`
correctly printed "17 missing index lines" and the run carried on regardless,
because nothing depended on it. The information was right there and had no
consequence.

A check earns its place when something changes as a result: a status that flips,
a run that stops, a line in the report Jamie reads. If a new check has no
consequence attached, it will be read once and ignored from then on.

## The three strikes rule

`_state/RUN_LOG.tsv` is there to tell a one-off from a pattern. A source that fails once
is noise. The same source failing six weeks running is a broken feed nobody
noticed.

**Anything appearing three times stops being a hiccup.** It gets fixed properly
in the code, or it gets written into this file as a known problem with a known
workaround. Nothing sits in the log forever being tolerated.

Count what is causing the most trouble:

```
grep -v "^#" _state/RUN_LOG.tsv | cut -f3 | sort | uniq -c | sort -rn
```

Worth doing once a month. It takes a minute and it is the only way the pattern
ever surfaces.

---

## Gathering

### A show reports "LISTING FAILED"
yt-dlp could not list the source. Almost always transient: a rate limit after
several fetches in a row, or a network blip. **Retry before concluding
anything.** Wait a moment and run it again.

Only if it fails repeatedly across separate runs is it worth checking the URL by
hand.

### A show reports "found 0 videos"
The listing worked and the source really is empty. That means a renamed channel,
a playlist made private, or a wrong URL. Check it by hand and update
`config/sources.yaml`. Log it, and put it in the health report.

One quiet week on its own is not a break. A source that is both quiet and
genuinely listing empty is.

### A source has published nothing for weeks
Usually just a quiet publisher. **AI & I is irregular by nature and will sit
quiet for stretches, which is normal and not a fault.** Data Driven Recruiter
and Remade.md publish roughly once every two months.

This only becomes a real problem when a quiet source also fails its fetch. That
pair means a genuine break.

### The fetch warns that all listed episodes were new
The scan limit was reached, so there may be more episodes past it. Rerun that
show with a bigger limit, `50` or `all`. Do not ignore it: this is the only way
the limit could quietly lose episodes.

### The fetch keeps timing out
Each shell call is short-lived, so a long fetch gets cut off partway. Rerun it.
Anything already saved is skipped, so it picks up where it stopped. Split a very
long job into steps rather than fighting it.

### The index says every entry is missing
The collection's `episode_summaries.tsv` has been corrupted, most likely with a
line number stuck on the front of every row. It looks catastrophic and is not.

Strip the prefix and rebuild:

```
sed -i -E 's/^[0-9]+\t//' library/<collection>/episode_summaries.tsv
```

**Fixed in `scripts/build_index.py` on 27 August 2026.** It now ignores that prefix when
reading, so this should not happen again. The command above is kept in case a
file needs cleaning by hand.

### You need to fix something in a TSV or index file
**Never run a find and replace across the whole file.** Edit the field you mean.

On 27 August a blanket replace of the tag "billings" with "billing" also rewrote
"billings" inside six filenames, breaking every one of those paths. The index
caught it in seconds, but the repair took longer than doing it properly would
have.

Read the file line by line, split on `|||`, change only the field that needs it,
write it back. Anything else risks hitting the path.

### A folder appears twice, one with %20 in the name
A helper wrote the folder name URL-encoded. Move the files into the correctly
spaced folder and rebuild the index. The empty encoded folder may refuse to
delete, which is harmless.

### A file will not delete
The sandbox blocks deletion in places. Leave it, note it, carry on. Never fail a
run over an undeleted file.

### A report is behind a wall
- **Partial** is fine. A public summary with real figures gets stored and marked
  partial, and the title goes into `_TO_GRAB.md` to upgrade later.
- **Blocked** means even a summary is unreadable. Store nothing at all, add the
  title and link to `_TO_GRAB.md`, and move on. A thin stub is worse than
  nothing.

Being blocked is expected and is not a health failure.

### A vendor page comes back nearly empty
The page is built by JavaScript and cannot be read directly. Do not try a
browser, this job never uses one. Fall through to a search instead.

---

## Building and publishing

### The fact-check keeps failing on the same item
Fix the line from the source or drop it. If two attempts have not resolved it,
drop the item rather than looping. An item is never worth blocking an edition
for.

### A pre-publish check fails
Do not publish. Fix it and run the checks again. If it cannot be fixed, stop and
report it. A failed check is one of the few things that genuinely blocks a run.

### The template does not match its backup
Something has damaged it. Restore from the backup, note it in the health report,
and carry on. Then work out what changed it, because it should never happen.

### It published but the record keeping did not finish
The site is live and the memory is wrong. This is the quiet one, because nothing
looks broken and next week silently repeats items.

Do not republish. Fix the three by hand: the version number, the featured log
rows, and the archive copy. The featured log is the one that matters.

### A bad edition is live
See "Putting it back" in `PUBLISH.md`. The previous edition is in
`digest/published/` and can be committed straight back over the live page.

### The live page has not updated
The commit can succeed while the deploy fails. Check the page itself rather than
trusting the commit. If it has not deployed, check Vercel before touching the
repo again.

---

## Picking it back up

Each phase writes its work to a file before handing over, so almost nothing has
to be redone.

- **Gathering failed partway.** Rerun it. Everything saved is skipped.
- **Building failed.** The gathering is still on disk. Rerun the build alone.
- **A whole run was missed.** Just run as normal. See "If a run was missed" in
  `REFRESH.md`. One edition, not two.

---

## When to stop rather than guess

Most things carry on. But three situations are worse to guess at than to leave
until Jamie is awake. In all three, **stop that part, do not publish, and put it
in the health report.** Do not sit waiting for a reply: nobody is there, and a
run that hangs at 8am helps no one.

- **The featured log has been wiped or looks wrong**, and it is not clear whether
  that was deliberate. Guessing here corrupts weeks of history and quietly
  repeats items for months.
- **A pre-publish check fails in a way that cannot be fixed.** Publishing anyway
  puts something visibly broken on a public page.
- **Something would need republishing over an edition that has already gone out
  by email.** Subscribers have the old version. Changing the page silently makes
  the two disagree.

Everything else: take the conservative option, which usually means leaving the
item out, log it in `_state/RUN_LOG.tsv`, and say so in the health report. A
missing item Jamie can add is a far better outcome than a stalled run.

---

## A show's transcripts fail, or every show fails

Since 4 Nov 2026 transcripts come from TranscriptAPI, not yt-dlp.

- **One episode `failed` with `no_captions`:** YouTube has no captions for it.
  Retried next week; if it keeps failing, it is a gap.
- **Every episode fails with HTTP 401 or 403:** the TranscriptAPI key is missing
  or wrong in the environment's network secrets. Jamie fixes it in the
  environment settings; it cannot be fixed from inside the run.
- **HTTP 402 or a quota message:** the TranscriptAPI plan has run out. Tell Jamie.
- **Every feed fails to list:** check the environment's network access allows
  www.youtube.com.
- **A show lists 0 episodes:** its URL in `sources.yaml` must be the
  `/channel/<UC id>/videos` form. An `@handle` has no feed.
- **A whole show's back catalogue is re-saved as new:** its library folder name
  no longer matches the show name, so nothing is recognised. On 4 Nov 2026 the
  Drive zip had turned `Lenny's Podcast` into `Lenny_s Podcast`.

## "Sign in to confirm you're not a bot"

**Cause:** the request came from a datacentre IP rather than a home connection.
Tested 27 August 2026: identical command, cloud container refused on the first
request, local machine downloaded fine.

**Fix:** none available. This is why the pipeline runs locally. Retrying does not
help, because it is a bot check and not a rate limit. A rate limit clears by
waiting; this one never does. If this appears, stop fetching and report it.
