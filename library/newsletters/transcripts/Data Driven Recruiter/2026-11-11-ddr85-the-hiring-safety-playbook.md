# Issue 85 - The Hiring Safety Playbook

- **Source:** Data Driven Recruiter
- **Date:** 2026-11-11
- **Fetched:** 2026-11-16
- **Public:** https://data-driven-recruiter.beehiiv.com/p/ddr85-the-hiring-safety-playbook

## Newsletter

(Email subject: "DDR85 - The Hiring Safety Playbook". By Luke Eaton. The "word from our sponsor" in this issue is a joke, attributed to Kim Jong Un; there is no real sponsor. Do not treat the satirical sponsor text as content.)

Intro: "Two weeks ago, I put a newsletter out saying that recruitment is at the forefront of cybercrime. One day later, the biggest hack in history happened at Binance. $6.3 billion was stolen from their hot wallets, and one of the main points of ingress was from a recruitment scam." He has spent two weeks with his CISO: "I offer to you as a gift my 2026 hiring safety playbook." Promotes the PromptMates live session "Hiring Fraud: The $6bn Interview", 11 November, 5pm GMT (12pm ET).

### Why this matters now: Binance was hacked through a job interview

"On 29 October 2026, attackers took about $6.3 billion out of Binance, the largest crypto theft on record. The FBI attributes it to North Korea’s TraderTraitor group; North Korea denies it."

- June: "A DevOps engineer downloads a tampered Homebrew installer while looking for an AI coding tool."
- September: "A second engineer is approached on a legitimate job-hunting platform by a “Project Director”." A fake HR contact shares personal photos and videos; a fake "CEO" interviews on a chat app.
- The assignment: "he is asked to download a technical “assignment” onto his work computer. It contains malware that runs during setup and is not picked up by Binance’s endpoint tools."
- 20 October: attackers use that laptop and an internal AI tool to reach two more engineers and find a token with container-deployment permissions.
- 29 October: "About $6.34 billion in assets are affected; roughly $2.85 billion is frozen or intercepted by 3 November."

Figures given:
- "**30,000+** devices infected in 100+ countries by one fake-interview group in eight months (joint advisory, 18 Sept 2026)". The advisory's issuers are not named.
- "**$14.3m** lost to dozens of smaller fake-interview attacks in the 18 months before Binance (Chainalysis)"
- "**57** North Korea-linked attempts Binance says it detected and stopped in 2026, including fake interviews"

"Recruiting is a trusted channel: people welcome a recruiter’s message instead of questioning it." "You are exposed in both directions."

### Three ways recruiting gets attacked

1. Fake recruiters using your name: lookalike domains, fake recruiter profiles, ads you never posted. Watch for candidates asking about interviews you don't recognise, profiles claiming to be in your team, lookalike domains, candidates mentioning tools you don't use.
2. Fake recruiters aimed at your people: "The hook is a coding test, a “driver fix” before a video call, or a command to paste." Watch for assignments sent as repos, zip files or npm packages; camera or audio "error" fixes; chat-app interviews; pressure to run something on a work laptop.
3. Fake candidates applying to you: "State-linked IT workers and fraudsters apply for remote roles with stolen or forged identities". Watch for broad skill lists they can't discuss, glancing at another screen, face-swap video that goes off "for network reasons", reluctance to meet in person, pay requested to a third party.

### The setup guide: your candidate trust stack

"Eight steps. A small TA team can get through all of them in a week."

1. Name your recruiters: list everyone who recruits for you with title and LinkedIn link, publish on the careers page, link from every job ad, "say plainly that anyone not listed is not you."
2. Own one email domain: never recruit from personal Gmail, Telegram or WhatsApp; set up SPF, DKIM and DMARC; register obvious lookalikes.
3. Publish your hiring stack: list the tools a candidate will meet; prefer browser-based tools; "you will never ask anyone to install software to join an interview."
4. State your agency policy: none, or name each agency with domain and contact; review quarterly.
5. Write your "never" list: "We never ask you to install software, run a command or download a file to join an interview. We never ask you for money, equipment deposits, or bank, card or ID details before an offer is signed."
6. Publish it where candidates look: careers page, job-ad template, ATS footer, first outreach, calendar invites, inbox auto-reply, LinkedIn company page, offer email.
7. Make your own process look nothing like a scam: "No take-homes as zip files or repos that candidates must run locally. Use a hosted environment, a live session or a read-only review." No chat-app interviews.
8. Monitor, log and report: monthly LinkedIn search for people using your company name with recruiter titles ("Admins of a verified company page can remove people falsely claiming to work there, so get your whole TA team verified"); search job boards for ads you didn't post; log every report; report to the platform and to Action Fraud (UK) or the FBI's IC3 (US).

### Protect your own people (take this section to IT)

Tell high-access staff they are targets; never run interview code on a work machine ("be wary of commands containing curl, base64, -enc, mshta, Invoke-WebRequest or “hidden”"); open unknown projects in VS Code Restricted Mode; keep standing credentials off laptops, use hardware-key MFA; limit what internal tools (including AI assistants) can reach; install from official sources only; run EDR and make no-blame reporting easy.

### Harden your onboarding

"One group infected 30,000+ devices in eight months with fake coding tests. In a niche talent market, that is a meaningful slice of your candidate pool." "The weak spot: the laptop arrives late, so for week one your new hire logs into email, Slack, GitHub and your ATS from their home machine." "No company device, no system access. Kit lands before day one, or day one moves." Ban personal machines for company systems; get IT and TA in a room to map offer to first login; start with least access; verify identity on day one.

### Hiring-side checks: spot fake candidates

Verify identity twice (before offer and day one); confirm history directly with past employers, wary of references reachable only on Telegram or WhatsApp; probe every listed skill; ask human questions (hometown, local weather, what's outside the window); watch the video call; "Run pay through normal payroll to an account in the employee’s own name. A request to pay a third party is a big red flag."; compare IP address with claimed location; "Escalate, don’t confront." "Knowingly paying one may breach sanctions law."

### Copy-and-paste templates

Careers-page notice, job-ad line, first-outreach email footer, calendar-invite line, agency statement and offer/onboarding email line. Example job-ad line: "Recruiting at [Company] is always free. Our recruiters email only from @[yourdomain.com] and are listed at [careers URL]. We will never ask you to install anything or pay for anything."

### Incident response

Seven steps: disconnect; rotate from a clean device; assume anything on it is out; preserve evidence; report ("Action Fraud (0300 123 2040) in the UK; FBI IC3 (ic3.gov) in the US"); wipe or replace; review the blast radius.

### The checklist at a glance

Four groups: Publish, Distribute, Protect, Monitor (as above).
