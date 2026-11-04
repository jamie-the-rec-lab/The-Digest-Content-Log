# My AI Agents Got It Wrong. Recruiters Do This Too.

- **Source:** Full Stack Recruiter
- **Date:** 2026-10-24
- **Fetched:** 2026-11-04
- **Public:** https://newsletter.fullstackrecruiter.net/p/ai-agents-recruiters-handover-note

## Newsletter

(The email carries a paywalled "bonus" section with tool-by-tool setups; the part visible in the email is saved here, condensed. Paid-subscriber promotion text removed.)

Almost every recruiter asking about AI agents opens with "Which tool should I use?", which the author calls the last decision to make. The harder question: "whether you could explain your own process to someone who has never met you." Orchestration, for a beginner, means one piece of software does a task, hands its result to another, and "Somebody has to decide what gets handed over, in what shape, and where a human looks at it before it moves on. That somebody is YOU."

**The genealogy lesson.** The author built a chain of three agents to find the parents of his great-grandfather in scanned parish registers (transcriber, checker, summariser). The summary agent confidently reported a marriage on 23 December 1929; the 1930 census says that, while a church excerpt says 23 November 1930. "The second agent had found both dates, picked the one from the more official-looking source, and passed it on without a word about the conflict." Fix: one line in the checker's instructions: "if two sources conflict, keep both, flag it, and stop." The setup had three agents and no human checkpoint, "which is exactly what I'm telling you not to build."

**The handover note.** The closest thing most recruiters have to an agent specification is the note left for a colleague on holiday. Beginner build: agent one turns raw intake notes into a structured search brief (must-haves, nice-to-haves, deal-breakers, target companies, why someone would leave); the recruiter fixes it; only then does agent two draft search strings and outreach. "If each step in a chain gets it right 9 times out of 10, five steps in a row get the whole thing right about 59% of the time... Each human checkpoint resets the chain, which is why I'd rather have two agents and a person than five agents and a hope."

**Pushback from peers (buy, don't build).** Recruiters are paid to fill roles; ATS vendors and AI companies ship agents with security reviews done; homemade chains disappear when the builder leaves. Counter-example (one friend's story, unverified): a two-person sourcing agency ran bought agents; "By day three, the sourcing agent had quietly widened the location to 'remote in Europe'... She caught it after 31 messages had gone out." The author now treats a first build as a learning exercise.

**Fairness.** The EU AI Act puts AI used to recruit and select people in its high-risk category; "the deadline for high-risk recruitment and hiring tools has officially been delayed to December 2, 2027." Screening is the wrong place for a beginner to start; anything that ranks or removes people shouldn't be the thing you learn on. Search strings themselves make filtering decisions.

**Tools and setup (visible part).** One reusable instruction block for an intake agent (7 headings; every must-have needs a supporting sentence; conflicts flagged; never invent salary, location or seniority). Hermes Agent (open source, Nous Research, MIT licence, released February 2026); OpenAI Dots ("Dots launched inside ChatGPT at the end of September 2026.", with four-level Custom Rules; "The first dot is included with ChatGPT Pro, except in the EEA, Switzerland and the UK"); Grok Bot (from SpaceXAI, "in public beta since August 2026 on desktop and iOS"; the author runs 12 agents and is presenting at the ERE Recruiting Innovation Summit). Also a comparison-only checker agent and a coordinator agent with PAUSE steps. Practices: replay a closed role first, give candidates IDs in early steps, keep a running log, keep a human before anything is sent, before anything removes a candidate, when a checker flags a conflict, and when the brief changes.
