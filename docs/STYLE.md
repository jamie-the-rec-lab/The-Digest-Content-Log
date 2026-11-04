# STYLE: how the digest is written

This file is the single source of truth for the words. If anything else
disagrees with it, including the comment at the top of the template, this file
wins.

It covers HOW things are written. Which items get picked is `SELECTION.md`.
How the page is built and published is `PUBLISH.md`.

---

## 1. Voice

Write like a sharp, warm colleague. Not a model, not a thought leader.

**Banned words.** These are the giveaways that AI wrote it:
delve, leverage, harness, landscape, dive deep, seamless, unlock, empower,
robust, crucial, pivotal, realm, tapestry, testament, navigate, foster, and
filler like "it's worth noting".

**Banned tics.** These creep in even when the banned words are gone:
"quietly", "leans into", "a reckoning", "stacking up", "hollowing out", "a rare
bit of", and the "not X, but Y" seesaw.

**Banned shapes.** The giveaways are often structural rather than vocabulary,
and these four are the ones that show up in a digest:

- **The rule of three.** "Practical, useful and actionable." Three adjectives
  where one would do. Pick the one that carries meaning and cut the others.
- **The closing summary sentence.** A final line that restates the paragraph
  without adding anything. Delete it. The bullet ends on its last real point.
- **Vague attribution.** "Industry reports suggest", "experts say", "research
  shows". Name the report, the person or the number, or drop the claim.
- **Importance claiming.** "Marks a significant shift", "a major development".
  Show why it matters instead of asserting that it does.

**If a phrase sounds like AI wrote it, rewrite it plainer.** Say it the way you
would say it out loud to a smart colleague.

**Reference:** Wikipedia's AI Cleanup team maintain a thorough list at
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing. Worth reading when
refreshing the lists above. Do NOT have the weekly job fetch it: it runs to
about 15,000 words and most of it is about encyclopedia articles.

**British English.** Spelling throughout. But avoid UK-only shorthand that will
not travel, because the list is UK, US and Europe. See `READER.md`.

**Never an em dash or an en dash.** Use a comma, or restructure the sentence.
The only exception is the page title in the head, which keeps its dash.

**Write for a recruiting professional, not an engineer.** That is the line, and
it is about which vocabulary the reader already owns.

- **Recruiting language needs no explanation.** ATS, CRM, req, sourcing, silver
  medallist, time to hire, boolean, TA ops. They live in this world. Do not
  talk down to them.
- **AI language that has crossed over is fine too.** Prompt, agent, model,
  automation, workflow, MCP. They have been using these tools for a while.
- **Engineering language is where it breaks.** API, endpoint, webhook, repo,
  vector database, RAG, fine-tuning, inference, deployment, schema. If a word
  belongs to someone who writes code for a living, either say the same thing in
  plain English or explain it in one clause.

> BAD: "Hit the Greenhouse API from a webhook to sync your scorecards."
> GOOD: "Connect it to Greenhouse so scorecards sync across on their own."

The test is not "is this word technical", it is "would a recruiter use this word
in a meeting".

---

## 2. The bullets

This is the value of the digest. Everything else is packaging.

**Three bullets per item by default.** Aim for exactly three. Drop to two only
when the source genuinely cannot support a third real, distinct insight. Never
pad and never invent to reach three.

A grouped vendor launch block is the exception: one bullet per release.

Every bullet carries an actual practical insight. A specific tactic, a number, a
framework, a named tool, or a sharp claim the reader could act on or quote. Not
a description of what the episode was about.

### The bullets are a way in, not a replacement

Three bullets should do two things at once: give the reader something usable
without leaving the page, and leave them able to decide whether the source itself
is worth their time. See `READER.md`.

Give the sharpest thing in the piece, and make it clear that this is the KIND of
thing behind the link. The reader should finish an item knowing what they would
be clicking into and roughly what more is there.

Two ways to get this wrong:

- **Over-summarised.** The bullets say everything the source says, so there is no
  reason to click. Usually a sign the item was thin and should not have run.
- **Under-sold.** The bullets are so compressed the reader cannot tell what they
  would get. They skip something good.

