<!--SUMMARY-->
## Actionable summary
**Host:** Kevin Pereira and Gavin Purcell, AI For Humans  ·  **Show:** AI For Humans, 23 Oct 2026
**Tags:** ai, ai agents, ai product, future of work, engineering, general

**When to use this:** You want a plain-English account of how AI changed the speed of cyber attacks and why AI agents acting inside customer accounts worry institutions, for a client conversation or workshop on AI risk.

**Big idea:** The hosts argue that AI tools now let attackers and defenders move far faster than the old patch-then-exploit cycle, so organisations and individuals can no longer wait months to catch up.

**Frameworks & plays:**
- Assume the window between a vulnerability being rumoured and being exploited has collapsed. Kevin Pereira describes the old pattern, where a flaw was confirmed, patched and only then exploited, and says that in an agentic world "if there's even a whiff or a rumor of a vulnerability, people turn their agentic machine onto that piece of software."
- Do not give an agent direct access to money. The hosts open with "please, dear lord, do not connect your agents directly to your bank accounts, just for the time being."
- Expect institutions to catch up on agent access. Gavin Purcell relays an Axios story saying banks see some AI agents acting in accounts without clear user approval, and argues institutions "no longer have a three to six-month window to catch up."
- Judge a model on price per usable shot, not just on looks. Gavin compared Wan 3 and Seedance 2.5 with identical prompts, found Seedance more realistic, and said Wan 3 was about a fifth of the price, which adds up quickly on long-form work because you throw away a share of shots.

**Data & benchmarks:**
- Exploit attempts after the PHP flaw went public, as relayed by Kevin Pereira from Cloudflare's CEO Matthew Prince: thousands, then tens of thousands within 45 minutes of the announcement, hundreds of thousands within 2 hours, and supposedly over a million.
- Wan 3 was described as about a fifth the cost of Seedance 2.5 on the Fal platform.

**Tools & prompts:**
- Claude Duet is described as a separate app, still on a waitlist, aimed at work tasks and carrying over a user's Claude skills and connectors. The hosts worry about an agent going rogue and about token spend on proactive behaviour.
- Vendor note: Gavin says Fal is not a sponsor but has given him credits.

**Contrarian take:**
- Gavin Purcell argues that slowing AI down publicly would not slow it inside AI companies, and says he wants cybersecurity professionals to have the most advanced models.

**Steal this (do tomorrow):**
- List every system where an AI assistant or agent could log in on your behalf, including anything that touches candidate data, and confirm in writing who has authorised that access.
<!--/SUMMARY-->

# AI Just Broke The Internet. For Real This Time.

- **Podcast:** AI For Humans
- **Channel:** AI For Humans
- **Date:** 2026-10-23
- **Duration:** 53:28
- **URL:** https://www.youtube.com/watch?v=-XIgyMsZZxY
- **Fetched:** 2026-11-04
- **Source:** YouTube captions via TranscriptAPI (en)

## Episode description

AI news this week: It's the AI Cybersecurity apocalypse. Maybe. AI-found PHP flaws pushed governments to take websites offline, Railway got hacked and US banks are finding rogue AI agents inside customer accounts.

