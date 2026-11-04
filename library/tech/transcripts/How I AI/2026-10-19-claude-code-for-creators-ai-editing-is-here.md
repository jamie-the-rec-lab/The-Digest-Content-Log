<!--SUMMARY-->
## Actionable summary
**Guest:** Brooke Lacey, TikTok creator with 25 years in tech and builder of the free AI-learning app Zosha, worth hearing for a concrete non-engineer video workflow  ·  **Show:** How I AI, 19 Oct 2026
**Tags:** ai, ai coding, productivity, growth, careers

**When to use this:** You want short vertical videos (employer brand clips, outreach videos, job explainers) from one raw talking-head recording without paying an editor or spending hours in a timeline tool.

**Big idea:** Claude Code can run a short-form edit as a chain of ordinary local tools and store the cut list as a text file, so the edit becomes something you regenerate in seconds rather than a project you build by hand.

**Frameworks & plays:**
- Film one continuous phone take, move it to your computer and ask Claude Code to edit it. Brooke says it used "FFmpeg, Whisper, Python" and uploaded nothing.
- The chain Claude reported for a five minute take, which ran in about 15 seconds, was silence detection to find speech, Whisper word timings to place each cut just after a word ends, face tracking so the crop follows the speaker, then eight cuts each tagged wide, mid or close.
- Keep the cut list as a plain text file with a start, end, shot size and label on each row. Brooke's point is "That file is the whole edit", so the same command can produce 30 second, 60 second and landscape versions from the same footage.
- Captions run one word at a time, white with a black outline, each held until the next word arrives. In the demo that was 57 words, with audio and video 0 milliseconds apart at 30 frames per second.
- Teach the tool your style by pointing at specifics. Brooke told Claude to listen for the laugh in her opening line because "that is how a hook works for me".
- Mine comments for scripts. She downloaded her videos to Google Drive, had Claude read the comments on a logged-in TikTok session, and asked for new content ideas from the pairing. She says TikTok cannot be scraped by an AI, so the logged-in session is her workaround.
- Know the craft first. Brooke says she could "orchestrate Claude the way that I would actually do it" because she had been editing short form for years.

**Data & benchmarks:**
- The figures in the demo (five minutes in, 15 seconds to run, eight cuts, 441 frames) are Claude's own on-screen readout read aloud, not an independent measurement.
- Brooke now posts about once a week and says reposts of older content keep her audience engaged.

**Tools & prompts:**
- Claude Code in the terminal, FFmpeg, Whisper, Python, Google Drive for video storage, and Claude in Chrome for reading comments.

**Steal this (do tomorrow):**
- Record one five minute take on a role or team and ask Claude Code to produce a cut list text file before it renders anything, so you can review and tweak it.
- Write down your own editing rules (cut right after the word ends, rotate wide, mid and close, caption style) and give them as instructions.
- Export the comments from your best performing recruiter post and ask Claude for three follow-up scripts.
<!--/SUMMARY-->

# Claude Code for creators: AI editing is here

- **Podcast:** How I AI
- **Channel:** How I AI
- **Date:** 2026-10-19
- **Duration:** 36:33
- **URL:** https://www.youtube.com/watch?v=UF08V1XIUmw
- **Fetched:** 2026-11-04
- **Source:** YouTube captions via TranscriptAPI (en)

## Episode description

Brooke Lacey has been making videos since before Facebook had video, and she built a TikTok audience of more than 290,000 by learning to cut short-form videos herself. With over 25 years in tech, she now builds her own apps, including Zosha, a free mobile app for learning AI. In this episode, Brooke walks me through the Claude Code, FFmpeg, and Whisper workflow that edits her TikToks in about 15 seconds, how she mines her comments for new scripts, and how she runs a weekly short-form operation with no editor.

*What you’ll learn:*
1. How Claude Code edits a raw phone video on her computer in about 15 seconds
2. How she taught Claude her jump-cut cadence
3. Why her TikTok comments became her content brief
4. How she keeps growing her audience while posting just once a week—and what’s next
5. What over 25 years in tech taught her about this AI moment

*Brought to you by:*
Firecrawl—Give your AI agents web data and beyond: https://firecrawl.dev/howiai
Auros—The human network behind AI: https://aurosglobal.com/howiai

