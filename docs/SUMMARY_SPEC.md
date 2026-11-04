# Episode summary spec (tier-2 "Actionable summary")

## What this is for, read this first

Jamie runs The Rec Lab, helping recruiting teams get value out of AI through
workshops, content and hands-on client builds. This library is his working
memory: 1,600 podcast episodes, newsletters and reports, stored so he can ask
questions across all of them months later.

**The reader of a summary is never someone who listened to the episode.** It is
Jamie, or an AI searching on his behalf, six months from now, asking something
like "what do I know about community-led business development" or "how are
teams actually measuring quality of hire" while building a workshop, writing a
post, or advising a client.

So the job is not to describe an episode. It is to leave behind the parts that
someone could USE, in a form they can use them in.

**The test for every line: would this help someone who searched for this topic
and has never heard the episode?**

## What you are given

One transcript file. Near the top is a "## Episode description", which is
marketing copy. Below it is the real transcript, the timecoded text of what was
actually said. The description is not a source. The transcript is.

## What you produce

One summary block at the very top of that same file, above the `# ` title,
wrapped in `<!--SUMMARY-->` / `<!--/SUMMARY-->` markers so it is invisible when
rendered and trivial to strip out. Roughly 250 to 450 words. Format below.

Extract it later with `sed -n '/<!--SUMMARY-->/,/<!--\/SUMMARY-->/p' <file>`.

## Specific is not the same as useful

This is the mistake to avoid, and it is easy to make.

"Sam and Ulli hit £298,000 of revenue on £2,000 a month of overheads from
Munich" is specific. It is also useless to almost everyone, because it is a fact
about their business.

"Fund your first year by having one founder take an embedded TA contract at
around 30 hours a week, which covers overheads while the other builds without
sales pressure" is the same moment, written as something a reader could run.

**Write the play, not the biography.** Keep the number, because the number is
what makes it credible and searchable. Lose the assumption that the reader cares
who did it. Name the person only when their identity is the point, for example
when a claim only carries weight because of who is making it.

A useful test: could someone in a different country, at a different size of
company, do a version of this? If not, it is trivia, and trivia does not earn a
line.

## How to write one: two steps, and both are required

Measured on the same episode, same model, 27 August 2026:

**Writing it in one pass** gives you "document your best practices in
playbooks". True, useless, could have been written without the episode. About 4
blocks in 10 were usable.

**Collecting quotes first, then writing** gives you specifics, but they come out
as biography: what these people did, in their company, in their city. Honest and
accurate, but a reader in a different situation gets nothing from it.

**Knowing who reads it, without the quote step**, gives you genuinely useful
plays and also invents things. On that test it produced a "3x engagement" figure
that appears nowhere in the transcript, and reported next year's £500k target as
revenue already achieved. Pushing for useful is exactly when things get made up.

So do both, in this order.

### Step 1: gather the evidence

Read the whole transcript. Collect the 10 to 12 most specific moments: a number,
a price, a named tool, an exact phrase, or a step-by-step account of how someone
did something. Write each as a short verbatim quote plus a line of context.

Skip general opinions and anything most recruiters already agree with. You are
hunting for what only this episode contains.

### Step 2: turn each one into something a stranger could use

Now write the block, using only what is on that list. For each play, ask what
someone in a different country at a different size of company could actually do,
and write that. Keep the number, because the number makes it credible and
searchable. Drop the names unless the name is the point.

### The rule that keeps step 2 honest

**Every figure and claim must trace back to a quote from step 1.** If you find
yourself adding a statistic to make a play land, or rounding a target up into an
achievement, stop. That is the exact moment errors enter.

Generalising the METHOD is right: "a WhatsApp group, Slack workspace or
membership site" when they used WhatsApp. Generalising the FACTS is not: a
target is not a result, and a number nobody said does not exist.

## The block format (omit any section that genuinely has no content)

Two notes before the format:

**Host-only episodes use `**Host:**` instead of `**Guest:**`.** Panels, roundups
and solo episodes have no guest, so name the host and show instead. One or the
other is always present.

**No em or en dashes in your own prose.** The one exception is inside a verbatim
quote: never alter a quote to remove a dash, because an accurate quote matters
more than the punctuation rule.

```
<!--SUMMARY-->
## Actionable summary
**Guest:** <name, role, company, plus a few words on why they're worth listening to>  ·  **Show:** <show>, <DD Mon YYYY>
**Tags:** <the episode's tags, copied from episode_summaries.tsv field 4>

**When to use this:** <one sentence naming the specific problem or situation this episode helps with, e.g. "your outbound is getting ignored" or "a hiring manager's brief is unrealistic">

**Big idea:** <the core thesis in one standalone sentence>

**Frameworks & plays:**
- <the actual method, WITH the worked example, exact step, or number behind it, not just the takeaway; a play you could run, not a principle you already know>
- <3-7 bullets>

**Data & benchmarks:** <omit if none>
- <exact numbers, rates, benchmarks, market sizes, pricing, each with its context>

**Tools & prompts:** <omit if none>
- <named tool and exactly how it is used; include the guest's actual prompt or Boolean wording verbatim where they gave it>

**Contrarian take:** <omit if none>
- <the counterintuitive claim or myth the episode busts, attributed to who said it>

**Steal this (do tomorrow):**
- <1-3 concrete actions a recruiter could apply on their next role>
<!--/SUMMARY-->
```

## How it's written (the rules)

1. Complete, STANDALONE sentences. Each line makes full sense on its own and reads like a person wrote it.
2. NEVER use em dashes or en dashes (— or –) anywhere. No fragment-stacking, no "colon-then-list", no three ideas crammed together with semicolons or parentheses.
3. Every claim carries a SPECIFIC: a number, a named tool, a step, a worked example, or a quote. If a sentence could apply to any episode, cut it.
4. Only what is ACTUALLY said. Never invent. Turn the dial up as far as the guest went and no further; if they stayed abstract, capture the method rather than faking a worked example.
5. British English, and attribute the sharp or contrarian lines to who said them.
6. Aim ~250-450 words. Longer is fine when the episode is genuinely dense with specifics; shorter (and drop empty sections) when it isn't.

Net test: someone who never heard the episode could act on it, and someone who did would say "yes, that's the useful bit."

## Applies to
Every podcast transcript in `library/podcasts`, `library/tech` and `library/adhoc`. Skip pure trailers, teasers and previews. Newsletters and reports use their own shorter format and do not get one of these blocks.
