# Per-report file format

One markdown file per report at `reports/transcripts/<Source>/<YYYY-MM-DD>-<slug>.md`.
Store reports the SAME way as podcast transcripts and newsletters: keep the FULL
extracted report text as the body, with a **Key figures** block pinned at the
top for fast lookup and citation. Keep the header fields exactly as below so
`build_index.py reports` can read the title, date and URL. Never invent a
figure; only record what the source states.

```
# <Report Title>

- **Source:** <Publisher, e.g. Ashby>
- **Date:** <YYYY-MM-DD real publish/refresh date>
- **URL:** <canonical report URL>
- **Fetched:** <YYYY-MM-DD>
- **Sample:** <sample size / dataset, e.g. "109M applications across 247k jobs at 1,200+ startups">
- **Extraction:** <full | partial — say why if partial, e.g. "summary page only; PDF gated">

## Key figures
- <one stat per line, with the number, quoted faithfully from the report>
- ...

## Full report
<the full extracted report text, cleaned of nav/boilerplate/ads. Preserve
section headings and any figures/tables as text. This is the durable copy, so
capture as much as the source allows.>
```

## Extraction rules
- Aim for the FULL text. Try mcp__workspace__web_fetch first; on a 403 or a
  JS-only shell, use the Claude-in-Chrome tools (navigate + get_page_text). For
  a PDF, download it and extract with the pdf skill.
- FALLBACK: if the full report cannot be reached (e.g. the real PDF is gated and
  only a summary/landing page is accessible), store the best text you can get,
  fill the **Key figures** you can see, and mark `Extraction: partial` with the
  reason. A partial record is still worth keeping; the URL stays in the header so
  the original is one click away.
- Never fabricate: if a number cannot be read from the source, omit it.

Then add a tagged one-line summary to `reports/episode_summaries.tsv`:
`<Source>/<file>.md|||one-line summary|||<Publisher>|||tag1, tag2, ...` (6-10 tags from reports/TAXONOMY.md),
and run `python3 build_index.py reports`.
