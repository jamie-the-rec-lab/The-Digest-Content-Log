# How Reddit’s designers build ultra-realistic prototypes with Figma + Cursor

- **Podcast:** How I AI
- **Channel:** How I AI
- **Date:** 2026-10-26
- **Duration:** 29:40
- **URL:** https://www.youtube.com/watch?v=zF-J3rMbzZw
- **Fetched:** 2026-11-04
- **Source:** YouTube captions via TranscriptAPI (en)

## Episode description

Blair Metcalf is the principal UX engineer at Reddit and the builder of Reddit Proto, the company’s in-house vibe-coding harness. With a design system MCP that maps Reddit’s product language to production code, Proto has reached 100% adoption across Reddit’s UX and product org, and more than 700 prototypes are live on it.

*What you’ll learn:*
1. Why Reddit built its own prototyping harness
2. How designers share prototypes with leadership safely
3. Why real Reddit data beats mock data
4. How one annotation becomes a code edit in Cursor
5. What a “feature capsule” is
6. Why Blair built a “Rosetta stone”
7. Blair’s surprising fix when AI goes sideways
8. Who turned out to be Reddit’s best prototypers

*This entire episode is brought to you by:*
Firecrawl—Give your AI agents web data and beyond: https://firecrawl.dev/howiai

*In this episode, we cover:*
(00:00) Introduction to Blair
(02:31) Reddit Proto demo
(09:15) Annotations to Cursor: the targeted edit workflow
(11:19) Internal deployment and adoption
(14:14) How leadership reviews and gives feedback
(15:52) Engineering handoff and the feature capsule
(17:50) How the custom MCP was built
(21:41) Quick recap
(24:55) Lightning round and final thoughts

*Blog and detailed workflow walkthroughs from this episode:*
Inside Reddit Proto: Real Data, Constrained Prototypes, and a Better Handoff: https://www.chatprd.ai/how-i-ai/blair-metcalf-reddit-proto  
↳ Create a Realistic Prototype with Live Data in Reddit Proto: https://www.cha

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube. A new paragraph marks a change of speaker where the captions show one (speaker names are not available).

**[0:00](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=0s)** Now, the distance between design and product is wide. If we made everyone a builder, they could vibe code new features and products easily. And so, we made a harness that uses our design system and all of our components, UX patterns,  and it keeps all the designers and product managers on rails. And so, this way that you can make a million ideas, they can be reviewed, and then you can pick one, and then that's where we spend our time, and that's what goes into prod.

**[0:25](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=25s)** I have not heard anybody say, "Okay, go ahead and let you off into your production data and render that."

**[0:31](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=31s)** why that we do this is because Reddit has personalized data. But if designers are mocking everything in Figma, and then they show that to leadership, leadership's going to look at that and be like, "This isn't relevant to me." And you don't have to take 9 months to get that into prod, see if that works. It saves so much time, and everybody can work on other  things. And so, if you make one of these real-world prototypes with real data, they'll put it through the paces of like some new feature. Search is like a is a great example to like how I AI. And it knew the podcast.  Like, it's pulling that real data, it sends it to an LLM, ranks it, and then  you can test out that design.

**[1:08](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=68s)** Are designers prototyping the most, or product managers prototyping the most? Like, who is prototyping the most?

**[1:17](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=77s)** Welcome back to How I AI. I'm Claire Vell, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today, I Blair Metcalf, principal UX engineer at Reddit, and he's going to show us Reddit Proto, their custom harness for product managers, designers, and anyone else to get their ideas into a production-like prototype they can share with anybody in the company. This is an awesome one for anybody interested in design systems, prototyping, and how to make high-quality things without exposing GitHub. Let's get to it. This episode is brought to you by Fire Crawl, which gives your AI agents data from the web and beyond. Your agents can search and scrape the web while accessing Alexandria's rapidly expanding library of over a hundred million index sources  and more than 200 data providers all through one connection.

**[2:08](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=128s)** Connect Firecrawl to ChatGPT or Claude to find people and their work emails, pick your fantasy football lineup, or analyze trends for your next marketing campaign. Firecrawl is building the library for super intelligence, bringing more of the world's knowledge into the tools you already use.

**[2:26](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=146s)** Go to firecrawl.dev/howiai to get started. Blair, welcome to How I AI. Thanks for joining.

**[2:35](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=155s)** Thanks. I'm glad to be here.

