<!--SUMMARY-->
## Actionable summary
**Guest:** Ezra Mechaber, growth product manager at Figma, who turned his personal Claude Code setup into a shared 31 skill "PM OS" used across the product team  ·  **Show:** How I AI, 2 Nov 2026
**Tags:** ai, ai agents, ai coding, product management, productivity, team building, growth

**When to use this:** You want to roll AI out to a whole function (PMs, recruiters, ops) with a shared, versioned set of skills rather than everyone improvising alone.

**Big idea:** Start from the jobs you do badly or skip, encode them as shared skills in one repo, and let a small group hack it down to what is genuinely useful, a goal Ezra describes as being "lazy in the right places".

**Frameworks & plays:**
- Structure the repo simply. Ezra describes an agent file that tells the AI how to behave, skills that say when to fire, a memory file, and command hooks including a check on boot for a new version "to keep our 60 to 70 PM kind of roughly in sync".
- Give each user a private workspace. It is technically two git repos, a parent everyone downloads and a sub repo for private write-backs.
- Build it with a small team. Three people fired off as many pull requests as possible, ended up with a "Cambrian explosion" of skills, then a company offsite where every PM installed and roasted it. He now removes skills that models no longer need.
- Run a "what's up" skill roughly six times a day to pull Slack threads, owed replies and outstanding decisions into one list.
- Add org lookup skills (who owns this area, who is my designer or engineering manager) so docs add the right reviewers automatically.
- Bug bash with an agent. Keep a FigJam page with the test account, path and actions, run the agent through it on two accounts, and have it write findings back. In the last month it found that a thousand emojis in a text box broke the field, and a grammar slip of "a" versus "an" before a team name.
- Automate experiments. Slack triggers three automations (data science, UX writing, engineering), with one human review before launch and a webhook that triggers analysis when the test ends.

**Data & benchmarks:**
- 31 skills, 60 to 70 PMs, about 2,000 people at the company, and about five live concurrent experiments from the automated growth PM. Ezra says it "found a huge win on its very first experiment" but gives no figure.
- He archives roughly 10 Slack channels a day and had no usage telemetry, partly so people would not feel watched.

**Tools & prompts:**
- Claude Code then Codex (browser use, scheduled desk booking), Cursor automations, FigJam and the Figma MCP, a small fast model for real-time writing checks.

**Contrarian take:**
- Ezra says he tried and failed to build a benchmark and is "curious how this performs relative to like totally vanilla Codex", and that he now removes skills as models improve. The value of the repo is unproven.

**Steal this (do tomorrow):**
- List the three jobs you routinely skip or do badly, such as looping in stakeholders or meeting notes, and write one skill for the first.
- Create a shared repo with a behaviour file and a "what's up" skill for your team.
- When an AI loops, open a new conversation rather than arguing with the poisoned one.
<!--/SUMMARY-->

# The AI chief of staff that this Figma PM uses all day

- **Podcast:** How I AI
- **Channel:** How I AI
- **Date:** 2026-11-02
- **Duration:** 42:30
- **URL:** https://www.youtube.com/watch?v=ztt8irafLMQ
- **Fetched:** 2026-11-04
- **Source:** YouTube captions via TranscriptAPI (asr-en)

## Episode description

Ezra Mechaber is a growth product manager at Figma whose goal is to be “lazy in the right places.” When he joined Figma, he found almost no one outside engineering using AI to get real work done, so he and a couple of fellow PMs turned his personal Claude Code setup into PM OS, a shared repo of 31 skills that every PM at Figma now uses. In this episode, Ezra walks me through his favorite skills, how he bug bashes with Codex, AutoXP—an automated growth PM that found a huge win on its very first experiment—and a real-time writing assistant he built with Jev.

*What you’ll learn:*
1. Why PM OS is a repo, not a product
2. The skill Ezra runs six times a day to tame Slack
3. How one repo keeps 60 to 70 PMs in sync
4. Why his bug-bash agent catches things he never would
5. How AutoXP runs experiments with one human checkpoint
6. Why Jev took over every meeting he was in for two weeks
7. What to do when you want to yell at your AI

*Brought to you by:*
Optimizely—Your AI agent orchestration platform for marketing and digital teams: https://www.optimizely.com/howIAI
Jira Product Discovery—Prioritize with insights, build with confidence: https://atlassian.com/howiai

*In this episode, we cover:*
(00:00) Episode preview
(00:51) Introduction to Ezra Mechaber
(02:04) The origin story of Figma’s PM OS
(06:30) PM OS demo: the “chief of staff” setup
(10:28) How the repo works: skills, hooks, and private sub-repos
(12:00) How the skills got built, roasted, and whittled down
(14:15) Build art

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube. A new paragraph marks a change of speaker where the captions show one (speaker names are not available).

