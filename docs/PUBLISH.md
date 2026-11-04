# PUBLISH: building the page and putting it live

Phase 2, after the items are picked (`SELECTION.md`) and written (`STYLE.md`).

Never hand-write the HTML or the CSS. The look lives in the template and is
reused exactly.

**How an edition goes live (since November 2026).** The job never goes live by
itself. It pushes the edition to the `digest-review` branch of the site repo and
opens a pull request to `main`. Vercel builds a preview of the whole site from
that branch, which Jamie reads at the review address in `config/config.yaml`.
**Merging the pull request is what puts it live.** This replaces the old direct
commit to `main`, which an automated safety check blocked on 17 October.

---

## 0. Reconcile last week's review (start of every run)

Last week's edition may or may not have been merged. The record has to match
what readers actually saw, so check before building anything.

Read `_state/pending-review.json`. If it does not exist, there is nothing to
reconcile. Otherwise it names last week's pull request, version and featured
rows. Look the pull request up in the site repo:

- **Merged.** It went live. Keep the version number, the featured rows and its
  file in `digest/published/` exactly as they are. Delete
  `_state/pending-review.json`.
- **Closed without merging.** Jamie decided against it (he closed it, or told a
  session to). Remove its rows from
  `digest/featured-log.tsv` so those items are eligible again, set
  `digest/version.txt` back to the version that is actually live, and move its
  file in `digest/published/` to `digest/published/not-published/`. Log the
  decision. Delete `_state/pending-review.json`.
- **Still open.** Jamie has not decided yet, and that decision is his alone.
  **Leave it exactly as it is**: do not close it, replace it or push to
  `digest-review`. Run the refresh as normal so the library keeps growing, but
  **do not build a new edition this week**. The health report says, near the top,
  that last week's edition is still waiting for review, with its link. Log it.
  Keep `_state/pending-review.json` for next week.

If the pull request cannot be found, or its state cannot be read, **stop the
build** (the featured log may be wrong) and report it. This is one of the three
hard stops.

---

## 1. Check the template

```
diff digest/template.html digest/template.backup.html
```

If they differ, the template has been damaged. Restore it from the backup and
note it in the run report.

Then clear out last week's build, which has no job left now, and copy the
template to this edition's build file:

```
git rm -q digest/builds/*.html 2>/dev/null || true
cp digest/template.html digest/builds/<YYYY-MM-DD>.html
```

Removing it is safe: git history keeps every earlier build. (On the laptop this
was a move to `_to_delete/`; that folder is no longer used.)

Never touch `digest/published/`, which keeps every edition forever.

Edit the copy. Never edit the template itself.

---

## 2. Never touch these

The template ships a lot of working furniture. All of it is static and none of
it changes week to week:

- the `<style>` block, in full
- the `<head>` tags: title, description, social preview, favicons
- the "Go back to TheRecLab" link and the header subtitle
- both newsletter signup forms and their script
- the sources overlay and its script
- the welcome overlay and its script
- the footer, including the sign-off block and the sources link
- every wrapper and class name

If a change seems to need new CSS, a new heading style or an inline style, it is
the wrong change. The template already has what is needed.

**Strip the instruction comment** at the top of your dated copy. Otherwise the
checks below, which read the whole file, will trip on the placeholders inside it.

---

## 3. Fill it in

**The edition line.** Replace the version number and date so it reads:

```
Version 3 (26th August 2026)
```

The number is the last edition plus one, read from `digest/version.txt`. If
that file is missing, treat the last edition as 0. The date is the Wednesday
this run happens, written with an ordinal and the full month.

Also replace the date in the page title, same Wednesday.

**The standouts block.** Write the "This week in the world of recruiting" preview, or delete both its
lines on a thin week. Keep the heading exactly as it ships. Then fill the rows
in the fixed order, deleting any that have no genuine pick.

```html
<li><span class="pick">Podcast</span><span class="body"><a href="URL" target="_blank" rel="noopener">item name</a><span class="why">the why</span></span></li>
```

The label sits outside the link, in its own column. The title is the only linked
text. The reason goes in its own span and renders on the line below. No comma
between them. Never hand-write widths, borders or inline styles, the template
handles all of it.

**The four sections.** Duplicate the example article inside each section for
your real items.

A normal item:

```html
<article class="item">
  <div class="chead"><span class="src">Source</span><span class="cdate">DD Mon 2026</span></div>
  <a class="ttl" href="URL" target="_blank" rel="noopener">title</a>
  <div class="guest">Name · Title @ Company</div>
  <ul class="pts"><li>point</li><li>point</li><li>point</li></ul>
</article>
```

The guest line is podcasts and tech picks only. The last item in each section
takes `class="item last"` to drop its bottom rule.

**Newsletter links in this build copy use the Gmail permalink**,
`https://mail.google.com/mail/u/0/#all/<threadId>`, in both the section item and
the standout row. This copy is Jamie's archive, so it links straight to the
issue in his inbox. Step 6 swaps them for public links on the copy that goes
live. If a newly subscribed newsletter has no issue email yet, use its public
URL in both copies.

