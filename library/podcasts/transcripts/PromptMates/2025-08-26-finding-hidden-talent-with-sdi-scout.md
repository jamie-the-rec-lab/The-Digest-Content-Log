<!--SUMMARY-->
## Actionable summary
**Guest:** Host walkthrough of SDI Scout, a free custom GPT built with a community of talent leaders.  ·  **Show:** PromptMates, 26 Aug 2025
**Tags:** building ai tools, custom gpts, ai sourcing, ai market research, sourcing, talent mapping, recruiter workflow, talent intelligence

**When to use this:** Reach for this when you have one role you cannot fill and need a target-company and Boolean battle card fast.

**Big idea:** Paste any job description into SDI Scout, which stands for Skills Density Index, and it becomes a sourcing battle card of where to look, which titles to chase, which companies hold the highest talent density, plus copy-paste Boolean.

**Frameworks & plays:**
- Feed in a JD, kickoff notes or role details and the GPT searches for other roles with the same skills, then ranks companies and titles by where that talent concentrates.
- Read the two-part output, where the top half is machine JSON that the GPT writes as code to reuse in a multi-tiered GPT-5 setup, and the bottom half is the human battle card with SDI scores, Boolean strings, tips on where to look first, and competitive positioning against named rivals.
- Take the readout straight into a hiring-manager meeting as defensible market intelligence, as the demo positioned Perplexity against Databricks and Snorkel.

**Data & benchmarks:**
- The demo used a live Perplexity req for an AI Software Engineer on the Evaluation Platform, open about a month with only 60-plus applicants, and the GPT thought for about five minutes to generate the battle card.

**Tools & prompts:**
- SDI Scout is a free, open-source custom GPT with links in the video, its Boolean strings drop straight into Google, Bing or LinkedIn Recruiter, and the prompt used was "help [company] find where to look for talent like this" followed by the pasted JD.

**Steal this (do tomorrow):**
- Run your hardest open req through SDI Scout and copy its SDI-ranked target-company list and Boolean into your next sourcing session.
- Bring the human battle card to your next intake meeting as your talent-density evidence.
<!--/SUMMARY-->


# Finding Hidden Talent with SDI Scout

- **Podcast:** PromptMates
- **Channel:** PromptMates
- **Date:** 2025-08-26
- **Duration:** 4:29
- **URL:** https://www.youtube.com/watch?v=xKXELZtNMHE
- **Fetched:** 2026-06-29

## Episode description

Every recruiter has that one role that just won’t close.
SDI Scout was built to fix that.

SDI = Skills Density Index.
This free tool takes any job description, kickoff notes, or role details you feed it… and maps out:

- Where to find talent with those skills
- Which titles to chase
- Which companies have the highest talent density
- Boolean strings you can copy/paste into Google, Bing, or LinkedIn Recruiter
- Competitive positioning you can use with hiring managers

In this video, I walk through how SDI Scout works — using a live req from Perplexity (AI Software Engineer, Evaluation Platform). You’ll see how it generates a “battle card” with both machine logic and human-ready insights that recruiters can actually use in the field.

This is meant to be open-source.
Steal it. Share it. Use it in hiring manager meetings.

👉 Links mentioned in the video:
Try SDI Scout yourself: https://chatgpt.com/g/g-68952a57b4408191852b00e747a3c1f1-sdi-scout
See the full Perplexity example readout:  https://chatgpt.com/share/68ae10a2-8b38-8010-8b1a-068f0ed82ee1

If you’ve got a tough role you want to test it on, drop it in the comments.

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube.

**[0:00](https://www.youtube.com/watch?v=xKXELZtNMHE&t=0s)** Okay, so like I promised about a week ago, I wanted to give away a tool that is specifically designed to help you fill that one or two roles that no matter what you do, you can't find the right person for. Before we get into it though, I just want to give a special thanks and shout out to all the people who gave me feedback on this, told me what they liked, told me what they didn't. This was the result of a community of talent leaders coming together to help me make something better. All right, let's get into it. All right. So, this is what I'm calling SDI Scout. SDI stands for skills density index. And in essence, what it is is a tool where you can take a job description or some kickoff nodes or something about a role that you're looking for, put it in here, and what it's going to do is it's going to go out and search for any other roles that have those same skills, and then rank where to look for folks like that at individual companies. and the titles you should be taking a look at. You know, anybody in talent heard kind of the the shot that went through recruiting about 3 months ago when the Perplexity CEO came out and said that we were all going to be out of jobs. Uh what I figured is

**[1:15](https://www.youtube.com/watch?v=xKXELZtNMHE&t=75s)** while we still got a couple months left, let's see if we can't help Perplexity fill one of their roles using the SDI scout. So just went on here grabbing what looked like to be kind of a tough role. AI software engineer eval platform that's been open for a month. They've only got 60 plus people that have applied. I know a lot of recruiters would kind of kill for only having look through 60 applicants. Can't all be so lucky. Here's their bang up JD. Amazing job wrapping down here. All we got to do is copy this. Go over here to scout and say help Perplexity find where to look for talent like this. And then I'm going to go ahead and paste the job description. Now you'll notice up here it's SDI Scout thinking five.

**[2:07](https://www.youtube.com/watch?v=xKXELZtNMHE&t=127s)** This is going to take a second because thinking is going to take a minute. So we're going to go ahead and let it run and I'm going to come back once it's done. Okay. So you'll see here it thought for about five minutes. I'm just kind of hopping back in. You're going to see the first thing it's going to do is actually going to create a lot of this JSON code. I purposely let it show this. But the neat thing about this is what this is doing is it is actually creating code for itself that with this GPT5, it's going to then go back and reuse. So it's like a multi-tiered custom GPT. I'm going to pause it again and then we'll come back and we'll see the final result. Okay, so get through all the code. For what it's worth, code is actually kind of cool to look at sometimes. Like you'll see, you know, why it suggests certain companies and sort of how it's thinking, but what you really want to get down here is the good stuff. So, first thing comes back as a battle card. See, it's called the human battle card because top part was for the robots, bottom parts for the humans.

**[3:06](https://www.youtube.com/watch?v=xKXELZtNMHE&t=186s)** It's going to list out different places to where to look. Gives you an SDI score. So this is the systems guess at the density of that level of talent at any of these places. In addition to this, it's going to give you some boolean search string options. Like for instance, you can go ahead copy here, go to Google or Bing, like we're old school boolean recruiters. It's going to give you folks that have publicly facing profiles that you can reach out to. if you are still paying for LinkedIn recruiter. Here is the boolean search string there. Some tactical tips, places to look first and then also some competitive positioning for how to sell in this case perplexity against the data bricks here a snorkel etc. I will put a link to the GBT itself up above in the comments. And then just if you want to play around with this output, I'll actually put a link to this uh this SDI scout readout in the first comment. Please use it, steal it, take it into a hiring manager meeting that you're afraid to go to and show them all this amazing work that you've done. I want this to feel as close to open source as possible. So, happy hunting. If anybody's got any questions, hit me up directly or leave a comment.

