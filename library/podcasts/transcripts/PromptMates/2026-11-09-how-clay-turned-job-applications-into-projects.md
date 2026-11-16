# How Clay Turned Job Applications Into Projects

- **Podcast:** PromptMates
- **Channel:** PromptMates
- **Date:** 2026-11-09
- **Duration:** 11:32
- **URL:** https://www.youtube.com/watch?v=BxL-h9Q29YY
- **Fetched:** 2026-11-16
- **Source:** YouTube captions via TranscriptAPI (asr-en)

## Episode description

What if the job application was the project instead of a CV? Clay skipped the resume screen and let every applicant show what they can do from day one.

Jen Ayala and Ryan Ellis walk through how Clay rebuilt its application process for high volume roles. Candidates complete real work simulations instead of a resume review, Clay tables grade every submission against hiring manager rubrics, scorecards land in Ashby, and recruiters stay in the loop with an AI opt out for anyone who prefers standard review.

Chapters
00:00 Flooded with inbound applications
01:13 Making the application the project
04:34 AI grading into Ashby with human review
07:29 How candidates should use AI
10:07 Under the hood in Clay tables

Jen Ayala is Head of Recruiting at Clay. Ryan Ellis is Recruiting Ops Manager at Clay.

This clip is from the PromptMates Live Show, where talent and people leaders share what they are actually building with AI.

Join the PromptMates community: https://www.promptmates.ai/community
Weekly newsletter: https://www.promptmates.ai/newsletter
Catch the next live show: https://luma.com/promptmateslive
Full episode: https://www.youtube.com/watch?v=fPLzPKP75ts&t=2201s
Connect with Jen: https://www.linkedin.com/in/jenniferecarberry
Connect with Ryan: https://www.linkedin.com/in/bobafett

#TalentAcquisition #AIRecruiting #Clay

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube. A new paragraph marks a change of speaker where the captions show one (speaker names are not available).

**[0:00](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=0s)** How would you describe the current state of inbound applications across I guess the folks in our community and the folks we speak to?

**[0:05](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=5s)** I don't think anybody's having a problem with inbound lately, no. I mean it's it's no joke. We went from on average for engineering, we went from 143 to 243 to 389 to now we're at 614 over the past four years of applicants per engineering and that's just that's just engineering, right? So I mean like I think we all know that we are flooded's not even the right word, man. We're inundated with inbound lately because to Jen's point it's very very very easy to automate that now. It's very easy to create a wildly bespoke resume or CV or what not.

**[0:38](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=38s)** Yeah, nearly Do do you know who Churchill the dog is in the US? It's a very UK story probably but like Churchill Churchill dogs have this nodding dog like he like nods up and down like this and we were on a community call and I was like describing a few different problems of inbound and like we had 20 30 TA leaders on there and everyone was just like nodding their head like along as I was describing the problems like it feels like it's every single org. So I guess like Jen let us know what's this been like for you at Clay and what knock-on problems has it been causing for you?

**[1:05](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=65s)** To caveat this, like we're in a moment where a lot of people are coming inbound and this isn't always the case. If you know if you've been in recruiting, things change all the time. So I just want to call out that like yeah sure a lot of people are applying now but that can change so quickly as we've all seen in our careers probably. We are experiencing a lot of inbound especially for early career roles, frankly. I think we opened up our I can't remember if it was the full-time or the internship role for software engineering. I think we got 7,000 applicants in less than a week. So yeah, we're experiencing that for early career roles and I think that's a condition of the market that we're in that it seems like a lot of companies are taking a pause on early career hiring so it makes sense to me that we're getting so many applications from them. So certainly a challenge for us too. The way that we solved this problem for actually two roles now are early career engineering roles. I was talking to Varun about our interview process for sales and see version of CSM role. He had this idea of like what if we just open sourced the project portion of all of our interviews to allow everyone who

