# The Claude TA Playbook, Part 2: 20+ ideas to build in TA.
- **Source:** TA Unboxed
- **Date:** 2026-07-24
- **Fetched:** 2026-07-25
- **Public URL:** https://taunboxed.substack.com/p/the-claude-ta-playbook-part-2-20

## Newsletter
Part one [link] covered the setup work: the req, sourcing, and assessment design, all the leverage that exists before a single candidate is in front of you. Twenty-nine builds in total.
One of the links I included in the last post (the first one) was incorrect. Here is the correct one 7 Pre kick off questions [link].
In today’s newsletter, it’s all about what happens next. Once the process is running, the question shifts from are we finding the right people to is our process good enough to judge them well, and can we prove it afterwards?
Same principle as before. Every build here runs on job content, process data, anonymised interview records, or reusable templates. None of it needs a candidate’s personal data sitting on a third-party server.
As explained in part 1. These aren’t my ideas, but a curated list from the TA industry.
Have a read through and let me know which one is your favourite?
A word from our sponsor: Metaview
Before we get into today’s conversation, a quick thank you to our friends at Metaview, who are sponsoring today’s show.
They’ve just launched fillmore, their fully autonomous recruiting co-worker.
And the interesting thing here is that fillmore doesn’t ask recruiters to log into yet another platform or learn a new dashboard. It lives directly in Slack, working alongside your team like a colleague.
You can tag fillmore, give it the role context, the job spec, your hiring notes, and it will ask the follow-up questions it needs before going off to research the market, identify relevant candidates, and create deeply personalised outreach.
The promise here is pretty powerful: better top-of-funnel recruiting, with the kind of candidate research and personalisation that’s almost impossible to do manually at scale.
fillmore is currently waitlisted, so if you want to see what an autonomous recruiting co-worker could look like inside your team, head to:
metaview.ai/fillmor [link]
During the process
30. Kickoff meeting prep brief
Before each intake or kickoff call, generate a structured brief for the recruiter: the hiring manager’s past patterns (if you have ATS data), suggested questions, likely risks, and the calibration you need out of the conversation.
31. Kickoff to recruiter screen
Link intake recordings to screens and surface up to 50 matched candidates from prior pipelines, so the recruiter walks in with context, not a blank page. Deel built this with Claude and Metaview.
32. Debrief synthesis
Paste anonymised debrief notes and ask Claude for a structured evidence table — what was observed, against which criteria, at what confidence level. It separates evidence from inference and makes panel disagreements visible rather than buried in group dynamics.
Jamie Lyons frames this as a hiring manager coaching loop: compare the interview transcript against what great interviewing looks like, then give the hiring manager specific feedback after each interview. Over time, the same pattern can become an interview-quality score for the business.
33. Scorecard reminders
End the manual chase for pending scorecards; deliver them automatically. Deel built this with Claude.
34. Candidate communications (templated)
Draft stage-by-stage templates: confirmations, interview prep guides, status updates, and rejection notes that reflect your employer brand. No individual candidate data — templates applied by the recruiter.
35. Offer customised script
Turn candidate motivators surfaced earlier into a multi-level offer strategy, so the offer conversation is tailored rather than templated. Deel built this with Claude and Metaview.
36. Pre-final-stage prep call brief
Use the role brief and final-stage plan to prepare a recruiter-led call two days before the late-stage interview. The guide should cover the interview format, the people involved, the practical setup, and a realistic picture of the role — then leave space to surface unanswered questions or concerns.
The point is not to give candidates scripted answers. It is to add the context that an email cannot: what the interview will feel like, what preparation is useful, and whether there are blockers worth resolving before both sides invest more time. Luke Eaton reports that making these 30-minute calls standard increased late-stage conversion by 4–15% in their experience, while creating a more collaborative “player/coach” relationship going into an offer conversation. Source: Luke Eaton [link]
37. Interview brand coaching brief
Before each interview, give the hiring manager a short brief: how to represent the employer brand in the room, what language to avoid, and how to run the conversation so the candidate leaves with a positive impression, regardless of the outcome.
Jamie Lyons adds a useful operational version of this: send hiring managers a same-day interview brief via Slack that includes the candidate summary, what has already been covered, and what to double down on. The important design note is to ask hiring managers what would actually be useful before automating the message.
38. On-hold req governance tracker
Build a structured hold-state system: required reason capture, 30-day revalidation prompts, auto-closure at 90 days, and candidate comms templates for each checkpoint. Turns “on hold” from a pipeline black hole into a controlled, auditable state.
Pipeline and ops
39. Pipeline diagnostics
Aggregate pipeline data stage conversion rates, time-in-stage averages, drop-off points — with all PII stripped. Ask Claude where the process is breaking and to generate hypotheses: is the offer stage underperforming on comp, process length, or competitor activity?
Jamie Lyons also points to click-reduction as part of the operating system: Chrome extensions that export LinkedIn profiles into an ATS, or scan and analyse GitHub profiles from a LinkedIn page or CV. This one needs more governance when profile data is involved, but the broader pattern is useful for reducing manual admin at the workflow edge rather than asking recruiters to copy and paste their way through the day.
40. TA metric reporting
Pull ATS data into branded decks with live TA metric querying, turning diagnostics from a manual spreadsheet exercise into an on-demand briefing. Pull ATS data into a branded, on-demand briefing rather than rebuilding the same spreadsheet every week. The useful shift is from a static dashboard to a recruiter or TA leader being able to ask plain-English questions such as: Where is time-to-hire rising? Which stage is creating the biggest drop-off? Which functions have the most ageing requisitions?
The system should query an agreed metric layer with consistent definitions for measures such as time-to-fill, stage conversion, offer acceptance and recruiter capacity, then return both the numbers and a concise narrative: what has changed, where the issue sits, likely explanations, and the decision or action required.
The final output can be dropped into a repeatable, branded leadership deck: headline KPIs, funnel health, bottlenecks, risks, and recommended interventions. It is not “AI makes prettier slides.” It is a way to turn live operational data into a briefing that leaders can actually use without waiting for someone to reconcile exports and build charts by hand. Deel built this with Claude and their ATS.
41. Recruiter capacity modelling
Replace a flat “reqs per recruiter” target with a live view of the work actually sitting in each portfolio. One practical model scores every open role by its current stage, for example, a new role requiring intake, job design and funnel setup carries more weight than an offer awaiting acceptance, and refreshes the score weekly. It also makes room for unplanned work rather than pretending it does not exist: Stephen Collopy’s Delivery Hero framework assumes 30% of recruiter time is lost to interruptions.
The useful output is a capacity score, not a performance league table. Compare that score with actual hiring output and stage-conversion data to see whether the constraint is recruiter workload, a slow hiring panel, market supply, compensation, or a misaligned brief. It should also include support for the recruiter coordinators, sourcers, tools, and interviewer capacity — because each of these changes what a sustainable load looks like. Source: Stephen Collopy / Delivery Hero [link]
42. University hiring CRM
Treat university hiring as a long-term talent-market system, not a series of isolated campus events. Build a shared CRM of universities, schools, societies, programme leads, alumni contacts and partnership activity — then make it searchable by the things the business actually needs: skills, discipline, location, graduation year, diversity goals, business unit, target role family and likely hiring volume.
For example, a team planning to hire software engineers in two regions should be able to ask: Which institutions have produced strong candidates for comparable roles? Where do we already have an active relationship? Which events, alumni networks or internship routes are available before we pay for another broad campaign?
The CRM should track the relationship history as well as the institution: careers-fair attendance, lecturer or careers-service contacts, sponsorships, alumni involvement, previous applicant and hire outcomes, candidate conversion, and upcoming opportunities. That makes it possible to distinguish between a university that is genuinely becoming a productive talent source and one that simply appears on an annual events list.
Claude’s role is to make this information easier to interrogate and act on. It can prepare an account brief before a campus meeting, identify gaps in coverage, draft outreach or event plans, and summarise what has worked across a portfolio. The underlying decision should still be made by the early-careers team: data can highlight patterns, but it cannot replace judgement about relationship quality, brand fit or the local market. Deel built this with Claude. ⁠
43. “Why we are not closing” analysis
A structured retrospective on roles that closed slowly, fell over at offer, or produced poor quality-of-hire. Feed in anonymised data and generate a diagnostic narrative. This is where TA becomes data-driven rather than anecdote-driven.
44. TA budget ROI builder
Generate a hard, P&L-linked business case for TA tech investment: recruiter capacity gained, time-to-fill reduction value, and quality-of-hire revenue impact. Built to survive a CFO review, not just a productivity narrative.
45. Career site conversion optimiser
Audit career site traffic against application conversion (industry average sits around 4%). Model the job board spend you could cut by improving to 8–10%, and generate a prioritised fix list.
46. Tiered req routing engine
Classify each incoming req by complexity and route it: Tier 1 automated end-to-end, Tier 2 recruiter plus hiring manager, Tier 3 full strategic partnership. Protects team capacity from being eaten by low-complexity volume.
47. Agile sourcing sprint board
Treat sourcing as a short learning cycle rather than an open-ended search. Glenn Cathey’s model begins by assigning complexity points to each requisition — reflecting market availability, competition, pay competitiveness, hiring-manager decisiveness and role complexity — then measuring how many points the team actually completes in a one- or two-week sprint. That gives stakeholders a finite capacity budget and forces an explicit choice between competing priorities.
For a difficult search, set a specific sprint outcome (for example, profiles researched, conversations held and candidates presented), then run a short retrospective: which target companies worked, what the market calls the role, whether compensation is credible, and which requirements are excluding viable people. Carry those lessons into the next sprint. Add a visible Kanban board and a strict work-in-progress limit — Cathey suggests 3–5 active requisitions per recruiter, depending on complexity — so bottlenecks such as candidates waiting for hiring-manager feedback are obvious rather than hidden in an ATS. Source: Glenn Cathey [link]
48. Recruiter enablement metrics dashboard
Build a view connecting recruiter KPIs to business outcomes: hires per recruiter, pipeline conversion health, hiring manager satisfaction, and time-in-stage. Shifts TA reporting from activity-based to value-based.
Post-hire
49. 30/60/90 feedback synthesis
Build the post-hire check-in around the outcomes that were defined before hiring — not a vague “how are they doing?” question. A practical version sends a short assessment to the hiring manager at 30, 60, and 90 days, asking whether the new hire is on track against their plan, whether they have achieved the expected goals, what early signals or risks are emerging, and whether the manager would hire them again.
Close the loop from both sides: the 10x Recruiting example pairs manager assessments with new-hire conversations at roughly 45 and 90 days, so the team can distinguish a selection problem from missing context, unclear goals or onboarding support. When there is a gap, run a small retrospective against the original scorecard and interview evidence, then alter the process only where the evidence supports it. Source: Evan Connor, Ambience / 10x Recruiting [link]
50. Hiring manager profile
Build a profile of each hiring manager’s patterns: time-to-decision, offer acceptance rate, common rejection reasons, scoring behaviour, and scheduling latency. Use it to tailor your approach on the next req.
51. Hiring manager effectiveness score
Take the profile further with a quarterly coaching brief per hiring manager, surfacing where their behaviour helps and where it costs the business slow decisions, poor scorecard completion, low offer acceptance.
52. Quality of hire index
Use a composite measure rather than a single retention number. The Quality of Hire Index research by Steven T. Hunt, Chris Drake and Mike Fitzsimmons defines quality through three outcome groups: enrolment (new-hire retention through 12 months), commitment (retention from 12 to 36 months), and achievement (promotion, education and peer recognition). That is a useful reference model, but any internal index should use the outcomes that are credible and available in your own organisation — with the 30/60/90 feedback loop acting as an early signal, not as proof of long-term success.
The study analysed publicly available data on more than 4.3 million Fortune 500 hires and found an association, not proof of causation, between a one-point increase in QHI and a 0.14% increase in year-over-year revenue growth. It also warns that quality of hire depends on what happens before, during and after the decision: job design, selection, onboarding and management all matter. That means the index should be used to find learning opportunities, not to assign simplistic blame to TA or an individual hiring manager. Source: Hunt, Drake & Fitzsimmons — Quality of Hire Index Science [link]
53. Offer decline root cause analyser
When an offer is declined, generate a structured retrospective from anonymised process data: where candidate confidence eroded, what signals were missed, and what to change next time.
Jamie Lyons makes this broader: once an offer is triggered, analyse the end-to-end process from anonymised transcripts, scorecards, and process records to identify what could have been done better, what was overlooked, and which proactive steps might improve offer acceptance next time.
The pattern, again
Same four inputs run underneath all of it:
Job and role content — descriptions, briefs, criteria, outcomes. Yours to use.
Process and structural data — stage data, conversion rates, time metrics with no names attached.
Interview content — notes, transcripts, and debrief records are anonymised before they reach Claude.
Templates and frameworks — outputs designed to be applied by a human, not to process individual candidates.
None of these requires candidate PII. None creates the data governance exposure people worry about. All of them improve the hiring process.
The bottom line
Put the two halves together, and hopefully you get an idea of the ideas you can build with Claude. 50+ places to use Claude across the hiring lifecycle, and the one everyone argues about online resume/CV screening is the single worst place to start. It carries the most compliance risk and the least improvement to decision quality.
Everything else on this list is lower-risk and higher-leverage. Better reqs. Sharper sourcing. Assessment design that actually predicts performance. Cleaner debriefs. Honest pipeline diagnostics. A post-hire loop that finally closes.
You don’t need candidate PII to do any of it. You need the discipline to build the boring infrastructure rather than chase the shiny, risky shortcut.
Start with one build from part one. Then work your way down the list.
If you build one of these, reply and tell me how it went. I’m collecting the ones that work.