**[2:36](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=156s)** Well, one of the reasons why I was so excited to have you on the show is I feel like the best teams, their answer to what are we how are we going to use prototyping in our product design engineering flow is eventually to decide, you know, we're just going to build our own our own rig here. We're going to build our own prototyping harness and it's going to give us exactly what we need for exactly how our team operates. And the folks that do that and it is not impossible to do, unlock some magic in the team. So, walk me through what this is and why you built it.

**[3:07](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=187s)** We wanted to innovate, go faster, and get new features into users' hands. And so, we made a harness that uses our design system and all of our components, UX patterns, and it keeps all the designers and product managers on rails. And so, this way that you can make a million ideas, they can be reviewed, and then you can pick one, and then that's where we spend our time, and that's what goes into prod.

**[3:31](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=211s)** So, what I'm looking at right now is a little render of the the mobile app or the mobile site um for for Reddit. So, tell me how how would somebody come to this inside your team and actually design something? What do you think is is unique? I mean, it has the design system, but what else, you know, why did you build this and what is super unique about how you approached the the harness that you built?

**[3:52](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=232s)** When we started working with designers, we wanted to start off you skating all of Git, what the file structure is. And so, we actually made an app on your desktop that just gets you right into a new project and you would load the boilerplate and name it and then you would end up here in a vibe coded environment. You can work in any IDE you like and it sets up like what the app's a starting point. And we think of that app is like, you know, this is the whole world and as people add new features, it's kind of like a mountain and we absorb that mountain and it's everyone's starting point.

**[4:29](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=269s)** So, one, if I'm a designer or product manager, I don't have to think about like am I cloning the repo, am I on a branch, am I running locally? You've created a little custom app that says to start a project. Happy happy. Um you name that project and then you all do the hard work of like a baseline scaffold. And then does that scaffold put the app in a specific state? Like what are the kind of convenience things that you get when you land with this scaffold as a designer or product manager?

**[4:59](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=299s)** That's right. Yeah, so I just showed like how you create a new project. It's cloning the get. You don't need to know any of that. We'll go back to that screen and you'll just start coding. And the things that you get right out of the bat are examples of like features. And this is what every product development team does. They're going to add new features to the product and they're explorations. There's other doodads under here of like navigation. Um you can change the navigation. You can prevent navigation because some stakeholders click too much and you don't want them to click.

**[5:35](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=335s)** We have like

**[5:37](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=337s)** Yeah, and then so everything is controllable. You can change the device, the theme and so you can switch to dark and you can test out every every um every state that you can get in. Even like who is a moderator. And so Reddit has complex user ecosystem. And then the nice the the nicest doodad here is that you can then use signed in data and so you'll know if your design works. This this helps with all kinds of real-time data feed. So, like if you wanted to do search, you can actually do search right here. And before we we we started this, I was just playing around and I was wondering could I add search with these annotations? And surprisingly, I was able to I commented here, "Make relevant type aheads, trending recent communities, etc." And then down here, I said overall direction using the signed-in Reddit data and real type aheads as user types in the search box. And then I sent that to Cursor and it vibe coded it on the spot. And this was just playing around.

**[6:45](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=405s)** I was stunned. It worked.

**[6:46](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=406s)** Okay, so I just want to kind of like walk this through for folks that that are listening or maybe miss some of this. So, first of all, you have like features as configuration. Basically, like the ability to toggle on or off features inside this constraint prototype. Um you have the ability to configure the prototype itself in terms of like turning off the interactivity of features like navigation. I love this because if it is a fully like featured sort of prototype, you can kind of go anywhere with it.

**[7:14](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=434s)** Mhm.

**[7:14](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=434s)** Um but this is letting a product manager designer sort of constrain and say like this is the piece that I want you to pay attention to. Um you can obviously switch between devices, but you can also switch between persona views, which I thought was very interesting. And then I want to make sure people did not miss that this. One of the things that looks like you do, and correct me if I'm wrong, is you scaffold it with mocked data, but then you can log in with your account and render production data in the the prototype as well. And so, this is not a tactic that I've heard people use before, which I think is really really clever. I've heard a lot about mocked data. Um we have a great episode about using JSON as the backing for your prototypes and updating the JSON instead of updating kind of like hard-coded data in your prototype. But I have not heard anybody say, "Okay, go ahead and let you off into your production data and render that," which gives you a much more flexible set of data to work with when you're testing new features.