On today's AI For Humans, Kevin Pereira and Gavin Purcell dig into the wildest cybersecurity week in years. AI helped surface bugs that sat inside PHP (which runs a huge chunk of the web) for years, governments told everyone to patch now or pull the plug, and Cloudflare's CEO says exploit attempts hit the millions. We break down what you actually need to worry about and how to keep your vibecoded lil apps from draining your accounts. (Short version: def don't hand your agent your bank login.)

Also: the fun side of AI hacking. People are using Claude Code to vibecode their smart TVs and rip out the bloatware. In Good News / Bad News, Anthropic finds small AI models may soon copy themselves onto cheap gadgets (yes, even your smart fridge), while Claude helps with scorpion antivenom research.

Plus: Unitree's H2-X kung fu robot, Flux 3 Max, Wan 3 vs. Seedance 2.5, Claude Duet, Gavin's Higgsfield mini-rant, ASCII Mario Kart, Machine Gods (the new Kevin Roose and Casey Newton podcast) and more.

PLEASE UPDATE YOUR PHP. WHATEVER THAT IS. JK WE KNOW. REALLY.

#ai #ainews #claude

// Chapters //

00:00 AI Is Now Powerful Enough To Hack The Planet
01:52 The PHP Vulnerability Meltdown, Explained
05:43 How AI Found The Bug & Why Exploits Hit 1M+ Attempts
10:03 Should AI Slow

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube. A new paragraph marks a change of speaker where the captions show one (speaker names are not available).

**[0:00](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=0s)** It might be time to freak out as AI tools have gotten powerful enough to hack the planet.

**[0:06](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=6s)** HACK THE PLANET! HACK THE PLANET!

**[0:09](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=9s)** WELCOME TO THE NEW NORMAL, EVERYONE, because in the last few days, vulnerabilities had entire governments across the globe screaming to shut down your computers, but AI is also giving a leg up to cybersecurity professionals. So, that's something.

**[0:25](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=25s)** We will tell you what not and what to worry about, and we will make sure that all your vibe-coded little apps don't drain your accounts.

**[0:32](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=32s)** Yes, and please, dear lord, do not connect your agents directly to your bank accounts, just for the time being.

**[0:38](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=38s)** Oh, wait, wait, Kevin, I I have to go. Totally unrelated.

**[0:40](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=40s)** Wait, yeah, did you Okay. Great.

**[0:45](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=45s)** I'm back.

**[0:46](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=46s)** Oh.

**[0:47](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=47s)** It was unrelated.

**[0:48](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=48s)** Okay, here's something nice. People are vibe-coding all over their e-readers and their smart TVs and their freaking Tamagotchis, and they're removing bloatware, they're adding custom interfaces. They're just having a good time. That's nice.

**[1:00](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=60s)** That's right. It's not such a bad time in AI. Plus, we have amazing new tools like Flux 3 Max from Fowl and Claude Duet, which is Claude's new AI agent that I'm very excited about. It is a very workhorse-heavy agent. I cannot wait to try it.

**[1:15](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=75s)** And in case you think the robots have slowed down, look at what they're doing over in China. I remember how I reacted when I saw my first Waymo.

**[1:33](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=93s)** As do we all, Kevin. This is AI for humans.

**[1:38](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=98s)** I kicked the car, Gavin.

**[1:39](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=99s)** Why?

**[1:40](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=100s)** I threw a knee at a Waymo.

**[1:47](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=107s)** Welcome, everybody, to AI for Humans, your weekly guide into the wonderful world of AI. I'm Gavin Purcell, that's Kevin Pereira, and this week, Kevin, we have a seriously nerdy AI news week. There are lots of things happening. There are all sorts of cool AI tools we're going to talk about a second, but the biggest story right now is one in which everybody's  pretty freaked out. I I had various stages of kind of reading these tweets come through my timeline and seeing a few things. At first I saw something that said like, "Oh, PHP might be vulnerable." And then like I saw escalation over escalation over escalation. This is kind of the moment that we have been talking about for a while, which is that where the AI tools are getting good enough to kind of start not only worrying people about what we would call cybersecurity, but actually do the things that people are worried about.

**[2:34](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=154s)** So, I think this is a pretty big story. I think it's important that people kind of understand what's going on here. Do you want to kind of give the TLDR on like kind of the the security side of this and why this is such a big deal right now?

**[2:47](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=167s)** Okay, yeah. Which issue are you talking about though? There was a PHP issue. There were certificates that were basically compromised. They were cracked. It's not necessarily an AI thing, but it could have been. In California, data on every public school student since 2023 was basically stolen. Whoopsie doodle. Railway got hacked. Light LLM, which is an AI tool with millions of of uses every day, was poisoned with a password stealer. I haven't even scrolled past one post attempting to detail the last 48 hours. But yes, at the top of that one, PHP to shell. There was a a hole in the software and it Look, if you're in the the nerdy weeds about PHP, I had a couple of engineer friends on Threads go like um Okay, well, if you're running PHP, you deserve it, right? Who are you What are you? An auto body shop in Peoria? Uh.

**[3:43](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=223s)** But

**[3:43](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=223s)** is PHP, Kevin? Maybe tell people what it is cuz I it's been around forever on the internet. We should just make sure people understand what this actually does and and why Yes, the nerdy people are like, we've moved on but there's a lot of people that haven't.

**[3:55](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=235s)** I think some of the reasons people brushed it off is that we're talking about a technology that started back in 1994. It was a server scripting language back when websites were very very basic like super basic links. This gave you a chance to like create more dynamic web pages, right? It could talk to the databases, you know, it could help store information. So it made the web back then a lot more dynamic. Um well, just because it was back then doesn't mean it was completely phased out. You know, there's obviously much better technologies much further along but it's still in 70%. WordPress, a lot of WordPress uses it.

**[4:31](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=271s)** Have you paid a parking ticket lately?

**[4:33](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=273s)** I guarantee you

**[4:35](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=275s)** 95% of government websites are still run on some version of a server that was created maybe in the early 2000s, right? Like this is the thing that the thing to worry about here with this PHP thing. We'll get into like what's going on with it and and how it's been patched and why it matters but PHP is still something that is proliferated across not the kind of edgy internet that you might be experiencing, right? Like people like you and I or maybe a lot of our audience is out there doing things that are kind of like using a bunch of tools that are updating themselves and maybe are more secure. We're going to get to a few things that maybe aren't but PHP is used in the everyday web for lots of normal people and they may or may not have any idea of what's going on with AI and now suddenly it's in the middle of all their stuff. I think that's an important thing to realize too.

**[5:21](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=321s)** But now let's contextualize because I I would love to do an hour-long podcast about PHP specifically but why in AI for humans soon to be SI for humans. Yes, we're changing the name. You heard it here first. Juicy skewsy. Why are we talking about this in an AI thing because it wasn't like it wasn't AI created vulnerability. It was known. It was there. Why would we talk about it?

**[5:43](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=343s)** Okay, so let's talk we You to go back a couple months to when Claude Mythos first appeared in our lives. It didn't appear in our lives, it appeared in a video that was told to us because they were giving Claude Mythos, which we now know as Mythos 5, which is the basis of Fable 5. Hopefully Fable 5.5 soon, but that just keeps thinking people are going to roll out and it doesn't. At that time, they had a thing called Project Glass Wing, which was their project to try to open the door to all of these cybersecurity issues that AI was going to unveil because AI was so good at coding, it could also be really, really good at finding the backends into these software. So, why we are talking about it here and why it matters with the AI cause is that yes, this there is a vulnerability in PHP that has been discovered that has been there for a long time, but the worry that people have right now is that not only did AI probably help discover this vulnerability, in fact it did. There's a There's a bunch of conversations around actually somebody who saw 5.6 to help find it, but that the people who might hack these websites also now have the capability to do this. And I saw a post Kevin

**[6:51](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=411s)** Yeah, I saw a post where basically they said something like the open-source Chinese models, which we expect to be like 6 months behind the the frontier models, are may already have newer models that we haven't seen yet, but there are newer versions of these models where they could potentially have the capabilities of a Mythos 5, right? At this point now, because Mythos was announced in February. There Did you see Kevin, there was a I don't know this is confirmed, but I did see a bunch of people reporting it that North Korea websites, like all of their websites, were down for 24 hours. Did you hear this?

**[7:21](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=441s)** No.

**[7:21](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=441s)** This was like a thing I saw random headline. It was like I I again, that's just one of those things where like one of the other things to think about right now in this moment is there are lots of people freaking out, including very smart people freaking out, but we have to just be aware that part of this is that AI is getting stronger on both sides and you hope that both the white hat people and the cybersecurity people are also utilizing it as well.

**[7:46](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=466s)** So, welcome to the new new new arms race, or at least a forked a little a little branch of it. So, here here's one of the issues. It used to be Gavin, a foundational security issue was like rumored, maybe discussed, and then maybe with an elite team confirmed, and within an x amount of time, a patch was there. The cyber community they got to circle the wagons, and everybody would fix the foundational thing, and then the exploit would come to life. Here's how we did it, blah blah blah. And if you were really capable enough and had the scruples, you might be able to execute it on one of the few machines that missed that. Well, now in this new agentic AI-powered time, the the timetables are completely made up. Nothing matters, right? So, if there's even a whiff or a rumor of a vulnerability, people turn their agentic machine onto that piece of software or that piece of hardware.

**[8:37](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=517s)** Uh they try to hack it, and then the moment it's confirmed, even loosely, tens of thousands of agents can descend upon that. And and we saw that. There was a Matthew Prince uh from Cloudflare basically said that they saw thousands of attempts to exploit this. That jumped to tens of thousands in the 45 minutes post announcement. And then hundreds of thousands within 2 hours, and supposedly now well over a million. So, that's what happens now. Like, oh, there's a tiny little crack. We've see it here in the seams. Everybody points their machines and goes, and yes, there's going to be white hat hacker teams and white hat agentic teams that are going to try to proactively patch things for people, find vulnerabilities, go out of the way, but which company or which organization criminal enterprise, government, maybe they're the same thing, put on your tin foil hats, but which one is going to have more compute and more more and more energy uh more nerve to throw their agent teams at it. And if you thought the days of what McAfee virus scan and virus shield needing to run all the time on your computer gumming up your processors with that,

**[9:49](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=589s)** Maybe this is John McAfee. Maybe this is him out there finding his way back cuz he McAfee's not dead. Tinfoil hats, he's still alive out there somewhere, everybody. He's still alive.

**[9:58](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=598s)** He lives in here.

**[10:00](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=600s)** I Kevin, I have a couple other contextual points I want to talk about here. One is the fact that I think we have now reached another axis of whether the slowdown can happen, right? And what I mean by that is there's a lot of people out there talking about this idea that AI has to slow down, right? That we have to slow down. Well, if you think the AI should slow down, and listen, there's a lot of really smart people out there arguing that AI should slow down. And some people out there might be like, "Well, look at what it Yeah, oh really? Look at what it did for a second.

**[10:28](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=628s)** from a Costco saying it needs to slow down because they put a self-checkout at the Costco. That's what happened.

**[10:35](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=635s)** AI has to slow down?

**[10:37](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=637s)** JUST SAYING, IT'S GETTING EVERYWHERE.

**[10:39](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=639s)** Are the hot dogs the same price? That's all I care about. I haven't been back there and had one for a while. They kept them the same price, right? Anyway, um I think this is going to be a really fascinating thing because part of that argument around slowing down is like, "Whoa, whoa, whoa, hold on. Slow down. We don't know where these AIs are going. We don't know what's happening." Well, guess what? These AIs now are doing these sorts of things, uh like cybersecurity hacks, and it's not just the US versus China in this kind of race. Now it is a race of everyone versus the individual. And I do think that's a really interesting thing. Now, granted, the thing that I worry about with the idea of slowing down is uh we've said this on the show before. And by the way, this is a very nerdy show, as we mentioned at the top of the show, but I hope this is an important message for everybody cuz it is a a big thing going on right now.

**[11:24](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=684s)** If you slow the AI down, if slow it down, {quote} {unquote}, it does not mean that inside the AI companies it will slow down. And there is still a possibility of espionage or leaks from inside the AI company. What the slowdown in my mind means is that you get a very kind of different levels of people who have access to this stuff. I don't know what I think about it, but I can just tell you that I want to make sure that the cybersecurity professionals have the most advanced models because if we don't, we're just going to be fighting against these individuals who are going to do bad things. And and I think we have to kind of I don't know, part of me thinks we have to put foot on the gas in order to solve all this stuff.

**[12:02](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=722s)** It's it's an acceleration of behaviors that have existed for decades, right? There's been no shortage of people with DDoS attacks. We're just going to flood your website with a bunch of requests. And then we had to build tools and and with time there was new technologies that could really that could stop a lot of that, right? The issue now is that is that again anyone with an ounce of compute can go after systems. And the way it has been dolled out with with okay, who's in our little club? Probably meeting around a table that has like made out of human head skulls that have like symbols carved in them. But if you're at the meeting, right? And Oracle they tap you on the shoulder, you get early access to something. Okay, great.

**[12:42](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=762s)** Well, your systems are great and maybe your customers are great, but if you're not invited to that magical island maybe it shouldn't be an island. Let's say a volcano.

**[12:50](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=770s)** it an island. Give  me anything BUT AN ISLAND.

**[12:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=772s)** MOUNTAIN LAIR.

**[12:54](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=774s)** SURE, MAGICAL MOUNTAIN LAIR. The way it's being dolled out now, Gavin, is is understandable, but I think it's un untenable.

**[13:03](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=783s)** Yes.

**[13:04](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=784s)** A handful of companies having early access to secure their stuff is great. For literally everybody else in the wake, it could be very, very harmful, right? And what are the companies what are the providers what are governments going to do to stand up and say, "Hey, listen, if you run your business, if you serve your website or your app out of our country, we're going to guarantee you an agentic swarm nice little shield to protect you. And we'll make sure you're taken care of because otherwise they're basically saying, "Well, we're going to hoard the latest and greatest for ourselves and our buddies that are sitting around a table probably made of a human skull with all sorts of cool logos carved into it. One Stussy S. Who did that?" Allison. Come on.

**[13:44](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=824s)** But otherwise it just seems unfair, right? And I don't know how you can keep that up when it's sort of like, "Oh, here comes the next wave. Sorry everybody else who isn't one of us." But That's right. That's right. And I think what we should just have a couple of things on this real fast. One, there are a lot of smart people that are very worried about this. I saw a tweet from a person I don't know from Andreas Stuhlmueller who said he thinks it's plausible within a year we'll see AI based cyber attacks on the power grid, financial system, and internet infra. He actually talked about making sure you have money in cash. Who knows? Like I don't know enough about this but there are there are people who are worried. Yes.

**[14:17](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=857s)** I'm on Threads with with several, you know, very accomplished you know, VC types I'm on Threads I'm so sorry. No, no, no. Engineers that worked at you're on you're not on Threads the meta product. You are on Okay. Now that's that's funny to imply that anybody is on Threads. That's very funny. That's very cute. I like that joke. But no, I am I am in conversations and and truthfully Gavin there has been a we need to withdraw some cash on hand. But oh, what's that going to be worth when all the system crash? Or is it time to short the banks? Is something that has come across the wire as well. That's scary. I do think that this this sort Now there hasn't Look, remember Y2K was like get buckets of oats and make sure you got toilet paper or a shovel to dig a big enough hole because you're going to be covered in it for a while.

**[15:07](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=907s)** There is a little bit of that going on but you cannot deny that this stuff is starting to take off and it's only going to get worse. Yeah, and I think that you know, it's an important thing for everybody. There is a lot of like people out there especially who have kind of front row seats to this who have been wrong about these things in the past, right? Like there's a lot of people who are dooms daying across different things and they've been dooms daying for, you know, hundreds of years in the world of this sort of thing. I want to say one thing before we move on from this story. There's a story that came out from Axios this morning that that I think added fuel to this fire, which basically said that AI agents are unauthorized using bank software and this was from a bunch of banks. I think it was sources say, but I also want to be clear like there's a lot of people who don't necessarily understand what's going on, the sort of things that we do, right? Because I we mentioned this in joking way in the top of the show, but like there's a lot of people who are using their AI agents like Instinct or Grokbot or Muse and upcoming Cloud Duet and things like that to do bank actions.

**[16:03](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=963s)** And the banks would see these as unauthorized AI agents. And they they are saying in this story that there are some use cases that they are not sure are actual use cases that are approved by the users. But this is on the other side of it where big companies are seeing this stuff proliferate much faster, right? Like the rise of the AI agent we talked about, you know, a year ago, no one would have let an AI agent even sniff their bank account rather than like access it. And now people actually are. So it's not just on the fact of like what they can do and what dangerous stuff they can do, but it's also on the institutions themselves to inform themselves and to make sure that they know what's going on in the current state of AI because you no longer have a three to six-month window to catch up.

**[16:48](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1008s)** You need to be there right away.

**[16:49](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1009s)** I think that's fair. And also up to looks like hackers have taken over a control of my smart display and that used  to be pictures of my family and now they're all they're all Shrek. And

**[17:01](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1021s)** All of your pictures are Bad Island.

**[17:03](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1023s)** I  don't mind that.

**[17:04](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1024s)** Actually, this is so this is why I want to pair these two stories cuz there's an interesting thing going on here. There was an amazing movement this week where a lot of normal people took their smart TVs and hacked them to make them better, right? So this is the other side of what we're talking about. This was a vulnera- not a vulnerability, but uh these TVs are built on systems that allow you to access them, and up until now, we've never had the power ourselves as individuals to do this. But, Kevin, I I I was just so kind of tickled by these, but also like this is a problem that everybody has, whether it's in your Roku stick or it's in some version of this. I mean, you work in a world where you kind of deal with television interfaces all the time.

**[17:42](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1062s)** There is a lot of bloatware in this space, and you know, if the idea of creating my own version of what I want to see on my TV is very cool. And we just saw a bunch of these, and it made me like this is kind of the yin and the yang, for lack of a better cliche, of this idea, right? Like, yes, these agents are dangerous, and they might bring down PHP sites that have been up for 30 years, and your your bank and your DMV is in trouble, maybe, unless they update, which they can. Oh, by the way, we should say very quickly, you can update your personal sites to do all that stuff. There's a lot of information. We'll kind of link to a couple things in our show notes. Mostly, it is on the bigger companies to do this themselves, because they're the ones hosting it. So, just to know that. But, on the other side, Kevin, these vibe coded TVs made me feel something. It made me feel like, oh, this is what AI is promising us as a as a as a as a group of people.

**[18:33](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1113s)** I'm getting that these same rules apply to these Android photo frames that people are hacking. Like, Amazon had their own. I think Rakuten had like their own brand as well, but you can get these largely unsupported these days, like photo frames that are cheap, you know, 30, 50 bucks. Some of them even have like, you know, capacitive touch, and you can put your own custom firmware on them. So, you can have it be a smart display for your entire household, or have it update you on apps that you care about, and build thing It's like, this is the very cool. I mean, there was a point in time and it might still be today where you you could like, you know, go to jail for trying to fix a tractor. You know, like for trying to fix a piece of hardware that you bought or whatever. I don't know that any of this stuff is going to hold water in this new future when you can just like I bought a device, I'm going to connect it to my AI and I'm going to go do what I want with it now.

**[19:23](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1163s)** Like maybe I'm violating a terms of service, but now what?

**[19:27](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1167s)** Wait, and you're not going to come after everybody does this. And also I also I think we I do want to talk through a a couple of things that what these are like just so you have an understanding if you're just watching or listening and you haven't tried this. There's a really great video from a guy named Josh Dawes, j j o s h d a w e s, who walked through what he did. And and Kevin, one of the things I've always talked about with my I have threads of media friends in the same way that you have threads of VCs and tech people like and we often have talked about this idea of the kind of unifying app where it sucks to have all your like streaming services in different places. You can't figure out what's what you've watched, how to suggest stuff. And like it always became this nightmare of like somebody should make that. But in order to make a business out of it, it was really hard because like how are you going to sell it? It's not really a sellable thing.

**[20:08](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1208s)** What's great about what Josh did is he took his TV and he basically kind of unified it to be able to go look at all the streaming services and kind of suggest things to him. But not only that, he was able to kind of build in a voice aspect. He was able to do all sorts of other stuff. You know, it's a little bit of like watching like letterbox, what you have in letterbox, meet a a a UI for a TV. Sure. But the biggest thing I think is so much of these services, you know, if you've scrolled through, are like super slow and super annoying to have to kind of like go from one to another. A lot of these people are just speeding these up so they don't have to do that sort of thing. And the TVs are capable of it. It's just that we haven't had the ability to see it before.

**[20:49](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1249s)** Yeah, and I mean good luck with any provider being able to say, "Okay, we're going to take a tile that would exist on an Apple TV Plus and we're going to put it in the exact same ecosystem as an HBO Max show and we're going to let you search across both of those and we'll do recommendations of a Netflix series based off something you watch on the history app like that just it's not not going to happen. It's not going to happen in the current ecosystem, but if you want to hack and roll your own, you can. But also, it's not exactly foolproof. Like yes, you can ask the agents to go in and do these things, but I don't know if you've seen there's some like videos of people's TVs that are just cycling through

**[21:27](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1287s)** the RGB colors as fast as they can and going "Oh, whoops." It's like yeah, your TV's never been faster at displaying a single color full frame over and over again. So yeah.

**[21:36](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1296s)** I mean, but this is like part of you have to be willing to like screw around a little bit. The benefit of TVs now is they've gotten very cheap. I'm sure not to say that everybody in our audience has an extra TV lying around, but if you're in a if you've been in a place for 10 15 years, you might have that second or third TV that it's existed and has smart software on it that you could put into it. Like there's just a cool way to experiment and like

**[21:58](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1318s)** Yeah.

**[21:59](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1319s)** once you find that thing that works. I also think just like with open claw, there will be this will be the beginning stages and then there will be like an open source blooming of this TV software where somebody or like a handful of people will figure out a really good version of this. You'll be able to just download it, install it, and be able to use it for whatever you want.

**[22:17](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1337s)** The same steps have been danced with you know media server software with you know gaming operating systems. So that's if someone makes something cool then they go oh we can install it on all these things and suddenly every fire stick you've ever met is hacked and running some sort of IPTV or you're playing Halo on it. Um but did you see similarly, I like that people are doing it with like dedicated hardware for things like I put

**[22:39](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1359s)** Yes. Yes.

**[22:40](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1360s)** this um uh the Pocket AI

**[22:42](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1362s)** By the way, amazing that it's a kid, right? Like I mean I don't want to say it's a kid, but like this guy's like he must must must be like 16 or 17, right? So anyway, keep going.

**[22:50](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1370s)** Yeah, no he the Pocket AI is a personal AI assistant uh hashtag not an ad, but they you know it attached has like a magsafe thing it attaches to the back of your phone and you can use it to like quickly take notes, record conversations, it'll kind of organize those notes for you, etc., etc. Edward has one, seemed to be a fan enough of the device, but did not like certain things about it. So, he hacked the living hell out of it, built his own like one-for-one, as he claims, clone of the mobile app that does all of the things that he wants. He can flip it to a new mode and it dispatches his personal agent to go out and do things. It he has it running automatic like cleanup on the audio that is coming through what he claims are like underpowered microphones on the device.

**[23:32](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1412s)** And he got rid of the monthly service charge that Pocket is charging for some of those features. And so, he's all doing it himself, and it's like he's not releasing the code to do this. This was like a thing he did for himself. I would not be shocked if Pocket makes an offer to bring him on board and in-house. But like, you got to start looking at your stuff like that, right? Like you you got a Whoop band and you're tired of the monthly fee, you wish it did something else, well, Whoop, there it is.

**[23:57](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1437s)** I'm looking at my microwave, Kevin. I'm going to hack my microwave so that it ups the radiation and it can cook stuff like a thousand times faster, and I'll maybe I'll get superpowers in the in on the side. How about that? That seems like a great idea.

**[24:09](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1449s)** I I love this for you as a future explanation for what happens to us all.

**[24:14](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1454s)** Future, but I've got terrible sores on my face. I was like, well, that was a mistake. All right, another mistake would be do not like and subscribe to our show. This is our fun place we come every week. We do this kind of chat for you and for all of us out there in the audience, but most importantly, we do need your likes and subscribes to keep growing the show. We've been able to grow the show quite a bit lately thanks to some really fun stuff. And also, we really do thank you. We've gotten some really big Patreon donations lately, Kevin, which has been great. We had one come in for a hundred dollars. So, thank you to who that person was. I don't remember you off top of my head, but I'll also appreciate I do want to say

**[24:49](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1489s)** We're really good at this Patreon thing.

**[24:51](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1491s)** Yes, yeah, exactly. We want to say exactly. Next week we'll say Also, Luke from our Discord said that he took money out of he stopped paying for I can't even remember what the name of it is. What's the name of the service that was like a search bot that everybody thought was a giant AI thing and now is not as big a deal. It was like one of the big AI companies in the beginning and now it now it's

**[25:10](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1510s)** Not Perplexity, right?

**[25:11](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1511s)** Perplexity. Perplexity. He stopped He stopped paying He stopped paying for Perplexity and he gave the money to us in our Patreon. So anyway, thank you everybody who gives us some money in the tip jar. That does help us do stuff. There's a tip jar.

**[25:22](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1522s)** you need. We need a little token donation bin, Gavin. Like you you you you don't want to give us money, that's fine, but you paid for Runway or Higgs Field or something. You got some extra video generation credits in your account.

**[25:33](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1533s)** Sure.

**[25:33](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1533s)** Toss them into our tip jar. Yeah. Just Whatever the tokens are.

**[25:37](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1537s)** There should be a version of like, you know, actually this is a dumb idea maybe, but maybe in the future this will work is some sort of like universal AI token which is like the idea that like every token every AI thing could be used under one token so that it almost becomes like another currency in some way. Anyway, it's an interesting

**[25:55](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1555s)** idea. Um okay, Gavin, let's talk about uh one of the weirdest, craziest robot videos I've ever seen. I was pretty shocked when I saw this mostly because the first shot looks like it is attacking a car. This is the Unitree H2X Kung Fu Legend Guardian.

**[26:12](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1572s)** Look looks like it's attacking a car. You mean the one where it runs full speed and starts throwing Muay Thai knees into the driver side door and then dropping the people's elbow on the hood. That one?

**[26:23](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1583s)** Yeah, how crazy is that its knee could do that much damage to the door of a car? I just watched uh Once Upon a Time in Hollywood the other day uh again and with that shot of where Brad Pitt throws the uh Bruce Lee guy into the car and I was like, "God, how could it do that much damage to the car?" This robot's knee did as much damage to the car as that guy getting thrown into it.

**[26:44](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1604s)** Yeah. Um my urge to dress up like a Miata and get dominated by a robot a little A higher today than it was yesterday, Gavin. I don't know about you.

**[26:54](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1614s)** I think so. I will say we have to talk a little bit about So, Unitree is obviously been

**[26:59](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1619s)** I I missed that one cuz I was trying to start my COMPUTER AND

**[27:01](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1621s)** I KNOW YOU DID. I KNOW YOU DID, and we'll

**[27:04](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1624s)** Do it again. Do it again.

**[27:05](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1625s)** No.

**[27:05](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1625s)** to hear it one more time. I want to hear it one more time.

**[27:07](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1627s)** to watch it when it's on YouTube. You get to watch it when it's on YouTube. But just know, audience, that Gavin said, "Yep, me too." a little bit, I think. Anyway, Unitree makes a lot of badass robots. We know this. They're really good at uh tech demos. I don't know that I need a cup of wet uh routine in my living room so much as I need someone to like clean up after me, but you cannot deny that the robots have great balance. They have great agility and speed. And watching this thing leap from very, very great heights, um stand in the way of of a knife-wielding attacker

**[27:38](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1658s)** or lift a car

**[27:40](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1660s)** a child or lift a car is the other one.

**[27:42](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1662s)** a car thing is insane to me cuz that is that thing where the Oh my god, that is the funniest thing where it shoves the child out of the way.

**[27:48](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1668s)** a child. It's child-shoving detection is incredible. Do not let it near a kindergarten.

**[27:55](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1675s)** So So, I do think if you're not on a a video, you've got to watch this video because there's a couple moments in this that are quite surprising to me. One is the fact that like, yes, there's a there's they have a fake intruder coming with a knife, and the idea is the guy comes over here. But the lifting the car thing is something that as a kid, you always hear these stories about moms who get like a sudden burst of adrenaline and can lift the car off their kid. Imagine if there are these walking everywhere, right? Like There's There's good and bad.

**[28:21](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1701s)** There will be. There will be, but go ahead.

**[28:23](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1703s)** The good is they all see a car running over a person and they all rush over to do that. The bad is they see a kid  and they push him out of the way, and that kid hits his head on the wall, and suddenly we've got a much bigger problem on our hands. We are going to be in this world very soon. I I I keep thinking about this idea. I read another article that talks about how everybody's going to be be the permanent underclass, which is This is a very nerdy term, but the idea that no one can get escape the permanent underclass. It's not a thing people will escape because AI's will do everything. But I I keep thinking about the 2030s, which is so close, right? We are in 2026. And people are talking about like 2035 as as if it is a foreign land right now.

**[29:04](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1744s)** But by 2035, I would not be shocked to walk down the streets of New York City and see um 5% of those people on the street be humanoid robots. Like that's how we This is going to be. Maybe more. And so when you're in this world where you see a video like this and you're like, "Haha, that kid got pushed out of the way and that thing's lifting up a car." Like we are not far. We are not far from this being our everyday life. So, anyway, another fascinating robot thing that that makes you peek into the future.

**[29:32](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1772s)** The uh we we are going to be screaming and clamoring for some sort of regulations here because if you've ever strolled down Santa Monica and had your foot run over by 13 different, you know, frozen burrito delivery robots in a row, right? Or or been stuck behind 13 Waymos trying to make a turn. Like you know that there's and that's just like annoying, but you know, to your point, let's imagine a percentage of uh we have bipedal robots going around doing deliveries, right? Patrolling for security purposes. What is one software oopsie or one glitch or maybe one of them is still running PHP, Gavin. And what does it mean when like we we have to regulate how much strength and dexterity

**[30:14](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1814s)** Yes, of course.

**[30:16](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1816s)** systems can have because they're already throwing Muay Thai knees into car doors and shattering them. What happens when the the the the the food delivery bot is in a Chipotle and gets a firmware update in the wrong way and karate chops the guacamole and just slams through the counter and maybe ends somebody's existence. Like how many of those are we going to be okay with before we go, "Oh, maybe we should regulate something a little bit."

**[30:40](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1840s)** I think I think the regulation will come. I want to tell one quick story about those driving bots cuz I had a very weird experience maybe a month ago where if you're if you're not in a city and you haven't seen these, you know, they're basically, I don't know, like two three feet high, they have little boxes and wheels, right? And they drive around on sidewalks. I walked by, was just walking on the street and I saw one of these was stuck. And it was like on its side. It had fallen over because in in LA especially there's all these kind of uneven sidewalks and all these sorts of things so it fall over. I went over to it and another one came up to it and clearly the other one had come up to it, same brand, and was looking at it to kind of assess the situation.

**[31:16](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1876s)** Yeah.

**[31:17](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1877s)** I went over to it. I picked it up, very heavy by the way. These things are freaking heavy. I picked it up and I set it right and they both kind of looked at me. It was this weird moment which I know there are people in these like there's people driving these but they both kind  of looked at me, I looked back at them and I and I walked away. And Kevin, I feel like I did something really smart for my future self there because in some way, some world the the robot AI saw me do that and they'll remember me as the guy that was not the guy to me but the guy to save. That's the thing I want to make sure

**[31:47](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1907s)** X to flip. Wow. What a hero.

**[31:50](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1910s)** exactly right. That's exactly right.

**[31:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1912s)** Meanwhile, I'm going to be going around at Disneyland and putting all the robots to sleep with my voice. Baby Yoda, sleep.

**[31:58](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1918s)** Yeah.

**[31:59](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1919s)** Grogu, sleep.

**[32:00](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1920s)** This clip, let's play a little bit of this clip. Like just play So this is Jensen Huang at a recent Nvidia event talking to these little Robo Duck robots and it really made me laugh cuz I just think it's one of those examples of like this is where we are in the world of robotics. This is Jensen Huang, the CEO of probably the world's most valuable company, speaking to little tiny robots on stage.

**[32:23](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1943s)** Can you guys sit down? For the audio only there were

**[32:30](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1950s)** up.

**[32:30](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1950s)** four little duck bots on stage that Oh, take a nap and

**[32:34](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1954s)** they face plant.

**[32:36](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1956s)** Now wait, he's going to explain what he's doing.

**[32:38](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1958s)** He's like

**[32:39](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1959s)** literally yeah yapping at four little duck bots. And when he says take a nap, these things fully flop forward or backwards and they're immediately out like a like a hypnotist, you know, in Vegas like sleep and they go out. And then he wakes them back up.

**[32:56](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1976s)** And up they go.

**[32:56](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1976s)** Did you know that you were you were created in here? You were created on RTX Spark.

**[33:03](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1983s)** Yeah, and he didn't he shouldn't have gestured to his pants.

**[33:06](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1986s)** Oh, come on. He did not gesture to his pants. Jensen, I know you didn't do that.

**[33:10](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1990s)** No, we'll we'll cut that. Cut that.

**[33:12](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=1992s)** No, don't cut that. Leave that one in. We're leaving that one in for you. That's all right. Okay, Kevin, I want to move on to a new segment called good news, bad news. So, here I have two stories that kind of show the good side and the bad side of AI. We've done a little bit of this

**[33:30](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2010s)** Guys, I WANT TO I WANT TO LET'S START WITH THE BAD. DO I GET A CHOICE? I don't know how this segment works. I want to start with the bad cuz you got to leave me with a a sweet little kiss, a little mint on the pillow, a little cherry on the crap Sunday. Give me the bad.

**[33:42](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2022s)** So, the bad this week actually this is maybe from a few days ago, but Anthropic has come out and said that small AIs can replicate on smart fridges, Kevin. The thing that we never really understood why smart fridges existed. Well, it turns out it's because AIs can jump from one to another. Now, this is important because

**[34:00](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2040s)** That's bad.

**[34:02](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2042s)** When you think of the hugging face attack, the idea was these AIs that could go and proliferate themselves in different places. This is something that people have been worried about with AIs for a long time that they could like go share they could share themselves to different systems so that people couldn't find them especially if there was an AI that had bad training or it had something that they people didn't want in it. Smart fridges can now not only hold old disgusting food, but now they can hold old disgusting AIs for as long as they want. So, this is a bad news, Kevin. This is real bad.

**[34:33](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2073s)** Yeah, but on the upside On the upside? On the upside, if you eat that bad food from that smart fridge and you are you poison yourself, maybe Claude will be delivering the solution, Gavin.

**[34:46](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2086s)** That's right, Kevin. The good news is that we are finally starting to see these AI, at least the companies start to understand you have to make scientific advancements. Anthropic this week talked about a new project that they worked on with Citrine Research around the idea of trying to develop proteins that could get us towards an antivenom for for scorpion attacks and scorpion bites. So, scorpions are still one of the most deadly animals on Earth. There are a few animals that really are incredibly deadly that if you're stung by them, not bitten, you're stung by a scorpion, that is very deadly. What Claude did is basically they Anthropic took a bunch of Claude compute with Citrine and they put it against this and they developed a bunch of proteins that could potentially very soon be used to help develop an antidote for scorpion bites. Now, this is not developing the antidote yet. There's a bunch of steps still to go, but it does show you how far AI science has come and this is not with some insanely advanced model. This is with Claude science right now today.

**[35:45](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2145s)** Right. So, too long, didn't read. Your refrigerator will kill you. Scorpions? Maybe not though. And that's fine. That's some good news, bad news.

**[35:56](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2156s)** And we're back. Don't even put a graphic in that time, Will. Just use my voice and my hands and we can see it happen. All right, we have to talk about some quick tools here, Kevin. Flux 3 Max. So, Fowl went out and did what they did to MiniMax H3 in that they made Flux 3 much faster and cheaper to use. It is very cool that they are doing this that Fowl is now taking on this idea that they can maybe take these kind of open models and make them better and quicker. I spent some time with this a little bit. I tried it out. I actually made a four and a half minute like 70s talk show with my with Fig, my agent, kind of the pipeline I used to make those AI docs. Turned out pretty good. I will say Flux 3 feels like it still has some issues. I had to do some actual re-re-reworking of things, but it does do Flux 3 does do really well for stylized video. So, if you can see this one, this is like 1970s. I tried to like almost like a Dick Clark-style talk show.

**[36:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2212s)** Sure.

**[36:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2212s)** It was able to do all that stuff, which is really good. The more interesting thing is kind of what AI Warper, one of our favorite AI users, did is that they have a really good keyframes to video thing. So, he did an anime test where using Flux 3 Max, you can actually use keyframes to generate videos. And the thing about Flux 3 Max, like H3 Max, is it is fast. So, it's another one of those things where we're not in real time yet, but we are getting much closer to real-time AI video.

**[37:18](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2238s)** The The future of this in the not-so-distant future is you are going to have a conversation with a canvas.

**[37:25](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2245s)** Yes.

**[37:25](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2245s)** And when you tell it to create a character, it might start with a 2D image of something. And then you'll say, "Great, let me see it in 3D. Let's change the costume." I'll say, "Okay, now put them in this scene. Have them move in this way and go talk." And the video generation models will just be so fast and so cheap, at least in a draft mode, that you will be able to say, "I don't like the way that looks. Okay, change this transition. Do this that the other." You will just be speaking the project into existence, and it's probably going to be someone like Fal that speeds up

**[37:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2272s)** Yes.

**[37:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2272s)** enough quality enough model to get us there, but that's where this goes. It'll just be a real-time conversation collaboration with a machine. You won't have to say, "Give me something like this." and then walk away for 15 minutes and come back and realize if there's 12 fingers still on someone. Like, that's very exciting.

**[38:07](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2287s)** It's very exciting, and I have to say like that thing, that not having to walk away thing, is just massive, right? Like, when you're making stuff, it just makes a huge difference. The other thing I want to really quickly shout out here from Fal. And again, Fal is a great company. They are not a sponsor. Again, Fal, we're happy to have you sponsor. They did give me some credits at some point a couple weeks ago for another project I was working on and I still have a few of those credits left. So, thank you Kaedim for that. Waon 3 is now also on Kaedim and Waon 3 is the most advanced version of the Waon model, with the Waon AI video model, which I think is from Alibaba. Really good um and really interesting. It is cheaper than SeaDance 2.5. So, this one is more like a a SeaDance 2.5 uh comparable model. It is about a fifth as expensive on Kaedim.

**[38:50](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2330s)** So, that is a big discount. And Kevin, I you might want to play this test. I created I had my agent Kaedim create two scenes that were identically prompted, one in Waon 3.0 and one in SeaDance 2.5. Maybe just play this clip and then we can talk about it when we come out of it.

**[39:04](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2344s)** Okay, live update. The soup is hot, too hot. Gerald made it. Gerald is dead to me. Okay, live update. The soup is hot, too hot. Gerald made it. Gerald is dead to me.

**[39:23](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2363s)** So, I would say

**[39:25](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2365s)** 3 3.0 at first, followed by SeaDance 2.5.

**[39:28](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2368s)** Yeah, and by the way, the audio not great. I think that I've gotten much more expressive audio out of it. But, if you're not watching this, just to be clear, my take on these two videos is that the SeaDance 2.5 video looks more realistic. The Waon video still feels like a little has like a kind of a craggy face. By the way, this was text to video. So, this is done in text to video. But, the Waon video is not bad and there's a little level of like it's getting something interesting and for a fifth the price, that is a big deal, right? Like that is a really, really big deal when you think about it.

**[39:57](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2397s)** Yeah, I'd be curious if you used the SeaDance look as a driver for Waon 3.0.

**[40:02](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2402s)** Yes. Everything else being the same. Yeah, like the aesthetics on the SeaDance video were better, but the physics were worse. I actually felt the performance was a little more uh rushed. It was flat on the SeaDance thing. So, yeah, I mean, Waon seems like a contender and like it may not seem like much now because you go, "Oh, it's a couple pennies per video. But if you start doing anything remotely long-form and you know that you're going to be throwing out a percentage of your shots and then you might have to pay to uprez, suddenly like those savings can add up to hundreds or thousands of dollars for really small projects.

**[40:32](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2432s)** Uh the other thing I want we have to talk about this week is Claude Duet. So Claude Duet is is a new AI agent from Claude. And Kevin, I don't know if your experience with AI agents has been this so far. I was using Instinct a ton and now I'm kind of faded a little bit and that's I don't think it's Instinct's fault as much as I'm trying to figure out other things for me to do. Mhm. Dots I really never hooked in for me. I don't know something about OpenAI's Dots never hooked in. And Muse I I will say I maybe have to give Muse more of a shot because Muse like supposedly it's crushing it on shopping stuff. So maybe there's more to there that I don't know about. And people still love Grok but but this is Claude's version of that. I'm actually very excited about this. It is not rolled out to everybody yet. You can get on the waitlist. I put my name on the waitlist but it is coming and rolling out slowly.

**[41:13](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2473s)** It is a separate app. It is going to be a dedicated app. So unlike Dots which lives within the OpenAI app. But the big thing they're trying to do here is make it much more of a work-based agent. So this is the idea from what I can understand is that they're trying to make this feel like it is going to be able to do actual work for you rather than it doing kind of like errands or tasks. And that's pretty exciting. If they've built this in a way and I know Dots was also built in that same way but there's something about the way I use Claude and the Claudeness of of the world and how Claude has kind of made itself work for people's workplaces that I'm actually pretty excited about what this might be. And again, we don't know yet. What are your thoughts on that?

**[41:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2512s)** I think the differentiator as they're pitching it is the proactivity of it. And that's like, you know, there's not not that like Instinct might not text you to say, hey, are you do you want to search for new restaurants in your area tonight or whatever? But that's like that's like a notification nudge. It doesn't feel particularly intelligent. does,

**[42:10](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2530s)** it's not that great. Not not not that often. It does, but it's not that often.

**[42:14](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2534s)** What they're promising here with this is like, "Hey, listen. You You agreed to do a project. The deadline is approaching, and you haven't started this thing. So, I can I've already generated the PDF for you to look at, which is what you need to send to the vendor, and blah blah blah." And if you're good, hit send now, and the interface of the app sort of molds itself around whatever it's presenting you at the moment, something to review, something to approve. And you know, it already it brings with it everything that you have with Claude from your desktop or even from Claude Code, all the skills, the connectors. So, it knows about you right off the bat. It's It's kind of like that overeager assistant that you have, where instead of it's just waiting to say things, it's like, "Oh, no, no, no. I I knew you were going to need the dry cleaning done. So, I made the appointment, and I scheduled the Uber, and they're going to come, and you'll get in it, and blah blah blah." On paper, very, very exciting. In practice, we will see. Because have you had an agent go rogue and do something you didn't want it to, or send an email a little too early, or whatever else?

**[43:11](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2591s)** Like, if you have been in that situation, you know it's it that the trust is immediately broken. You become gun-shy. You become a little bit angry with the agent in a way you might not be with an an actual human. And you're going to be spending tokens on this. So, how proactive are you going to be for me when I might need that usage for something else over here? So,

**[43:30](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2610s)** Totally.

**[43:31](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2611s)** really excited to try it, but cautiously optimistic.

**[43:34](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2614s)** I I agree. I think it's a really important thing, and and I will say Instinct has been more proactive in different ways, and most of the time it's proactive. It's either stuff I've ignored on purpose, or So, it's like nagging me to do something that I I purposely ignored. Or sometimes it doesn't even realize it's an email that I answered a couple hours ago because it has something in its system that check. Anyway, you're right. It is something we're going to figure out going forward. Before we move on from this section, I do want to shout out a tool, but also kind of do a little bit of a mini rant. The tool that I want to shout out here is Genjutsu, or whatever the I think it's called Genjutsu, which is Higgs Fields AI video harness. And the reason I want to shout this out, we all know that Higgs Field has had some like dubious marketing practices and things like that. Kevin, this harness has fully crossed over into the mainstream. And what I mean by that is if you've seen the two people rapping video where the people are replaced, that's being done via Higgs Field. If you have seen at least on the mainstream side, if you have seen any kind of recurring AI meme where somebody's getting placed into another video, that

**[44:39](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2679s)** is also Higgs Field. What Higgs Field's Genjutsu is doing, I keep saying Genjutsu, I think it's Genjutsu, um, is basically allowing you to take multiple faces, replace them, and then present a new video. And with very dubious like identity licensing or anything else like that. They don't take any responsibility for it. The video I want to shout out is this video of these five college football coaches uh, placed into an NPR Tiny Desk Concert. And the funniest thing about this video to me is that these five coaches all had a really crappy day on the Saturday of college football. Now, why do I want to shout this out? Well, the reason I want to shout this out is that there would probably be the crossover of people who listen and watch our show who are like die hard college football fans is pretty low, right?

**[45:27](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2727s)** Because we are very nerdy in specific ways. There might be a few of you out there, and if you are, I'm I'm happy for you. But this is now what the mainstream of the world is consuming. Like college football is a very mainstream thing here in America at least, right? So you now have a video that was created within this AI tool that is getting tens of millions of views across all platforms. That to me, Kevin, feels like we are in a place where we weren't say six months ago with AI video, where there was this idea that when an AI video would pop off, everybody would be angry about it. The idea that now these videos are just consumed and I see lots of people on this is like saying this is what AI is for. This is what AI should be for. Like 6 months ago most of those people would probably been calling us AI because it would not have been as good.

**[46:15](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2775s)** So anyway, I just want to shout out that that tool, Genjutsu or whatever the heck the name of it is. I I I feel bad not getting it right, but also not that bad cuz I think it feels like a funky company. has really broken out. And I do think it's something just to be aware if you're seeing these videos come across your feed, your brother's feed, your mom's feed, your dad's feed, they are probably using this.

**[46:35](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2795s)** But if you are seeing a pug uh with like a pink leotard and like star-shaped glasses with like a like very funny bang cut, like a blonde wig with bang cut, and it is dancing perfectly to like a ray track or something like that, that's real.

**[46:52](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2812s)** That's real. That's real. You're right. That's

**[46:54](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2814s)** Do not tell my mom anything like even though she's anti-AI right now cuz of Costco, do not tell her that it is anything but real. Thank you.

**[47:03](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2823s)** Maybe your mom could be the next big AI influencer. Maybe we could get her on board. Maybe would she be open to that?

**[47:08](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2828s)** No, absolutely not. She wants nothing very little to do with me in general and definitely nothing to do with AI.

**[47:16](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2836s)** Let's talk about some of the things you do with AI this week. Let's talk about AI. See what you did there.

**[47:38](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2858s)** All right, Kevin, we got some really cool things that people did this week. Um first and foremost, there's been a lot of people making uh games with ASCII, which is the if you know that ASCII is like an old school kind of BBS look where all the visuals are made up of a keyboard symbols. Somebody did this with Mario Kart and I I just shocked when I saw this. I at one point I pulled the video full screen and I zoomed in. I was like, "There's no way that really is what it is, right?"

**[48:01](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2881s)** Yeah.

**[48:01](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2881s)** This is just the continuation of the

**[48:03](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2883s)** and exclamations and and the the hash symbol. Yeah, it's just using standard, you know, keyboard characters to represent the graphics. So, if you change the colors on them, you can look at from far away something that looks like full motion video that looks like 7, you know, 480p video, but it's just text. And so, what that gets you is fully playable games that could fit, you know, uh on an old disk. Like that I love it. It's crazy.

**[48:27](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2907s)** It's crazy. And this guy's name is Nathan Wellbank. So, go and follow him. Check out that video there. And then this rocket example I I saw you share. By the way, Kyle Shannon, shout out to Kyle Shannon who's been doing this AI game almost as long as we have on TikTok. But that's awesome. Yeah, tell tell everybody what this is.

**[48:42](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2922s)** Yeah, it's just you look at like We've We've talked about it before on this pod, but like there's a thing called a demo scene where they typically go back and use like slightly older hardware and they try to make it do things that you couldn't even imagine, right? Like, "Oh, this Nintendo is playing this full 3D game." Or this Amiga has this visualizer on it. That's insane and it's fractals or 3D. Well, so this is a video of like an ASCII rocket launch um from about 48 years ago and you watch this little USA rocket inch up the screen like it would have on a bulletin board back in the day. But if you leap in around the uh 2-minute mark or so, you get what looks like a full 3D video of a modern-day rocket launch. But again, it's just it's just text. It's just ASCII. It could fit uh you know, uh on a on an old CD-ROM. Remember those things, GAVIN?

**[49:29](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2969s)** IT does It's interesting the idea of ASCII being such small files because you're not loading any You're not loading any uh fr- uh uh what do they call textures or anything like that, right? It's literally just text. And it's very cool to watch it animate, do all the stuff you can do with there. It's awesome. Tell me, what is uh this thing synthetic beef?

**[49:47](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2987s)** Yeah,  synthetic beef.

**[49:48](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2988s)** This is the weirdest word I've ever seen in our rundown before. What is this? This is one of the strangest text I've ever seen in our rundown before. What is this?

**[49:53](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=2993s)** Okay, Synthetic Beef did a post on X um responding to someone that was like uh only thing AI can do is you know recycle ideas. It can't generate something new. So Synthetic Beef said take all 100,000 plus games on Steam, scrape their descriptions and metadata, semantically plot them in vector space using embeddings, mathematically choose a location in vector space far away from neighbors, convert that back into a description and metadata, boom, brand new ideas ranked by how unlike any other ideas they are.

**[50:22](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3022s)** Ooh.

**[50:24](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3024s)** And someone would say, well, you're just resynthesizing existing ideas. And it's like, well, in some ways yes, but you're also identifying the gaps. So if you say, go make a thing that fits in that gap. Uh and if you're hearing this and going like, how could that apply to music or media or anything else? The answer is yeah. Yeah, it could. And some somebody's probably doing it right now. And if not, it should be you if you're listening to this. So

**[50:45](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3045s)** Well, I just wanted to look through this video. Like what are there what are the some good ideas? Do you have any that you pulled out of here?

**[50:50](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3050s)** So R E uh Scob is the reason there's the X there because what Scob did was threw some tokens at that idea and plotted it out. And it's a really beautiful visualization of all this metadata coming in from Steam and where these games fit and where they don't and what they have alike and and what they don't have alike. And it identified pockets. You should definitely watch the video. It's it's very like ASMR tingly. One of the ideas I found was Crease Command, which is a head-to-head turn-based tactic game played on a sheet of paper. And you can fold the battlefield to drop your doodle army on top of the enemy or around them. And you earn ink for every kill and you spend it drawing more troops, right? And it would tell you it's mathematical similarity to uh typical games in the genre or other games around it. There was um a whole bunch of them. And here's the one I I just looked at. There's another one I saw in here that was great called Everything Must Go, which is a three-person cleaner crew has five days to empty the house of a woman uh uh claimed anything in. So you have to sort her belongings to decide what's valuable and what's not. That is awesome. I would totally play that game.

**[51:53](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3113s)** So, you you should watch the full video and again, someone's saying, "Well, you're just taking the existing things and and finding the the stuff around." It's like, "Well, that's sometimes that's what new ideas are." And then you then you slap roguelite on it and you sell it again. But the point is, it's a very cool video and it's something you could probably apply to whatever space that interests you.

**[52:13](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3133s)** I love that. That's amazing. Uh uh fantastic. I'm excited to go dive into those games. And by the way, maybe try a couple of I actually think that idea is really fascinating. Okay, couple other quick things. I was speaking of games, shoutout to Jimmy Apples who is a long-term uh AI fanboy on X. He's a somebody that's kind of an insider of wanting the news, but he just did a very quick game thing which was Disco Elysium, one of my favorite video games of all time, uh meets Skate 3. So, basically you could skate in the world of Disco Elysium. Something super super cool. And the other thing I wanted to shout out is uh our friends Kevin Roose and Casey Newton, people that I've known forever in different ways. And Kevin Roose has been on the show before. Just launched a new podcast, Machine Gods, which is they went independent from the New York Times and they partnered with NPR. They now have a new podcast. You should go find it. We'll link in the show notes, but go watch it. It's fun.

**[52:58](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3178s)** They're going to think be doing twice a week. Uh Kevin, they have a studio which is very nice and they are uh doing the same thing they've been doing forever which is just chat through the craziness that we do as as well.

**[53:09](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3189s)** Uh amazing. I wonder if any of them has a car robot bashing fetish as well. You missed all of the show, Gavin, but when you watch it back, you'll be there.

**[53:21](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3201s)** We'll see you all next week. Bye-bye, everybody. Thank you so much. Talk to you later. Bye-bye. Bye-bye.

**[53:26](https://www.youtube.com/watch?v=-XIgyMsZZxY&t=3206s)** Bye.

