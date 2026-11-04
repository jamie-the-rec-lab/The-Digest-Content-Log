<!--SUMMARY-->
## Actionable summary
**Guest:** Dan, Senior Talent Engineer at Zapier, with Viet, Founder of Talent Collective, hosting  ·  **Show:** PromptMates Live, 14 Sep 2026
**Tags:** building ai tools, claude code, ai job descriptions, candidate experience, recruitment marketing, prompt engineering, recruiter workflow

**When to use this:** you want a candidate outreach asset that is richer than a plain job description, and you want to build it yourself with Claude rather than waiting on design or engineering.

**Big idea:** you can turn a job description into a branded, single-page candidate landing page live in Claude in minutes, then package the whole workflow into a reusable skill so building the next one takes about 60 seconds instead of an hour.

**Frameworks & plays:**
- The working prompt gave Claude two inputs: the job description and a screenshot of an existing company page ("see attached screenshot of Juice Box's website"), instructing it to "lift the visual design system from this, colors, typography, spacing, layout style, overall vibe" and open with "a strong hook based on the role's value prop."
- Iteration happens in plain language: after the first draft, the ask was simply "let's add a kind of meet the team section," and Claude added it with photo placeholders and instructions for dropping in real images.
- Once the page is right, the same session is used to "turn this whole workflow uh into a reusable skill" that accepts the same inputs (JD, design reference) so any future role reuses the build rather than starting over.
- Model choice is a cost lever: Dan used Opus for the demo, but the advice for everyday use is "use Sonnet 46... you don't need incredibly high processing power," and to crop screenshots tightly rather than capturing whole pages to save tokens.

**Tools & prompts:**
- Claude (used live), fed a job description plus a design-reference screenshot, with the explicit instruction to extract "colors, typography, spacing, layout style, overall vibe" from the reference image.

**Steal this (do tomorrow):**
- Build one candidate landing page from your next open role's JD plus a screenshot of your careers page as the design reference, then ask Claude to package that prompt into a reusable skill so you can repeat it for future roles in under a minute.
<!--/SUMMARY-->

# Build A Candidate Landing Page With Claude (Live Talent Engineering)

- **Podcast:** PromptMates
- **Channel:** PromptMates
- **Date:** 2026-09-14
- **Duration:** 8:15
- **URL:** https://www.youtube.com/watch?v=C3TOnYRcjvg
- **Fetched:** 2026-09-16

## Episode description

How do you turn a job description into a candidate landing page in minutes? Viet and Dan build one live in Claude, then package the whole workflow into a reusable skill

📌 Timestamps
00:00 - Building a candidate landing page from a JD
02:26 - Sonnet vs Opus
04:15 - Iterating with feedback
05:57 - Turning it into a reusable Claude Skill

Viet is Founder of Talent Collective and Dan is Sr Talent Engineer at Zapier, and together they show what talent engineering looks like in practice by building a candidate landing page live in Claude, then turning it into a reusable skill for any role

This clip is from the PromptMates Live Show, where talent and people leaders share what they're actually building with AI

🔗 Join the PromptMates community: https://www.promptmates.ai/community
📧 Weekly newsletter: https://www.promptmates.ai/newsletter
🎙️ Catch the next live show: https://luma.com/promptmateslive

#TalentEngineering #AIRecruiting #ClaudeSkills #Zapier

## Transcript

Each paragraph starts with a timecode linking to that moment on YouTube.

**[0:00](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=0s)** Me and Dan were thinking like, what's one thing that anybody who wants to could go build and that would actually be useful. And so, what we decided to do was we wanted to build a candidate landing page based on a job description. Let's say I'm hiring for a forward deployment engineer at a company and I want them to have this landing page that just isn't a job description. It basically shows the job description, some additional context with the role that may not be on the JD, etc. And it is something that you can just use as like part of your outreach. So, what we're going to >> you get? Okay, let's walk through it. We're going to build a landing page. All I'm going to do is have Claude open in my Claude brain folder. I'm going to paste my prompt.

**[0:38](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=38s)** I'll share what that looks like right here just so you can see it, but I want to build a candidate landing page for the role I'm hiring for. It's going to take two inputs, job description. See attached Juice Box candidate recruiter and then a design reference, see attached screenshot of Juice Box's website. Lift the visual design system from this, colors, typography, spacing, layout style, overall vibe. And then we're going to build a single page candidate facing landing page that opens with a strong hook based on the role's value prop. >> All Dan's doing is explaining what he wants. And I think over time you start to understand like what is it that you want? No one knows what they want until they see the thing that they don't want.

**[1:13](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=73s)** And then so you iterate on sort of what you want and then it's like you start to get better at sort of prompting just purely just by practicing. Um I bet most people here have wholly abused ChatGPT and have sort of gone down have asked like one too many questions like, man, if I just asked this question correctly the first time I would have gotten this answer faster. And it's the same idea with prompt was sort of like prompting with with like building applications. >> 100% and I mean even the way this prompt is built out. Okay, I have my sort of TLDR here. I have the inputs that it's going to have. I have more of the specifics uh of what it's going to look like and then the kind of output that it's going to be. And so, all that is simply what I've pasted here and I'm just going to hit enter.

**[1:53](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=113s)** And Claude is going to do its thing. It's also going to let me know that it well, probably will let me know that I don't have the job description or the design reference yet. Yeah. So, what I'm going to do is come over here and I'm just going to select all, paste the JD in. We're going to come to our example page here. I'm simply going to just screenshot the whole thing. Just going to drop that in there. I don't need to give it any specific information because it's asked those two things. >> Well, again, Dan's using Opus 47, which is one of the models. It's way overkill for what we're doing here. You can use Sonnet, which is like cheaper. If your engineering team is like, "Yo, you can't be using all these tokens." Don't feel like you need to use like the most complex like model.

