# How to Automate Hiring Launches (Claude + Slack)

- **Podcast:** PromptMates
- **Channel:** PromptMates
- **Date:** 2026-11-02
- **Duration:** 8:42
- **URL:** https://www.youtube.com/watch?v=wI-TYLIO9ic
- **Fetched:** 2026-11-04
- **Source:** YouTube captions via TranscriptAPI (asr-en)

## Episode description

What if opening a role took one Slack command instead of half an hour across three tools?

Emily Paik walks through the workflow she built at Kit to launch a role from Slack. One Slack command opens a modal, creates the Ashby job and opening, sets up the Slack channel with the right naming, invites the stakeholders and pins the Notion and Claude resources the hiring manager needs.

Chapters
00:00 The 30 mins behind every new role
01:13 One Slack command linked to Ashby
03:06 Resources for the hiring manager
05:11 How it was built
07:01 What you need to build yourself

Emily Paik, Senior People Operations Manager at Kit, where she runs recruiting and people operations as a team of one and built this workflow with Claude as her coding partner.

This clip is from the PromptMates Live Show, where talent and people leaders share what they're actually building with AI.

Join the PromptMates community: https://www.promptmates.ai/community
Weekly newsletter: https://www.promptmates.ai/newsletter
Catch the next live show: https://luma.com/promptmateslive
Connect with Emily: https://www.linkedin.com/in/emilypaik

#TalentAcquisition #AIRecruiting #Ashby

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube. A new paragraph marks a change of speaker where the captions show one (speaker names are not available).

**[0:00](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=0s)** So, today I'm going to walk through a workflow that I built that automates the hiring launch process across Slack, Ashby, and Notion. And probably like many of you, I don't consider myself a technical person whatsoever. I'm not the most AI-fluent person you'll see on Prompt Meets, but I am AI-curious and it has helped me create impact and expand my skill back kit. So, the problem that I was trying to solve for is every time we opened a role, it was the same monotonous 30 minutes of manual busywork. And I'm sure many of you can relate. Hiring managers want to move fast once head count is approved. And sometimes it took days before the actual role was open, which the business did not love. I also did not love that, but that was the reality because of manual process.

**[0:48](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=48s)** So, for example, the time spent on getting the hiring manager up to speed on the hiring process, finding and sending the right Notion links that house our resources, checking if they actually saw them, setting up the Slack channel, and making sure all the right people are in it, creating the job and opening it to Ashby, and then finally the role getting posted. That was all very time-consuming. So, that is the friction that motivated this. So, I created a workflow, which is just a Slack command /newrole, which pops open a modal in Slack. And for context, Slack is where we do everything as a company. That's where we spend the most time, like many companies do. So, I didn't want to be bouncing around different tools by hand. I wanted this all to get created within one tool. So, this is what the actual modal looks like. It has fields for title, department, team and squad, location, employment type, and hiring manager. And I do want to call out that this is intentionally minimal, just enough to drive everything downstream. So, the modal also has an option to draft a job description. It'll link to a cloud project to GD writer that I created and a prompt which I'll talk more about in just a few minutes.

**[2:03](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=123s)** And it's connected to Ashby via API and in the opening drop down in the model, there are a few options. First, it can create a new opening in Ashby which is the default and most common case or it can link to an existing opening. And that's because we use Ashby for headcount planning and sometimes we bulk pre-create openings in Ashby ahead of time so that we can reference it with our finance team. So this path just attaches the new job to one of those instead of creating a duplicate. The third just creates a new job which is honestly personal preference sometimes. But the reason that I wanted to highlight these options and why they exist is because the tool matches how Ashby and our planning process actually work instead of forcing one path on each scenario. And as we scale, I realized having good naming conventions is really important. Casey has called that out in his example, too. And I think this is true outside of hiring as well. But because we have so many hiring Slack channels, we needed a solid naming convention. And by the way, I realized this before I built the actual workflow.

**[3:10](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=190s)** I've been using the same naming convention for a couple of years. It's always hiring {dash} name of the role, whichever quarter we're currently in and the year. And engineering roles get the squad name added automatically. Contract roles get a contract prefix so they're immediately distinguishable in the Slack sidebar. And the quarter calculates from the server date match to fiscal year which is again a small detail, but it means every channel is easily searchable even the archived ones which is important for historical context. And also if anyone else besides me is using the work this workflow, um they're able to follow that same naming convention. And this screenshot shows all of the hiring resources that I used to manually send or forget to send automatically pinned to the channel by the bot. The bot also invites all of the stakeholders needed, which is usually myself, the hiring manager selected in the modal.