**[8:17](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=497s)** Right. Yeah, it's it's a clever trick. Our our team is like a bunch of magicians. And the reason why that we do this is because, you know, Reddit has personalized data. But if designers are mocking everything in Figma and then they show that to leadership, leadership's going to look at that and be like, "What? This isn't relevant to me." So if you make one of these real-world prototypes with real data, they'll put it through the paces of like some new feature. Search is like a is a great example because they're going to want the search results. I think I already did it. I said like how I A I. And it knew podcast. Like it's pulling that real data. It sends it to an LLM, ranks it, and then you can test out that design. This This design, I didn't spend any time on it. Um but a designer could then populate the landing, the type-aheads, and and the results.

**[9:06](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=546s)** And you don't have to take 9 months to get that into prod, see if that works. It saves so much time, and everybody can work on other things.

**[9:15](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=555s)** And then to make modifications to it, just because I'm I'm kind of inferring based on what you've showed us, you have sort of like a prompt-based thing, but that's ultimately just kicking prompts over to Cursor. Is that right?

**[9:28](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=568s)** That's right. Yeah, so the way that this kicked off was I this is a surprising workflow. But once I showed these annotate Once I wrote the annotations, I just said send a cursor, and it writes a file, and then I just tell Cursor apply annotations, and it takes the location in the code, the annotation, and the overall to kick it off. And you can with that specificity, you can target any surface, any composite, any component, and add real data to it with very little training.

**[10:01](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=601s)** Got it. So if I click something in this prototype and write an annotation on it, the prototype has already been enriched with This is like roughly where the code is. This is roughly what this component is. This is what the request is from the user. And so, it's like a very targeted um edit request in this repo. Is this the real repo or is this like a an approximate repo that's just for prototypes?

**[10:27](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=627s)** So, yeah, everything that you asked, I can go into the annotations. I can clear these and I can say make this italics. And so, you can target very specific things. It'll use all of our design system tokens, components, etc. And then this is the real thing. Um that launchpad that I showed earlier, it deploys it on our infra. And so, it basic It uses in It uses Kubernetes. It's basically like an internal Vercel. Um and so, then you don't have to worry about any deployment and you can share it. You can share it internally. It'll copy the URL. Or you can share it externally and you can like scan that. You go through some security and then now it's on your phone. And so, then that is a PWA. And these are these are apps that I've already installed and you can click around them as if you were on desktop and you can check.

**[11:19](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=679s)** Got it. So, that's the way that you I was I was curious. So, how do you share these prototypes internally? Are you just able to give links to people or QR codes and then they can pull up and and play with your prototype? Is that how it works?

**[11:30](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=690s)** This is a piece that we're working on right now and it's it's going into great places. Internally, you can share this URL quickly like on Slack. And we have we have a dashboard that just keeps everyone's prototypes. Right now, there's about 700. The problem with this is it doesn't scale. That list doesn't scale. And so, what we're working on now is a very searchable console. So, you can find people's prototypes, what areas they work in, um people, tags if that if that feature was like labeled, um you know, search or growth. And then you can go into prototype types. We're going to go into iOS, Android. And then you can also go through your prototypes. And so, what teams you work on. This would be the way that everybody can just discover quickly who's working on what and like gives a visibility to leadership.

**[12:19](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=739s)** And are all of these prototypes public? Are our prototypes public by default or private by default? I'm just curious.

**[12:25](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=745s)** Right. Yeah, so internally they're all public. Um but then like

**[12:29](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=749s)** Yeah. We we need to add that. We should add some so you can work under the and skunk works.

**[12:34](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=754s)** Yeah, under under the radar. I don't know. I kind of like this idea of like everything's public. You can kind of see what people are are messing around with. I'm I'm curious who is prototyping the most. Like are designers prototyping the most or product managers prototyping the most? Like who is prototyping the most?

**[12:52](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=772s)** Yeah, so it's a mix of designers and product. Um we have 100% adoption in UX and product. But there are like some surprising folks that show up. Like a visual designer turned out to be one of our best prototypers. An animator turned out to be one of our best prototypers. And what it seems like is these people are like great directors. They have huge context. They can describe all of the things. Um they they are vulnerable and they try things without like worry of failing. Um but yeah, it's it's a mix. It's almost a perfect mix over design and product over 150 people.

