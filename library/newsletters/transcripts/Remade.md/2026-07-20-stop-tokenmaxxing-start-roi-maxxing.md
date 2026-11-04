# Stop tokenmaxxing. Start ROI maxxing.

- **Source:** Remade.md
- **Date:** 2026-07-20
- **Fetched:** 2026-07-20
- **Public URL:** https://remadebyleandro.substack.com/p/stop-tokenmaxxing-start-roi-maxxing
- **Author:** Leandro Gomes da Silva

## Newsletter

Standfirst: Everyone should be allowed to experiment with AI. That does not mean everyone needs an unlimited budget.

At the end of a panel with Hung Lee, Anna Ott and Mozilla CTO Raffi Krikorian, Hung gave each panellist seven seconds to make a prediction. Leandro's was: "For your high-performing AI users, match their salary in tokens, because they will earn that back." He calls it deliberately provocative and also incomplete, and this article is the correction.

The tension Raffi described: companies want people to experiment, but they cannot fund every experiment equally. The strongest AI models are becoming more capable and more expensive. Some people will use that capacity to solve valuable problems. Others will simply generate a bigger bill.

### First, what is a token?

A token is a small unit of text that an AI model processes. It can be a whole word, part of a word or a punctuation mark. When you send information to a model and receive an answer, both sides consume tokens. Providers commonly use those counts to calculate usage and cost.

As AI systems take on longer and more complex jobs, token use can rise quickly. They may read documents, inspect databases, use tools, check their own work and try several approaches before returning an answer.

That has created industry slang: **tokenmaxxing**, meaning maximising AI consumption as if consumption itself were proof of adoption or performance.

"It is a bad metric, though. A person who burns ten times more tokens has not necessarily created ten times more value. They may be solving a harder problem. They may also have built a token incinerator."

This is not theoretical:
- By April 2026, Uber had reportedly used its full-year budget for AI coding tools. Its COO later said the link between rising AI use and useful features shipped was still difficult to prove.
- Adam Mosseri, who leads Instagram, suggested a strong engineer's annual token spend could eventually approach their total employment cost. Leandro notes the important part was not the number but the trust: higher budgets make sense for people expected to use them in an ROI-positive way. Mosseri also dismissed token leaderboards as silly.

Proposed replacement term: **ROI maxxing**, defined as "increasing AI investment when the evidence suggests it is creating worthwhile business value."

### Give everyone access. Do not give everyone the same budget.

Leandro wants everyone in a company experimenting with AI. If only a small technical group has access, the company misses problems and ideas from the rest of the organisation. A recruiter sees a different set of problems from a developer; someone in finance notices repetitive checks an engineering team never encounters; a people manager understands where communication breaks down.

"Equal permission to participate does not require equal spending power."

His tiered system:
- **01 / Baseline tier** — lets everyone learn, test ideas and improve everyday work within clear data and security rules.
- **02 / Experiment tier** — supports people running approved experiments with a defined problem, owner and review date.
- **03 / Scale tier** — reserved for AI Operations and people who have repeatedly turned expensive model access into material results.

Model tiers are company-defined access levels. Routine work can use cheaper models; difficult or high-value work may justify stronger, more expensive ones. Allocation should follow the work and its evidence, not someone's enthusiasm or seniority: "A junior employee with a valuable experiment may deserve more capacity than a director using AI to rewrite emails."

This also avoids a common mistake: buying the newest tool before understanding the problem. "A high-performing AI user is not the person with the largest collection of subscriptions. It is the person who can do more with the resources already available."

### An experiment should earn its next two weeks

The objection is that experiments cannot prove ROI before they exist. Leandro agrees. Early work needs room to be uncertain. He would not ask every idea to show revenue after its first sprint, but he would ask it to show a reason to continue.

His preferred unit is a two-week experiment. At the end the team answers five questions:
1. What problem did we try to solve?
2. What changed for the user or the workflow?
3. What evidence suggests the idea has value?
4. What did we misunderstand?
5. Do the next two weeks deserve more time, money, or model capacity?

Evidence can be modest at first: a task completed faster, fewer errors, better user feedback, a stronger output, or a discovery that changes the original hypothesis. The point is to build in layers. "Ideas often fail for reasons that are not obvious at the start. The core idea may be sound while the interface, data or instructions are wrong. Killing it immediately would be premature. Funding it indefinitely would be worse."

He notes AI can help here too, referencing the "Council of LLMs" concept (asking several large language models to answer or critique the same question before another model combines the results). He is explicit that it is an experimental method, not a guarantee of a better decision, and that it consumes more tokens.

"The rule is simple in the end: an experiment does not need to prove its final ROI within two weeks. It does, however, need to show it earns another sprint."

### What this looks like in recruitment

AI sourcing is his test case. He has trialled Avery, MetaView, Juicebox, Noon, Exa and several other tools with agency consultants and internal TA teams. "The pattern was consistent: most tools still depended heavily on the user's domain knowledge and ability to communicate their needs to AI systems."

Most people call this prompting. He argues a better term is **context engineering**: deciding what the system knows when you ask it to do something, including instructions, role data, previous conversations, available tools, and relevant documents.

"In my experience, users who provided little context generally received weaker results. They tried a short prompt, saw an unconvincing list of profiles, and returned to either LinkedIn or the ATS." He is sympathetic: recruiters work under commercial pressure and have little time to nurse a tool through repeated failed attempts.