**This is not permission to hold detail back.** Rule 2 below still stands: no
teasing. A vague bullet is not a snippet, it is just a worse bullet. The way to
make someone click is a bullet so specific they want the rest, never one so
guarded they have to click to find out what you meant.

### The seven hard rules

**1. Lead with the specific.** Open on the number, the named tool or the tactic.
No wind-up clause.

> BAD: "Zapier's framework for assessing AI fluency."
> GOOD: "Zapier tests whether candidates reach for AI unprompted in a live task,
> because asking 'how would you use AI here?' is too easy to fake."

**2. No teasing.** Name the payload or drop the bullet.

> BAD: "The research names the two areas where TA teams most consistently
> struggle before adding AI."
> GOOD: "The two things teams botch most are intake alignment and structured
> scoring, so fix those before adding AI."

**3. Be as specific as the source allows.** Use the real figure or named tool
when there is one. A bullet with no number can still stay if it carries a real
specific insight. Do not drop a bullet just for lacking a stat.

> BAD: "How AI agents change sourcing, nurture and pipeline."
> GOOD: "Talent CRMs now re-engage your past silver medallists automatically,
> instead of sitting there waiting to be searched."

**4. One idea per bullet.** If you are joining two thoughts with "and" or
"plus", split them or drop the weaker one.

> BAD (40 words, three ideas): "'Selfish software' means building for the
> problems you touch daily, and Nguyen built a recruiting-benchmark MCP solo
> plus an enriched, searchable map of his own network that he queries to win
> exec debates."
> GOOD (split, one idea each): "Nguyen built his own recruiting benchmark tool
> solo, for the problems he hits every day." / "He turned his contacts into a
> searchable database he queries to win exec debates with data."

**5. Keep it short and plain.** 15 to 35 words. Read-aloud test: if you would
run out of breath saying it, it is two bullets.

**6. No ambiguity.** A first-time reader must never guess what a word points to.
Replace vague pronouns with the actual noun.

> BAD: "Nguyen built a benchmark tool and a map of his network, then queries
> them to win exec debates." (queries which one? how?)
> GOOD: "Nguyen built a searchable database of his own contacts, and searches it
> for evidence to win exec debates."

**7. Every bullet works on a blank page.** Imagine the bullet written on its own,
with nothing around it. No title, no guest line, no other bullets, no digest.
Read as a single sentence, does it still make complete sense?

That is the bar. It means naming the subject rather than pointing at it, and
saying the whole thought rather than half of it.

> BAD: "He also warns the same approach falls apart once you pass 50 hires a
> year." (who? which approach?)
> GOOD: "Structured scorecards fall apart past about 50 hires a year, so build
> for the volume you will have, not the one you have now."

> BAD: "This is why most teams get it wrong."
> GOOD: "Most teams write the job advert before agreeing what good looks like,
> which is why the shortlist argument happens at offer stage."

No bullet opens with "he also", "this means", or "the second point is". If a
bullet needs the one above it to make sense, the two are really one thought and
should be rewritten as one bullet, or the weaker one dropped.

### Numbers

**Cite the source's number as the source gives it. Never convert it, never
recalculate it, never round it into something the source did not say.**

If a UK report says £45,000, write £45,000. If a US survey says $60,000, write
$60,000. Two items in the same issue can carry different currencies and that is
correct, because each is reporting its own market. A converted figure is a
figure the source never published, and it cannot be fact-checked.

The same applies to percentages, time periods and sample sizes. Use what the
source says. If it says "down for a 45th consecutive month", do not turn that
into "nearly four years".

Always name the market the number belongs to. See `READER.md`.

### Launches are not press releases

Launch bullets come from the vendor's own release notes, which are written to
sell. Rewrite them lightly and their sales language comes with it.

**Say what the thing actually does and who it helps, in plain words. Never the
vendor's adjectives.** Powerful, seamless, revolutionary, game-changing,
next-generation, supercharged and cutting-edge do not appear in the digest.

> THEIRS: "Ashby unveils powerful new AI-driven scorecard capabilities to
> supercharge your interview process."
> OURS: "Ashby now drafts the interview scorecard from the job intake, so the
> questions match what you agreed with the hiring manager."

If you cannot work out what a release actually does from its announcement, that
is a reason to leave it out, not a reason to repeat the vendor's description of
it.

