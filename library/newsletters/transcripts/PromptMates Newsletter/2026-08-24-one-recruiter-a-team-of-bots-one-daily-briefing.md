# One Recruiter, a Team of Bots, One Daily Briefing

- **Source:** PromptMates Newsletter
- **Date:** 2026-08-24
- **Fetched:** 2026-08-26

## Newsletter

👋 Hey,

Welcome back to PromptMates Weekly.

This week: One AI agent does not have to handle everything. We're breaking down how one recruiter built specialist bots for Slack, email, Ashby, offers, onboarding, and more, then connected them through one central coordinator.

Plus: what talent flows reveal about OpenAI and Anthropic, and why AI sourcing should be measured by conversations started, not candidates found.

---

LIVE THIS WEEK!

🗓️ How to Build Slack Recruiting Agents
Wednesday, August 26 at 12:00 PM EDT / 5:00 PM UK

Joshua Gill, who leads Talent Engineering and Ops at Luma AI, shares recruiting tools he has already built inside Slack, then walks through a live build you can adapt to your own workflows without waiting on IT.

🗓️ Case Study: Hiring With AI Recruiting Agents
Tuesday, August 25 at 11:00 AM EDT / 4:00 PM UK

Jack & Jill's Joe Leggat unpacks PromptMates' first hire using Jill, sharing how the AI recruiting agent worked in practice and what they learned throughout the hiring process.

---

TOP STORY: Building the Recruiting Agent Stack

One recruiter just hired their first engineer with the help of a team of specialist bots.

In an interview with Joe Leggat (CEO of Jack & Jill, a hiring bot platform), they explained: most recruiting tech integrations fail because they expect one system to understand all your needs. What actually works is connecting several single-purpose tools through one human coordinator.

Joe learned this from building Jill, an AI recruiting agent. But it got him thinking: what if companies deployed multiple, specialized recruiting bots and had one main "orchestrator" bot coordinate them?

Here's what this recruiting bot team looked like for that one hire:

"Slack Bot" - runs the day-to-day recruiting workflow
Interface: Slack
What it does: Posts open roles, collects candidate profiles from team members, logs conversations with recruits

"Email Bot" - handles candidate communications
Interface: Email
What it does: Sends templated emails, flags important messages, summarizes email threads

"Ashby Bot" - syncs candidates into the ATS
Interface: Ashby API
What it does: Creates candidate profiles, updates pipeline status, tracks interview feedback

"Offer Bot" - guides candidates through offers
Interface: Email + offer link
What it does: Sends offer letters, coordinates background checks, onboards accepted candidates

"Onboarding Bot" - integrates new hires
Interface: Ashby + email
What it does: Tracks onboarding progress, alerts when tasks are overdue, reports back to hiring team

"Orchestrator Bot" - manages all the above
Interface: Everything
What it does: Routes information between bots, tracks hiring metrics, makes recommendations to the recruiter

The recruiter's job? Approve moves, build relationships, and make human calls that the bots flag as important.

This is a massive shift from the current state of recruiting tech. Today, companies use 3-4 different platforms (ATS, email, calendar, CRM) that rarely talk to each other. The recruiter spends 40% of their time copying and pasting candidate names between systems.

But when you have five bots talking to each other through one coordinator? The recruiter just sits in Slack and moves things forward. No data entry. No context-switching. Just pure recruiting judgment.

Joshua Gill at Luma AI has already built some of these bots internally. In this week's live session (Wednesday, August 26 at noon), he's showing the Slack bot specifically—how he built it, how it connects to Luma's recruiting flow, and how you can adapt it for your own team.

"We realized that Slack is where our team actually lives," Joshua told us. "Why force them to go to another app to do recruiting? Build the bot where the work happens."

---

TALENT FLOWS: OpenAI vs. Anthropic

Here's what we learned from tracking talent movement between two of AI's biggest companies:

OpenAI → Anthropic: 47 engineers (and counting)
Anthropic → OpenAI: 8 engineers

That's a 6:1 net flow toward Anthropic.

Why? Two signals:

1. Anthropic is hiring faster
Anthropic has posted 89 open roles in the past 6 months. OpenAI has posted 23. This is a recruiting choice—Anthropic is building out teams faster than OpenAI right now.

2. OpenAI engineers are being pulled, not pushed
When we talk to people who've made the move, the pattern is consistent: "I got recruited hard. Anthropic kept in touch. When the time was right, they had a spot."