**[4:08](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=248s)** And the resources that are pinned to the channel include our hiring manager Notion hub, the Claude project JD grader I mentioned, and also another Claude project that creates an interview plan and helps generate questions as well. Again, links that I would manually track down or often times forget to send. And then there's also a Claude prompt pre-filled with the role details automatically added by the bot. So the hiring manager just can copy and paste it and get a first draft JD instantly. And that project has our brand voice, our standard JD template, uh career growth frameworks baked in. So I know when they're using that, they're creating a job description that meets our standards, aligned with career growth career growth frameworks, and is written with good copy. So quick look under the hood for how I actually built this. There are three pieces. The first is a Node.js with Slack's Bolt framework to handle the slash command and modal.

**[5:07](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=307s)** Replit is hosting this as an always-on server running 24/7 waiting for Slack with the Ashby API key stored securely in Replit secrets. And then Ashby's REST API on the other end called directly for job create, opening create, and opening add job. So I want to call out it's it's a small stack. It's not a lot of tools. Claude was my coding partner throughout. When I first had the idea, I went to Claude. It suggested Replit because I'd used it to build other tools, and it wrote the code and helped to verify the API calls against Ashby docs for me. So in summary, before I built this workflow, I spent over 30 minutes of manual work across three tools every single time and it created delays for the business.

**[5:53](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=353s)** But with the workflow and with one command, the job, the opening, the channel, the invites, the JD, and the resources are all set up consist- consistently without me having to remember every single step. So, it's been a game-changer for me to get roles posted uh much faster and far less time and work on my end. And then, if I can just leave you with some takeaways, it's that you need to start with the tools your team's already using and they that they spend the most time in. So, for us, that's Slack, as I mentioned. The workflow just had to live there. Um second is to find your own friction point or bottleneck first. For me, as I mentioned, it was always getting the job actually open and getting hiring teams up to speed. And then, don't automate everything at once. Automate the thing that's actually slowing you down. Ship something as soon as as soon as it's useful and then keep iterating as you discover more friction to remove. I've already iterated on this a few more times and I have a long mental list of ideas to add to the workflow, which is the fun part of building and testing and shipping and continuously improving. And that's it.

**[6:58](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=418s)** So, happy to answer any questions here or offline.

**[7:01](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=421s)** Awesome. I uh I love it and I love it for a few reasons. Like, one, the bit you just mentioned, like, meeting people where they are. Like, we know hiring managers are super busy. Yes, they need to hire, but trying to get them to go into five different systems is is super difficult. But not only that, and like not only making a process more efficient, but actually thinking about how can we make this process better? And I love the bits where it's like all the kind of hiring manager enablement to help them like with interviews and and how to like be a great hirer or a great recruiting partner is is really cool. Would you mind just going back to the slide where it was like the stack you built it on?

**[7:36](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=456s)** Yeah.

**[7:36](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=456s)** I would love to see that one. Yeah, great. And for folks who haven't like come across the Node uh Node.js and Bolt section, Can you just explain like what what that part means?

**[7:45](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=465s)** Um this is what's building the um actual app. So, if anyone's created a Slack app, I think this is done either on admin or on the developer platform. Um it needs something to um like talk to, right? So, like Replit is connected to this app cuz you need to add a URL, but the code that I gave to build the actual like modal and the um like what you see what you actually see in Slack, that is what this is referencing.

**[8:15](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=495s)** Got it. Cool. So, in terms of what you would need to build it in the way you built it, you would need Slack admin or you would need to pull from your Slack admin effectively to be able to build the app. Um yeah. Some kind of either MCP or API access to your ATS, and then something to build it with, e.g., Replit code, this this kind of thing.

**[8:32](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=512s)** Yes.

**[8:33](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=513s)** Awesome. Cool. By the way, the chat So many people in the chat saying everyone in RecOps is self-taught, so uh your tribe is absolutely uh

**[8:40](https://www.youtube.com/watch?v=wI-TYLIO9ic&t=520s)** is with you, I believe.

