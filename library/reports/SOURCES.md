# Reports collection — source list, queries and fetch method

Seed configuration for the automated reports scout. Mirrors the other
collections: one markdown file per report under `transcripts/<Source>/`, a
tagged one-line summary in `episode_summaries.tsv`, index rebuilt with
`python3 build_index.py reports`.

## Target sources (direct pages to check each run)

| Source        | Page to check |
| ------------- | ------------- |
| Ashby         | ashbyhq.com/talent-trends-report |
| Gem           | gem.com/resource-library |
| LinkedIn      | business.linkedin.com/talent-solutions/resources ; business.linkedin.com/hire/resources/future-of-recruiting |
| Greenhouse    | greenhouse.com/guidance ; greenhouse.com/recruiting-benchmarks |
| Lever         | lever.co/resources |
| iCIMS         | icims.com/hiring-insights |
| SHRM          | shrm.org/topics-tools/research |
| Korn Ferry    | kornferry.com/insights |
| Josh Bersin   | joshbersin.com/research |
| Workday       | workday.com/resources |
| Beamery       | beamery.com/resources |
| HireVue       | hirevue.com/resources |
| GBD Talent    | gbdtalent.com/talent-insights |
| Lighthouse    | lighthouse.lsvp.com/reports |
| Employ Inc.   | employinc.com/resources (Employ / JazzHR / Lever hiring benchmarks) |
| Metaview      | metaview.ai/resources (AI & Hiring Alignment Report) |
| Deloitte      | deloitte.com/insights (Human Capital Trends, Gen Z survey) |
| Phenom        | phenom.com (State of AI & Automation for HR) |
| Bullhorn      | bullhorn.com/resources (GRID Talent Trends) |
| NACE          | naceweb.org/research (Job Outlook) |
| REC           | rec.uk.com/our-view/research (Report on Jobs w/ KPMG, JobsOutlook) |
| CIPD          | cipd.org/uk/knowledge (Labour Market Outlook, Resourcing & Talent Planning survey) |
| APSCo         | apsco.org/insights (staffing/agency market data) |
| ISE           | ise.org.uk/research (Institute of Student Employers — early careers) |
| ONS           | ons.gov.uk/employmentandlabourmarket (UK labour market stats) |
| Hays UK       | hays.co.uk/salary-guide |
| Robert Walters| robertwalters.co.uk/insights/salary-survey.html |
| Reed          | reed.co.uk/recruiter-advice (salary guides, market reports) |

These UK sources are added because the audience is UK TA. Many are gated or
PDF-only, so expect the unattended scout to flag them to `_TO_GRAB.md` rather
than ingest them directly; seed the flagship ones (CIPD Resourcing & Talent
Planning, REC Report on Jobs, ISE student recruitment survey) via `_inbox/`.

## Search queries (fallback discovery)

1. "recruiting benchmark report 2026 new"
2. "talent acquisition trends report 2026 data"
3. "hiring benchmarks 2026 methodology"
4. "recruiter productivity report 2026"
5. "candidate experience survey report 2026"
6. Site-restricted search across the sources above (Ashby, Gem, LinkedIn, Greenhouse, Lever, iCIMS, SHRM, Korn Ferry, Josh Bersin, Workday, Beamery, HireVue, GBD Talent, Lighthouse, Employ, Metaview, Deloitte, Phenom, Bullhorn, NACE, REC, CIPD, APSCo, ISE, ONS, Hays, Robert Walters, Reed).
8. UK-focused: "REC report on jobs 2026" OR "CIPD labour market outlook 2026" OR "CIPD resourcing and talent planning 2026" OR "ISE student recruitment survey 2026" OR "UK hiring trends 2026".
7. "talent acquisition benchmark data 2026 Korn Ferry OR Bersin OR Gartner OR Mercer OR Workday OR Greenhouse OR Lever OR Deloitte OR Metaview"

## GENERAL DISCOVERY (net-new reputable reports we'd otherwise miss)

Each run, ALSO do a broad web search (WebSearch) for recruiting/TA/hiring
research published in the last 8 weeks, NOT limited to the sources above. The
point is to catch a strong report from a publisher we haven't catalogued yet.
Run a few broad queries such as:
- "recruiting report 2026" / "talent acquisition report 2026" / "hiring report 2026" newer results
- "state of recruiting 2026" OR "state of hiring 2026" OR "state of talent acquisition 2026"
- "candidate experience report 2026" / "recruiter survey 2026" / "future of hiring 2026"
- "<this month> 2026" + "recruiting benchmark" OR "talent acquisition study"

REPUTABILITY BAR (only ingest or flag if it clears this, otherwise ignore):
- Published by a credible originator: an established ATS/HR/recruiting vendor
  reporting its own platform data, a recognised analyst/research firm, a major
  consultancy, a professional body/association, a university, or a well-known
  job-market data source.
- Has a real METHODOLOGY: a stated sample size, dataset, or survey base. If you
  cannot find who produced it or how, do NOT add it.
- Is PRIMARY research, not a content-marketing listicle, an SEO "X stats you
  need to know" roundup, a press-release rewrite, or an aggregator blog quoting
  other people's numbers.
- Is genuinely NEW to this library (not already in episode_summaries.tsv) and
  within the 8-week window.
When in doubt, prefer to FLAG it in _TO_GRAB.md for human review rather than
ingest, so a borderline source never quietly pollutes the library.

## FETCH METHOD (IMPORTANT — read before scouting)

The pipeline runs UNATTENDED, so do NOT use a browser (no Claude-in-Chrome).
Only two fetch methods are used:

1. Try `mcp__workspace__web_fetch` (cheap; works for many report/landing pages).
2. For a report PDF that is directly linked, download it and extract text with
   the `pdf` skill.

If a report is **gated** (HTTP 403 to bots, an email-capture form, or a member
/login wall) so neither method gets the full text, DO NOT store a thin stub and
DO NOT try a browser. Instead add it to `_TO_GRAB.md` (title + link) so the user
can grab it and drop the PDF into `_inbox/`. A short partial is acceptable only
if the publicly readable summary carries real key figures (mark Extraction:
partial and still add it to _TO_GRAB.md). Never invent a figure; if a number
cannot be read from the source, omit it.

## Freshness

Only ingest reports genuinely published or refreshed in the last ~8 weeks
(match the digest's cutoff). Skip anything already in `episode_summaries.tsv`.
