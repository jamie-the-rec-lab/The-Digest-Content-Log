# SELECTION: which items make the cut

This file decides WHAT goes in. `STYLE.md` decides how it reads.

The guiding rule sits in `RUN.md`: quality over volume, every time. A short,
honest edition beats a padded one.

---

## 1. The two gates

An item is eligible only if BOTH are true:

1. **It was published within the last 8 weeks.**
2. **It has never been featured before.**

Anything failing either gate is out, however good it is.

A source with nothing new simply does not appear this week. Do not go looking
for an older item to fill its place. Digest length varies week to week and short
weeks are normal.

---

## 2. How "featured before" is checked

Every item featured gets logged in `digest/featured-log.tsv`. Before selecting,
read that log and exclude anything already in it.

**The key is the library path**, not the title and not the link. Titles get
reused and links change, the library path does not.

| Type | Key |
|---|---|
| Podcast | `Show/file.md` |
| Newsletter | `Newsletter Name/file.md` |
| Report | `Publisher/file.md` |
| Tech pick | `Show/file.md` |
| Launch | its URL |
| AI news | its URL, or `ainews/YYYY-MM-DD-slug` if it has none |

**Always the library folder name, never the display name.** So
`PromptMates/...` not `PromptMates Live/...`, and `RecOps Collective/...` not
`RecOps Roundup/...`. See `config/sources.yaml`.

For a grouped vendor launch, each release is checked and logged separately by
its own URL.

**If the log has been deliberately wiped** to start fresh, treat it as correct.
Do not rebuild the history from whatever page happens to be live, and do not
drop a strong item because an old test page once used it.

**Never prune the log.** It is small, and it is the only record of what has
earned a place.

---

## 3. Reader fit

Read `READER.md` before selecting. Being in window and unfeatured is not enough.
An item has to earn its place with this reader, and if it does not, drop it.

Two hard rules from that file:

- **Never feature a report the reader would have to pay for.** A free email
  signup is fine. Money is not. The link must never land on a paywall.

---

## 4. What fills each section

### Section 1: Recruiting Podcasts
The newest unfeatured in-window episode from each recruiting show. Freshest
first. Recruiting shows only, no tech.

Recruiting Roadshow: full interviews only, never the short teaser clips.

### Section 2: Recruiting Newsletters
The newest unfeatured in-window issue from each newsletter. Order by interest,
so AI-in-talent first, then freshest first.

### Section 3: Recruiting reports, product updates, and more
This section is REPORT-LED, and it is RECRUITING ONLY. Order within it:

1. Reports from the tracked publishers
2. Wider-net "curve ball" reports, at the end of the reports group
3. Events
4. Product launches
5. Essays

Two to five curve ball items, so the section is not only reports and launches.

Everything here must be about recruiting, talent or the hiring market. General
AI news and AI regulation belong in Section 4, even when a recruiter would find
them interesting. An AI item earns a place here only if it is genuinely about
hiring: an ATS vendor's release, or a regulation whose subject is recruitment.

### Section 4: AI & Tech Picks
This section is where the AI material goes. It holds two kinds of item:

1. The newest unfeatured in-window episode from each of Lenny's Podcast, How I
   AI, AI & I and AI For Humans, freshest first.
2. Any standalone AI news or AI regulation item, including the weekly AI news
   scan, placed after the episodes.

This section sits last.

**Subject gate, on top of the two gates, for the EPISODES only.** These shows
cover product and startups generally, so most of what they publish is not for
this reader. The gate does not apply to news items, which are chosen by the AI
news scan in `REFRESH.md`. An episode only
qualifies if it is about **AI**, or about **hiring, talent, teams or people**.

Everything else is dropped, however good it is and however new. An 84 minute
masterclass on enterprise sales technique is a fine episode and belongs nowhere
near this digest.

Judge it from the title and description. If it is borderline, drop it: this
section is a bonus, not an obligation. If no episode from a show qualifies, that
show simply does not appear, and if none of them qualify, the whole section
goes.

### Never go backwards through a dated series