**[13:30](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=810s)** This episode is brought to you by Firecrawl, which gives your AI agents data from the web and beyond. Your agents can search and scrape the web while accessing Alexandria's rapidly expanding library of over 100 million indexed sources and more than 200 data providers all through one connection. Connect Firecrawl  to ChatGPT or Claude to find people and their work emails. Pick your fantasy football lineup or  analyze trends for your next marketing campaign. Firecrawl is building the library for superintelligence, bringing more of the world's knowledge into the tools you already use. Go to firecrawl.dev/howiai to get started. I can imagine how this changes how ideas are generated um and I and I see a lot of teams moving to this more like prototype style um requirements for designs. What I'm curious is how has this changed how designs are reviewed? Like how do you give feedback? How do people make iterations? How do they collaborate?

**[14:34](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=874s)** Right. Yeah, and so this is a part that we're working on also, but long story short, these go into like leadership reviews. Leadership uses them, clicks through them, and you know, you're getting feedback live. You're getting feedback in Slack, but we want to add, you know, you can comment live on the prototype. And so you have those annotations. Those annotations can be kicked off, they could be comments, they could kick off another build.

**[14:58](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=898s)** Mhm.

**[14:59](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=899s)** If a leader just wants to say like make this change, it could it could be live momentarily. Um but then um you know, like that console, it also has a place for commenting. These are all things that are coming.

**[15:12](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=912s)** Got it. And so do you feel like this has What What does this changed in terms of you know, is it velocity? Is it quality? Like craft? What do you Where do you feel like the impact to how you build products has been felt the most?

**[15:27](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=927s)** It's instant alignment. And so if you use systems with high craft, all the velocity like comes because you have, you know, alignment with leadership using real data, reviewing real design system components that nobody's hanging up on like a a gotcha and they don't rat hole on a detail, and they can quickly approve it. That goes out to everyone. Nobody Everybody knows like the North Star that they're heading towards, but it's it's instant alignment.

**[15:53](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=953s)** And then how does this get handed off to engineering?

**[15:57](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=957s)** Right. Yeah, this is the big puzzle piece here, which is that like, you know, can you take this code and send it to prod. Um so here I've I've um sketched out a fake feature. Um it's just like saving posts to folders. And so, would there be a way that we could select a component and then copy the example prompt and take this into prod? So, under this um launchpad, we can also start a new project where we make a feature capsule. So, what you do is you copy the location in Figma. You go over to Figma MCP, you create from Figma, and it's going to make this thing that we call a feature capsule. And what it does is it takes a lot of things. It uses Figma MCP, it goes through all of the design system, maps it to what we know is in prod.

**[16:59](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1019s)** It has also incorporated, you know, CI review feedback and engineer feedback into this MCP. And then now it's analyzing all of those uh Figma frames, components, and it'll spit out a PRD. And so, I'm going to say, "Yes, this is what you're looking at." I'll continue. And then it'll generate this PRD. These can get really large. This We just selected a specific frame. Uh but you could do many surfaces. We've tried the kitchen sink, but we kind of backed We're We're going back to just like high-fidelity UI. And so, here you've got your generated PRD, and it'll say like, "This is what the user goal is. This is the acceptance criteria." It'll get into details here. Links to the the Figma. And then uh once it's done, I'll accept and continue.

**[17:48](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1068s)** And you you save this file locally, and then we'll send that to Cursor.

**[17:53](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1073s)** Can you explain Go go a little deeper. Somebody wanted to build this themselves Is this a lot of this you built yourself, or like how did you get here? Cuz this is really interesting. It's going from a Figma link um and frame link all the way through PRD, and then something that your cursor can execute. So, just like walk us through how it got built.

**[18:12](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1092s)** Right. So, we started with the Reddit proto design system.

**[18:18](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1098s)** Mhm.

**[18:19](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1099s)** And so, we have all of the colors and typography baked into our design system. And then we read prod and we mapped the two. Um so here you have all of the button sizes. And so we use code connect and we know that those are everything is connected. This is kind of the whiz-bang moment where like you're like, "What am I looking at?"

**[18:42](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1122s)** Oh, yeah, exactly.

**[18:43](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1123s)** This right here is is every single token, component, surface, journey that we know of across RPL, Reddit product language. And so here this one token is mapped into Figma into iOS in the GitHub and into the prototyping GitHub. And here it is picked out that there may be uh difference in the actual literal values in the token on some platforms. And so what we we then take that and we map it to prod code. We submit PRs that do and don't get through CI reviews and like we take all of the the engineer feedback and that iterates back. So basically you start with a map and then you try, fail, iterate and you refine the MCP through feedback.

