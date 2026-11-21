# Data record: what personal data TheRecLab holds, and why

One page, kept up to date. It is the record of processing a small business is
expected to keep, and the place to look when someone asks "what do you hold
about me?". It holds no personal data itself.

- **Who is responsible:** Jamie Jay Lyons, sole trader, trading as TheRecLab,
  International House, 64 Nile Street, London, N1 7SR. Contact: jamie@thereclab.ai
- **Public notice:** https://thereclab.ai/privacy (keep the two in step: if this
  page changes, check whether the privacy policy must change too, and the other
  way round)
- **Last reviewed:** 21 November 2026. Review once a year, and whenever a tool
  that touches personal data is added, changed or dropped.

## What is held

| What | Whose | Why | Legal basis | Where it lives | How long |
|---|---|---|---|---|---|
| Email address, sign-up date, subscribed or unsubscribed | Digest subscribers | Send the weekly digest and welcome email | Consent, given at the sign-up form | Resend (stored in the US) | Until they unsubscribe; then kept as "unsubscribed" so they are not emailed again; deleted on request |
| Delivery, bounce, open and click records (clicks include IP address and browser) | Digest subscribers | Keep the list working; see which editions and items are read | Legitimate interests. Open and click tracking is on at Jamie's decision (see below) | Resend | About 30 days in Resend's logs; edition totals only in `digest/email-metrics.json` |
| Email address in a signed confirmation link | People who unsubscribed and are entered in the form again | Let them confirm before being re-subscribed | Legitimate interests | In the link itself and Resend's send log; nothing stored by the site | Link works for 48 hours |
| IP address, browser details | Website visitors | Deliver the pages, keep the site secure | Legitimate interests | Vercel and Cloudflare logs | About a day in the logs we can see; the hosts keep their own for their own periods |
| Emails people send | Anyone who writes in | Reply and deal with the request | Legitimate interests | Google Workspace mailbox | As long as needed for the request |
| Name and email when booking a call | People who book | Arrange and hold the meeting | Legitimate interests | Google Calendar | With the calendar entry |
| Contact details, notes, invoices | Clients and workshop attendees | Deliver the work, get paid, keep accounts | Contract; legal obligation for accounts | Google Workspace, accounting records | About six years (tax rules) |
| Name, role, employer, photo, quote | People giving testimonials | Show on the home page | Their permission | The website repo and live site | Until they ask for a change or removal |
| Name, role, employer, what they said in public | People named in the digest and its sources | Report what is said in public about recruiting | Legitimate interests | This repo (`library/`, `digest/`) on GitHub, and the live digest page | Kept as an archive; corrected or removed from the site and future editions on request |
| Name and company typed by players, score | CV Invaders players | Public leaderboard | Their choice to submit | Supabase; Vercel analytics counts visits | Until removal is requested |

Not held anywhere: subscriber addresses in either repo, payment card details,
passwords or logins for the public, special category data.

## Who else handles it

| Company | What for | Agreement |
|---|---|---|
| Resend (Plus Five Five, Inc., US) | Subscriber list, sending, open and click tracking | Processor terms accepted with its terms of service |
| Vercel (US), Pro plan | Website hosting, the sign-up function | Processor terms apply on Pro |
| Cloudflare (US) | Domain, DNS, routing traffic | Processor terms in its self-serve agreement |
| Google (Workspace) | Mailbox and calendar | Processor terms in the Workspace agreement |
| Anthropic (Claude, personal Max plan) | AI tools that build the digest; they can read the mailbox and the Resend account | **No processor agreement on a personal plan.** Model training and location metadata switched off in settings, 21 Nov 2026. A Team, Enterprise or API account would add one |
| GitHub | Private storage of this repo and the website | Standard terms; keep subscriber data out of the repos |
| Registered Address Ltd | The published postal address; scans post | Their terms; renews 21 Nov 2027 |

Data leaves the UK for the US with each of the US companies above. Safeguards:
the UK-US data bridge where the company is certified, and standard contractual
clauses in the processor terms.

## Decisions on record

- **Open and click tracking stays on** (Jamie, 21 Nov 2026), disclosed at the
  sign-up form, in the privacy policy, in the welcome email and in a one-off note
  to existing subscribers. UK and EU regulators' guidance is that per-person open
  tracking needs consent first, so this is a known, accepted gap.
- **ICO data protection fee: not registered** (Jamie, 21 Nov 2026). The
  exemption is arguable, not confirmed. Revisit if the list grows, a paid product
  starts, or a complaint arrives.
- **Single opt-in for new sign-ups.** Returning unsubscribers must confirm by
  email. Revisit double opt-in for everyone if junk sign-ups appear.
- **No EU representative, no formal impact assessment.** Judged out of
  proportion for a list this size; revisit with growth.

## If someone asks about their data

Reply within one month, free of charge. Look in: Resend (the contact and its
recent sends), the Gmail mailbox (search their address), and this repo
(`grep -ri "<name>" library/ digest/`) if they are someone named in the digest.
To delete a subscriber, remove the contact in Resend. Note what was asked and
what was done, with the date, in `_state/RUN_LOG.tsv`.

## If someone complains

Acknowledge within 30 days, look into it, and tell them the outcome. They can
also go to the ICO: https://ico.org.uk/make-a-complaint/ . Log it as above.

## If something goes wrong (a breach)

Examples: the Resend, Google, Vercel, Cloudflare or GitHub account is accessed
by someone else; the subscriber list is sent or exposed somewhere it should not
be; an email goes to the wrong list.

1. Stop it: change the password, revoke API keys, remove the exposed copy.
2. Write down what happened, when it was found, whose data and how many people.
3. If people could be harmed by it, report to the ICO within 72 hours of
   finding out (https://ico.org.uk/for-organisations/report-a-breach/), and tell
   the people affected if the risk to them is high.
4. Log it in `_state/RUN_LOG.tsv` either way, including the reason if it was
   not reported.

## Keeping accounts safe

Two-step sign-in on every account that can reach this data: Google, Resend,
Vercel, Cloudflare, GitHub, Registered Address and Claude. A password manager.
API keys with the least access they need, and never in a file.