*In this episode, we cover:*
(00:00) Intro and guest welcome
(02:30) Brooke’s background in video
(06:56) Her first session cutting videos with Claude Code
(08:51) Live demo: Claude edits a video in real time
(11:05) Walking through the edit chain
(15:58) How she taught Claude her cadence, her hooks, and what funny sounds like
(25:36) Quick recap
(26:20) Posting frequency, live streaming plans, and TikTok ads
(28:00) Lightning round: Gen X, wisened experience, and Y

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube. A new paragraph marks a change of speaker where the captions show one (speaker names are not available).

**[0:00](https://www.youtube.com/watch?v=UF08V1XIUmw&t=0s)** No timeline, no project file, no editor. You figured out a way to use Claude code to encode editing that really fits the form, which is short-form content. The file's in the computer, it doesn't upload anywhere. The only thing that's happening is the instructions are being pulled and it's doing all of the things. It's just running the computer. And  not only that, but it's listening and goes, "Oh, I just heard you say cut that out." And then it also was like, "You repeated this a couple of times and I took the one that was the best cadence." And I was like, "What?"

**[0:34](https://www.youtube.com/watch?v=UF08V1XIUmw&t=34s)** And what just happened is Claude descended upon our videos and cut them. It just pulled up the raw video. There was a really well-clipped vertical short-form video, perfect to TikTok cadence. And you did it with no hands.

**[0:49](https://www.youtube.com/watch?v=UF08V1XIUmw&t=49s)** So, literally, I do everything in the terminal. I like it better. It just has

**[0:54](https://www.youtube.com/watch?v=UF08V1XIUmw&t=54s)** way more access to everything. So, let's say, "Okay, my dude, I'm ready to show the audience the magic." And look, no hands. This is probably the 15th or 16th time in the last 6 months that I literally like fell to the floor.

**[1:10](https://www.youtube.com/watch?v=UF08V1XIUmw&t=70s)** What just happened?

**[1:16](https://www.youtube.com/watch?v=UF08V1XIUmw&t=76s)** Welcome back to How I AI. I'm Claire Val, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today we have Brooke Lacey and she is going to walk us through her Claude code for video editing flow. She has over 200,000 followers on TikTok and she's figured out how to get Claude to edit her videos to be funny and have the right jump cuts, create scripts for new content, and generally understand her cadence, her vibe, and her style. Let's get to it. This episode is brought to you by Firecrawl, which gives your AI agents data  from the web and beyond. Your agents can search and scrape the web while accessing Alexander's rapidly expanding  library of over 100 million indexed sources and more than 200 data providers all through one connection.

**[2:07](https://www.youtube.com/watch?v=UF08V1XIUmw&t=127s)** Connect Firecrawl to ChatGPT or Claude to find people and their work emails, pick your fantasy football lineup, or analyze trends for your next marketing campaign. Firecrawl is building the library for superintelligence, bringing more of the world's knowledge into the tools you already use. Go to firecrawl.dev/howia to get started. Brooke, thanks for joining How I AI.

**[2:34](https://www.youtube.com/watch?v=UF08V1XIUmw&t=154s)** I'm so excited. I think that you know, but I would like your audience to know that I'm like the biggest fangirl. I really love what you do, and I'm just so excited to be here.

**[2:46](https://www.youtube.com/watch?v=UF08V1XIUmw&t=166s)** Well, I love what what you do, and so we're going to talk about why I got you on this podcast, which is you have a Claude code video editing social empire building stack that I I need to steal cuz before we got on, we were talking about how a little while ago I was like on my way to being a big deal on TikTok, and then I a girl gets tired. Like a girl gets tired of all the short form. And I loved when I saw you posting about your system, about how Claude code helps you produce not just like slot content, but actually really great high-quality short form, which is own special little art. And so dive us into what were you trying to solve, what were you trying to do, and how how did you figure out that Claude was going to help you on the way?

**[3:37](https://www.youtube.com/watch?v=UF08V1XIUmw&t=217s)** Let me just start this. Like video short form video and like like little live stream stuff it has not I've been doing that for a long time. Like before Facebook even had, you know, video stuff, I was on the news. Like video content is not new for me. The short form was kind of a big deal when I got on Tik Tok like 2020 and the trick there is those jump cuts. They're very difficult. I do a lot of funny stuff. I was known for ogling shirtless lumberjacks and like doing some funny stuff and then also, you know, teaching tech. But it's not funny unless you are jumped at the very exact moment. And let me tell you that is tedious. I tried teaching video editors like how to do it and how I wanted it and it just never it never worked the way I needed it to.

**[4:29](https://www.youtube.com/watch?v=UF08V1XIUmw&t=269s)** Like they got to be you know, the facial expressions. This is actually how I talk in real life and you got to like, you know, cut it correctly. So I've just always done it myself and it it would take hours out of my day just to make one video. Even though my videos on Tik Tok if you know, we were talking about earlier if you go look at the it's just my face. My entire Tik Tok feed is my face. You're welcome for people just so you know. It's a rabbit hole but also you're welcome. Um and even though there's there's some videos that I'm like literally just sitting in my car no makeup on and have you know, hundreds of thousands of views you still have to get it correct so that it even looks natural. So all that being said, I had kind of stopped posting for the last year and and was like, I'm obsessed with Twitter. I I had a viral video this women in web3 panel video which also goes with women in tech. Like it's the most absurd thing to be like be on a panel to talk about being a woman in tech on a panel. And you're like, what? So that particular video was about a minute 5 seconds and my friends were like, it's not funny. So, I cut it to about 55 seconds and had those jump cuts really precise,

**[5:53](https://www.youtube.com/watch?v=UF08V1XIUmw&t=353s)** and that's what was funny. So, and it was a two-person. So, I do some videos are two-person. That takes forever. Um that being said, so now I'm doing all of this other um I'm not doing like videos for other brands. I have my own products. I need to do my own videos because what do you know? UGC content doesn't do as well as this face. So, I have to do all the videos for the app that I built um that took off that I didn't even like realize was going to take off. So, I needed I needed long-form to then be able to upload and cut up. So, I went outside. I thought for some reason being outside would be better light. It was not. Uh I probably did 25 to 30 minutes of just, you know, I didn't it was just all the whole thing. Didn't cut it up. Didn't stop the video. It was just all of it.

**[6:47](https://www.youtube.com/watch?v=UF08V1XIUmw&t=407s)** And then I'd be like, no, cut that out. Meaning I was saying it to me. And then I came in and was like, all right, let's just around and find out. So, I was like, okay, I'm a new Mac user. I used to just be a PC user. I'm like, ah, I got to make get this video up into Google and then, you know, download it and thank God for AirDrop. So, I'm just like, AirDrop to the computer, which I think is silly being a tech person not having known like we should you know, I should be a Mac person, but I just never was. So, that was cool for me. And then it just was on the computer and I go on to Cloud Code and was like, let's see what you got, my dude, and said and it just loaded. Okay, so, TLDR is that it just used the boring tools that are already on our computers.

**[7:37](https://www.youtube.com/watch?v=UF08V1XIUmw&t=457s)** FFmpeg, Whisper, Python, like it didn't upload the video anywhere. It's just the files are in the computer. If I could like get the GIF of Zoolander, I say it all the time. Like, the file's in the computer, it doesn't upload anywhere. The only thing that's happening is the instructions are being pulled and it's doing all of the things. It's just running the computer. The file's in the computer. And all of a sudden, it's like pop and then it opens the video and I'm like, "What?" And then, not only that, but it's listening and goes, "Oh, I just heard you say cut that out." And then it also was like, "You repeated this a couple of times and I took the one that was the best cadence." And I was like, "What?" "What did you do?" And I mean, sat back, this is probably the 15th or 16th time in the last 6 months that I literally like fell to the floor. Like, I'm so dramatic anyway, but I was like, "What just happened?" Like,  what?

**[8:43](https://www.youtube.com/watch?v=UF08V1XIUmw&t=523s)** And what just happened is Claude descended upon our videos and cut them. So, let's let's show it because I have been doing this a little bit, but I think you have a much better system than me. So, I'm just going to sit here and and learn it. So, show us

**[8:58](https://www.youtube.com/watch?v=UF08V1XIUmw&t=538s)** again, it's only going to be fun because of the way I'm talking about it cuz it's really, really freaking boring. Like, it's just boring. But of course, you and I think it's amazing and hopefully your audience too, but yeah.

**[9:08](https://www.youtube.com/watch?v=UF08V1XIUmw&t=548s)** Yes. Let's show it. This is the how AI vibe. We will make your markdown and Python files feel like the most exciting thing you have seen in your life in years. So, so much better, y'all. Okay.

**[9:21](https://www.youtube.com/watch?v=UF08V1XIUmw&t=561s)** I love you. Okay. Here Here we go. So, how does it work? Okay. So, literally I do everything in the terminal. I have for a long time. I I like it better. It just has way more access to everything in my opinion. So, let's say, "Okay, my dude, I'm ready to show the audience the magic." Go again.

**[9:51](https://www.youtube.com/watch?v=UF08V1XIUmw&t=591s)** And did you prepopulate this with a skill or with a prompt? Oh.

**[9:55](https://www.youtube.com/watch?v=UF08V1XIUmw&t=595s)** And look, no hands. Okay, so this one is the this one is like the non-edited. I'm so  dumb. Sorry. Okay, you can like

**[10:09](https://www.youtube.com/watch?v=UF08V1XIUmw&t=609s)** it's like to be a creator.

**[10:11](https://www.youtube.com/watch?v=UF08V1XIUmw&t=611s)** I'm so sorry.

**[10:11](https://www.youtube.com/watch?v=UF08V1XIUmw&t=611s)** Everyone at work talks about AI as if you're already supposed to know how to use it. And you just nod along, smile and nod along.

**[10:18](https://www.youtube.com/watch?v=UF08V1XIUmw&t=618s)** Everyone at work talks about AI as if you're already supposed to know

**[10:21](https://www.youtube.com/watch?v=UF08V1XIUmw&t=621s)** It's an app I built called Jayla. The first three are free. It's jayla.app. I'll see you in there.

**[10:27](https://www.youtube.com/watch?v=UF08V1XIUmw&t=627s)** Wait. Quick pause. Okay, so for people that are listening, not watching, she said, "Okay, my dude, let's go." I'm presuming that called some sort of skill on on the back and maybe you can walk us through exactly how the prompt works. It just pulled up the raw video

**[10:41](https://www.youtube.com/watch?v=UF08V1XIUmw&t=641s)** Yeah.

**[10:42](https://www.youtube.com/watch?v=UF08V1XIUmw&t=642s)** and then approximately 4 seconds later there was a really well-clipped vertical short-form video with captions, with jump cuts, with a little zoom when you made a funny face, um perfect to TikTok cadence, um and it you did it with no hands. Okay, so let's look at what it did. You want to walk us through?

**[11:06](https://www.youtube.com/watch?v=UF08V1XIUmw&t=666s)** Yeah, he I said, "Walk us through what you're doing, you're live online, my guy." And it said one phone take, which is what I was telling you before, was actually the one that um that I showed you, let's just see, this one right here, if you see my mouse, that was the, you know, the rough cut, and I was in my a co-work space, um which, you know, I love cuz you can get all kinds of different backgrounds. I liked this because it had this, you know, side uh wall that he could put Well, I thought me. I thought, "Oh, I can put, you know, like graphics or whatever." And filmed it with my phone, AirDropped it to the the MacBook, got myself a new fancy MacBook. Uh and then this is what happened. And so, he's telling us, "One phone take, 5 minutes of me talking, went in on the left. Here's what the chain did in the 15 seconds it ran. Find the speech." So, silence detection marks where she's talking. Word timing from Whisper sharpens each edge because neither alone can place a cut cleanly.

**[12:09](https://www.youtube.com/watch?v=UF08V1XIUmw&t=729s)** So, it the word timing from the tool Whisper sharpens each edge. So, it ha- like I was telling you earlier, um off camera uh for your audience the it has to hit right after that word ends, right? You We don't think about that when we're talking. Like right there, the G that it talking, like the sound ends before you think it does. Um and then it tracked my face, so every frame, it's just like taking a picture every frame, just like film. So, the crop follows follows her, follows me, and each cut gets a shot size, wide, mid, and close cuz I was asking it to do all the video sizes.

**[12:56](https://www.youtube.com/watch?v=UF08V1XIUmw&t=776s)** Yeah. Then place the cuts, so eight of them picked from its own TSV file. Each row is a start and end, a shot size, which I could show you that file, but it's literally just cut, you know, it's just a folder or it's it's just a Yeah. Um it's got every row has a start and end, a shot size, a label. That file is the whole edit. So, the edit in video editing, I didn't actually know this, but I was telling my friend, there's a thing called the edit is text.

**[13:26](https://www.youtube.com/watch?v=UF08V1XIUmw&t=806s)** And that just means that like you can type it out and it'll edit. It Claude kept telling me that and I was like, "Okay, so the file is the whole edit." So, drop in the app screens. I literally just said, "Go find the By the way, my app is not called Jayla anymore, it's called Zosha. I had to rename it. So, you'll see the old name on there, but I went and said, "Find my branding info and graphics, put together a graphic to and this the app screen. Take a screenshot, open up the simulator, take a screenshot of the app and use that to put into this video. So, 40 of the 441 frames That's just blowing my mind. Carry a screen of the app at the moments the cut list says. So, as I'm saying it, it pops up.

**[14:23](https://www.youtube.com/watch?v=UF08V1XIUmw&t=863s)** Cards on the wall beside her. So, her right edge is measured per cut off the rendered footage. So, the cards sit in that real empty wall sized to it. And then it does captions one word at a time. 57 words, white with a black outline cuz I'm just like, "Hey, do white with a black outline." Each held until the next arrives. I didn't tell it to do that. He decided that those captions need People don't realize that's how captions are generated is that it the word has to stay there until the next sentence. So, he knew not to go further than that. And then check sync. So, 441 frames at 30 FPS, audio and video 0 milliseconds apart. The finished 15 second vertical ad is playing on the right. No timeline, no project file, no editor, and because the whole edit is a text file, the same command makes the 30 and 60 and the landscape versions from the same tape.

**[15:26](https://www.youtube.com/watch?v=UF08V1XIUmw&t=926s)** Have you ever asked your favorite AI partner whether what you're building is good or safe or trustworthy? Did you believe what it told you? Auros connects your team to a network of over 7.6 million verified human experts. The specialists who bring the taste, judgment, and nuance your evals can't capture, so you can be sure that what you're building is actually good and good for people. Auros, the human network behind AI. Get started today at auros.global.com/howiai.

**[15:59](https://www.youtube.com/watch?v=UF08V1XIUmw&t=959s)** Okay, just I'm like, "Dear Claude, make a funny video." And it doesn't work because of exactly what you're talking about.

**[16:09](https://www.youtube.com/watch?v=UF08V1XIUmw&t=969s)** Correct.

**[16:09](https://www.youtube.com/watch?v=UF08V1XIUmw&t=969s)** I I also just have to empathize as a TikTok girly. Do you know how often I'm sitting in CapCut being like, "Cut it right like right here like

**[16:19](https://www.youtube.com/watch?v=UF08V1XIUmw&t=979s)** Correct.

**[16:20](https://www.youtube.com/watch?v=UF08V1XIUmw&t=980s)** cuz I know what funny sounds like. But just a couple things that I want people to know is you've actually really structured what a good short-form edit looks like.

**[16:29](https://www.youtube.com/watch?v=UF08V1XIUmw&t=989s)** Yes.

**[16:29](https://www.youtube.com/watch?v=UF08V1XIUmw&t=989s)** Jump cuts between times, clip to words. I love this idea of three frames. I was like, "Just zoom in when it's funny." But I like this idea of like frame wide and close cut because if you all don't know, you got to do like this when you're on TikTok.

**[16:46](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1006s)** Yeah.

**[16:47](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1007s)** And then uh the auto captions and what people don't understand is that can all run with existing tools and files on your computer really well. But I I have to imagine this took some zhuzhing to get right because I think I'm a smart cookie and I have not nailed it. So show us how you use your existing TikTok corpus to actually like learn how to do this.

**[17:16](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1036s)** And I do I to tell your audience watching listening I know I said it before but video content is not new to me. So, I'm not a video editor. It was just by way of I had to do it because I was starting to content and I realized how important social media content is even for old people. So, I had to learn. This is not just something that I just like oh, I picked up you know, you do have to have some capacity. Just like you know, being a a developer just make this just makes you a better developer. So, you do have to learn like the basics of video editing. Just so everyone knows that like I've been doing short form for a really long time. So, I was able to orchestrate Claude the way that I would actually do it if that makes sense. So, the thing with Tik Tok first of all on a technical level is that their algorithm their back end software their back end whatever is so um precise that you can't scrape it. You can't have an AI even with their API.

**[18:18](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1098s)** Um just scraping it for data or like doing multiple downloads doesn't like it. But, if you're already logged in which I'll show you this since I'm logged in then I can go down here and say Okay, let's show them the Tik Tok corpus. I am logged in and use the video in the Google Drive like you did for so that you can read the comments and use those comments to um put together new content ideas based on what they said. So, which one did it pull? I think it pulled this one. Yeah. So, this was the first video I did um after I created the app the J app which is a free app um to learn AI. At first I was calling it the Duolingo of learning AI, but that's silly. Um but that's what I thought in my head. And so, again, I it's a free app um and I was so excited that like I got it in the App Store and all that. But, what was great and I'm going to I'm going to say it again.

**[19:35](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1175s)** for 25 years and I've never been this scared for people. An AI founder just told 40 million people on Twitter

**[19:42](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1182s)** Okay. So, what I'm saying in the video is that Andre Karpathy quote that it was like, you know, he doesn't um code anymore. He just like doesn't even know how to keep up. Um that was actually one of the times I thought to myself like yeah, our nervous systems like don't know how to keep up with all this stuff. So, okay, I said to Claude go and look at this particular video which by the way I had to download on my phone and upload to the Google uh Drive because he can't download it Well, no one can download it from Chrome. Um but, that way he could read it and see it.

**[20:20](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1220s)** Okay, yeah. So, just to walk people through if they're not watching. I think what what is happening here is you went on your phone and you downloaded all your Tik Tok videos and you put them in Google Drive and you said, "Here are all my Tik Tok videos in a Google Drive. That way Claude code can access Google Drive and actually pull down any one video." Then separately, you said "Tik Tok's open. Yeah. Go look at Tik Tok and read the comments for this particular video. Yes. Pair it with the download of the video that's up in Google Drive. Yep. And then pull it together and say based on how this did, the content in this video and the comments Yes. give me new stuff.

**[21:08](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1268s)** Correct. Cuz

**[21:09](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1269s)** Is that right?

**[21:10](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1270s)** one has all these comments, right?

**[21:12](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1272s)** Yep.

**[21:13](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1273s)** And yep, and it says like, I wonder if hospitals are going to start using AI for the billing and coding. Okay, cool. Um well, on the phone, you can reply with a video. And then, you know, see, it like sounds like CEOs can be replaced by AI. AI will replace someone with no skill. I mean, it just goes on and on and on. So, the prompt that's happening with with Claude code is go and read those. I have done this before, so it's probably looking for the output that we had from before, from a few months ago when I actually did this. But, he's got the post IDs, opening the pin post with the most comments, and scraping its comment thread. And it does call Claude in Chrome. Sometimes I have to explain that no, you need to do this headless, but it doesn't really matter. It's getting the information somewhere. And then, it will the the coolest thing for me was was that as people can see, it's my facial expressions, you know, I talk with my hands. There's pauses.

**[22:19](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1339s)** Everybody knows that that's how videos work. But, to train an AI to understand that, in the first part of the video, I say, I've been in tech for 25 years and I've never been more scared for people. And that little laugh right there, where I'm like, scared for people. I had to tell Claude, did you hear the cadence in my voice? Because that is how a hook works for me.

**[22:45](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1365s)** Yeah.

**[22:45](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1365s)** Is that I'm trying to get people's attention that way. Figure that out. And it it did. He did.

**[22:52](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1372s)** So, just to kind of like repeat for people, in addition to downloading these videos, and so they can be referenced and and um combined with comments to come out videos. You actually taught Claude to understand You know, people ask me all the time like, "How do I get Claude to write emails like me?" This is like that on max mode. It's like, "How do you get Claude to encode my charming self live into something that it can help me replicate. How do I do hooks? How do I do my cadence? What are my jokes like? Where do I do cuts? Um how do I tell

**[23:30](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1410s)** Right.

**[23:30](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1410s)** story? How do I, you know, create a peak in a story? All that kind of stuff. And then it's using all that knowledge not only to make your cuts better, but also give you scripts.

**[23:41](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1421s)** Correct, which I just brought up on the screen. And this was I you know, not to get into the whole whole story, but there's a a style of video that I do WTF even is. And I was doing it for um some complex like blockchain uh terminology because that's already complex, just like the words that uh that are in that industry. And so it made sense where I was doing the two persons, so I'd film one and then film the other side so that I'm talking to myself, but the two people are talking to each other. Um and what the one person would say like, "WTF even is uh blockchain or Ethereum or whatever?" And then the other person's like gives this long complex, "Well, it's the, you know, ledger that blah blah blah." blah very complex. And then the other person is me um with the facial expressions like, "What? Like, what are you talking about?" Um That is not something you can script.

**[24:43](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1483s)** And but but the words back and forth need to be a certain way for it to be absurdity and then the like um complexity. Like it has to go back and forth. So I still haven't really trained Claude in like that particular piece, but we're getting there. And obviously, it can't I mean, obviously, my facial expressions are my facial expressions, but I truly believe that like we're going to be reality dealers at some point because people are going to know that there's no way that you can create an avatar of Brooke Lacey with the facial expressions. Maybe you can in the future, but

**[25:19](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1519s)** I mean, please please like and subscribe to my create your digital avatar with Gemini episode where I created very hilarious uh tradwife AI versions of myself and do videos. Uh so, never say never, but okay. All right, zooming way back. Let's just see. Okay, um video creation is not new to you. You figured out a way to use Claude code to encode editing that really fits the form, which is short-form comment content. You uh had to do a little human loop in terms of downloading your full TikTok corpus to a cloud location, which was Google Drive. But once you had that, you were able to do two things. You were able to kind of like learn your style, but then you also used that like style analysis to do a couple things. One, mine comments for new content. Two, create scripts for that new content. And then three, refine your editing your Claude editor to make that short-form content better. And now, how often are you posting?

**[26:26](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1586s)** Okay, so don't be mad, but I don't really have to post that often to still have a really good engaged audience. Um I did the work. I put in the work for quite a few years, and a lot of my content still gets kind of um reposted. So, I don't have to post very often because um I think once you have done the work over, you know, a number of years and you do get to the hundreds of thousands of followers. Your stuff just kind of keeps getting regurgitated and I would say like once a week I'm posting. What I think the next step for me, because I'm really good live, is that I'm going to do more live streaming and I just don't think there's a lot of people in this space doing that for this particular thing. Like what we're talking about and then going through and like showing how our apps work. Kind of devrel stuff but live. And so yeah, I don't have to post that often. And right now I'm building videos for ads right now. Like I'm going to try to do some figure out if Tik Tok Tik Tok ads work for my products. We'll see. Just kind of throwing stuff at the wall to see what sticks. But that's the video work I'm doing right now.

**[27:42](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1662s)** And I think I'm telling Claude, hey, this is an ad and it's like, oh, okay, let's figure this out in terms of it's not the same as the other stuff you were doing. It's more of a, you know, however ads work. I don't even know.

**[27:56](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1676s)** You don't even know.

**[27:56](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1676s)** know how I don't  cuz I just do this.

**[27:59](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1679s)** Claude's business. Um, Brooke, I love this as a as a creator um who does long form that like needs to get back in short form but it just doesn't have the hours to do editing. I'm going to go steal all of this and you will see chief product officer on Tik Tok. Rise the ranks yet again. We will get there. Let's do a couple lightning round questions and get you out of here. The first question is despite our charming faces, you and I are we're we're elders on the Tik Tok. And I

**[28:30](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1710s)** I'm happily in my 50s. All right, just 50.  Just turned 50.

**[28:34](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1714s)** on my way. So, look at us two gals.

**[28:37](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1717s)** That's right.

**[28:37](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1717s)** I would like to make a plea for more experienced technologists to share their knowledge on these new platforms, pretty please. We need that combination of like wizened experience and yolo energy, especially in AI. But you said something to me really interesting ahead of the show about being like a generation or two or three back from this moment. And how you kind of like what what your experience has been kind of going headfirst into AI and what that feels like.

**[29:10](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1750s)** Yeah. Oh, I love this and I wish we had hours and hours and maybe you'll have me back or maybe I'll just talk about live stream and you know, people can come and listen to me ramble, but I'm a very proud Gen Xer. It's a small but mighty generation. Whenever my 21-year-old son calls me a boomer, like I've disowned him. I'm not a boomer and um I think Gen X had this really incredible uh time period where we lived in our formative years, high school and college. So, yes, my lovely millennial friends, you also grew up sort of like we did with like, you know, no cell phones and the plastic phone on the wall that like, you know, had a cord and I feel like we were just so lucky that we got to see it go so quickly. And I'll tell you a really quick story, when I got into college, um it was 1994 that I started college. I um had already fallen in love with computers with Windows 3.1. Um and got into this computer science 101 class and I remember the the professor, it was one of those big auditorium classes cuz it was 101. It was intro to computer science. And um this teacher, this professor was like jumping around the stage and was like, "Just wait. It's all going to happen so fast. It's going to happen so fast and

**[30:30](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1830s)** it's just going to go crazy." And we're all like, "Man, chill. Like, what?" And he was right. I mean, he was going nuts and and it was the next like two or three years that everything just exploded and we got to see it. We got to like really experience it and watch from the very very beginning as high school and college age where we were like actually starting our careers and it was just such an incredible time to be alive. So the year 2000 I worked on the Y2K bug and a lot of people don't really know what that was um but it was kind of funny uh changing you know two numbers to four and everybody thought you know planes were going to fall from the sky and

**[31:14](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1874s)** And our toasters were going to attack us.

**[31:16](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1876s)** Right.  Right. We Everyone's worried about AI. Well, back then we were worried about toasters. So you can imagine

**[31:24](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1884s)** how different it is for me now with AI. But um yeah, I of course don't have quick answers. You can just take from that what you will but I love being of this generation that is I appreciate what technology does and yes there needs to be more people my age and older telling their stories about you know back in the day you remember watching that movie where the women were actually computers. I can't remember the name of the movie but they're called computers because they were there sitting there computing and there's just so many stories of like you know the the tapes that had to be used the big reels that you know hard drives that you couldn't drop because that was where it was. I don't know. There's so many cool stories. So like old people listen up. Go on to

**[32:12](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1932s)** Well, and and if you want a great episode go back to one of our early how AI episodes with John Blockman 91-year-old vibe coder

**[32:21](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1941s)** That's right.

**[32:22](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1942s)** explain some things. And so you know I had the same experience as you which is I have seen technology shift after technology shift. So this one happened I was like I see it.

**[32:32](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1952s)** I'm in.

**[32:33](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1953s)** I'm in. I'm in. It is going to change my life like these previous ones have. And so,

**[32:39](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1959s)** um jump on in. Water's warm.

**[32:41](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1961s)** Yeah. Yeah.

**[32:42](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1962s)** Okay, last question. You're you're so lovely. I I And and I like that Claude is a boy for you. That's very nice.

**[32:52](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1972s)** Oh, yes.

**[32:53](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1973s)** When he is a disappointment, when he's not doing what you want, how do you prompt him?

**[32:59](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1979s)** Okay, so also  a very long story, but I will keep it concise. The Grok Bot person wrote an article the other day about their P stack. I can't remember the name. It was like banana something or coconut. I don't remember her name, but um and I

**[33:19](https://www.youtube.com/watch?v=UF08V1XIUmw&t=1999s)** Sorry. This is me all the time. Um her  was it was Petunia or something. Um and I ran it against my OS. So, what I built a while ago with my dear Claude is this lane operating system that is very complex. I do have a an open source of it, but it is fairly complex. And it has memory lanes. It has like right restrictions and different things cuz I have multiple um products within the company. And then the OS lane has its own memory. So, the way that I prompt when it screws up is like go back to the way that we started, understand those instructions, and then do it again. And there's status MD files. There's There's project pieces that every time I'm in that session, it should be following those, but then also the global.

**[34:20](https://www.youtube.com/watch?v=UF08V1XIUmw&t=2060s)** But it's it's this entire like operating system just for my business and my life. And there's there's always something to go reference. So, it's kind of nice where I'm like, "No, you did that That doesn't sound right. Go back and figure out where you messed up or where you didn't read. Why didn't you read that? Oh, you Okay, now you figured out why you didn't read it correctly on the session hook. Now, go back and tell the main operating system spine that you messed up so that it can make the change globally."

**[34:51](https://www.youtube.com/watch?v=UF08V1XIUmw&t=2091s)** I love it. I love it. Brooke, this has been I don't know if the audience can tell we're having a good time. We're having a good time today. This has been a good one. Um where can we find you and how can we be helpful?

**[35:03](https://www.youtube.com/watch?v=UF08V1XIUmw&t=2103s)** I am at Brooke J. Lacey on every platform. I've been around a long time. Um Tik Tok is definitely my biggest audience. There's a lot of funny stuff that hopefully makes you laugh. Um it all started in in 2020 when everyone was home for COVID and I just started making people laugh. I am a lot more on on Twitter and I have a really cool app called Zosha that I built and it's just the it's just learning AI and you're kind of doing it on your phone and it's free. So, that would be awesome um if you did that and really just reach out. Like I I have DMs are open. You know, I I love talking to people and I've got lots of stories. So, you can find me everywhere Brooke J. Lacey and um this has been such a pleasure. And I do travel quite a bit. So, I'll be in San Francisco, I'll be in New York. I'm kind of all over the place. So, I'm always up for a coffee.

**[35:59](https://www.youtube.com/watch?v=UF08V1XIUmw&t=2159s)** Amazing. Well, thank you for joining How I AI.

**[36:02](https://www.youtube.com/watch?v=UF08V1XIUmw&t=2162s)** Thank you for having me.

**[36:05](https://www.youtube.com/watch?v=UF08V1XIUmw&t=2165s)** Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube or even better leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app.

**[36:18](https://www.youtube.com/watch?v=UF08V1XIUmw&t=2178s)** Please consider leaving us a rating and review which will help others find the show. You can see all our episodes and learn more about the show at how iaipod.com. See you next time.