**[19:35](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1175s)** Got it. And And this is an MCP that you've built?

**[19:38](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1178s)** Mhm. Well, uh the team. Um

**[19:41](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1181s)** Okay. Yeah, I meant you the the you know, the collective the collective you. And what are some of the tools in that MCP? Is it like where's the component? What's the design token?

**[19:51](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1191s)** That's right. Yeah, so right here we got it hooked up this proto MCP ultra and it it's basically like looking for um what are you feeding it? And and then it's finding tokens, components, and examples to write that prod shaped code. This is what the code ends up looking like. I can't show the code but like

**[20:13](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1213s)** course.

**[20:13](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1213s)** just proof in the pudding like it goes through all the get reviews.

**[20:18](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1218s)** Yeah.

**[20:18](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1218s)** Um and makes a build for you to test out on um on your device.

**[20:24](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1224s)** Okay, so I want to make sure that people don't don't miss this process, which is you all have built an MCP basically to translate any input and in this instance that input might be like a Figma frame into discovering the correct tokens, design system components, code snippets, whatever based in production. So that when you're generating prototype style code, it is as close to production as you can reasonably get because it's done this traversal kind of like through this MCP.

**[20:57](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1257s)** Yeah, that's right. Yeah. And so in this example, we're going from Figma to prod. We have tried out going from prototypes to prod. But we think that this is like a very like accurate way of getting like high-fidelity Figma, high-fidelity architecture. Uh but yeah, it's doing that through a map.

**[21:14](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1274s)** You know I'm a PRD girl. Do you feel like the PRD makes a difference?

**[21:18](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1278s)** Yeah, it's it actually carries a lot of weight. And so when we started talking, the reason why we added this is because that was the handoff

**[21:24](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1284s)** Mhm.

**[21:24](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1284s)** with engineering. And so then you clearly define your scope, all of the user goals, and you know, workflows. Yeah, it's it is it is the perfect handoff. It has all the context.

**[21:35](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1295s)** I mean, you heard it here, folks. The PRD is the perfect handoff. Keep making them. Um I I really I really love this. I mean, I think what folks should take away from this is not just can you build your own prototyping system and can you make it form fit to how your team likes to build things. Um you can hide away some of the complexity of vibe coding and prototyping from your less technical friends um while still running it in something like Heroku in the background. And then uh the idea of building sort of convenience method um design system-based MCPs is a really clever one because a lot of times you're just leaving these LLMs to kind of flail about in the code and find what they think they can find.

**[22:20](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1340s)** Yeah, that's exactly it. Like, you know, um folks say that bots hallucinate. They hallucinate writing code. And our opinion has always been like, well, what what's your goal? What's the context? And you look at the design system, you look at the end state shape, and then we refine from there. But uh yeah, this is this is the um this is the MCP using that feature capsule and asking me where it should which where it should write the code.

**[22:49](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1369s)** Mhm. Amazing. And it could write that code basically in in the app or in a prototype or whatever you might want.

**[22:56](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1376s)** It's right now it's writing it in a sibling repo uh to keep uh prod clean. And then it'll iterate and then it'll send off a draft PR. And then yeah, and then that'll get reviewed and may or may not go through.

**[23:10](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1390s)** May or may not. And then can you go back to the Rosetta Stone because I don't want people to miss this amazing thing that you had, which is you have this like nice visualization of what's going on in our design system.

**[23:21](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1401s)** Right.

**[23:22](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1402s)** Why did you all decide to build this?

**[23:27](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1407s)** Well, so the theory was how do we get the design system into a harness and then the harness goes into an MCP. And we had made several attempts and the number one thing was, well, I don't know if what's in there. And so I was like, well, this is a visual verification. And if I can hunt down and see that I know that a avatar has these colors and is used in these surfaces and is a is a part of these workflows, I can visually verify ah, well, I know that the harness and therefore the MCP has all of the parts.

**[24:06](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1446s)** So, it's just like kind of and and is this how your brain works because you're like, oh, I can easily visualize. I'm like, you can visualize what, man? It's like a bunch of fuzzy auras over here. So, tell me, like is this just is this what what what is inside Blair's brain?