A vendor with two or more releases gets ONE grouped article instead: a `.src` of
"Vendor · launches", a one-line vendor header in `.vgroup-title`, then a list
where each release is entirely wrapped in its own link, with the release name in
`.rt` and a plain one-liner after it. Each release links to its own page. A
single launch uses the normal article above with "Vendor · launch".

**Section counts.** Each section header carries a count. Set it to the number of
items in that section.

**Empty sections.** If a section has no items this week, delete the whole
section, header and all. No empty headings and no "nothing new this week" line.
A quiet week shows three sections, or two. The surviving sections keep their
order.

---

## 4. The quick checks

Run these first, before the fact-check. They take a second, and there is no
point spending a strong model verifying a file that fails one of them.

If any fails, fix it and run them again. If one cannot be fixed, do not publish,
and report it.

1. No `{{` anywhere in the file
2. Between one and four `summary class="sec"`, and every one that is present
   uses its exact shipped label
3. No em or en dashes in the body. The title in the head may keep its dash
4. The page title and the header both read "TheRecLab Weekly Digest"
5. The standouts heading reads exactly "Standout content from this week"
6. Every standout has its section present. A Podcast standout needs the Podcasts
   section, a Newsletter standout needs the Newsletters section, a Report or
   Launch standout needs section three, an AI pick needs the Tech Picks section.
   The reverse is not required: a section can exist with no standout. If this
   fails, the page is highlighting something that is not in it.
7. The duplication sweep is clean:

   ```
   python3 scripts/check_duplicates.py digest/builds/<file>.html
   ```

   The featured log stops repeats by exact key, which works for anything with a
   library file. It fails for launches and news, where one release gets linked
   from a changelog, a blog post and a release note, so three different URLs
   point at the same thing. This compares NAMES against everything featured in
   the last 8 weeks instead.

   It reports, it does not block. Some sources use formulaic titles, so "Week of
   August 10th" and "Week of August 17th" will always look similar and are
   fine. Read each flag and decide.

---

## 5. Fact-check

Hand the finished file, plus the library files each item came from, to a
verification helper on the strongest model available. Never anything less.

It opens each source and confirms that every number, tool name, date, company
and quote in the bullets and the standouts actually appears there. It checks the
"This week in the world of recruiting" preview only names topics the digest actually covers. It flags
any of the banned words or shapes from `STYLE.md`.

For any item with no library file, give the checker the URL rather than your own
summary of it, and let it read the page itself. Checking your wording against
your own notes only proves the wording matches the notes.

It returns either a pass or a list of mismatches, each one being the digest line
against what the source really says.

**Fix every mismatch from the source, or drop the line, then run it again.**
Nothing publishes with an open mismatch. Record the result for the health report.

---

## 5b. The final read

Run this AFTER every fact-check correction and after any edit. Corrections are
exactly when clumsy writing gets introduced, so it has to come after them.

```
python3 scripts/final_check.py digest/builds/<file>.html
```

Surface level on purpose: dashes, banned words and tics, lines that lean on the
one above them, two items opening the same way, bullets outside 15 to 35 words,
vague openings, engineering words a recruiter would not use, ideas welded
together with too many joins, and the brief mushing topics into one sentence.

## 5c. The run check

```
python3 scripts/run_check.py --pre
```

Everything else looks at the finished page. This looks at the RUN: did the week
actually happen. Every index rebuilt today, no index warnings, every episode
saved this run also summarised, the handover files dated today, the tools having
recorded that they ran.

**This is the one that catches a phase quietly not happening**, which no page
check ever will, because a digest built from a stale library looks perfectly
fine. On 27 August the summarising step was skipped and nothing noticed.

Run it again without `--pre` after publishing, and it also confirms the version
was written back, the edition was archived, and every featured item was logged.

## 5d. The structural check

```
python3 scripts/publish_check.py digest/builds/<file>.html
```

This is everything a person would otherwise catch by eye: section labels and
order, counts matching the real number of items, two or three bullets per item,
episode numbers stripped, date formats, everything inside the 8 week window,
freshest first, guest line format, brand credits, display names used instead of
library names, market figures naming their market, no more than two launch
blocks, and Brainfood never taking the podcast standout.

**These two run before Jamie is asked for anything.** He should never be the one
to notice a missing brand credit or a four bullet item. By the time the review
request reaches him, everything mechanical is already right and the only thing
left for him is judgement.

---

## 6. Make the public copy

The build file uses Gmail permalinks for newsletters, which only work for Jamie.
The public page needs public links.

Make a copy at a temporary path outside the digest folder, and swap each
newsletter link, in both the section item and the standout row, to that issue's
public archive URL. Use a small find-and-replace, not a rewrite of the whole
file.

If an issue has no public URL, use the newsletter's subscribe page from
`config/sources.yaml`. Ashby Community has no per-issue archive, so it always uses its
subscribe page. An event item keeps its event link.

**Then check the copy that is actually going live:**

```
python3 scripts/publish_check.py /tmp/public-<date>.html --public --links
```

`--public` refuses any Gmail link that survived the swap. If one does, every
newsletter link on the live page is broken for every reader, and nothing else in
the pipeline would notice.

