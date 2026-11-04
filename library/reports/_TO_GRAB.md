# Reports to grab manually

The weekly job writes this list: reports it found within the 8-week window but
could NOT fetch in full (email-gated, login/member-walled, or PDF behind a form).
Grab any you want the full text of, then drop the PDF into `reports/_inbox/`
(or paste the text) and it gets ingested and indexed automatically. Delete a
line once it has been captured full.

## Currently outstanding (as of 2026-09-17)

- REC/2026-09-07-report-on-jobs-september-2026.md — KPMG and REC UK Report on Jobs, September edition (August data). Full index data confirmed subscription-only (economics@spglobal.com); the KPMG page states "Full reports and historical data from the KPMG and REC, UK Report on Jobs are available by subscription." This is a genuine registration/subscription wall, not a fetch failure — treat as a **permanent gate**, do not retry. Press-release summary is captured in full; record stays `Extraction: partial`. The August edition (REC/2026-08-10-report-on-jobs-august-2026.md) is superseded and stays in the library as-is.

## Resolved this pass (2026-09-17)

- CIPD/2026-08-16-labour-market-outlook-summer-2026.md — upgraded to full text. The source PDF at cipd.org was directly downloadable (no gate); re-fetched and parsed in full.
- iCIMS/2026-09-10-workers-teaching-themselves-ai-skills.md — upgraded to full text. The full 16-page "September 2026 Workforce Report" PDF was found via icims.com/company/corporate-newsroom/research/, served through a FlowPaper flipbook whose PDF download endpoint (`.../docs/<filename>.pdf`) was reachable directly; not gated, just not linked from the press release page.

## Flagged 2026-09-30 (not ingested)

- Draup, "Macro Labor Market Trends 2026: A Draup Perspective" (press release dated 2026-09-30 on PR Newswire: prnewswire.com/news-releases/draup-report-finds-ai-builder-roles-now-claim-27-of-tech-demand-as-companies-rethink-hiring-302893864.html). Vendor report on its own dataset ("more than one billion tracked profiles and job descriptions", cohort data corroborated against the Stanford Digital Economy Lab). Full report is behind a form on the Draup site. Borderline under the reputability bar (vendor press release, methodology only described in one line), so flagged for a human look rather than ingested. Headline figures in the release: AI Builder roles at 27% of technology demand; internships and contract roles 27% of early-career hiring, up from 13% in 2020.
- Indeed Hiring Lab UK, "UK Labour Market Snapshot, September 2026" (published 2026-09-28, hiringlab.indeed.com/uk/blog/2026/09/28/uk-labour-market-snapshot-september-2026/). Watchlist item, new edition in window. The fetch returned "Too many redirects" on every attempt, so it is not captured. If it still fails next week, drop the PDF or text into _inbox/.

## Flagged 2026-10-07

- Criteria Corp, Ninth Annual Hiring Benchmark Report 2026-2027 (published 2026-10-06, criteriacorp.com/research/2026-2027-hiring-benchmark-report). Ingested as partial (press release plus landing-page preview, 1,027 US hiring professionals). Full report is behind a download form; drop the PDF into _inbox/ to upgrade.
- Indeed Hiring Lab UK, UK Labour Market Snapshot September 2026 (published 2026-09-28): still returns "Too many redirects" on 2026-10-07 (2nd week). Not captured.

## Flagged 2026-10-17

- ISE/2026-10-14-student-recruitment-report-2026.md - ISE Student Recruitment Report 2026 (ise.org.uk/knowledge/research/606/ise_student_recruitment_report_2026). Ingested as partial: only the sample (155 employers, 1.7m+ applications, 31,577 hires) is on the ISE page; the statistics come from press coverage (Resultsense 14 Oct, HR Grapevine 15 Oct). Full report is members-only or about 216.67 GBP plus VAT. Drop the PDF into _inbox/ for the full text.
- iCIMS/2026-10-08-workforce-report-october-2026.md - October 2026 Workforce Report: only the 8 Oct press release was read, the full report PDF was not retrieved.
- REC/2026-10-10-report-on-jobs-october-2026.md and Bullhorn weekly indicator (weeks ending 26 Sep and 3 Oct): public headline figures only, full data is subscription or members-only.
- Indeed Hiring Lab UK, UK Labour Market Snapshot (September and October 2026): not retried this run (it failed twice before with "Too many redirects"); a search found no October edition. Left for next week.