Training every consultant to become excellent at prompting and sourcing strategy would require serious time and money. So he tested a different hypothesis: could the system extract the missing knowledge from the user and translate it into a better sourcing run?

At Nobel Recruitment they built a layer of agents behind the sourcing process. The agents pull information from the ATS, intake transcripts and notes, and the recruiter's conversation with it. The agent questions the user, surfaces market information, and confirms the sourcing strategy before the search begins. "The easiest metaphor is that every consultant gets a personal sourcer with an army of mini-sourcers behind it."

The process has two gates:
1. The sourcing tool searches and removes candidates who do not meet the stated criteria.
2. Their own context-rich agent checks the remaining profiles against the client conversation, intake meeting, and recruiter's instructions.

Only the candidates most likely to fit are presented. Setting up a sourcing run now takes less than five minutes.

**Early internal numbers:**
- About half of the candidates presented by the system are judged worth contacting.
- Sourcing time has fallen by roughly 80% (his estimate).
- The team's overall response rate has moved from 19.7% before this work to around 40% today, with some users above 60%.

**His own caveats, stated plainly:** the 80% is an estimate, not a controlled time-and-motion study. The response rate includes every reply, not only positive ones. They do not yet have reliable attribution for AI-sourced candidates through to interviews and placements. There was no randomised control group, and other process changes may have contributed. "So I cannot honestly claim proven ROI from placement yet."

What he will claim: six or seven rapid iterations produced a faster process, a meaningful candidate-contact rate, and enough adoption to justify the next sprint. "That is what scaled experimentation should look like: evidence accumulates layer by layer, and the claim never runs ahead of the measurement."

### Someone has to own the plumbing

His current idea of AI Operations. For a startup or scale-up he would start with two people:
- A domain expert (SME) who understands the work and has an affinity for AI.
- A technical builder who understands AI systems and has an affinity for the domain.

He compares it to the art director and copywriter model in advertising. The pair holds the central idea, then brings in designers, developers, legal, security, data and other specialists when the work moves toward production. The pair finds the core problem, inspects the underlying process, builds the short and long-term fix, drives adoption and reports the result.

"Many companies are adding agents to processes that were already fragmented, badly documented or full of rotten data. The prototype may look impressive, but the foundation is weak. Building more agents on top creates a faster version of the same mess."

So an AI Operations team should be allowed to ask a more basic question: does this problem require AI at all? Sometimes the answer is normal automation, a clearer policy, a better handoff, or a database fix. "The team's job is to solve the business problem, not to defend AI's involvement."

He is explicit about the limits: two people can work for a startup or scale-up, with specialists joining around particular projects. He does not think it is a complete blueprint for a large enterprise, because without clear governance it could become a bottleneck or an ungoverned shadow IT team. Security, privacy, legal responsibility and architecture still need formal ownership. "I would rather publish the working model with those limits than pretend it is finished."

### Decide what AI should do before measuring what it costs

He uses the AI Delegation Matrix from Bharat N. Anand and Andy Wu (HBR). It maps work on two dimensions: is the knowledge explicit and documented, or tacit and based on experience? Is the cost of an error low or high?

Four practical modes:
- **AI can do the work** — explicit information, low cost of error. Example: formatting a CV to a template or updating routine ATS fields.
- **AI creates options, a human chooses** — experience matters but mistakes are recoverable. Example: outreach angles or job-ad variations.
- **AI produces, a human verifies** — information is explicit but an error could be costly. Example: checking a contract draft or applying a defined screening rule.
- **The human leads, AI assists** — work depends on judgement and an error could damage a person or relationship. Example: a sensitive rejection, final negotiation or disciplinary decision.

"This is more useful than a blanket instruction to 'use AI more.' It connects model choice, human review and budget to the actual work." He argues it also gives HR and TA a serious role: a technical team may understand the system's architecture, but the domain expert understands the human consequences, exceptions and tacit knowledge hidden inside the process.

### What counts as a high-performing AI user?

Four things:
1. **They solve problems that matter.** The result changes cost, speed, quality, revenue, risk or someone's ability to do the job.
2. **They are resourceful.** They use the tools already available before asking for another shiny subscription.
3. **They know where the human belongs.** They can separate work that should be automated, work that benefits from collaboration and work that should remain human-led.
4. **They leave behind a better system.** Their experiment can be repeated, adopted, measured and improved by other people.

"Tokens are an activity input; they tell part of the story; I would rather look for improvement-related data."

He cites BCG's 2026 survey of 11,749 workers: many regular frontline AI users reported saving at least a day a week, but most received little guidance about what to do with the saved time, and more than half did not redirect it into strategic work. Companies reporting stronger business improvement were redesigning workflows, not merely handing out better tools.

"A saved hour does not automatically become an hour of company value. It may disappear into more meetings, a larger workload or a faster version of an unnecessary process. The organization has to capture it."

### His revised seven-second prediction

"Give everyone enough AI access to experiment. Give substantially more to the people and teams who repeatedly turn it into value. Review both the result and the bill.

Some exceptional users may eventually consume AI capacity worth a meaningful share of their salary. That can be entirely rational. One successful recruitment placement, one critical security issue found or one redesigned workflow may cover a long period of model use.

But a large token budget is a consequence of trusted performance. It shouldn't be the definition of it.

Forget the question 'who can consume the most AI?'. It is: Who in your organization can turn it into something worth paying for?"