`--links` requests every link on the page and reports anything that fails. It
needs network and takes a minute. Worth it: a dead link is the most visible
error a digest can carry.

Do not commit until this is clean.

---

## 7. Propose it for review

1. In a clone of the site repo, reset the `digest-review` branch to the latest
   `main`, so the preview shows this edition on top of the current live site and
   nothing else:

   ```
   git fetch origin main
   git checkout -B digest-review origin/main
   ```

2. Copy the public copy over `digest/index.html`. Change nothing else.
3. Commit with the message `digest: Version <N> - <Wednesday date>` and push the
   branch. The push may need `--force-with-lease`, because the branch is rebuilt
   from `main` each week; that is the one place a branch is ever rewritten, and
   only this branch.
4. Open a pull request from `digest-review` to `main`, titled the same as the
   commit. In the body: the edition line, the review address from
   `config/config.yaml`, the section counts, and the fact-check result.
5. **Confirm the preview built.** Wait for the Vercel deployment of that commit
   and check the review address shows this week's version number. A push that
   succeeded is not the same as a preview that built. If it has not built after
   ten minutes, say so in the health report rather than claiming it is ready.

Record the pull request number and link, and the review address, in
`_state/publish-report.json`.

**Never merge the pull request, and never push to `main` of the site repo.**
Jamie's merge is the green light.

**Do not touch `api/subscribe.js`** or anything else in the site repo. This job
only ever changes `digest/index.html`.

---

## 8. Record it, in the same breath

These go together with opening the pull request. Treat them as one action, not
as tidying up afterwards. The record is written now, as if the edition will go
live, and step 0 next week corrects it if Jamie did not merge.

0. **Write `_state/pending-review.json`**: the pull request number and link, the
   version number, the Wednesday date, and every featured-log row added below.
   This is what lets next week's step 0 undo the record if the edition never
   went live.

1. **Write the new version number** to `digest/version.txt`.
2. **Log every item featured** in `digest/featured-log.tsv`, one row each:
   date, source, item id, title. Every section item, plus the AI news item. Each
   release in a grouped launch gets its own row. Standouts point at items
   already logged, so do not log them twice. The item id is the library path,
   always the library folder name. See `SELECTION.md`.
3. **Archive the exact public bytes** to
   `digest/published/<YYYY-MM-DD>-v<N>.html`.

Nothing in `digest/published/` is ever deleted or overwritten. Every edition
survives in two forms: the build copy in `digest/builds/` with Gmail links, and
the published copy exactly as it went live.

**`digest/builds/` holds the current edition only.** The build copy exists to be
edited: when Jamie asks for a change after publishing, the change is made there
and the public copy is regenerated from it. Once the next edition is built, the
previous build has no job left, so delete it as part of step 1.

**`digest/published/` keeps every edition forever.** It is the record of what
readers actually saw, and it is what a rollback restores. Never delete or prune
anything in it.

None of these three files goes to the website. They live only in the project
folder.

---

## 9. Making edits after it is live

This is the normal case, not an exception. Jamie reads the live page and wants a
bullet changed.

1. Edit the dated build file, not the live page and not the template.
2. Rerun the quick checks. If the change touches a fact, a number or a tool
   name, rerun the fact-check on that item too.
3. Remake the public copy. If the pull request is still open, push it to the
   `digest-review` branch, and the preview updates. If it is already merged,
   reset `digest-review` from `main`, push the fix there, and open a new pull
   request titled `digest: edit Version <N>`.
4. **Keep the same version number.** An edit is a correction, not a new edition.
5. **Overwrite this week's file in `digest/published/`** so the archive matches what is
   actually live. Same filename, same version.
6. **Change nothing in the featured log.** The items are the same items.

If an edit removes an item entirely, delete its row from the featured log so it
stays eligible for a future week.

---

## 10. Putting it back

If a bad edition goes live and needs pulling:

1. Take the previous edition from `digest/published/`.
2. Put it on the `digest-review` branch over `digest/index.html` and open a pull
   request titled `digest: roll back to Version <N-1>`. Jamie merges it, and the
   site is back within a couple of minutes. (Jamie can also roll back instantly
   from the Vercel dashboard by promoting the previous deployment.)
3. Remove this week's rows from the featured log, so nothing is burned.
4. Leave the version file alone and fix the edition properly before republishing.

Never delete anything from `digest/published/`. It is the reason a rollback is
possible at all.

---

## 11. No email, ever

This job proposes the website edition and stops. It never sends the newsletter,
and it never creates a broadcast.

What happens next is human-gated:

1. The job Slacks Jamie that the edition is ready for review, with the review
   address and the pull request link.
2. Jamie reads the preview, asks for any edits, and merges the pull request to
   put it live.
3. On his green light, a **test email** goes to his own two inboxes only, so he
   sees the real thing in a real client.
4. Jamie reads the test, asks for any final edits, and gives a **second** green
   light.
5. Only then does the broadcast go to the list, scheduled for Thursday 08:00 by
   default.

No approval of the test that week means no email that week. The site still
updates either way.

The full runbook is `SEND_NEWSLETTER.md`. Do not start any of it from this job.
