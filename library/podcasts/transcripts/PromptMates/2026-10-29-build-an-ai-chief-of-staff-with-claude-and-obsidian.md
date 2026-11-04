<!--SUMMARY-->
## Actionable summary
**Guest:** Emily Gransky, VP of Talent at Formation Bio (an AI-native pharma company), who leads four recruiters and one ops person  ·  **Show:** PromptMates, 29 Oct 2026
**Tags:** building ai tools, claude code, ai agents, recruiter productivity, recruiter workflow, context engineering, human-ai collaboration, ta leadership

**When to use this:** you are buried in Slack, email, calendar and ATS notifications and want to build a personal AI "chief of staff" that surfaces only what needs you today.

**Big idea:** Gransky argues that a team of small agents, each with one job and each reading only what has changed since its last run, is more reliable and far cheaper than one big agent asked to read everything, with an orchestrator acting like a manager who decides what reaches the human.

**Frameworks & plays:**
- Use a "watermark" so every agent looks only at what is new. Each agent reads the timestamp of its last run, fetches only items since then, filters out the unimportant, hands over a bucket of what matters, and then stamps itself so the next run starts from that point. She said she "just asked Claude to do a watermark".
- Break the job into single-purpose sub-agents. Hers are a comms fetch for Slack and Gmail, a signal router that decides whether a change relates to a person, a project or both, one agent that enriches people, one that enriches projects, one that reconciles actions, and a synthesizer that writes the briefing.
- Keep the orchestrator as a decider, not a fetcher. She does not make it go and get anything; it takes the sub-agents' inputs and judges what matters now.
- Triage into three bands. Of roughly 60 signals a day, she said three need her that day, four are worth watching, and the rest are handled quietly but still captured in Obsidian, so a task that is not urgent now can be resurfaced in three days when it is.
- Restrict the system to reversible actions. It only updates Obsidian and never sends emails or Slack messages, and she said she would not yet trust it to "reject that candidate or tell this person that they need to do this".
- Build the smallest version first. When she kept making one skill bigger it broke; the single "just tell me what changed in my email" agent "never breaks", and if email fails she only has to debug one sub-agent.

**Data & benchmarks (all self-reported):**
- Her first attempt to read everything took about half an hour and "a gazillion tokens", and the context window was too big to pull signal from noise.
- The chief of staff now runs three times a day, with the dashboard refreshed at 6:30 a.m., noon and 4:00 p.m., covering about 20 items per run.
- She said it saves her an hour a day, though "more than anything saves me my sanity". This figure is her own estimate.

**Tools & prompts:**
- Claude builds and runs the agents, and Obsidian is the single source of truth and the only thing the system writes to.
- Inputs include Slack, Gmail, calendar, Google Docs meeting agendas (checked for changes and new comments), and Greenhouse for new scorecards and offers.
- The output is an HTML dashboard showing a "state of my world" brief, meetings linked to their docs and Zoom, tasks (marking one done writes back to Obsidian), projects with on track or at risk status, and people.

**Steal this (do tomorrow):**
- Pick one channel, such as your inbox, and ask Claude for a small agent that reports only what changed since it last ran and records its own run time.
- Write down the actions your agent may take and allow only the ones you could undo, so nothing is sent or rejected without you.
<!--/SUMMARY-->

# Build an AI Chief of Staff with Claude and Obsidian

- **Podcast:** PromptMates
- **Channel:** PromptMates
- **Date:** 2026-10-29
- **Duration:** 10:06
- **URL:** https://www.youtube.com/watch?v=KK334ebIreE
- **Fetched:** 2026-11-04
- **Source:** YouTube captions via TranscriptAPI (asr-en)

## Episode description

What if an AI chief of staff checked your Slack, Gmail, calendar and ATS three times a day, and only surfaced what needs you today? Emily Gransky shows the system she built with Claude and Obsidian, from a team of small agents to the daily dashboard she opens each morning.

In this clip, Emily covers:

- Why she started with one simple scheduled agent and built up to a team of agents
- How an orchestrator works like a manager, with each sub-agent doing one job
- The "watermark" trick, where each agent only looks at what has changed since its last run
- Why it only takes reversible actions and never sends emails or Slack messages
- Her dashboard of tasks, projects and people, all kept in Obsidian

Emily Gransky is VP of Talent at Formation Bio, an AI-native pharma company, where she leads a team of four recruiters and one ops person.

This clip is from the PromptMates Live Show, where talent and people leaders share what they're actually building with AI.

Chapters
00:00 Emily's role and why she built this
02:00 How the chief of staff agent works
07:20 The daily dashboard

Connect with Emily: https://www.linkedin.com/in/emilygransky/
Join the PromptMates community: https://www.promptmates.ai/community
Weekly newsletter: https://www.promptmates.ai/newsletter
Catch the next live show: https://luma.com/promptmateslive

#TalentAcquisition #AIRecruiting #ClaudeCode #Obsidian

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube. A new paragraph marks a change of speaker where the captions show one (speaker names are not available).

