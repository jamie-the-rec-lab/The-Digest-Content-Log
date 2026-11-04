# Rebuilding Your Talent Team Around AI

- **Source:** PromptMates Newsletter
- **Date:** 2026-06-16
- **Fetched:** 2026-06-29

## Newsletter

Hey,

Welcome back to PromptMates Weekly.

This week's edition covers what two talent leaders at Zapier and Talentful are actually doing to rebuild TA as an AI-native function.

Plus: Fable 5's takedown shows how fragile model access can be, while Microsoft, Gem, and Stanford point to the next hiring AI frontier: company memory, candidate verification, and algorithmic oversight.

We break down what each one means for your work.

### Live This Week: How to Build with Claude Code for Recruiters

Matt Parker (Head of Talent @ Fleek) is back on PromptMates Live for round two of Claude Code, this time going back-to-back with Jason Miller to demonstrate two distinct build cases for recruiters.

Where the first session covered installation and initial setup, this one focuses on building real tools. Live demonstrations from practitioners using Claude Code in production today.

### Build of the Week: How to Set Up a Zapier Agent That Researches and Drafts Recruiting Outreach for You

Alex Lieberman, founder of Tenex, needed to hire AI engineers at scale without sending generic 'saw your profile' DMs. His publicly documented solution is a Zapier agent that researches each flagged candidate, finds the specific hook, and drafts outreach in his voice. Of the first 10 drafts generated, he sent 6 as-is.

**Step 1: Open Zapier Agent Builder**
Create a new agent in Zapier's Agent Builder. No code required. The builder accepts plain-language instructions describing what the agent should do.

**Step 2: Write your system instruction**
Define your role, the candidate type you are hiring for, and what the agent should do when it sees a LinkedIn URL in a Google Sheet. Be specific about company voice, credibility signal, and the output format you want.

**Step 3: Set the trigger**
A new row added to a designated Google Sheet containing a LinkedIn URL. Keep the sheet structure simple: name, LinkedIn URL, and any brief context notes.

**Step 4: Define the research and drafting sequence**
For each new row, the agent should research the candidate's current role, past companies, and public technical work; identify one specific hook; then draft a sub-100-word DM leading with your credibility and ending with a soft ask.

**Step 5: Route outputs to a review queue**
Save drafts to an Outreach Drafts Google Sheet and post a Slack message with the candidate name and a link to the draft. Configure a flag for rows where no credible hook is found. Mark those as needs manual review instead of auto-drafting.

The conditional logic is the quality gate. If the agent cannot find a specific, credible hook, it should skip the draft and flag the row. The willingness to skip, rather than send something generic, is what keeps the outreach worth opening.

### Worth Seeing & Reading

A Stanford study of 4 million job applications found clear racial disparities from a single vendor's screening algorithm used across 156 employers. Notably, 10% of candidates who submitted at least four applications were systematically rejected, a rate far exceeding independent-decision baselines.

The EU AI Act classifies many AI systems used in recruitment, selection, promotion, termination, task allocation, and worker monitoring as high-risk. TA and People teams now need clearer visibility into where AI enters the hiring workflow, what data each system uses, how human oversight works, and who owns accountability when multiple tools shape the same candidate journey.

JFF's 2026 worker survey found that employees are building AI skills through social media, news articles, friends, family, YouTube tutorials, and personal experimentation, while employer guidance lags. For People and TA teams, that creates a governance problem: AI adoption is already happening, but much of the learning sits outside official training, policy, and workflow design.

Anna Ott argues that AI job-search agents are creating a brutal false-positive problem for hiring teams: the candidates working hardest to tailor resumes, match roles, and improve their odds may now resemble the very automation patterns ATS systems are trained to flag.

### Framework of the Week: The Distill Framework for AI-Generated Work

Emily Gransky argues that AI makes it dangerously easy to build artifacts that are useful to you and unusable to everyone else.

Before sharing the output, ask:

- Who is this for?
- What do I need from them?
- What do they already know?
- What is the takeaway?
- Why does it matter?
- What is the explicit ask?

Most teams use AI to add more context, more analysis, and more explanation. That is the easy part. The harder part is cutting the work down until another person can act on it.

The key insight: the version that helps you think is not always the version that helps someone else decide.

### Platform Updates

**Anthropic — Shows Model Access Can Break Overnight**
Claude Fable 5 was taken offline three days after launch following a U.S. government export control directive citing national security concerns. Anthropic had to disable the model for all customers to comply. The company disputes the security characterization and says it is working to restore access.

**Microsoft — Turns Copilot Into Company Memory**
Microsoft announced Frontier Fine Tuning at Build 2026, enabling enterprise teams to embed company-specific policies, hiring guides, and onboarding documentation directly into Copilot with a self-service Reinforcement Learning approach.

**Gem — Moves Fraud Detection Upstream**
Gem launched an AI Fraud Detection Agent that evaluates candidate applications across resume metadata, email validation, LinkedIn consistency, and IP and device signals, flagging synthetic identities and AI-fabricated credentials with 90%+ accuracy before they reach the interview stage.

### Big Idea: Rebuilding Your Talent Team Around AI

Two talent leaders at BrightHire's Shine 2026 conference defined AI-native TA as architectural, not tool-driven.

Tracy St. Dic of Zapier argued that without a strategic vision for how the function changes, teams are just chasing tools. Chris Abbass of Talentful described building two companies in parallel: one for humans and one for agents.

The overlooked work is data readiness. Job descriptions, scorecards, sourcing notes, and candidate context need to be accurate, structured, and available before agents can improve outcomes. The teams getting this right cleaned up the inputs before touching the tooling.

The governance lesson applies to internal builds too. Tracy created a four-stage pipeline for homegrown tools, with audit checks for PII and API-key issues before anything moves forward. Scott built plugin harnesses that keep agents from duplicating existing tech stack capabilities or going off-script.

The hiring implication: the new bar is not "I know how to recruit." It is "I can learn hard things fast."
