# Who Gets to Win the AI Talent Boom?

- **Source:** PromptMates Newsletter
- **Date:** 2026-09-01
- **Fetched:** 2026-09-03
- **Public archive:** https://promptmates.beehiiv.com/p/who-gets-to-win-the-ai-talent-boom

## Build of the Week: How a Recruiter Built His Own Recruiting Intelligence Platform

Michael Brinn, without an engineering background, built Insyt, a recruiting intelligence platform with role-based dashboards, candidate probability scoring, interviewer calibration, and automated alerts.

1. Write the spec before you build - used Claude to define Insyt's three user views, scoring model, and permissions before building a single screen.
2. Prove the idea with an AI app builder - Lovable for the prototype, Supabase for the database.
3. Move to a real codebase when you outgrow the prototype - moved into GitHub, used Claude Code, working through features with branches, pull requests and browser testing.
4. Build around recruiting decisions, not generic dashboards - different views for recruiters, hiring managers and executives; scoring engine calibrates for interviewers who score harder or easier than peers.
5. Automate the signals recruiters need to act on - alerts for stale candidates, high-potential applicants, falling fill probability, checked every 15 minutes.

Source: https://medium.com/@mikebrinn4/i-built-a-recruiting-intelligence-platform-without-being-able-to-code-d48907d05a8b

## Worth Seeing & Reading

- **Nobody Wants to Own Candidate Fraud** - Kyle Lagunas investigated candidate fraud over the summer and found CISOs are not claiming responsibility, while TA still lacks clear rules with candidates about acceptable AI use. https://www.ere.net/articles/nobody-wants-to-own-candidate-fraud
- **New H-1B Fees Are Coming in September** - Employers filing certain H-1B extensions face an additional $4,000 fee starting September 9; some L-1 extensions carry an extra $4,500 charge. https://www.shrm.org/topics-tools/news/dhs-proposes-new-h1b-fee-103k
- **Seven Things Recruiting Leaders Still Won't Let AI Do** - Seven boundaries AI-native TA leaders have drawn, e.g. a CPO whose coaching agent will not write the performance review, a Zapier talent engineer whose AI drafts interview prep but never runs the call. Pattern: decision support, never the decision itself.
- **AI Talent Is Flowing Out of the Labs** - Jason Salt tracked senior AI talent moving from OpenAI, Anthropic and Google into healthcare, finance, legal, education and other industries.

## Platform Updates

- **OpenAI**: previewing Private Safety Processing, which can detect misuse across multiple interactions without staff accessing underlying prompts/responses, for teams on Zero Data Retention.
- **Juicebox**: launched Agent 4.0 with a Context Intelligence Layer pulling context from ATS data and meeting notes before starting a search.
- **Thomson Reuters**: built its own specialized LLM ("Thomson") for $40 million using an open-source foundation and proprietary legal/tax/news data; trained on less than 10% of its content so far, early internal evals put it on par with leading frontier models on professional tasks.

## Big Idea

AI job postings in the US have roughly doubled since 2023, typical advertised salary around $177,000. Women accounted for just 26% of US AI hires in 2025, and hold only 13% of C-suite AI leadership roles at AI companies across 27 countries (LinkedIn research). "AI jobs are booming, but access to them isn't being distributed evenly."