That's not a reflection on OpenAI's culture or compensation. It's recruiting efficiency. Anthropic has built a talent acquisition machine—they're staying in touch with people, making a move when they're ready. OpenAI isn't doing that at scale.

Conclusion: The next wave of AI companies will be won by whoever can recruit and retain their best engineers. Right now, that's Anthropic.

---

THE METRIC THAT MATTERS: Conversations Started, Not Candidates Found

Here's a common conversation with AI-powered recruiting tools:

Recruiter: "Your bot found 200 candidates from the database."
Bot vendor: "Success!"
Recruiter: "Yeah, but only 3 turned into conversations. The rest ignored the outreach."
Bot vendor: [silence]

This is the problem with measuring recruiting success by candidate volume. It assumes that finding more resumes = more hires. In reality, it just means more noise.

The real metric is conversations started—how many people actually replied and engaged with your recruiting process?

Here's why this matters:

1. Conversations are a leading indicator of hire quality
If someone engages with your outreach, they're already interested. They're 10x more likely to be a good fit.

2. It's measurable and accountable
Bot vendors can't hide behind "we found 1,000 candidates." You can see: How many people did the bot reach? How many replied? What was the engagement rate?

3. It rewards the right behavior from recruiting bots
If you measure success by conversations, the bot optimizes for: writing better messages, picking better targets, timing outreach right. Not just casting the widest net.

When we asked Joe Leggat how Jill measures success, he said: "We don't care how many candidates we surface. We care about conversations. If the bot starts 10 real conversations, that's a successful week."

If you're evaluating AI recruiting tools, ask this one question: How many conversations did your tool start, and what was the reply rate?

If they talk about volume instead, they're not actually measuring recruiting.

---

WHAT WE'RE READING: The Art of Insider Recruitment

A three-part investigation into how Microsoft is rebuilding its recruiting team after a wave of departures. Key insight: They're hiring back former employees as contractors, allowing them to keep institutional knowledge while staying flexible.

Read it in Axios

---

EVENT RECAP: Recruiting Metrics That Matter

Last Tuesday, we hosted a panel on measuring recruiting success. Here's what stuck with us:

"Time-to-hire is a vanity metric." — Sarah Kim, Chief People Officer at Figma
"What matters is time-to-productivity. Did they hit the ground running?"

"We're not hiring for skills. We're hiring for learning velocity." — James Park, CEO of Fitbit (now Google)
"The best predictor of success is: Can this person learn faster than our challenges change?"

"Your recruiting funnel should look like a megaphone, not a funnel." — Laszlo Bock, former SVP of People at Google
"You want to expand your reach at the top of the funnel, not contract it. Too many companies try to filter out at the sourcing stage and end up with fewer great candidates."

You can watch the full recording here.

---

THIS WEEK'S BOT BUILD: Slack Recruiting Commands

Joshua Gill is building this live on Wednesday. But if you want to get ahead, here's the basic structure of a Slack recruiting bot:

/post-role [title] [location] [description]
→ Bot posts the role to a recruiting channel
→ Team members can react with 👍 to indicate they know someone
→ Bot collects names and DMs candidates

/log-call [candidate-name] [summary] [next-steps]
→ Bot logs the conversation to Ashby
→ Updates the candidate profile
→ Sends a reminder for next steps

/flag-for-offer [candidate-name]
→ Bot notifies the hiring manager
→ Triggers background check workflow
→ Sends offer template to the offer bot

These three commands handle 80% of recruiting workflow in Slack. Everything else is bots talking to each other in the background.

Join the live build to see how Joshua actually coded this. Wednesday, August 26 at noon EDT.

---

IN THE WORKS: Recruiting Agent Training Pipeline

We're building a course on how to train AI recruiting agents. Here's what's in it:

1. How to frame recruiting as an AI problem (it's not what you think)
2. How to build labeled data from your real recruiting conversations
3. How to structure prompts so the bot learns what "good recruiting" looks like for your company
4. How to measure success (conversations, not volume)
5. How to avoid the common pitfalls (over-filtering candidates, writing bad outreach, poor timing)

We're launching it in September. If you want early access, reply to this email.

---

CONVERSATION STARTER

What's the biggest bottleneck in your recruiting right now?

Send a reply or tweet at us @promptmates. We're collecting real recruiting challenges for our next research project.

---

Joe Atkinson
Founder, PromptMates

P.S. If you found this useful, forward it to a recruiter who's drowning in spreadsheets. They need this.

P.P.S. The Slack bot code Joshua is showing this Wednesday is open-source. We're putting it on GitHub Thursday morning.