**[0:00](https://www.youtube.com/watch?v=ztt8irafLMQ&t=0s)** I, as a growth PM, I feel like the biggest sin you can commit is wasting traffic. What if we could just automate myself out of a job and like create a little growth PM who could just like run and run and run. I call it Auto XP and right now one of our engineers is running it and has like five different experiments going that I have not taken a look at and it found a huge win on its very first experiment. Auto XP has its own channel where it can communicate with itself. Hey Auto XP, go find an experiment to run on our settings page. See what you can do. Go crazy. And it will trigger a data scientist to go find drop off and like look at the funnel and look at mix shift and all those things.

**[0:37](https://www.youtube.com/watch?v=ztt8irafLMQ&t=37s)** The whole hypothesis was like, how do you exploit all this traffic and maximize the number experiments and then like the time to be alive. It is here. You can just like live code it there. This is amazing.

**[0:51](https://www.youtube.com/watch?v=ztt8irafLMQ&t=51s)** Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive here on a mission to help you build better with these new tools. Today I have Ezra McCabe, product manager at Sigma and he's going to show us Sigma's internal PMOS, the 31 skills that every product manager at Sigma uses to make their life a little bit easier. We're also going to talk about, of course, my boy Jev and how you can build a real-time AI editor with that little cheap fast model. Let's get to it. Optimizely agent platform for marketers is built on a bigger idea, a whole directory of agents now joined by a newly revealed squad of virtual teammates each with a defined role and a personality of their own. This isn't about faster drafts, it's about handling the coordination too. The research, the  approvals, the hand-offs, the routing, the back and forth that quietly eats your week and never makes it into anyone's highlight reel.

**[1:49](https://www.youtube.com/watch?v=ztt8irafLMQ&t=109s)** Get the story behind it all. Hear the confessions from marketers who have handed off the busy work. Meet the squad and understand what virtual teammates can do for you at optimizely.com/howiai. Ezra, welcome to How I AI.

**[2:08](https://www.youtube.com/watch?v=ztt8irafLMQ&t=128s)** Thanks so much.

**[2:09](https://www.youtube.com/watch?v=ztt8irafLMQ&t=129s)** One of the things I love about this podcast in particular, because I know we have a lot of crossover listeners to Lenny's podcast, is PMs are really leaning into AI, but they're all doing it in completely different ways, right? I started like a jillion AI years ago with like chat PRD and like how do we make documentation and go really fast. We've seen so many different product flows. I think everybody's sort of crafting their like artisanal product platform now because they can. And so when you said you had a PMOS, I was just so excited to have you come on and demo it. So tell me, what was the origin story of what we're going to see today and why did you build it?

**[2:50](https://www.youtube.com/watch?v=ztt8irafLMQ&t=170s)** I like to tell my engineers that I my goal is to be lazy in the right places. And so for me a lot of it was I walked into Figma a couple years ago and I thought everyone was going to be using AI. It was going to be crazy AI built. Um I was just going to I was already feeling behind. Like I just I felt behind cuz we're all on Twitter and we all see like, you know, Tibo just posting about like the future of the universe. And I walked in feeling really behind and I realized basically no one was using these tools outside of engineering to like get real stuff done. And so I started just trying to automate some of my own productivity. Like I was the person who was trying to do too much in Zapier like many years ago.

**[3:35](https://www.youtube.com/watch?v=ztt8irafLMQ&t=215s)** And the more time I spent with it, one, Claude coded had just come out and I started to realize like there were things I could do in the terminal that were like really interesting all of a sudden. I could like build CLI, we you know, we were in that CLI phase. And like no other PMs who I was working with were doing it and they were all sort of curious. And we had this really interesting challenge from Yuki, who was our CPO at the time, which was basically like, what would it take to get all of our PMs kind of AI pill? Like what would that look like? And um working with a couple of other PMs, um shout out to Jinan and Lawrence, I started thinking about like what would it look like to turn this thing that I was doing just like hunched over my laptop like a little creep into this kind of like reusable thing that lots of other PMs could could build on top of.

**[4:26](https://www.youtube.com/watch?v=ztt8irafLMQ&t=266s)** Great. And so what what were like the problems that you thought were most important for PMs to think they could solve with AI?

**[4:35](https://www.youtube.com/watch?v=ztt8irafLMQ&t=275s)** First of all, I feel like the the like really trite thing about being a PM is that you're doing too many jobs, and the question is like, which jobs do you either do really poorly or not do at all? And so for me it was like, okay, how do I do for the jobs I'm not doing and the jobs that we are not doing as a team, how do we do them at like the minimum allowable level of like missing things? Like my IR support team is incredible, and the thing that I forget to do on every launch is to loop them in at the right time. And so one of my questions was like, how could I do this to make sure that I don't forget Katie, one of our support ops people, or meeting notes, not my friend. I'm really bad at them. But like we have transcription tools. How do I just get like good enough so that I'm not blocking other people? So a lot of them started from my jobs of what I wanted to do, find someone in the org who works on such and such thing. We're like 2,000 people now, so just understanding who the code owner is is really useful.

**[5:32](https://www.youtube.com/watch?v=ztt8irafLMQ&t=332s)** Um and understand who we are in relationship to each other. And then also just like, how do I get fun productivity out of all of our other PMs? So um one of the skills that's in there was this like really detailed spec skill that started to walk through how does our code base work if you wanted to do this really intensely? Like if you wanted to do this the right way, what would that look like?

**[5:57](https://www.youtube.com/watch?v=ztt8irafLMQ&t=357s)** Amazing. And so I I love this idea that you had a couple tasks on the PM plate that you were like we need minimum viable doing of these tasks. Like it just needs to write it.

**[6:10](https://www.youtube.com/watch?v=ztt8irafLMQ&t=370s)** out of it.

**[6:11](https://www.youtube.com/watch?v=ztt8irafLMQ&t=371s)** Yeah, and I talk a lot about you have to like both raise the floor. Like we have to do just a little bit better on our baseline and take off the ceiling and I think AI can help you do both and often you have like one set of people taking off the ceiling and saying hey everybody else like take off the ceiling instead of like this is how I can help you raise the floor. Okay, so show us what PMOS is, its skills, what it does, how are you relying on this day-to-day?

**[6:39](https://www.youtube.com/watch?v=ztt8irafLMQ&t=399s)** Cool. Okay. So, this is the rough structure. It started just as like a really simple repo inside of Cloud Code as a TUI. So, it's got this you're a you're the PM's chief of staff, you know their work. I hate the term chief of staff, but like that's just means really useful for like PMing. It's really good shorthand, um which makes me die a little bit every time I read this. Um when the session kicks off, it reads some information about like who the um who the PM is, who they work with. It's got a memory file. And then it's got a couple of different skills that we can walk through. So, one of them was just like we had no good data on like which set of people work on X thing. Like we have several different org chart tools and like none of them are stitched together in useful ways.

**[7:30](https://www.youtube.com/watch?v=ztt8irafLMQ&t=450s)** And so, one of them is just like literally who works on this team, who owns X, and it calls it when it writes docs. So, if you need review on a doc, you the PM do not need to remember to say my my engineering manager is Aman. It just adds all of the relevant people as like Charlotte is my designer and Aman is my engineering manager and it adds them as the relevant people and remembers who your skips are. So, that's skill number one, which is just like a nice way of reducing some of the like repetitive work uh inside of new docs. I use it a lot as like a meta Slack. So, our our Slack is insane. I feel like anyone who's in a large enough org in tech just like slack becomes really unruly. I archive roughly 10 channels a day. It's bananas.

**[8:17](https://www.youtube.com/watch?v=ztt8irafLMQ&t=497s)** Um and so one of the things that we were really focused on uh was how do you help PMs know where to focus and what to do and like go run down all the things that are important. And so, I run this skill what's up like six times a day. It pulls all of my relevant slacks and projects together. It pulls all of the things that I like who I owe stuff to, what decisions are outstanding. I have a version of this that runs through all of my live experiments on the platform and like gives me a Not that I peek at my, you know, I just stop using my I don't peek at my experiments.

**[8:55](https://www.youtube.com/watch?v=ztt8irafLMQ&t=535s)** Say it. Say directional. Say directional, I dare you.

**[8:59](https://www.youtube.com/watch?v=ztt8irafLMQ&t=539s)** It's right. Um and so uh I I find this thing to be incredibly useful and let's see if we didn't find anything. So, it will look at like certain channels that we've identified as useful. It will read the whole thread. This is probably a little over specified. Like I feel like we're all moving towards like the models are just good enough now, but there's a lot of stuff in here about how to find exactly the right stuff for the way that we are all set up in Figma. Um which is just enormously helpful for how I run my day-to-day as someone who's just in way too many meetings and trying to do too many projects.

**[9:36](https://www.youtube.com/watch?v=ztt8irafLMQ&t=576s)** What I like about what you're showing because so many of these like PM OSes that we've seen skip all this like foundational piece. Which is in large organization, it is actually really hard to know like who should have an opinion on this product? Is somebody else working on it? And so, I like that you invested in sort of like the baseline context gathering as skills. And then I'm presuming that helps like level up some of the more like complex or strategic workflows that come out of PM OS.

**[10:06](https://www.youtube.com/watch?v=ztt8irafLMQ&t=606s)** Yeah, it's been a long time. I like tried to build a benchmark for unsuccessfully and I'm curious how you think about it for all the stuff you're doing now, but like I would be really curious how this performs relative to like totally vanilla Codex these days. Um, but I do think like in general, especially in that early like I don't know, like last October through like May as like the models were getting better, but we're not like superpowered yet. Felt like it was really, really helpful for how it navigated all the weird parts of like Figma's IA.

**[10:38](https://www.youtube.com/watch?v=ztt8irafLMQ&t=638s)** Yeah. And one thing again, we actually didn't specify this for folks, but Product Team OS is a repo, right? So like take a step back and tell us like what is it? Is it a repo of skills?

**[10:52](https://www.youtube.com/watch?v=ztt8irafLMQ&t=652s)** Yeah.

**[10:53](https://www.youtube.com/watch?v=ztt8irafLMQ&t=653s)** Is there more to it? Like what is actually the thing?

**[10:56](https://www.youtube.com/watch?v=ztt8irafLMQ&t=656s)** Yeah, so it's a really, really basic repo. Um, and so it's got an agent.md which just tells it how to behave. It's got a bunch of related skills that tell it when to fire and what to do. It's got a couple of command hooks. So things like on boot go find out if there's a new version of PMOS because we wanted a good way to like keep our 60 to 70 PM kind of roughly in sync. Um, we've also got a couple of built-in folder structures. So the base template when you onboard is this like it's a dot folder so it's invisible and you can't mess with the context, but then it duplicates and it sort of builds your version out. And then it's technically two get repos. It's the parent repo that everyone can download and then their workspace is a sub repo so that if you want to write stuff back, you can write it back privately.

**[11:52](https://www.youtube.com/watch?v=ztt8irafLMQ&t=712s)** Amazing.

**[11:52](https://www.youtube.com/watch?v=ztt8irafLMQ&t=712s)** Again, cuz like none of this was in a UI at the time and so we were all just trying to figure out ways to like make GitHub work for PMs who had never touched GitHub before.

**[12:00](https://www.youtube.com/watch?v=ztt8irafLMQ&t=720s)** And there was there a small group that sort of like brainstormed what these initial skills should be? Was it like, "Hey, everybody just pick their favorites."

**[12:09](https://www.youtube.com/watch?v=ztt8irafLMQ&t=729s)** How did that work?

**[12:10](https://www.youtube.com/watch?v=ztt8irafLMQ&t=730s)** Yeah, so Jen and Lawrence I think talked about this a lot at Config this year cuz they did a a little presentation on this, but basically we we had a really small Slack channel of just the three of us hacking away and firing off as many PRs as we could for a little bit. We had that sort of like Cambrian explosion of like a thousand skills and then started to like whittle stuff down. And then we did an offsite with every PM at Figma this spring where we had everyone install it, use it, hack on it, come up with like what was good, what was bad, just like roast it. Um and so some of the skills that are in here came out of that. Some of the skills either got whittled down or whittled away. And I would say as the models have gotten better, I've been trying to basically take stuff out that's no longer useful.

**[12:53](https://www.youtube.com/watch?v=ztt8irafLMQ&t=773s)** That's that's great. And so I have a question. Do you have as a team any telemetry on this? Like how it's being used? What have you Is it instrumented?

**[13:03](https://www.youtube.com/watch?v=ztt8irafLMQ&t=783s)** No, I thought about doing this and I did I decided one, I like didn't want anyone to feel creeped and uh and like I wanted to be fun and I also just didn't have the time for it cuz all of this was, you know, like sort of 20% time. Um the biggest thing for us was just we like PMs at Slack are chronically online. And so we got a lot of feedback. And then we had a public channel and so we started getting like all of the engineering managers started using it and asking us if we could like come help them talk about how to do knowledge work for engineering. Um our data scientists have one that is like essentially a fork of this. Um and so we were getting a lot of feedback about what it was good at and what it wasn't good at.

**[13:45](https://www.youtube.com/watch?v=ztt8irafLMQ&t=825s)** And I think for us the the big next thing and we can talk about the evolution into what it is today if that's helpful, but like mostly for us it was we managed to get a bunch of PMs comfortable in the terminal, but like surely that's like not the right end state. Like especially if you're doing a lot of writing, it like sucks to read monospace font all the time. And so for us like that was where we wanted to spend our time is like okay, what what would be next? How do we get people out of the terminal now that we're we've got them comfortable to concept.

**[14:15](https://www.youtube.com/watch?v=ztt8irafLMQ&t=855s)** Well, before we go to what's next, can you walk us through like just a couple more of your favorite skills in here? Maybe ones that teams haven't thought of or you think are particularly unique or kind of helpful?

**[14:26](https://www.youtube.com/watch?v=ztt8irafLMQ&t=866s)** Yeah, sure. So, I do think for us like with a busy Slack, the the kind of like meta what's up that is tuned to just like literally what do you have to do every day and how do you judge whether you're doing a good job is really useful. Build artifact is um one of my favorites at the moment, which is if I have something like actually this um this demo like dashboard that I made for this podcast is just like a really simple HTML artifact and then we have the ability to publish it. We've got a like little hosting tool that we use internally. And so it takes it through it's got um in this case it has a template HTML and I've got a couple I don't know where they're sitting and I've like totally lost track of my folder structure at this point, but um there's like a couple of different templates of little CSS that I like and I've sort of grabbed from different places.

**[15:19](https://www.youtube.com/watch?v=ztt8irafLMQ&t=919s)** Um and so build stuff like this when I want to show stuff off. FigJam, the MCP for Figma is insane. I don't know if you get to use it on a regular basis, but I feel like I use the MCP all the time and one of our PMs built this amazing FigJam builder that produces these like wild workshop templates very quickly. And so just figuring out like how to load it up with like what do you think looks good or how do you think should work? And so there's a lot of taste in here on how it's designed. There's you can also tell there's like we've got a lot of Claude Slap in here from earlier, right?

**[15:55](https://www.youtube.com/watch?v=ztt8irafLMQ&t=955s)** I was going to say that is such a Claude Slap sentence right there.

**[15:59](https://www.youtube.com/watch?v=ztt8irafLMQ&t=959s)** Um but it's a mix. Like there's a lot of stuff in here that like if you look at this output compared to some of the FigJams that we would put together natively internally, like it's it's just a really good set over time. And then maybe my favorite other one is coaching, which I use um as someone who used to manage people and is now I see it again. Like I spent a lot of time Oh it's so nice. It's so good. I used to spend a lot of time thinking about how to coach people and you know, I feel like managers are very busy especially now and so thinking about like I always wanted to make sure I was doing the first pass of my own coaching before taking it elsewhere and it's just really good at saying like hey, here's our career ladder. Here's where you are. Here's all the feedback that I have about you. I'm going to listen to your problem or I'm going to listen to this thing that you're working through and I'm going to tell you basically like get over yourself and don't be like don't worry about it and just like keep working on this thing or like learn how to communicate with this person cuz I remember that the last time you had an experience with this person like you misunderstood them and when you

**[17:12](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1032s)** had a conversation about it, you understood that you had just misunderstood. So I really like it for coaching. I think it's really really strong on that one.

**[17:18](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1038s)** And you have about 30 31 like just looking through the list they seem like both a combination of very tactical, interpersonal and then like generative in some ways. That seems to kind of be the the the the catalog of them. Okay, so how do people actually use this? Is this a kind of like app that you built? Like Yeah. How are people using this?

**[17:43](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1063s)** Yeah, so I think it's been a little bit of a journey. So we started in Claude with the like literal TUI in terminal. We had like a lot of debates about like the best terminal app cuz people were coming over from UIs. Then we built a little front end for it which runs locally and tried to make it really fun. It's got like all of the like lead code type ASCII art in it and the goal here was just bring it into the web browser so that people could type like we're doing a lot of writing. It's hard to read monospace. It's got some nice markdown formatting. We built it it works on mobile. I actually like right after This was This was pre-Astra, but like I spent a bunch of tokens building like a local native version just to like see what it look like.

**[18:30](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1110s)** Now I'm basically in Codex 100% of the time. One, I think browser use has gotten really good.

**[18:37](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1117s)** So good.

**[18:39](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1119s)** Really good. Um we have uh we don't have permanent desks in the New York City office and I don't like thinking about booking a desk every day. And so every once in a while I have it running on a schedule to just like book my desk one day out. Um but it's also it's a total beast at bug bashing. And so um like in Codex I have a little bug bash. I have like a threaded conversation that just lives here all the time. And when something new comes up for our team where we're about to launch an experiment or redesign or something, we have these FigJam files that explain here's here's how to bug bash it. Like here's the test account to take. Here's the path to follow. Here the actions to do. And like here are the things to look for.

**[19:23](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1163s)** And I have started basically snagging one account for me and one account for Astra. And just having it run through. So in this case we are trying to make some of our uh request models inside of Figma just like much more straightforward and much more streamlined. It's all UX stuff. It's all UX writing. It's fairly straightforward, but the like logic behind it is really complex. And so Astra is just much much more diligent about following directions than I am. And so I will run it through and I will say like keep doing all of these specifically. And just like it will run through all of these scenarios and it will use the browser and uh it's a dream. And then when it's done it writes out back to the FigJam board of all of the things that it has done.

**[20:11](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1211s)** Uh and I feel like we are still tuning it so that it is not like annoying in the comments that it develops. But in terms of like what it finds for me, like it it found for Two things it found in the last month. One it discovered that if you put a thousand emojis in a text box, it would break. Which like weird weird edge case, great, good to harden. Two it did it found that the way we had you request a seat for a given team inside of Figma. And when you do it uh it shows your team name. And we had a like a quote team name seat.

**[20:49](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1249s)** Mhm.

**[20:49](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1249s)** And if your team name starts with a, you need to use an.

**[20:53](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1253s)** And

**[20:55](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1255s)** It had just not shown up in our earlier bug bashes because it really depends on what the team name is. And so it was just it wound up being so diligent that it caught really small notes like that that I would never have caught on my own.

**[21:05](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1265s)** This episode is brought to you by Jira Product  Discovery. With AI, a single PM can summarize research, draft a PRD, and build  a working prototype. But multiplayer mode, that's broken. You can't get everyone aligned on what should actually ship with just a markdown file. Jira Product Discovery gives your team one place  to capture insights, prioritize with evidence, and build living roadmaps everyone can rally around.

**[21:33](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1293s)** And because it's powered by Atlassian's teamwork graph, it has the context you need to decide what to build. Those decisions flow straight into Jira, so your developers or coding agents can start building with the context behind every decision. More than 25,000 companies already use Jira Product  Discovery. Try it free at atlassian.com/howiai.

**[21:59](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1319s)** That's atlassian.com/howiai. Jira Product Discovery, better product decisions in the AI era.

**[22:09](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1329s)** I I love that so much. And so I think this like bug bashing workflow is a really great one. I highly recommend people do this and then keeping track of it in a FigJam or some other sort of like kind of asset is helpful for you to just track what the feedback is. You have another automation that you're using in the team around experiments, right?

**[22:28](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1348s)** Yeah, so one of the things that I had been thinking about for a while as our models have gotten better is like what are all of the different ways that we can improve cadence. And so one of it like I as a growth PM, I feel like the biggest sin you can commit is wasting traffic, right? To like have unallocated traffic that is not running towards an experiment at any given time. It's like why are you wasting that traffic? And so thinking about ways that we could run an experiment on a surface we would never have spent time doing normally was really, really interesting to me. And then the models were just getting good enough across a little bit of engineering, a little bit of data science, the user like the user experience writing was not so bad, the ability to come up with like within a really bounded sandbox was getting better.

**[23:18](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1398s)** And so I started to thinking about like what if we could just automate myself out of a job and like create a little growth PM who could just like run it, run it, run. Um and there's there's been a couple of other folks who have done this. I think some of the folks at both Labs have done it, um which is where a bunch of this inspiration came from. But I realized that internally we finally had all the tools. And so I call it Auto XP. And right now one of our engineers is running it and has like five different experiments going that I have not taken a look at and are just and it found a huge win on its very first experiment. And basically the way that it works is this you can see this is like one of the fancy schmancy artifacts that we made for this. Um is it works as a cursor automation. So there's it there are three cursor automations that trigger based on stuff in Slack. Auto XP has its own channel where it can communicate with itself.

**[24:14](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1454s)** Someone can either tee up an experiment uh in the Slack channel or they can or it can just like run on a loop. So one of the things you can do is just say, "Hey Auto XP, go find an experiment to run on our settings page. See what you can do. Go crazy. And it will trigger a data scientist to go find or data scientist agent to go find uh to go find drop-off and like look at the funnel and look at mix shift and all those things. It will trigger a UX writing agent that will come up with some ideas for copy in a given place. Um we're like moving towards more front-end design now. Um and then uh lastly it'll trigger an engineer that'll pick up a PR and run it. And then again, with all of these steps it writes back to the Slack channel in the same thread so you can follow over the course of the experiment basically like what's happening.

**[25:06](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1506s)** Um and there are two things that I think it does here that are really amazing. One of which is we are able to run experiments in places we would never have bothered to dedicate time or traffic. It's way faster to get from I have an idea to this experiment is launched. And then two, um when it's done, uh when an experiment finishes, it triggers uh essentially a webhook back to the original experiment to say, "Hey, it's time to analyze these results." And it has a bunch of instructions from all of the time that I have spent as a growth PM to figure out like, "Do we want to explore more? Do we want to try to exploit? Is this a win? Is this a loss?" And the goal for all of this is the only time you're allowed to look is before you launch the experiment. So you review the data science findings, the hypotheses, the UX writing, and the code all at once. So like one human touch. And then it watches and then you can review whether or not it's a winner or a loss, but it has already started iterating on the next rounds.

**[26:08](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1568s)** I would say like where we are in theory is pretty like is great. Where we are in practice is almost there. And so one of our engineers, Maryanne, has been taking this really, really far. Um but we're now at like five live concurrent experiments on things that we would not have been doing otherwise.

**[26:26](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1586s)** So this is a little bit of Clervo lore, but for those that are are new to me. I have worked at every experimentation platform company in history and did a startup literally well 13 years ago, something like that called Experiment Engine and the whole hypothesis was like how do you get how do you exploit all this traffic and maximize the number of experiments and then like what a time to be alive. It is here. You can just like five code five coded there. This is amazing. Okay, I want to show one last thing which is my boy Jeff. And we've been doing a lot of Jeff

**[27:06](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1626s)** We wouldn't have heard Jeff.

**[27:08](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1628s)** Poor I we I don't know. I think Jeff got a got a real shot at someone longevity here but

**[27:13](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1633s)** Jeff's juice.

**[27:14](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1634s)** You have Jeff's  juice. But you built something really cool with Jeff that I want you to show cuz it's a use case I haven't seen yet.

**[27:20](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1640s)** Yeah. Yeah, totally. So right. So for people who don't know well how could you not know? I feel like if you're listening to how how I AI right now, Jeff is this model where you can ask it really weird complex questions in text and you get like essentially a number back, right? So like how good is this on a scale of one to 10 or is this true or false or like what is the meaning of life? Is it A, B or C? And it's really fast and it's really cheap. And so I started thinking about all of the different places we could shove this that would really change the way that people work, right? So if you've used Figma has an agent on the design canvas. I adore it. It's really really good but it is still subject to all of the latency that you get with all of these top tier models which is like it's slow in places where you want to have a co-worker and it doesn't feel like a co-worker.

**[28:09](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1689s)** And so as we work on that, Jeff feels like really really interesting for some of those possibilities and one of the first things I was thinking about was this idea of like what if it could run questions about things you were writing as you were doing it. Like what if it could know that you needed to if you've ever written a blog post and had a section where you aren't sure what's going to go there, maybe you write TK or you leave some brackets. And sure, you could do that like totally programmatically. It's just like look for and identify. But also maybe you have a claim that you're not sure like you have data for or you need to go look up in your notes later. And so I basically I built this prototype. I'm going to forget the name of it, but there's I think it's called Marker, which is this beautiful looking writing app from this guy Stein Deck, which is an incredible name for a guy who runs a writing company. They have some of these ideas around it. And so as I was just playing with like what could be possible with Jev, that was kind of one of the inspirations here.

**[29:13](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1753s)** And I wanted to have Jev basically make a call to Jev anytime I stopped typing. And so the thing that it does is when you stop typing, it will look for places where you've left blanks or claims worth supporting. And it will use stuff in your library to go ahead and actually like substantiate those claims. So in this case like I said most people find it easier to keep writing than to stop and look something up. And it's making a call here as soon as I stopped writing it into the library where it has all of these interviews about like what these people actually did. Like if I go hunting for a number this it will I forget the sentence I was trying to write. We recently put the API behind our own internal firewall so let me see if I can actually run it live or if it's going to get mad.

**[30:09](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1809s)** Uh Okay, and then

**[30:14](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1814s)** Hot dog.

**[30:14](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1814s)** Oh no, hold on. But it doesn't actually want to Is it blocking it? Oh, it is blocking it.

**[30:21](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1821s)** I don't know. It It impressed me. It did something fast.

**[30:25](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1825s)** Right.

**[30:26](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1826s)** Okay, so I just want to like reiterate this for people because it is mind-blowing, which is as you write as soon as you stop for a minute, it runs a quick Jev check, which is very, very fast and says like, "Does something need to be filled in? Does something need to be supported? Like, what questions do I have about what you're writing?" And then like hooks up to data sources and actually helps you improve your writing as you I Jeb.

**[30:50](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1850s)** Right. Okay, so this is how it works. So, you've got um here you've got your title. So, this is my title. And as soon as I stop, it's going to start checking things. So, maybe I've got um I was thinking about how we serve writers and I thought TK. Okay, and it's like you had a thought that you didn't finish. But then you'll see like it also ran a check and it said I I have no idea what you were thinking cuz it's not in this library. But then I could say something like uh we spoke with X writers and they said and it both knows that I need to finish this and it went and pulled from the library like literal interview quotes from like writers we allegedly spoke to for this. Um so, this one is actually blew my mind.

**[31:38](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1898s)** I like this. You do you rarely uh one of these at How I I a full clear hands up. Jeb.

**[31:45](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1905s)** It's so cool.

**[31:47](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1907s)** It's so cool.

**[31:47](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1907s)** Um I just know all I for literally for like 2 weeks after Jeb dropped, I was just like running around going like, "Okay, but like can we talk about Jeb?" Like it was every meeting I was in. My engineers, some of them are very excited about this. Some were maybe like a little irately about it, but it's just it's such a cool idea cuz I think you can imagine all of the different ways that if you could run checks on things at any given time like what you would do with it. And I the thing that sort of blew my mind was that they had built it for rag or for essentially for like search and document retrieval as well. And so, the ability not just to say like this looks like a pattern, I am confident that this you left something, but also I took this block of text and it relates to this section over here and I did it in real time is just like is kind of incredible.

**[32:38](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1958s)** It's unbelievable. Um this this podcast is now how I jev. Just

**[32:43](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1963s)** It did I did have this really bleak thought which is it made me wonder if like you could imagine you're interviewing for a PM job and you like yap your entire career into something and then you have a voice to text that is just like searching against like what your examples are and I did have this fear cuz I run a lot of product sense interviews that I was going to start running into people who are like jevving their own little helpers um which I don't know maybe I should hire them if they do that's great.

**[33:10](https://www.youtube.com/watch?v=ztt8irafLMQ&t=1990s)** Hire that I was like great sign me up. Um Ezra, this has been so good. Okay, we're going to get to lightning round. I just to reiterate for folks, what do we see? PMOS with 31 skills including what's up, what do I have going on today, find me people in the org, write specs, coach me, the whole thing. You basically are now using that through Codex entirely also because Codex is magical for browser use and then you built a real-time jev editor author writing tool um that you're afraid is going to cause you trouble in future PM interviews or impress you in future PM interviews. So many good workflows in this. Um so the folks that have stuck with us this long, you have gotten some good stuff. Um quick lightning round questions and then I will get you out of here. One, you told me a couple weeks ago you were using Instinct. Are we still on Instinct? What are we doing with our personal agent?

**[34:11](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2051s)** Okay, so I still get texts from Instinct and I don't respond. That's how the way it works. So um for people who don't know, Instinct is this um this really sort of beautiful idea like I'm really into it which is this idea that what if you had a proactive agent but instead of like needing a website to visit or an app to use, it just like texts you in iMessage. And I will say I still use it every once in a while. It was this kind of magical thing at at where it was proactive in the right ways and this like concept of memory it that was like useful in this kind of mind-blowing way. And I suspect there's a bunch of people who have been running open claw for months who are like, "What's the big deal?" But it just it productized this really nice experience in a way that was really great.

**[34:58](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2098s)** And for the first few weeks, you could buy things on Amazon with it. Um which while not like a killer use case was really nice cuz I would just walk around the house and I would say, "Hey Siri, tell Instinct that I need to buy paper towels." Or like my current use case is I bike my kids around Brooklyn and I will run into potholes all the time and uh now you can like you can 311 like a a fix my pothole and I never remember to do it on time because like you have to look at the address of where it is and you have to report it and the website is kind of trash. And so I have started like, "Hey Siri, text Instinct there's a pothole at like 269 Atlantic." And it just remembers like what it's supposed to go do and submits it. So I do use it for that and it's amazing for that. But I mostly switched over to dots now that I'm like fully codex built.

**[35:49](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2149s)** I I I So I um I'm trying to make dots. I'm trying

**[35:55](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2155s)** You're like you're like grokking youth, is that right?

**[35:58](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2158s)** so I like max codex maxing. I love codex. You could rip codex out of my cold dead fingers. But for work, I'm all grok. Uh and then for personal you should check out muse. It's a real it's a real delight.

**[36:12](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2172s)** Uh I can't I can't bring myself to do that.

**[36:15](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2175s)** I know, but they've been stealing our data for two decades, you know?

**[36:19](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2179s)** I know.

**[36:20](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2180s)** That's my as I say to people, the devil I know. This is really where I'm at with my personal data.

**[36:26](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2186s)** have the data. So fair.

**[36:28](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2188s)** Yeah, I said my joke is my Instagram ads will get better. I'll I'll end up spending more money.

**[36:32](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2192s)** This is I think this is like a real value prop. Um

**[36:35](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2195s)** Okay, and then my last question for you, when your dot is

**[36:40](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2200s)** Yeah.

**[36:40](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2200s)** being obstinate, your AI is not giving you what you want.

**[36:44](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2204s)** Are you a yeller?

**[36:44](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2204s)** Yeah. No. No, I'm not. I think we should all be nice to our AI. Um, I treat my AIs like a friend that you love who's really like messing it up. You know, you're like, "Buddy, like get your life together. Like you're too old for That is how I treat so Hold on, I will will show you. Cuz I I yelled at my dot twice today, but I I did it very friendly. Okay. So, I ordered some shoes. They were too big. I need a half size down, and I tried to like find it the cheapest version. And it was like, "Email search is temporarily rate limited. Can you go search your email?" And I was like, "I don't know, man. That's what I needed you for." Um and then uh it gave me some like really expensive stuff. And I thought maybe it was being lazy, and so I just said like, "Yikes.

**[37:35](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2255s)** Assume you aren't going to check this." And I I was trying to figure out why I don't yell. And I think partially like you can ask Ask my wife. I am like mercilessly not a yeller. But I also think someone posted this on Twitter recently and I it really expresses how I feel, which is not that I have some Like for for people who don't know, there's like this idea of like basil What is it? Basilisks? Like this idea that if you're mean to AI, but then it turns out they're alive, like wouldn't it have just been easier to be nice? Like isn't that cheaper than like getting turned into a paper clip? And I don't I don't think they're conscious. I don't think they're approaching conscious, but I do think it's really bad for the soul to just be mean to things all the time.

**[38:18](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2298s)** Like in the same way that you like Like there's just no reason. Like it's just I feel like I get worse when I like yell at things that can't help it, even though I don't think it's conscious.

**[38:28](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2308s)** You know, I like used to be a very hardcore not yeller. And I'm not like I'm not mean. I wouldn't say I'm not saying anything nasty, but I am a very I'm like a all caps like, "Why? Like why Why are you like this?" You know?

**[38:43](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2323s)** Why would you do this to me?

**[38:44](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2324s)** And here's and here's why I will say this. I'm spending thousands and thousands, if not tens of thousands of dollars, on LLMs.

**[38:52](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2332s)** Yes.

**[38:52](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2332s)** Like a why are you like this after like $2,000 of wasted tokens? That's like That's like a cheap

**[38:59](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2339s)** But that doesn't strike me as that mean.

**[39:01](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2341s)** Yeah.

**[39:02](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2342s)** like I have You know, there's like there's some real like

**[39:05](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2345s)** nasty cut it stuff. Yeah. No, I'm just uh expressive.

**[39:11](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2351s)** Yeah. I think that I will say my take is that normally when I want to yell at AI, it's because I have given it poor instruction. This is how you know I have kids is like there's so much of that which is like when you get a bad result, the odds that you have like poisoned the context and asked a bad question is like pretty high. And so, I will occasionally find myself in loops. Like Codex has this Codex, if you're listening, opening ITeam, if you're listening, has this really bad bug right now where if you start a local session and you kick it to a remote session, even if you have Yolo mode enabled on your remote session, it inherits the sandbox with ask permission every time. And so, I wind up in like clicking approval hell. And I get so mad and I go around in loops for a little while where I'm like we already fixed it. Like you have permission. I'm looking at the file. I pulled up the file. We're looking at the config.toml together. Like what are we doing?

**[40:10](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2410s)** And usually the answer is like the context is poisoned in that conversation and it's unrecoverable and yelling at it is not going to help, so start a new conversation and just move on with your life, which is not satisfying.

**[40:20](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2420s)** Let me give you a a TikTok parenting tip if you want to like really devastate your AI by being a kind parent, which is I know that you're capable, but you're not You're not You're not showing me how capable you are right now, and that's just signaling to me I need to be a better parent.

**[40:43](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2443s)** My Okay, I love that. Um that one, stealing the parenting tip, two, stealing it for AI. I feel like I really love to give my AIs like big expectations. And I You feel like you saw it in the math proof, but like I have been doing a version of this which is like buddy, like I know you can cook. Like you would not believe the things that I've seen out there that you are capable of. Like if you try a little bit harder, I am sure that we can vibe code this prototype that I can show my engineers so that we can build it. Like I know this is in your capabilities.

**[41:17](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2477s)** I know you can vibe code Salesforce. Just a little

**[41:20](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2480s)** Totally.

**[41:22](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2482s)** Okay, Ezra, this has been so fun. So many good use cases, so many good thoughts. Where can we find you and how can we be helpful?

**[41:30](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2490s)** Yeah, um mostly on Twitter. Uh I post too much. Um Ezra McCabe. Uh and then in terms of being helpful, uh we're hiring PMs. We're hiring a lot of PMs. And we're hiring a lot of different kind If you're an engineer or designer, we're hiring. Come work at Figma. It is the most fun I've ever had in a job. Uh we're just we're building really cool things and the people are great.

**[41:54](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2514s)** Amazing. Cannot cannot end it better than that. Ezra, thanks for joining How I AI.

**[41:59](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2519s)** Thanks, Claire. Bye.

**[42:01](https://www.youtube.com/watch?v=ztt8irafLMQ&t=2521s)** Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review which will help others find the show. You can see all our episodes and learn more about the show at howiai.pod.com. See you next time.

