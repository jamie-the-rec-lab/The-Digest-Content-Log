# Recruiting Research Library

A searchable archive of recruiting podcasts, newsletters and industry reports, stored as plain markdown so you can ask your AI questions across all of them. Everything lives under `library/`, split into collections so queries only load what they need: `podcasts` (the recruiting shows), `tech` (Lenny's Podcast, How I AI, AI & I, AI For Humans), `newsletters`, `reports` (industry benchmarks), `news` (product launches and the weekly AI news item) and `adhoc` (hand-picked one-offs).

## Collections

**Core — AI / TA strategy** (root `INDEX.md` + `library/podcasts/transcripts/`):

- `library/podcasts/transcripts/10x Recruiting/` — Metaview's 10x Recruiting (host: Nolan Church). 48 episodes.
- `library/podcasts/transcripts/Offer Accepted/` — Ashby's Offer Accepted (host: Shannon Ogborn). 77 episodes.
- `library/podcasts/transcripts/Brainfood/` — Hung Lee's Brainfood Live (2024 onwards). 122 episodes.
- `library/podcasts/transcripts/PromptMates/` — PromptMates, hands-on AI recruiting builds. 19 episodes.
- `library/podcasts/transcripts/Recruiting Future/` — Matt Alder's Recruiting Future (2024 onwards). 262 episodes.
- `library/podcasts/transcripts/Building the Talent Machine/` — Brandon Jeffs (2024 onwards). 44 episodes.
- `library/podcasts/transcripts/Recruiting Roadshow/` — Greenhouse's The Recruiting Roadshow (guest interviews; short teaser clips excluded). 10 episodes.

Default collection for AI, sourcing, interviewing and TA-strategy questions. Vocabulary in `TAXONOMY.md`.

**Frozen:** no longer auto-updated by the weekly job and excluded from the scout digest. The files remain fully queryable on demand — it just doesn't grow. Its strongest value to in-house TA is AI-adoption trends and sourcing craft; it's near-silent on candidate experience, assessment and internal mobility.

**Newsletters — written industry commentary** (`newsletters/INDEX.md` + `newsletters/transcripts/`):

- `newsletters/transcripts/PromptMates Newsletter/` — PromptMates weekly (AI recruiting). Ingested from email.

Short-form written pieces, ingested from the user's email inbox (not YouTube). Shares the core AI/TA taxonomy. More newsletters can be added by subscribing to them by email; see the refresh section.

**Reports — industry benchmark data** (`reports/INDEX.md` + `reports/transcripts/`):

- `reports/transcripts/<Publisher>/` — benchmark and trends reports from Ashby, Gem, LinkedIn, SHRM, iCIMS, Korn Ferry, HireVue and others, stored as markdown with a **Key figures** block of the actual numbers.

The place for hard benchmarks: time-to-fill, offer acceptance, recruiter capacity, source of hire, cost per hire and so on. Unlike podcasts and newsletters, report numbers stay useful for months, so this is the collection to query for a stat to quote in a workshop, blog or client build. Has its own `reports/TAXONOMY.md` (benchmark metrics, not just themes). Source list, search queries and the fetch method (many report pages block bots, so fetch via a real browser) live in `reports/SOURCES.md`; the per-file format is in `reports/FORMAT.md`. Refreshed by the weekly job, which also feeds the digest's Extras.

**Ad-hoc — hand-picked one-offs** (`adhoc/INDEX.md` + `adhoc/transcripts/`):

A manually-curated catch-all for individual items worth keeping that don't belong to a subscribed source: a single podcast episode or a one-off newsletter. Sub-foldered by type (`Podcasts/`, `Newsletters/`). NOT in the weekly scheduled job, it's filled by hand. Shares the core AI/TA taxonomy. NOTE: industry reports now live in the dedicated `reports/` collection, not here, drop report PDFs in `reports/_inbox/` instead.

To add an item: just tell Claude the link or file. A single YouTube video → `python3 scripts/fetch_transcripts.py "<watch-url>" "Podcasts" "adhoc/transcripts"`. A one-off article → Claude fetches and cleans it. Then Claude tags it and runs `python3 scripts/build_index.py adhoc`. (For an industry report, drop the PDF in `reports/_inbox/` and it gets ingested into the reports collection.)


## What each file is

- `scripts/fetch_transcripts.py` — pulls and cleans transcripts (adds clickable timecodes).
- `scripts/build_index.py` — rebuilds an index from its transcripts + summaries file.

Each core transcript opens with a rich **Actionable summary** block wrapped in `<!--SUMMARY-->` / `<!--/SUMMARY-->` HTML-comment markers (invisible when rendered, trivial to slice out). It carries the guest, when to use the episode, the big idea, frameworks and plays with worked examples, data and benchmarks, named tools and prompts, any contrarian take, and steal-this actions. This is the retrieval layer: read these blocks to answer a question, and only open the full transcript when you need a verbatim quote or a timecode. The recipe is locked in `docs/SUMMARY_SPEC.md`; the weekly job writes one for every new episode.

Below the summary, each transcript has a metadata header (podcast, date, duration, YouTube URL), the episode description, then the transcript. Every paragraph starts with a clickable timecode linking to that exact second on YouTube, so any quote can be traced back to the moment it was said.

## How to query it

Just ask in plain English, for example:
- "Search the library for what guests say about AI sourcing and summarise the main takes, with links."
- "Which episodes discuss employer branding? Pull the relevant quotes."

### Retrieval recipe (summaries-first)

Answer topic questions from the summary layer, not from whole transcripts. The order is:

1. **Find the candidates by grep, do not load the whole index.** The core `INDEX.md` is large (tens of thousands of tokens) and grows weekly, so searching it beats swallowing it. Grep the index or `episode_summaries.tsv` for the topic's tags or keywords and take only the matching file paths, for example `grep -i "sourcing\|outbound\|talent pool" episode_summaries.tsv`.
2. **Read the summaries, not the transcripts.** For each candidate file, slice out just its Actionable summary block: `sed -n '/<!--SUMMARY-->/,/<!--\/SUMMARY-->/p' "<file>"`. This returns a rich, standalone summary per episode, so cost scales with the answer rather than the size of the library.
3. **Answer from those summaries**, with links back to each episode.
4. **Only open a full transcript** when you need a verbatim quote or the exact timecode behind a specific claim, and even then open just the one file you need.

For big topic sweeps, run steps 1 and 2 inside a sub-agent so the sliced summaries stay out of the main context, then answer from what it returns.

Older files that predate the summary layer, and newsletters and reports (which keep their own shorter records), simply won't have a `<!--SUMMARY-->` block; for those, fall back to the one-line index summary and open the file only if the question needs more.

## Refreshing for new episodes

This runs automatically every Monday via a scheduled task ("fetch-recruiting-podcast-transcripts") that fetches new episodes for both collections, summarises and tags them, and rebuilds both indexes. To do it manually:

Core:
```
python3 scripts/fetch_transcripts.py "https://www.youtube.com/@10x_Recruiting_pod/videos" "10x Recruiting"
python3 scripts/fetch_transcripts.py "https://www.youtube.com/playlist?list=PLrd3ZPgPqLzmHvhgRKY0IH_5-1TuiDLDM" "Offer Accepted"
python3 scripts/fetch_transcripts.py "https://www.youtube.com/channel/UCNJ1ECjprHORfyAbE5qyqcg/videos" "Brainfood"
python3 scripts/fetch_transcripts.py "https://www.youtube.com/channel/UCBK-L-lWoLkSZw93S3f5VhQ/videos" "PromptMates"
python3 scripts/build_index.py
```

```
```

Newsletters (ingested from email, not a script): subscribe to the newsletter so it lands in Gmail, then the weekly scheduled task searches for new issues by sender, reads each, and writes them into `newsletters/transcripts/`. To add a newsletter, subscribe by email and add its sender address to the newsletter section of the scheduled task. (RSS was evaluated but the available tools cap browser feed-reading too aggressively to pull full posts; email delivers the whole issue reliably, so email is the chosen route.)


## Notes

- Transcripts come from YouTube auto-captions: expect the odd misheard word or missing punctuation. Good for search and summary; check the audio (via the timecode link) for exact quotes.
- Some videos (trailers/shorts) have no captions and are skipped.
- Offer Accepted and Elite Recruiter occasionally re-run older episodes, so a few near-duplicates exist; worth bearing in mind for "how common is this view" style questions.