**A pick must be NEWER than the newest item already featured from that same
source.** Being unfeatured and inside the 8 week window is not enough. That is
the floor, not the test.

This applies to every dated series: podcasts, tech shows, newsletters and
recurring reports alike. If a newer episode or edition has already been featured,
an older one never runs afterwards, even though no-repeats technically allows it.
Publishing July's workforce report a week after August's went out, or episode 819
a week after episode 820, reads as a mistake to anyone paying attention.

That source simply sits out until its next item. A show with nothing newer does
not appear, and short weeks are normal.

**Why this needs stating so plainly.** If the library gains OLDER items between
editions, from a backfill or a fetch that reached further back than usual, they
arrive unfeatured and inside the window and look exactly like valid picks. They
are not. On 3 September 2026 this put six podcast items into a published edition
that were older than the episode featured from that same show the week before,
including episode 819 following episode 820. The edition had to be corrected
live.

The check is mechanical, so do it mechanically: for each source, find the newest
date already in `featured-log.tsv`, and only consider items after it.

### Empty sections
If a section has nothing new, drop the whole section from this week's edition.
No empty heading, no "nothing new this week" line. A quiet week is simply a
shorter page. The sections that remain keep their order.

Never pad a section to keep it alive.

---

## 5. Product launches

Gathered fresh each week by the Phase 1 launch sweep, `REFRESH.md` Collection 6,
from the vendors in `config/sources.yaml`. They reach Phase 2 in the run report
like everything else. Then curated hard.

- **Group by vendor.** One block per vendor, its releases become the bullets,
  biggest first, maximum three. Never two separate rows for the same vendor.
- **Maximum two vendor blocks a week, total.** On a strong reports week, drop to
  one or none. Launches are the tail of section 3, never the bulk.
- **Only genuinely material releases.** A net-new product, a major AI
  capability, a notable acquisition. Ignore minor tweaks, new integrations and
  UI changes, even from a tracked vendor.
- **Tier A first.** Ashby, Greenhouse, Metaview, Teamtailor, Gem, Pinpoint,
  Juicebox, Pin, Jack & Jill. A tier B vendor only takes a slot when its launch
  clearly outweighs anything tier A shipped that week.

---

## 6. The standout rows

Up to five, in this fixed order: **Podcast, Newsletter, Report, Launch, AI
pick.** How they are written is in `STYLE.md`.

A standout is always the strongest of THIS week's already-featured items in that
category. It is never a separate pick and never something not otherwise in the
digest.

**Signals to weigh**, not a checklist an item must tick every box on:

1. A hard, quotable number the reader could take to a stakeholder
2. A named tool or concrete tactic they could try this week
3. A genuinely contrarian take that would change how they act
4. The credibility of the person speaking, judged from the title and
   description: seniority, a relevant senior role at a company that matters,
   real operator experience

When two are close, favour the more recent and the more practical. Practical and
actionable always beats interesting in the abstract.

### Per slot

**Podcast.** Always a recruiting show. The practical, creative, data-backed
episode with a clear purpose. **Never Brainfood.** If Brainfood is the only new
recruiting episode that week, drop the row rather than default to it. A tech
episode can take this slot only if it is clearly the best podcast all week.

**Newsletter.** The issue that hands the reader the most usable thing: a
specific prompt, workflow, named tool, tactic, or a hard number. Favour the
AI-in-talent issues. If the strongest issue is purely news aggregation with
nothing to act on, drop the row rather than force it.

**Report.** The freely readable report whose number the reader could take to a
stakeholder.

**Launch.** The release that would most materially change how the reader works.
Tier A favoured. If the featured launch is a grouped vendor block, point the row
at the single most material release.

**AI pick.** The strongest EPISODE from AI & Tech Picks. A standalone AI news or
regulation item sits in section 4 as a normal item and is never the standout: the
row is for an episode worth an hour of the reader's time, not for a headline.

### Dropping rows
Report, Launch and AI pick are conditional. Include each only if there is a
genuine standout, and delete the row otherwise. Podcast and Newsletter will
almost always be there, but on a very quiet week even those can go.

Keep whatever survives in the fixed order. Do not reorder.
