# Weekly newsletter send — runbook (human-gated)

The Wednesday job (08:00 UK) publishes the digest to thereclab.ai/digest and
Slacks Jamie a "ready to review" note. **Nothing is emailed automatically.** The
email only goes out to subscribers after Jamie reviews the live site AND a real
test email, and gives a green light in chat.

## The flow

Two approvals, and nothing happens between them without one.

1. **Wednesday 08:00 UK, automatic.** The job refreshes the library, publishes
   the new edition to the website, and posts the Slack health report plus an
   email to jamie@thereclab.ai, both with the live link and a request to review.

   By the time this reaches Jamie, every mechanical check has already passed:
   the fact-check, `final_check.py` and `publish_check.py`. He is never asked to
   spot a missing brand credit or a broken link. The only thing left for him is
   judgement.

2. **Jamie reviews the live page**, any time Wednesday or early Thursday, and
   asks for any edits in chat. Edits are made per `docs/PUBLISH.md`, which
   reruns the checks and republishes.

3. **GATE ONE. On Jamie's green light, Claude sends the TEST email immediately**,
   to jamie@thereclab.ai and jamiejaylyons@gmail.com, without waiting to be
   asked separately. The green light on the page IS the instruction to send the
   test. Then Claude tells him it is in both inboxes and stops.

4. **Jamie reviews the test email** in a real inbox, asks for any final edits,
   which are made on the live page and the test resent.

5. **GATE TWO. Only on his second green light** does the broadcast go to the
   list, scheduled for Thursday 08:00 UK by default.

Neither gate can be skipped or combined. A green light on the page never sends
to subscribers, and no approval that week means no email that week, though the
site still updates.

## Build the email (Claude runs on first green light)
1. Fetch the live page: GitHub `get_file_contents` on
   `jamie-the-rec-lab/thereclab-site` → `digest/index.html`. Save it locally
   (e.g. to the outputs folder) as the source.
2. Build the email from it:
   `python3 scripts/build_email.py <live-index.html> <out_prefix>`
   → writes `<out_prefix>.html` (email-safe, table layout) and `<out_prefix>.txt`.
   The `{{{RESEND_UNSUBSCRIBE_URL}}}` token is already embedded (for the broadcast).
3. Read the built `.html` and `.txt`. Sanity-check: the same number of section
   bars as the live page has (a quiet week drops empty sections, so two or three
   is correct, not a fault), the standouts, the "This week in the world of recruiting" preview if the
   page has one, and the grouped-vendor launch block (if any) showing its
   releases.

## Test send (to Jamie only — do this BEFORE the broadcast)
1. Make a TEST copy of the built HTML/text where the `{{{RESEND_UNSUBSCRIBE_URL}}}`
   token is replaced with `https://thereclab.ai/digest` (a one-off send-email does
   NOT process that broadcast merge tag, so leaving it raw would look broken).
2. Resend MCP `send-email`:
   - from: `TheRecLab Digest <digest@news.thereclab.ai>`
   - to: `["jamie@thereclab.ai", "jamiejaylyons@gmail.com"]`
   - replyTo: `jamie@thereclab.ai`
   - subject: `[TEST] TheRecLab Weekly Digest, Version <N>`
   - html / text: the test copies from step 1
3. Tell Jamie the test is in both inboxes and wait for his OK. If he wants edits,
   apply them to the live page, re-run build_email.py, and re-send the test.

## Broadcast send (to everyone — only after test is approved)
1. Rebuild from the LIVE page if any edits were made since the test (so the
   broadcast always matches what Jamie last approved).
