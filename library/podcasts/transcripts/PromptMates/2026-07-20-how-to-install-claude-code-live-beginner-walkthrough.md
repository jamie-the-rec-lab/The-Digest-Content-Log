<!--SUMMARY-->
## Actionable summary
**Guest:** Matthew Parker, former Head of Talent at Fleek and now managing director at Move, who walks a complete beginner through installing Claude Code on the terminal live, error included.  ·  **Show:** PromptMates, 20 Jul 2026
**Tags:** claude code, ai upskilling, building ai tools, recruiter enablement, ai agents

**When to use this:** You are a non-technical recruiter who wants Claude Code running on your own machine but has never opened a terminal.

**Big idea:** Installing Claude Code needs no coding knowledge, because when the install throws an error you paste the whole thing back into Claude and let it debug for you.

**Frameworks & plays:**
- Open Terminal, run "git --version" to confirm Git is installed, then paste the install command Matthew shares; if you lack Git, ask Claude "how do I install Git".
- Test the install with "claude --version"; when it failed, they followed the terminal's own "run echo export" set-up note and pasted the fix lines one at a time rather than all at once.
- Matthew's debugging rule is to copy your entire terminal history into Claude chat and say "I'm trying to install Claude on my terminal, what's gone wrong here", then run each suggested fix line individually.
- Start Claude Code by typing "claude", pick a theme, then choose option one to connect a paid account, which opens a browser login before returning to the terminal.
- Run a first agent by prompting "make a new folder called Shiv-Workshop and let's work in that folder", then "make a 150 character outreach message using these two files".

**Contrarian take:**
- Matthew stresses Claude Code will not work on a free plan, so you need a paid plan or your company paying for tokens.

**Steal this (do tomorrow):**
- Install Claude Code, then introduce yourself to it by describing your job, company and what you do so its answers improve.
- Pick one narrow task, such as searching GitHub for a coding language, and do just that one thing well to learn the tool.
<!--/SUMMARY-->
# How to Install Claude Code (Live Beginner Walkthrough)

- **Podcast:** PromptMates
- **Channel:** PromptMates
- **Date:** 2026-07-20
- **Duration:** 12:03
- **URL:** https://www.youtube.com/watch?v=LJ-6-IB1320
- **Fetched:** 2026-07-23

## Episode description

Matthew Parker walks Shiv Brodie through setting up Claude Code on her terminal for the very first time, including exactly what to do when the install throws an error

📌 Timestamps
00:00 - Installing Git & Claude Code
02:29 - Troubleshooting a failed install with Claude
05:11 - Launching Claude Code for the first time
07:32 - Running your first Claude Code agent
10:38 - What to do after installing

Matthew Parker is the former Head of Talent at Fleek & now managing director at Move

This clip is from the PromptMates Live Show, where talent and people leaders share what they're actually building with AI

🔗 Join the PromptMates community: https://www.promptmates.ai/community
📧 Weekly newsletter: https://www.promptmates.ai/newsletter
🎙️ Catch the next live show: https://luma.com/promptmateslive

#TalentAcquisition #ClaudeCode #AI #Recruiting

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube.