**[2:42](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=162s)** Joe Joe's using Opus 47 for everything. >> Yeah, use Sonnet 46. Like especially if you're if you're doing it yourself, like if you're paying for, you know, cloud subscription or something like that, you know, don't uh you don't need incredibly high processing power. I could probably turn it I could probably change it if I wanted to here, but I'll just leave it at the default for now. >> Yeah, the other token trick, too, is you notice when Dan grabbed the entire screen of Juice Box. Like when I'm super token cheap, like I don't even grab the white on the outside because it's like I'm not going to spend my my my my pocket full of tokens on having it understand the outside, but you know, when you're when you're running it 47 for demos, you can do whatever the hell you want.

**[3:23](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=203s)** >> I've also I've said this in the past >> when we I actually did the previous uh prompt made session, is like whatever Claude or whatever system you're using is generating, read read everything. Like read and try to understand like what it's doing cuz that's that's actually going to what's going to help you sort of understand like what it's doing, why it's doing it, etc. I wouldn't say ignore it and sort of like anything blindly sort of like sort of go through it. This is also the downside of using uh Opus is like when you're using sort of a like a beefier model like Opus, it it's smarter but also slower. And so like if you're using a sort of a everyday model like Sonnet or GPT or what's in Gemini's what's Gemini's I forgot but like if you're using sort of a sort of standard day-to-day model, they should they will run faster and they're going to usually get the work done. They just like don't have as much like they can't handle as much complexity.

**[4:13](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=253s)** >> Cool, looks like it's done done. I think it just needs easy Cool. So this is the page it just created. This is the HTML file. So I mean all things considered I think hey that's uh you know, pretty close to the style. It's giving us what we asked for kind of a hook. You can apply for the role here. All the information, everything's around. So it's like okay cool this is this is pretty great. But now we want to add a little bit it's like okay cool well let's add a you know, that that looks good but let's add a kind of meet the team section. So let's just copy this prompt. And I'll paste it in. >> Yeah, before you run this >> >> Nevermind. I was going to say do you want to switch models just so it runs a bit faster?

**[5:02](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=302s)** >> The I mean it it should go faster now that the >> That's true. Now that this is the first the first build always takes a while cuz I sort of has to build all the dependencies and like folder architecture etc. etc. So that makes sense. >> And so here we have it is now added the meet the team section. So it's put placeholders like we mentioned in the prompt but we could easily add photos. It tells me how to do it here but honestly if I wanted to actually just add them I would probably just drop the photos in here and have Claude do it. But if we are being sort of more token minded you can absolutely do that without Claude and it can kind of walk you through the steps like here. >> So yeah, I mean I think the the goal of this again is just a show of like how easy it is. Like all Dan did here is if you open your Google Doc Dan is just basically write out like what Dan wants.

**[5:48](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=348s)** And then just like write out, throw it in the cloud, have it generate whatever, and you'd be surprised like what it can do with like actually not like very much information. >> Yeah, and and you know, and if there's stuff you don't like, just tell it. Be like, "Hey, you know what? This is actually too long. Can we condense it? Can we, you know, you can certainly have it do a lot of stuff." But in the interest of time, we'll skip step three. We'll move right to the final step that we had for this. But so this is great. Just say you you're super happy with this and say like, "Hey, this is awesome." You know, maybe you've iterated over the past 30 minutes and you built something that's like great.

**[6:17](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=377s)** And you're like, "Okay, this is awesome, man. But like I need to do this for like 10 other roles that I'm going to hire for. Um And so with Claude or with on any of this stuff, you can turn it into a skill. So now let's make this repeatable. We want to turn this whole workflow uh into a reusable skill. Um so I'm actually just going to paste this in right now. And then I can kind of keep reading through it. >> >> Um but we want the skill to be invocable and call it code. We want it to accept three inputs. We want it to run through everything built. Uh that's what we're going to be a little confused with this piece because we did this earlier when we were running through it. The skill does already exist, so it won't have to do too much more. But what's going to happen is this is going to now create everything that we did, and it's going to build this into a reusable skill. And skills are when you start to really save time because it's not I mean, yeah, it's great to be able to build a page, but you know, if it takes you an hour, that's a good amount of time to invest in it. But if you can then take that, package it up into one sort of repeatable command, and now it's going to take you probably

**[7:17](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=437s)** 60 seconds from here on out to do this with any other role that you want to do. And so that's what Claude's doing right now. It's actually editing the skill that I previously built. And if, you know, for today, obviously this is we're not hosting this on the internet. This is hosted locally, so it's on my computer, so I can't just, you know, send candidates to this link. But we wanted to just make sure we could get it built. So as a takeaway, take this like markdown file, add a job description, and then it should be able to generate sort of like whatever landing page you want. And then any and he asked like what's the point of a landing page? Is so that you like whatever use case you need. For me, I would actually put this in my outreach.

**[7:52](https://www.youtube.com/watch?v=C3TOnYRcjvg&t=472s)** It is a more interactive way to get information to candidates outside of just like a job description, etc. And so, right now it's like pretty like it's pretty close to job description, so that's why maybe the value is not as clear. But sort of as you start to like sort of build more features within sort of landing page, it becomes more evident that like oh, this is actually a complete this is a way better experience than sort of just a job description that you're sort of uh you're adding to outreach message.

