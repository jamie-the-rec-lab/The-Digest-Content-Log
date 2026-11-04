# Build an AI Candidate Chatbot with Google Gemini

- **Podcast:** PromptMates
- **Channel:** PromptMates
- **Date:** 2025-12-15
- **Duration:** 9:47
- **URL:** https://www.youtube.com/watch?v=w2UnqBOhIDg
- **Fetched:** 2026-07-31

## Episode description

👉 Join the PromptMates community for hands-on AI builds, live sessions, and real recruiting workflows: https://promptmates.ai

In this video, we build an AI candidate chatbot using Google Gemini Gems & show how recruiters can create and share a candidate-facing AI assistant in minutes

This is a hands-on PromptMates Build focused on a real recruiting problem:
👉 answering candidate questions consistently, accurately, and at scale without adding recruiter workload.

Unlike Custom GPTs, Gemini Gems can be shared externally with anyone who has a Google account, making them a powerful option for candidate experience, interview prep, and FAQs.

What we build in this session:

- An AI chatbot candidates can use during the interview process
- Clear instructions and guardrails to prevent hallucinations
- A structured knowledge base (policies, benefits, interview info, FAQs)
- A shareable link recruiters can send to candidates instantly

We also cover best practices for:

- Designing candidate-facing AI safely
- Constraining AI to approved information only
- Deciding when Gemini makes more sense than ChatGPT

Who this is for:

- Recruiters exploring AI beyond ChatGPT
- Talent teams improving candidate experience
- Leaders looking to share AI externally without new tools
- Anyone experimenting with Google Gemini in real workflows

This session was recorded live during PromptMates Live, where we build practical AI workflows for Talent & People teams — no theory, no hype, just real builds

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube.

**[0:00](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=0s)** That's awesome. Thank you. So, this is actually kind of funny because Joe has been like emphatically carrying the Gemini flag for months now and I've been like the de facto GPT fanboy. And about three weeks ago, like it did sort of start to shift for me. And in in large part based on what he said, it's that like that slide he had with like the eight 10 different apps, that was me. like I was the shadow AI guy whose credit card was like getting charged 29 bucks a month way too many times. Um, and then here I am now making use of this new Gemini suite inside the safe confined walls of my my CISO and my head of AI and all that stuff are supportive of it. Um, and so that's what we want to talk about today is sort of like maybe how to move away and and kind of come back come back into the to the Google fold. There's a comment right there. my my recruiting workflows and GPTs have always been built in GPT. Are we now saying that Gemini is the go-to? I'm not saying Gemini is the go-to. I will say that right now there are some advantages to using Gemini. Most of which that I want to talk about is the ability to share externally. With GPTs, you can make a custom GPT and you can share it within

**[1:15](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=75s)** your company and you can share it external, but the only people that are able to access it are people that have a paid chat GBT license. With these new gems that we're going to create today, you can actually share them out and as long as somebody has a Google email, as long as they have a a Google access, they don't have to have a Gemini Pro, they can access your gems. So, what that got me thinking about was like, as a recruiter, what is something I wish I could share externally? So, what we're going to do today is probably spend like five minutes building a gem that you can share with candidates to basically have them answer questions when they're in the interview process. So, here we are. This is Gemini. You're going to go over here, open up the menu.

**[2:01](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=121s)** Right here, it says gems. Go ahead and click that and it'll take you to the gems page. These are the gems that I've created. For those of you that have been done a lot of stuff with like chat GPT, you know what it looks like. It's just all the stuff that you've created. We're going to click new gem. And this is probably going to look relatively familiar to those of you that have built custom GPTs up until this point. It starts with we're going to name this this app for all intents and purposes. Give a quick blurb, tell it what we want it to do, and then add files to its knowledge base. the things that might be missing here compared to what you may be more accustomed to seeing in chatbt. Chatbt does allow you the opportunity to connect it to things externally. That was kind of what Joe was talking about. Like it's coming from a Google perspective, but it's not quite there yet. So, we are going today to talk about what it's like to get a job at Hogwarts. So, this is going to be called I don't know your all right description. This is going to be your magical assistant to your new job at Hogwart. Now, for instructions, much like I said with chat GPT, all we're going to do here is tell this gem what

**[3:11](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=191s)** we want it to do. So, I've already created a prompt here. I will share this. We'll put this out in the the notes section or the detail section of the YouTube video. But in essence, what this is saying is it's telling it that you're a recruitment construct, the persona that you wanted it to be. For this particular version, we wanted it to be kind of silly and fun. How to handle the different topics that might come up in an interview process. And then the restrictions, like you'll notice here, don't make up facts. If you don't know the answer to something, just say that you don't know the answer to something. So what we're doing here is we're like highly constricting it to only be able to give responses based on the knowledge base that we are actually providing it.