**[0:00](https://www.youtube.com/watch?v=LJ-6-IB1320&t=0s)** Shall we install Claude code? >> Let's do it. >> Run two? Look. >> Yeah, let's do it. Right, Matt, tell us what you want on screen and and lead us through. >> All right. Um let's just let's just get Shiv to to share her screen. >> Oh. >> So, go into your search bar on the top top right. >> Yep. >> And just type in terminal. Okay, let's open. So, first things first, I'd like you to type in get space {dash} {dash} version. >> Like that? >> And just hit enter. Okay, so this is basically confirming that Shiv has Git installed on her desktop. Which is which is great. We need Git to be able to download files etc. to be able to install this. If you don't um have Git installed, first things first I would go straight to do is ask Claude to help you uh how do I install Git.

**[0:55](https://www.youtube.com/watch?v=LJ-6-IB1320&t=55s)** So, if you are following along at home, you don't have to have any code knowledge to do any of this. I just you just follow along. I promise you like if this is already too scary for you, I promise you to just follow along on your own terminal at home. Uh it is not scary as it looks. Okay, so now, Shiv, all I got to ask you to do I'm going to drop this in the chat uh this command in the chat and all I want you to do is copy and paste that in the chat. And then enter. Okay. So, this is now it's going to not like it's like look like it's doing anything, but this is installing Claude into your terminal. And we're just going to just going to hang out. And so, I think Joe, are you cross-posting into YouTube the the instructions?

**[1:36](https://www.youtube.com/watch?v=LJ-6-IB1320&t=96s)** >> Yeah, the two instructions are in the YouTube chat. We will also send out like the full deck which will break this out step by step. So, um feel free to follow along now or or do it afterwards. >> And I again I do really stress that like this might look intimidating, but I promise once you break through it, your life will become easier. I've just blindly followed the instructions when I set this up without really knowing anything that I was doing and then eventually it all it did start and I was like whoa I'm I'm a hacker. I'm writing code I'm in the matrix. Yeah. And so she's installed Claude. She's a hacker. She's installed Claude on her terminal and is now a bonafide coder. So now just to test that this has actually worked because that you know if you're a good software engineer you want to test what you do.

**[2:19](https://www.youtube.com/watch?v=LJ-6-IB1320&t=139s)** I put another prompt it's but it's Claude space dash dash version. >> Again, was that what we had before? >> So this is that now this is testing. Um well, that's not good. Let's see. Why is that not working? >> Well, how about right above the top where it says it's set up notes, right? It said it tells us what to do. So what if we listen to that, Matt, and tried the run echo export like it's asking to? >> Do you want to just copy and paste that shiv into your just copy and paste the echo >> The whole thing? So where do I paste that? >> Paste that into the like into the bottom where we were typing before. And just hit enter. >> That. And no argument. >> Okay, this is great. Well, let's So now let's troubleshoot this. So if I this was B now, I would copy and paste everything that I've done directly into Claude and say I'm trying to install Claude on my terminal. What what's happened? What's what's gone wrong here? So let's open up Claude chat.

**[3:38](https://www.youtube.com/watch?v=LJ-6-IB1320&t=218s)** >> Yeah. >> It won't work on a free version. You have to have a paid version. For for reference. >> What am I to be saying? I'm trying to install Claude on my desktop. >> On my terminal. >> on my terminal. >> I think the chat is uh is telling us that some people are saying that Claude is down, which would be quite hilarious. So now we're just So what it said here, let's fix this permission first. I don't understand what it said, but what I would do, I just copy this line. Copy this one at a time. Don't copy and paste entire things. So first run that first line. >> And put it back in the terminal. >> Yeah, put it back in terminal, paste, and then go back and copy the next line underneath it. Yeah, debugging is the first is the first skill. And then uh the one underneath that.

**[4:41](https://www.youtube.com/watch?v=LJ-6-IB1320&t=281s)** And then after you run that, you just remember to hit just hit enter, yeah. >> This works. I'll be amazed. >> It's working. It's there. >> It worked. That's really cool. >> using Claude code. I mean, honestly, like I can't tell you how much of my time is jumping from this interface these two interfaces to see if something's working before I then install. Okay, now just type in the word Claude. And then hit enter. You have just started Claude. So you can go auto dark mode, light mode, whatever. So this is just picking the like how it's going to look basically. So just pick whichever one you want. And then hit enter. >> Dark mode is fine. >> And then so this is where you might have to stop sharing. So you this is basically asking you to connect your your paid account to Claude. So you're probably going to choose option one. And so also saying that to use Claude code, but you need to have to have your company paying for your tokens or you'll be having to enter in your card details.

**[5:52](https://www.youtube.com/watch?v=LJ-6-IB1320&t=352s)** >> Just asked me to relaunch Claude, so that's why. >> Yeah, so um exit out of your terminal and then open a new terminal and just type in Claude. So, that's how you start up Claude from your terminal every time is you just type Claude. >> So, really quick, what happened was you hit one and then it more than likely opened this on your web browser and then you logged into your web browser and then you came back to terminal. So, if when you do it it opens a web browser, don't freak out, that's what's supposed to happen. >> Awesome. So, let's go back to terminal just see what's going on. Okay. Press enter to continue. Let's Let's follow the instructions. And then just hit enter again. This is all just setting up.

**[6:36](https://www.youtube.com/watch?v=LJ-6-IB1320&t=396s)** Yeah, I reckon just and then yes. So, this is basically saying this is kind and I do things in this folder, which is how it reads and writes different things. So, I tend to not give access to my photo library um because I don't see how that's relevant. All my music. >> Documents I tend to download, I tend to. >> But apps I don't tend to personally. Yes, I sometimes do for desktop. So again, this is all super normal. And then so now just to like test, why don't you just write in hello? >> Just here? >> Yeah, just say hello. Great. So, like you've now this is Claude working on your machine and this is like you can chat to it like you would do Claude normally or you can like write quite complex code with it and you can do everything in between. So, should we run it on an  agent?

**[7:32](https://www.youtube.com/watch?v=LJ-6-IB1320&t=452s)** >> Yeah. >> I'm going to paste the instructions. Hey Claude, make a new folder called Shiv-Workshop and then let's work in that folder. And just type that into there. You can't select in in terminal interface. It's really weird. You have to like you have to use your arrows. Okay, then hit enter. Now if you go on to your folder, there it is. So that's created new folder. Okay, now go back into your terminal. And just say move move the folders that I sent you earlier today. It's just going to execute that. So again, like this is actually changing things on your computer and it's it's back to my old behavior at this point. >> Cool. >> Moving about now. Click two. Great. And now let's run the agent. So you can just write make an outreach 150 character outreach message using these two files.

**[8:36](https://www.youtube.com/watch?v=LJ-6-IB1320&t=516s)** And see what it does. It says reading the files and then it's going to execute the files. Did I send you the blank one? Okay, I sent you the blank ones. That's not very helpful. Well, I don't know how to continue with that. We So here basically >> you can show what you did. >> Yeah, so then the outcome of if I sent her the right folder uh >> >> would essentially be this. After all the things that I was expecting would go wrong actually fits sending you the one the wrong folder was not actually what I was expecting. But essentially is this. So like it's automatically gone and it read Shiv's folders and interpreted the what I've asked it to do effectively because I've given it enough structure and then and then created an output. Um but obviously this is like again, just scratching the surface. When I when you get the pack that hopefully we send out from at Joe later, they'll get loads and loads of different ways that you can start doing this. Like you can make a CV reviewer, you can make a application like a a sourcing string. Like there's loads of different things that you can do that don't touch like your data as well. This was just like one kind of quite hopefully quite straightforward example

**[9:55](https://www.youtube.com/watch?v=LJ-6-IB1320&t=595s)** to show like how easy it is to make to make a an agent. And I think one of the the key things that if you want to start kind of thinking about this is basically like it's reading a file that you've saved onto your desktop and then executing what your ask is based on that file. So when you see people talking about skills, when you hear people talking about Claude.md files, when you hear people talking about soul files, all it is is these agents are just reading these files in the way that you all order that you tell them to. And then and then it's just executing against that. So you however complicated you make that flow is however complicated the agent will act. So hopefully that was like helpful.

**[10:30](https://www.youtube.com/watch?v=LJ-6-IB1320&t=630s)** Hopefully at least some other people here other than Shiv have now got Claude installed on their terminal. And if not, then Joe is going to send out a bunch of files as well. >> Yeah, very very cool. We definitely had a number of people in the chat who've like successfully installed it all already. So that is super cool to see and I'm sure more will do it. Let's say after this session I've installed Claude code on on my desktop, what do I do next? Like what are the kind of next use cases to kind of get started understanding what I can what I can do with code now that it's installed? >> I mean I'm a big fan of context, right? Like I'm a big fan of telling Claude about myself, about my job, about what I do, about my company, you know, this sort of stuff. So I would recommend with introducing yourself to your new buddy in Claude, tell them what you do, tell them where you work.

**[11:13](https://www.youtube.com/watch?v=LJ-6-IB1320&t=673s)** Um I mean you could literally be like, "Now that I got you installed, what can you do for me?" And I think you'd be surprised what you get back. >> Yeah, I mean I completely agree. The more information has about you the the better it will be. Like it just start with an idea, some some something very very simple that you would like to try. And then have it be as like basic basic as possible. Like I was talking to someone today and they were like, I want to be able to search GitHub for for people who have this skill or this type this like coding language. I'm like, okay. So, just work with code or work with Claude like understand how you would just do that one thing and do it really really well. And that through that process of trying to just do anything, you'll learn a lot. And that's exactly how I started. Follow along on YouTube, you can follow along on on loads of different places even even other places like this, but yeah, this is it just pick something and just try and see what happens and you probably will fail, but that's okay cuz the next time you won't.