**[2:08](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=128s)** was interested in interviewing for these roles to come show us what they can do rather than have them apply with their resume, talk to a recruiter, talk to a hiring manager, then get to the actual core of the process where they show us what they can do. And my response was basically like that's a great idea and let's do a pilot of that on one role and see how it goes and learn and then we can continue to do it over time. I also think for some roles we still get very little and are not as much inbound not inundated and the last thing I would want to do is add a barrier to application for some roles where I wanted to be actually very easy to apply to some of our roles where we're hired we're hiring at high volume. So we started with our product support role and basically the application became the project. So we have I think Ryan can show you in a second what this looks like but basically you go to apply for the role and we say hi, thanks for finding us. The application is your opportunity to show us what you can do instead of us reviewing your resume and talking to a recruiter and talking to a hiring manager, we can actually just skip all of that and if you would like to show us exactly what you can do with

**[3:12](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=192s)** a few different simulations. So we have three different parts to this process. So there's a customer support simulation. So it's basically a a chat GPT environment where they're helping a customer with a problem and then building in clay and then the third one is responding to where a user who is experiencing a bug but maybe we don't know if it's a user error or a bug. And so I think this one we're looking for how do you approach a customer or a user in a way that doesn't just say hey, this is your fault basically. Like can you have nuance in the way that you respond to people? And this was a really great success. Like it's helped us to jump you know to fast forward to the impact. We've hired an amazing amazing team.

**[3:52](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=232s)** We've hired people that I don't know if we would have necessarily said yes to a resume, right?

**[3:58](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=238s)** I think that's some of the coolest parts of it.

**[4:00](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=240s)** I think yeah and that's my frankly what I want to for is hiring the best people at Clay, not necessarily, okay, we need to figure out how to process all these applications. That's like on the road to how do we hire the best people at Clay? And so many people at Clay are doing their job for the first time, especially across our operations roles. And this was a way for us to kind of open up the doors for anyone who might not even have explicit product support experience to come show us that they want to do that job.

**[4:26](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=266s)** And I can jump in a little bit on the on the kind of workings of that as well. Again, this is very much focused on the experience part. It's it's part of the application. The team worked really closely with the hiring managers to develop these questions. They were interactive and kind of examples of what this role might actually you know, entail, which is I think also why it allowed folks from non-traditional backgrounds to like apply their skill sets and their knowledge in these environments that let them shine. I think there were some people with wildly different backgrounds to to PSS. I think we had folks from like finance, like even engineering do really well in these and and move forward, whereas otherwise like a recruiter looking at that resume might have dove over it, which just really need to see. From a a just technical perspective, I can walk a little bit through the clay table that it's built in as well. We are gathering this information that the folks like put in their application form and presenting it to recruiters to actually like make the human decisions here. So none of the decisions themselves are our AI. We obviously want to keep people in the loop here to understand and read through

**[5:28](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=328s)** like what folks have highlighted from from their experiences. So all of these applications go through a clay table, are graded by various like AI functions that have been set up with the hiring managers to build this really really complex rubric of how to actually grade these particular assignments. That is then compressed into a scorecard that is put into Ashby and moved into a stage of graded within this particular job and the recruiters are notified and so they again then get to go in there and review that and see the scorecard, see how folks have done in these particular assignments. and if someone chooses to hey like you know, I'm not interested in being assessed by AI, it allows them to still apply directly and go into the general application a review bucket for for a standard review and and resume there.

**[6:15](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=375s)** Just so just so I understand that part. Basically, they when they submit, they had a choice between whether they wanted their application to actually be reviewed by AI or not.

**[6:23](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=383s)** Of course, yeah. There's an opt out ability there.

**[6:26](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=386s)** Cool.

**[6:26](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=386s)** And so if they if they don't opt out, you know, they go through the process to send this is an example of what actually comes like into Ashby's actual scorecard system. This gives us information on how they performed on each of those particular sections with an overall recommendation that the recruiters then review and decide on whether to move forward.