**[3:56](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=236s)** This one's a little bit tongue-in-cheek. You can very easily copy this and put it into any LLM of choice and say please rewrite this Hogwarts talent recruitment construct for my company. I work at Lego or I work at Ooni Pizza or I work at Netflix, whatever, whatever it may be. So, we're going to go in here to Gemini and we're going to paste the instructions. And now what we're going to do is go ahead and add our knowledge base. And the knowledge base is just that it is the things that this gem will go reference when questions are asked of it. Now, you can upload directly from your computer or you can upload from a Google Drive. I personally tend to upload directly from my computer. What you'll see here, though, is I've got 10 different files. The most number of attachments that a gem can take right now is 10. But what you can do is if you wanted to put in like 20 different things, as an example, you can go in and you can consolidate. Like so for instance you'll see here I have like a holiday calendar as well as an employee handbook. I could very easily put the employee calendar into the employee handbook and that lowers the number of you know kind of maximum number of of files that I have. Another thing to call

**[5:20](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=320s)** out too is this is multimodal. Like kind of like Joe was saying, like you can throw a whole host of different types of information at it and it'll be able to handle it. Like so in this case, we're doing everything from, you know, the Hogwarts benefits guide is a branded PDF, but the candidate journey is a visual. And then there's even some data that is boring old markdown files because it's easy for the computers to read it. So throw Excel sheets, throw PDFs, throw images. You can throw a lot of different types of information into a gem. We're going to go ahead and take all these, add them. It's going to take a second to think about it. And now we have something that we could send out to candidates. We're experimenting this right now at at my company and we're actually putting a link to our questions about what it's like to work here in recruiter signatures. So, but you can go ahead and now let's go ahead and save it. We're going to start a chat just to test it out.

**[6:28](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=388s)** You can test it out in that little box. Me personally, I found that if I'm going to test something, I like to save it so I understand what the person that I'm going to be sending it to will experience. And we can ask anything we want, like, you know, do you have pet insurance for my dragon? I like to tend to leave it in thinking mode. I find that thinking mode tends to work better with deeper knowledge bases. All right, so here's information on what is covered. People can ask about what are the pay dates. I'll even load another one up. What can I wear? How about this? Let's be funny. Can I wear jeans to my interview? Maybe just one more question while this loads, Jason. Someone asked if you can reference Confluence pages.

**[7:12](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=432s)** >> So, what I have always found is you're better off putting in actual collateral as opposed to links. So, like with a with a confluence page, what I would do is probably save it as a PDF or try and save the individualized collateral and then load it as a knowledge base. My little saying though, AI is the worst it's ever going to be. I'm sure at some point we're going to get to the place to where you can give it, you provide it a series of URLs and then it can go back and reference it. >> Yeah, agree with that. We're not confluence necessarily, but I think when you see Mike's demo, we'll be getting into like connecting other apps together. So, you'll start to see that flow within Google. you you'd also have to remind the user to hit the plus button or the tools button and select Confluence or notion or whatever because you can't necessarily write that into the gem.

**[8:03](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=483s)** >> Yeah, that's a good point. So, that's the gem. This is sort of what I would say is every single person on this call could build one of these today. I'm not going to spend a ton of time on how you do the next thing, but the next version is called Google AI Studio. And what this is is this is going to look a little bit more technical, but you can literally start with this as I started with this as my prompt. And I said, I want to go ahead and build the Hogwarts talent recruitment construct. Here is my prompt. Here are my 10 items. And it builds this out. Imagine being able to like go even a step further and send something that is completely branded. This is a little bit more difficult not remotely impossible like I am by no means technical but here you can ask the same questions sort of like you know what's should I expect in the interview process so once you learn how to do one thing once you learn how to create a gem you can very easily move that on into more advanced techniques that's what I wanted everybody to see here one thing I actually realized I forgot to do though.

**[9:17](https://www.youtube.com/watch?v=w2UnqBOhIDg&t=557s)** By the way, when you go to Gemini and you go back to your gems, here's how you share things. See the little our favorite little share button, the the our familiar Google share button, if you will, down here, general access, what you're going to want to do is say anyone with a link can be a viewer, and then copy that link. And now, anywhere I go, if I paste that, if I if I go and put it into my own personal as opposed to my PromptMates one, there you go. Now I can know how to get a job at Hogwarts.