**[24:20](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1460s)** This is Well, yeah, the collectively this was what it was in the team's brain. But this was like, you know, I was trying to explain this to people like, you need a single source of truth that's upstream from everything. Um you know, and then when I would show this, people were like, I know it's in there. It was a visual verification for the team. Yeah.

**[24:39](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1479s)** I I love it, and it's very beautiful. It's very soothing. It needs a little It needs a little music, though.

**[24:46](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1486s)** What would you play?

**[24:47](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1487s)** I don't know. I don't know some some some sound bath bathy kind of stuff.

**[24:51](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1491s)** Oh, there you go. Yeah, some Brian Eno.

**[24:53](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1493s)** Exactly. Exactly. Um I love this. I just want to recap for everybody. Okay, so we saw Reddit proto, purpose-built prototyping tool for product managers, designers, public by default, anybody can open these, deployed sort of in your cloud, some controls via config, connection to um cursor, and then a really thoughtful, audited, and contextualized design system that's accessible to this whole harness via a custom MCP.

**[25:26](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1526s)** Nailed it. Yeah, that That is what we do.

**[25:28](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1528s)** No big deal. Easy peasy. Um this is really I just my my head is spinning. I'm going to swirl on like how much of this I think I can build because I think it would really change how I think about some of my um design system problems. As I noodle on this, let's go to some lightning round questions. Um if you're ready, one is just what are some non work, non-prototyping Maybe not non-work, but like what are some non-prototyping use cases that you're really loving AI for these days?

**[26:01](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1561s)** Before this podcast, I was working on um I was working on making playing cards for the whole team. And so, this is like this is the person who who helped start the the whole Reddit proto uh project. And so, we're making a play like a players uh all the players on the team, and then you have like all their stats on the back. And what's nice about this is like you have to like direct this and get it into like brand, and um yeah, and then everybody will have it in their hand.

**[26:34](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1594s)** I know. It's so fun to be able to make like creative physical goods that are high quality. I mean, again, and these are like very high quality, super cute, and and consistent. What What did you use to generate these? Like how did What was the process?

**[26:48](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1608s)** Yeah, so I I bounced around a bunch of places, um, but with my bots, I described everyone and I kind of just like ad-libbed. This is their like, you know, this is their persona. And then I actually took that I took that to Gemini. Gemini could have per performed better, but like, uh, ChatGPT ended up making the the illustration that was perfect. I took that into Cursor and generated on a high model. And then that used like a a markdown file to use the prompt that kept them all in the same aesthetic. Yeah, it was it was it was quite a workflow.

**[27:23](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1643s)** Oh, I love it. Super super genius. I mean, a hidden how I AI at the very very end of this episode. Okay, my my last question I ask everybody this. When your MCP is not replying, when Claude is being obstinate, well, you know, whoever it is. When AI is not listening, what is your prompting strategy? How do you get it back on track?

**[27:44](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1664s)** So,  I don't yell at them. I know some folks do, uh, but what I do is I take a day and then I get more vague. And we all have like bots with like projects and context, and I pop out of a project and I describe the thing large. Yeah. Like, uh, like a movie director. So, here all the facts and then here is all the intents. And then and then I pull that back into the project and then it knows enough to apply it to what what our goals are. But essentially, I become a better director that is more vague, not specific.

**[28:17](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1697s)** I like that. I I do tell a lot of people just like under prompt your AI. It's It's a lot more effective than than over prompting. Uh, that's that's a good one. That's one we haven't heard yet. Well, Blair, this has been really interesting, very very dense, and I think a lot of great ideas for teams out there looking to think about how they can improve their own prototyping harness, why they might build their own, and even just designers and product out managers out there that want to get better at using design systems to build production-like code.

**[28:47](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1727s)** Awesome. Yeah, thanks for having me. We're really excited to get these features in the users' hands.

**[28:52](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1732s)** Awesome. Well, where can we find you, and how can we be helpful to you?

**[28:56](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1736s)** I'm on LinkedIn, and when I'm not on LinkedIn, I'm touching grass. If you want to work at Reddit, feel free to reach out to me on LinkedIn. If you got any puzzles like this, I'm also really friendly. I love helping folks.

**[29:07](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1747s)** Amazing. Well, thanks for joining How I AI.

**[29:10](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1750s)** Thanks.

**[29:12](https://www.youtube.com/watch?v=zF-J3rMbzZw&t=1752s)** Thanks so much for  watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaiipod.com. See you next time.