**[0:00](https://www.youtube.com/watch?v=KK334ebIreE&t=0s)** Absolutely thrilled to be doing this one. I got a sneak preview into this about two days ago and it's literally already made me better. Like I stole things from from Emily already and have integrated them into my workflow. Super happy to hand it over to you, Emily. Take it away.

**[0:15](https://www.youtube.com/watch?v=KK334ebIreE&t=15s)** Awesome. Thank you so much. And if you found things useful, that is high praise. So that means a lot. Thank you very much. So I'm the VP of talent, like I said, at Formation Bio. We're an AI native pharma company and I have a team of four recruiters and one ops person. At any given time, I have a whole bunch of different projects going on in addition to the wrecks and just making sure that everybody has what they need. And so the things that I'm going to share today that are hopefully useful are just kind of how I manage my life and stay on top of a whole bunch of information. So I really have learned that the big unlock for me was when I could connect AI to my systems and my data and that from doing that I could create workflows that give me a ton of time back. So want to also caveat, like I know that that Jason and Joe talk about this that I talk about this a lot.

**[0:58](https://www.youtube.com/watch?v=KK334ebIreE&t=58s)** Like no one here feels like they're they're the expert, myself included. So your mileage may vary, but just start where you are and start small. This was one of the first things someone told me to try to build and I would recommend that everyone try to build one cuz I think it's really cool to have something show up in your inbox while you're drinking your coffee or your tea or or whatever your beverage may or may not be because it goes out on its own, it pulls information and summarizes it for me that I would like to stay on top of and it does that without me actually telling it to do anything. I set it up once, the agent kind of decides what's important. I certainly iterate on it. This was kind of the point where I was like, I wonder what else I can do.

**[1:35](https://www.youtube.com/watch?v=KK334ebIreE&t=95s)** Which started me down this rabbit hole of wanting to have like a team of agents and an agent orchestrator kind of getting signal from all of them. And so, you know, you think about it like um you've got one skill that's a recipe, you've got one agent that's one worker, you've got agentic orchestration, which is sort of like me thinking a manager reports to me and then they're managing a whole bunch of teammates underneath them. And each of those teammates has one job and they report up kind of what they're getting from doing their job, and then the manager kind of summarizes everything and make sure that I have what I need. And to me, that manager is my chief of staff. So, I will go through and tell you a little bit about what that looks like. So, it runs three times a day, uh and I say it saves me an hour a day, but it more than anything saves me my sanity. And so, basically, it looks across all of the different things that I interact with. It decides like what needs my attention right now. It kind of keeps my Obsidian current, and then it you know, keeps continuing to go. So, I'll show you how the orchestration works. It has six different things that it reads, and it has one thing that it writes to. So,

**[2:36](https://www.youtube.com/watch?v=KK334ebIreE&t=156s)** again, this is where I keep saying Obsidian is my source of truth. This doesn't send emails. This doesn't send Slack messages. All it does is it monitors all of those channels to see like what came in since the last time it ran. So, Slack, Gmail, calendar, a lot of my meetings have running agendas in Google Docs, looking to see if those changed, if any comments came in for me since the last time that it ran. It also looks at Greenhouse for like any new scorecards, any offers that are coming out, um anything that needs my attention. And so, this is what a run would look like from start to finish. So, step one is just look for what changed. This was a big learning for me. I use something called a watermark, and I just asked Claude to do a watermark, meaning I only wanted to go look for things that have changed since the last time it ran. The very first time I tried to pull this stuff Chief of Staff together, it would take about a half an hour and a gazillion tokens to like go through and read everything and try to tell me what the most important stuff was. One, that context window is way too big for it to be able to get the signal out of the noise, but two, it's just it's too big of a pull every time. So,

**[3:37](https://www.youtube.com/watch?v=KK334ebIreE&t=217s)** what I actually ended up doing was taking a step back, building tiny little agents for each one of these communications and channels to look at, and then saying, "Just go in there and tell me what changed since the last time we did this." So, now I can run it three times a day, and it's quick. It doesn't burn through a bunch of whole bunch of tokens, and I can feel confident that I'm getting the latest information. So, it fetches what changed, it routes the signal from that change, it then enriches in Obsidian the people and the projects that I'm working on. It reconciles any tasks, like it kind of keeps an eye out. Oh, she did that, cool. Oh, she needs to do that now, let's add it. It then synthesizes everything into a brief that I could call my world, like what changed in my world, I'll show you in a second, and then the dashboard pops up. Also, another HTML dashboard. A watermark just means that it runs since it only checks things since the last time I did it.

**[4:25](https://www.youtube.com/watch?v=KK334ebIreE&t=265s)** So, these are the different agents that are underneath the orchestration agent. I've got a calm fetch that that just looks at Slack and Gmail. I've got a signal router that kind of takes those differences and then figures out, is this related to a person, a project, or both? It enriches the people, it enriches the projects. It There's another agent that just kind of reconciles the actions I need to take, and then there's another agent that just says, okay, all of these things pertaining to projects, how do I add them and make sure that she has everything she needs there, and then there's like the synthesizer agent that writes my my briefing. So, it's looking across 60 different things every day cuz it runs three times a day and looks across 20 things. Um, what I love about this is it's like the dream of I would have loved to be a person that kept on top of this stuff all the time, but I also I'm like in back-to-back meetings all day long. So, knowing that there's something kind of in the background that's just checking everything and seeing how it relates to stuff really helps me because what it will do is it'll say, okay, of these 60 signals, three of them need you today. Like, three of them don't drop today. Four of

**[5:24](https://www.youtube.com/watch?v=KK334ebIreE&t=324s)** them, you should keep an eye on, but then everything else is handled quietly, which means it's still in Obsidian, it's still captured, I still have the record of it, but it's not on fire right now. It may be on fire in 3 days, and it knows to surface it to me then, but right now it's job is like to judge what's most important for me right now. And that's kind of what I think a chief of staff is supposed to do, right? Like, keep you abreast of everything that's supposed to be important right this moment. And then I don't make the orchestrator go fetch stuff. It's just supposed to take the inputs and then decide. So, again, it goes into Obsidian, and then it comes into my dashboard at 6:30 a.m., noon, and 4:00 p.m.

**[6:04](https://www.youtube.com/watch?v=KK334ebIreE&t=364s)** And then again, it only acts on things that are reversible. It's only updating Obsidian. It's not sending Slack messages. I wouldn't trust it yet to look across everything and be like, let's reject that candidate or tell this person that they need to do this. It does not do that. I just know what's on my on my list. So, I'll show you kind of what one of these sub-agents looks like just cuz I think it's interesting. So, one of them is called Comms Fetch. It just pulls what changed in Gmail since the last time it checked Gmail, which is usually anywhere from 4 hours to 12 hours since. It never reads the entire inbox. It just says I want to find the watermark of when the last time was time was that I ran and I only look at what's new.

**[6:39](https://www.youtube.com/watch?v=KK334ebIreE&t=399s)** So, then it reads the last run's timestamp. It asks Gmail for all the threads. It takes away all the stuff that's not important. It gives me like a bucket of data of things that are important. It then stamps itself again to say, all right, next time you come here, use this time because now this is the last time it ran. And then it just gives me gives the information. So, this was a again a really good learning. What I first tried to do is say, hey AI, go read everything and give me a summary. And look at all my projects and do all of this and I would just make it bigger and bigger and it would break. But when I said, all right, what is the smallest version of that? Just go check my email. Just tell me what changed in my email.

**[7:14](https://www.youtube.com/watch?v=KK334ebIreE&t=434s)** Now, that never breaks. Like that is something that's stable. Or if email's not working, I know I'm checking one sub-agent. I'm not trying to look across one big long skill that I tried to create. And then here's what it looks like. And this is truly like what this looks like for me every day. So, I come in, I have my world, and this is like my state of my world. So, what changed? An offer got sent. A candidate advanced to onsite. Um, we've now trained most of our interviewers. The screener shipped. It seems to be doing well. What's going on? Here's what's coming up for the rest of your day. And here's some things that you should probably keep an eye on. This offer's going to expire. You haven't signed it yet. We've got a couple scorecards that need to be put in, right? This is kind of like the state of my world.

**[7:57](https://www.youtube.com/watch?v=KK334ebIreE&t=477s)** But then, it also has all this information that's kind of grouped in ways that I care about. So, like I said earlier, and we all know this I think, like a person can be a teammate, a project, you know, collaborator, responsible for a bunch of stuff that you care about, cares about stuff you're responsible for. So like I wanted to have a bunch of different views so I could keep track of it that way. So like this will show me my meetings. And like I said, most of my meetings have one-on-one docs so it links right to the doc, it links right to Zoom. I can just manage everything from here. If I go into my tasks, it'll tell me again where the task came from, that it's urgent, and then if I mark it done here, you'll see it says marked done in Obsidian. So anything that I'm doing here, I know is happening in Obsidian, my master task list is being updated. So I can kind of go through here and say, "Oh, yep, that seems good." Um This came from email, yep, that's good.

**[8:49](https://www.youtube.com/watch?v=KK334ebIreE&t=529s)** So I can go through some of those. And then my projects, it kind of tells me what's on track, what's at risk. So if I look at this, this is my project, here's the Obsidian page referencing that project, here's the status. This is like all of the roles that are open. Here's the recent activity, the offer went out, this moved to finals. And then it also shows me all the people related to this project and kind of what they are doing related to that project here and some details about it. And then like who this person is for me. And then I also have people. So like if I look at just people, you can see like what's going on with this person, what they did here, and then I can also look at details. So who is this person to me, what matters. In my real chief of staff, there's actually a lot more detail, but it's just one place where I can know that like all of the information about each person is updated, about each project is updated. I probably spend the most time making sure that my tasks are under control and looking at my world because those are the things that matter to me today. So.

**[9:49](https://www.youtube.com/watch?v=KK334ebIreE&t=589s)** Hopefully that was a whirlwind and it was a little bit useful. Again, I took a lot of different iterations to get to this. So it's pretty cool when you can have all of your information kind of surfaced to you in a way that's useful. And it just saved me a lot of time but more than anything, it saved me a lot of anxiety.

