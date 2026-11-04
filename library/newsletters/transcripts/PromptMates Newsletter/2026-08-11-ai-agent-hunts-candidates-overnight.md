# This AI agent hunts candidates while you sleep
- **Source:** PromptMates Newsletter
- **Date:** 2026-08-11
- **Fetched:** 2026-08-14
- **Public URL:** https://promptmates.beehiiv.com/p/this-ai-agent-hunts-candidates-while-you-sleep

## Newsletter

Welcome back to PromptMates Weekly.

This week: an open-source sourcing agent finds newly available talent overnight, new AI legislation just came into effect, and the problems that start after an AI workflow actually goes live.

Plus: Claude Code for non-coders, a recruiter-built AI knowledge base, LinkedIn's latest labor market data, and new platform updates from Google, Microsoft, and OpenAI.

### LIVE THIS WEEK!

**Personal Branding for Recruiting & HR**

Wednesday, August 12 at 12:00 PM EDT / 5:00 PM UK

Recruiting leader at Zapier, Bonnie Dilber, joins us to break down personal branding for talent acquisition and HR professionals.

Bonnie has built one of recruiting's largest personal brands, with more than 500,000 LinkedIn followers, while leading GTM and ops recruiting at Zapier. She'll share how to grow a brand with intention, create LinkedIn content that reaches the right audience, and balance it all alongside a full-time recruiting career.

---

## **BUILD OF THE WEEK**

**How to build a zero-code AI agent that spots newly available talent overnight**

Bryan Hong (Director of People Ops & Systems) built Talent Alpha, an open-source n8n workflow that hunts for candidates before they update their LinkedIn headline. Instead of waiting for someone to apply, it scans WARN layoff filings and funding-distress news overnight, then ranks who is worth reaching out to first thing in the morning.

### Step 1: Wire up the daily distress-signal scan

Point the n8n workflow at WARN layoff notices and funding-distress news so it pulls fresh signals every night instead of waiting for candidates to update their own status.

### Step 2: Match each signal to your open role

Feed the workflow the exact requisition you are filling so it weighs every layoff or funding story against that specific role instead of flagging generic industry news.

### Step 3: Let the dual-judge debate run

One AI agent argues for reaching out, a second tries to tear the opportunity down, and a third reconciles the debate, weighting a fresher signal over a stale one before ranking the result.

### Step 4: Keep messaging out of the workflow

Nothing gets sent to a candidate automatically. The workflow only produces a ranked decision card, so a recruiter still makes the outreach call by hand.

### Step 5: Review your ranked list every morning

Each morning you get who to reach, why now, and a suggested opening line, built from signals that were still overnight news the day before.

---

## **WORTH SEEING & READING**

**How Lovable keeps culture moving at startup speed**

Lovable grew from about 100 to more than 250 employees in seven months, and its People team says the biggest challenge isn't hiring fast, it's building the operating system as the company scales. The interview shares how they hire for ownership, reinforce culture through weekly rituals, and use AI to automate operations without replacing the human side of HR.

**Claude Code without the coding**

Claude Code can look intimidating if you've never touched a terminal. Ruben Hassid built a free, beginner-friendly course that teaches you by building something useful, with no coding required, covering everything from creating your first file to launching a site and using reusable prompts.

**Hiring is cooling, but AI skills keep growing**

LinkedIn's latest labor market research finds hiring remains below pre-pandemic levels across many advanced economies, while demand for AI literacy and AI-enabled skills continues to grow. The report explores how employers are adapting as work changes faster than headcount.

**Build your own recruiting brain**

Jamie Jay Lyons built an AI agent that turns 500+ hours of recruiting content into a searchable knowledge base, automatically pulling from trusted podcasts, newsletters, and reports each week. It's a useful example of how recruiters can ground AI in the industry knowledge they actually trust instead of relying on generic answers.

---

## **FRAMEWORK OF THE WEEK**

**Disclose Before You Deploy**

You might be handling AI transparency as a legal review that happens once the tool is already screening candidates. Article 50 of the EU AI Act moves that decision upstream, requiring candidates to be told when they are interacting with an AI system or with AI-generated content, before the interaction happens.

**Questions we need to answer:**

- Does the candidate know an AI system is involved at this step?
- Is that disclosure in the flow itself, or buried in a privacy policy?
- Who wrote the candidate-facing wording, legal or marketing?
- Which of your vendors disclose on your behalf, and which assume you will?
- Is AI-generated candidate communication marked as such?
- If a candidate asked what the AI decided and what a human decided, could you answer?

Transparency obligations are not a document you produce on request. They are wording a candidate reads in the moment.

**Key insight:** Article 50 is not a compliance burden bolted onto your funnel. It is a design constraint on how the funnel is built.

**Bottom line:** Write the disclosure before you buy the tool, not after the regulator asks.

---

## **PLATFORM UPDATES**

**Google** Lets Spark Handle Tasks Inside Your Logged-In Chrome

Google is integrating Spark directly with Chrome, allowing the agent, with permission, to use logged-in accounts and saved passwords to handle multi-step web tasks. It can research options and start processes on a user's behalf, while handing sensitive actions back for approval.

**Microsoft** expands what Copilot agents can do at work

Microsoft's July Copilot release adds a range of agent and workplace capabilities across Microsoft 365, continuing the move from AI that answers questions toward AI that can participate in everyday work.

**OpenAI** Cuts GPT-5.6 API Pricing

OpenAI cut API prices on GPT-5.6 Luna by 80% and Terra by 20%, while introducing a Fast mode for GPT-5.6 Sol that runs up to 2.5x faster at double the price. The changes apply across ChatGPT Work, Codex, and the API.

---

## **BIG IDEA**

**The AI tool you shipped last month is quietly becoming this month's outage**

"You solve Day 2 problems by asking yourself the right questions on Day 0."

Recruiters are starting to build their own intake bots, sourcing agents, and automations. Getting one to work is only Day 1. The harder question is what happens after you start relying on it.

Software teams call these "Day 2" problems: failures that appear once something is running in the real world. An AI workflow can skip a step, lose access, produce the wrong output, or quietly stop doing part of its job without anyone noticing.

Before you build, ask yourself: How will I know when this fails?

That question may matter more than whether you can get the workflow working in the first place.

Before your next AI build, would you actually know if it started silently skipping work?