### Do not repeat a framing

Across the whole issue, no two items should open the same way or lean on the
same phrase. If three items touch AI in interviews, they get three different
angles, not three variations of the same sentence.

Read the finished bullets top to bottom before publishing. If a phrase or a
sentence shape appears twice, rewrite one of them. This is what makes an issue
feel written rather than assembled.

### Where the errors actually come from

Worth knowing before writing a single bullet. On 27 August a full digest was
fact-checked and came back with 16 mismatches across 17 items. The helpers'
quote-backed facts were accurate. **Every error was introduced while polishing
those facts into bullets.**

Three patterns, all of which read perfectly well:

- **Invented causation.** "Half of hires come through referrals, which is the
  main reason a small team can absorb 20 hires a week." Nobody said the second
  half.
- **A number tightened until it broke.** "Filled within a week", when the source
  said within a week of a two month target.
- **An editorial flourish.** "The first serious route to asking your ATS
  questions in plain English." Nobody said "first".

None of these would be caught by rereading. Only checking against the source
finds them. So when a bullet feels like it needs one more clause to land, that
clause is exactly where the error will be.

### Never

Never invent a statistic, a tactic or a claim. If the source does not support
it, it does not go in. Everything is checked against the source before
publishing.

---

## 3. This week in the world of recruiting

A short preview that sits above the standouts, roughly 50 to 110 words, under
the label "This week in the world of recruiting".

**What it is:** a taste of the TOPICS this week, written to make someone want to
read on. It is not a list of the standouts and not a headline-by-headline
recap. Group several items under one theme where they share one.

**The shape is fixed: recruiting first, general AI last.**

Everything with a recruiting angle goes first, grouped together, in two or three
sentences. The hiring market, what is changing for recruiters, what the reports
say, what the newsletters are arguing about, **and any AI story whose subject is
a recruiting team**.

That exception is narrow on purpose. It covers stories about recruiters doing
something: SpaceX's head of recruiting running a sourcing agent is a recruiting
story, because the story is about a recruiting team. It does NOT cover a general
AI release that a recruiter could point at. A new model that can drive software
is a general AI story even when one of its example tasks is updating a CRM, and
it belongs in the closing sentence.

The test: **would this still be a story if no recruiter ever used it?** If yes,
it is general AI. If the recruiting team IS the story, it goes up top. Read the
exception any wider and everything qualifies, the closing sentence never has
anything left in it, and the split stops meaning anything.

Then ONE closing sentence for the AI that has NO recruiting angle at all,
opening "And in the world of AI, ". General model releases, how other companies
are building with AI, the tech shows' non-hiring material.

**The split is by SUBJECT, not by section.** This is the part that is easy to get
wrong. An item can sit in Section 4 and still belong in the recruiting sentences,
because the sections sort content by type and the preview sorts it by what the
reader cares about. Ask "is this about hiring, recruiters or talent teams?" and
let the answer decide, no matter which section the item ended up in.

If the closing sentence would only repeat a recruiting point in AI clothing,
drop it.

> UK permanent hiring rose for the first time since 2022, only just. Entry level
> hiring bars are jumping a step, now junior staff must judge AI output the way a
> manager once judged a task, and a polished CV stops proving much once every
> application is AI-assisted. Camunda's five minute recruiting kickoff and
> SpaceX's always-on sourcing agent show what real workflow builds look like. And
> in the world of AI, OpenAI's new GPT-6 Astra can now fill in forms and update
> records for you, while Stripe runs an in-house AI assistant for 10,000 staff a
> week on a team of under ten.

Note where the two AI-side items landed. SpaceX went up top, because the story is
a recruiting team running a sourcing agent. GPT-6 Astra stayed in the closing
sentence, because a model launch is a model launch whoever ends up using it, and
the CRM angle is a use case rather than the subject. Both sit in Section 4 of the
digest itself. The section and the sentence are answering different questions.

If a week has no non-recruiting AI material at all, drop the closing sentence
rather than padding it. If a week has nothing but AI material, the preview has
not earned its place: see "Earn it or drop it" below.

**Every point must stand alone.** Each thing it names has to make sense on its
own, without reading the rest of the digest to decode it.