**[6:43](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=403s)** Another impact that I didn't think about before we went on this journey was the real fatigue that hiring managers and recruiters can develop from reviewing the same project over and over again, right? Because the first time you review the project after you create it, you're like, wow, so innovative. This person has such a cool creative idea. And then you see the 100th person who has maybe thought of the same cool creative idea. And that's not fair. Just because they weren't first in line for this role doesn't mean that we should knock them down for having the same idea as the first person. So I think AI is actually so helpful here in helping us stay objective and not moving the bar up or down as we continue to hire for a role with the same project.

**[7:21](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=441s)** Let's just do one question from the chat, which is on the candidate side. Like, what was your approach to communicating with the candidates, how they should use AI in in projects? And this is top of mind for us cuz someone from our community like showed us like an inside of their application feed from like a mini project they had to do.

**[7:35](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=455s)** Oh gosh.

**[7:36](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=456s)** Claude clearly approaches this project in a certain way because the answer was basically the same for everyone. And so yeah, interested in your guys' approach to this.

**[7:44](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=464s)** One of our software engineers at Clay, Sophie, wrote an amazing, I would say a beautiful manifesto on how we should think about using AI internally at Clay for writing. And Varun, I think the social post that's done the best was talking about this on LinkedIn. And that's my advice for people who are applicants who are going through the process is just of course use AI. Of course use all of the tools that you have at your disposal, right? Absolutely. We also have on our software engineering panel we have a prompting interview, right? We have an interview where we expect engineers to prompt to write code. And so yes, we're we're absolutely pro use it, but kind of to your point Joe of we know the first sentence that Claude will suggest or ChatGPT will suggest on that email that you are writing back to the user. We know what it looks like if you don't add any of your own thought or creativity.

**[8:38](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=518s)** So I think that's you know my advice and what we say to candidates for any project that anybody's submitting for any interview process at play is here's our AI writing policy. Of course use AI, but consider your audience and make sure it's something that you want to put your name on.

**[8:52](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=532s)** There's an interesting addition to that with this particular workflow where the candidates are are building a a clay table. So clay, you know within the product and and within a lot of products you you often have this AI co-pilot that is building for you. In clay it it was Sculpt, it's now like Global Agent. And we do call out in the application like you know it as much as possible don't use Sculpt to generate the table. We want you to play around with it. We're not expecting any any folks at this stage to be experts in in the platform, but we look for like how they experimented and and what they tested out, what they tried, what they built by themselves without using the agent to to prompt them. So it's it's this kind of interesting balance where it's not just text generation, it's also about utilization of tools and your kind of thought process there. But that's also called out in the exercise.

**[9:43](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=583s)** But I think that's going to change.

**[9:45](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=585s)** Yeah, yeah. Oh no, 100%

**[9:47](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=587s)** I feel like different hiring managers are in different phases of this, but I think one that saying of course use AI to use clay like use agent to use clay too to build in clay.

**[9:57](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=597s)** Awesome. Anything behind the hood we can see for this one Ryan or

**[9:59](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=599s)** Yeah, I can show a little bit of this. So this one is still So the the first example that I I had shown with the hiring thesis that's built in our newest product workflows. This is in our original and current tables sort of flows. It shows a little bit about the application form coming into the system and it's a little bit more linear like in this. Essentially you're you're getting the information of their application from Ashby and the application itself. This is the link that they submitted and it's validating. It's going through the bug versus user error submission that they put in and this is where it starts actually grading. So these are the rubrics and stuff that the the hiring managers and the team has put together and it's kind of running through all of these things grading on creativity like creative reasoning, like giving summaries of this, grading on business context and keeps going through a bunch of these like technical context and gives like a final score on here.

**[11:01](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=661s)** This is the ChatGPT conversation that they have. It pulls the transcript, it you know goes through that um uses AI you know to generate like a final assessment here, builds a feedback summary, final rounded score, adjustments and then this is the parts where it's actually pushing into Ashby. So flagging that we need human review here, that it's moved to like grading incomplete if there's an issue and posts the actual feedback form and starts tagging. So you can kind of see like the whole like water flow you know workflow here.

**[11:31](https://www.youtube.com/watch?v=BxL-h9Q29YY&t=691s)** Awesome.