2. Create the broadcast (Resend MCP `create-broadcast`):
   - segmentId: `13a771a9-83e1-4d1d-ae80-a93c41a1c1b6` ("General")
   - from: `TheRecLab Digest <digest@news.thereclab.ai>` (verified domain)
   - replyTo: `jamie@thereclab.ai` (subscriber replies go here; check it shows on the broadcast before scheduling, as Resend can drop it)
   - subject: `TheRecLab Weekly Digest, Version <N>` (match the site's version)
   - previewText: the "This week in the world of recruiting" preview line
   - html / text: the built files (keep the real `{{{RESEND_UNSUBSCRIBE_URL}}}` token)
   - IMPORTANT: pass the `from` with plain `< >` (do NOT HTML-escape to &lt;/&gt;).
3. SCHEDULE it: Resend MCP `send-broadcast` with the returned broadcast ID AND
   `scheduledAt` = the coming Thursday 08:00 Europe/London. Omit `scheduledAt`
   only if Jamie explicitly asks to send now (or the Thursday window has passed
   and he confirms an immediate send).
   - Resend only schedules up to ~72 hours ahead.
4. Confirm back in chat: recipient count AND the scheduled send time
   (or "sent now").

## After the broadcast has gone
Once the send is confirmed, empty both handover files so the next run starts
from nothing:

```
: > "_state/run-report.json"
: > "_state/publish-report.json"
```

They are working files for one run only. Leaving last week's behind risks a
failed gathering phase quietly handing stale material to the next digest. The
permanent records are elsewhere: `digest/published/` for the page,
`digest/featured-log.tsv` for what was used, `_state/RUN_LOG.tsv` for what went wrong.

## Email figures (opens and clicks)

**Tracking is on (since 21 November 2026).** Open and click tracking are enabled
on `news.thereclab.ai` in Resend. Every link in the HTML email is rewritten to
pass through `links.news.thereclab.ai` on its way to the real page. That address
is a CNAME to `links2.resend-dns.com`, held in Cloudflare, where thereclab.ai is
registered and its DNS lives. **The record must stay "DNS only" (grey cloud).**
With Cloudflare's proxy on, or the record deleted, every link in the email
breaks. Editions sent before 21 November (Version 9 and earlier) have no open
or click data.

If links in an email ever fail: switch click tracking off on the domain in
Resend (`update-domain`, `clickTracking: false`), which stops the rewriting for
anything sent afterwards, then check the Cloudflare record.

**The figures live in `digest/email-metrics.json`**, one entry per edition:
version, broadcast id, the date it was sent, sent, delivered, bounced,
unsubscribed, unique opens, unique clicks, whether it was tracked, and the top
clicked links. `scripts/health_report.py` reads that file and prints the last
four editions. The script never talks to Resend itself.

**Filling it in.** Read-only, with exactly these three Resend tools:

1. `list-broadcasts`: find the digest broadcasts and their sent dates.
2. `get-email-metrics` with the broadcast ids and the `broadcast` dimension, and
   a start date early enough to cover them: sent, delivered, bounced,
   unsubscribed, unique_opened, unique_clicked.
3. `list-broadcast-clicked-links` for the newest tracked edition: keep the top
   five as `{"label": <item title from that edition>, "url": ..., "unique_clicks": n}`.

Update the last four editions (figures keep moving for a few days after a send),
set `"updated"` to today, and save it with the run. Use the numbers exactly as
Resend gives them: never estimate, and leave a figure as `null` if it did not
come back. Never list contacts or recipients for this; the report needs counts,
not names.

Who does it: the weekly run, just before the health report (one try, skip if
refused, see `CLAUDE.md`), and any send session, straight after the broadcast is
scheduled, so the file is never more than a week behind.

**Open rates are rough.** Apple Mail loads images ahead of time, which counts as
an open whether or not the email was read, and some clients block the tracking
image. Read the open rate as a trend across weeks. Clicks are the number to
trust.

## A one-off note to subscribers

`business.email_notice` in `config/config.yaml` puts a short note at the top of
the next email, above the preview, with a link to the privacy policy. Use it to
tell subscribers about a change to how their data is used. `build_email.py`
says so when it builds an email that carries one. **Set it back to `""` once
that broadcast has gone**, or the same note goes out every week.

## Rules
- **Never broadcast without Jamie's explicit approval of the TEST email.** No
  approval that week = no email that week (the site still updates).
- Always test to Jamie's own inboxes first, then broadcast.
- Build the email from the LIVE page at approval time, never a pre-approval
  snapshot, so edits are always reflected.
- Sending domain is `news.thereclab.ai` (the only verified/send-enabled domain).
- The "General" segment currently holds the real subscriber list; a broadcast
  reaches everyone in it.

## build_email.py — notes
The converter mirrors the site's current template. Two fixes were made (Aug 2026)
after the standout/guest layout changed, keep them:
- **Standouts:** parsed from the `<span class="why">` span (title link on its own
  line, WHY beneath). The old "text after the anchor" logic mangled the copy.
- **Grouped-vendor launch block:** when an article has no `<a class="ttl">` it
  uses the `.vgroup-title` as the (unlinked) heading and renders each `ul.pts`
  release `<li>` with its own link, in both HTML and plain text. Otherwise the
  block rendered blank.
Guest lines are "Name · Title @ Company". If the site template changes again,
re-check both of these in build_email.py.
- **No em/en dashes, ever.** Standouts stack the WHY on the line below the title
  (no dash separator), and a final safety pass replaces any `—`, `–`, `&mdash;`
  or `&ndash;` in the built HTML/text with a comma. Keep that guard; the digest
  voice bans em dashes and the email must match.