> BAD: "Brussels pushing back its AI hiring deadline." (deadline for what?)
> GOOD: "the EU delaying its new rules for AI in hiring"

**Name things.** The concrete noun beats the vague umbrella. Name the actual
tools, the actual skills, what the data actually shows.

> BAD: "fresh jobs data, new tools that plug your ATS into AI"
> GOOD: "UK permanent hiring steadying after a 45 month decline while US
> openings run ahead of hires, and new releases from Greenhouse and Juicebox
> that plug your recruiting tools into ChatGPT and Claude"

**Grounded, never invented.** Every topic it names must actually appear in this
week's items. It describes the week's content, it never adds new facts.

**Keep it simple.** Short, punchy sentences someone skims in seconds. This is
where AI tells show up most, so keep it plain.

**Earn it or drop it.** If the week is too scattered to preview honestly, delete
both the label and the preview and leave just the standouts heading. A forced,
vague preview is worse than none.

---

## 4. Standout rows

The heading is exactly **"Standout content from this week"**. Never reword it.

Up to five rows, always in this order: **Podcast, Newsletter, Report, Launch,
AI pick.** Which item fills each slot, and when a row gets dropped, is in
`SELECTION.md`. This section is only about how the row reads.

**Each row is 25 to 50 words**, item name and reason together. Not a bare
one-liner, not a paragraph.

**The reason must carry a hard specific plus a "so what".** A real number, a
named tool or a concrete tactic, and something the reader can act on or feel.
Never a topic label, never a truism.

> BAD: "the real barrier to AI is adoption, not the tools"
> GOOD: "point your first AI agents at low-risk admin tasks where 'done' is
> obvious, the Uber playbook that sticks"

Every standout is a different item. Same voice rules as everything else.

---

## 5. Names and labels

**The four section labels**, used exactly as written, never reworded:

1. Recruiting Podcasts
2. Recruiting Newsletters
3. Recruiting reports, product updates, and more
4. AI & Tech Picks

**Display names.** Two sources are called one thing in the library and another
on the page. Readers always see the display name. The library name is only ever
used for remembering what has been featured.

| Library | On the page |
|---|---|
| PromptMates | PromptMates Live |
| RecOps Collective | RecOps Roundup |

**Brand credits.** Some shows are produced by a notable brand, and the credit
appears after the show name in a muted style. Only these:

| Show | Credit |
|---|---|
| 10x Recruiting | by Metaview |
| Offer Accepted | by Ashby |
| Recruiting Roadshow | by Greenhouse |
| How I AI | by Lenny's Podcast |
| AI & I | by Every |

Everything else stays plain. PromptMates Live is its own brand and gets no
credit. Nor do Brainfood, Recruiting Future, The Debrief, Building the Talent
Machine, Lenny's Podcast or AI For Humans.

**Guest lines** (podcasts and tech picks only):

> Name · Title @ Company

An @ between the job title and the company, not a comma. For example
"Jackson Lynch · Founder @ Talent Sherpa".

Taken from the episode description only. Omit it entirely for panel shows and
host-only episodes. The Debrief is a panel show, so it only gets a guest line
when the description names someone.

**Titles.** Strip episode numbers, so "Ep 805:" and "Episode 039:" both go. Trim
a trailing "with <name>". For newsletters, use the issue title only, never
repeated with the newsletter name. Never invent a title.

**Dates on items.** "DD Mon YYYY" when the day is known, "Mon YYYY" when only
the month is. Only if both fail, "Found <run date>".

**The edition line** in the header reads:

> Version 3 (26th August 2026)

The number increments each edition. The date is the Wednesday the job runs,
written out with an ordinal and the full month.

---

## 6. Section three sources

Items in "Recruiting reports, product updates, and more" carry a type after the
source name, so the reader knows what they are looking at:

> Greenhouse · launch &nbsp;&nbsp; REC · report &nbsp;&nbsp; RecOps Roundup · event

Types in use: launch, report, event, essay. The title does not repeat the
source name.

There is no "news" type here any more. AI news and AI regulation items moved to
Section 4 on 10 September 2026. They carry the same `source · news` marker there,
so the reader can tell a headline from an episode at a glance.
