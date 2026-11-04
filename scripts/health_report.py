#!/usr/bin/env python3
"""
Phase 3. Builds the Slack health report and appends this run's problems to
_state/RUN_LOG.tsv.

Reads the two handover files, prints the finished Slack message to stdout, and
writes the log rows. It does not send anything: the job takes the printed
message and sends it.

    python3 health_report.py [--project DIR] [--no-log] [--format slack|email]

The message goes two places, and they use deliberately separate machinery:
  Slack  the DM below, formatted with **bold**
  Email  jamie@thereclab.ai, via Gmail, plain text, subject printed first

The subscriber newsletter goes through Resend. This job NEVER touches Resend,
which is what keeps "this job cannot email the list" a wall rather than a
judgement call. A note to Jamie's own inbox cannot turn into a broadcast,
because it is not using the thing that broadcasts.

Everything here is mechanical. Given the same two files it produces the same
message every time, which is the point: the wording cannot drift week to week.

--------------------------------------------------------------------------
WHAT THE HANDOVER FILES MUST CONTAIN
--------------------------------------------------------------------------
_state/run-report.json      written by Phase 1
{
  "date": "2026-08-26",                     # the run date, checked for staleness
  "collections": {
     "podcasts":    {"10x Recruiting": 1, "Brainfood": 0, ...},
     "newsletters": {"TA Unboxed": 1, ...},
     "tech":        {"Lenny's Podcast": 2, ...},
     "agency":      {"Elite Recruiter": 3, ...},
     "adhoc":       {"Reports": 1, ...}
  },
  "reports":  [ {"name": "REC", "extraction": "full|partial|blocked",
                 "url": "...", "reason": "subscription only"} ],
  "to_grab":  [ {"name": "Mercer", "url": "...", "reason": "email form"} ],
  "index":    { "podcasts": {"items": 689, "missing": 0, "blocks": "81/688", "warnings": []},
                "newsletters": {"items": 31, "missing": 0, "warnings": []}, ... },
              # missing = transcripts with no index line, i.e. not summarised yet.
              # Anything above 0 means the summarising step did not finish.
  "zero_returns": ["The Debrief"],          # listed cleanly but empty: a real break.
                                            # A failed listing is a retry, not a zero return.
  "problems": [ {"phase": 1, "source": "Gem", "what": "page empty",
                 "severity": "degraded", "resolved": "yes"} ],
  "ai_news":  "headline or null"
}

_state/publish-report.json  written by Phase 2
{
  "date": "2026-08-26",
  "version": 3,
  "edition_date": "26th August 2026",
  "url": "https://thereclab.ai/digest",
  "published": true,
  "fact_check": "pass" | "corrected 2" | "failed",
  "checks_passed": true,
  "template_restored": false,
  "launches": ["Greenhouse", "Juicebox"],
  "problems": [ ... same shape as above ... ]
}

Any missing key is treated as absent rather than fatal. A missing file is
reported as a problem rather than crashing.
"""

import json, os, sys, datetime, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runlog

QUIET_WEEKS = 4          # a source is "quiet" at 4+ weeks since its newest item
SLACK_DM = "U0B5GMDT8AG"
EMAIL_TO = "jamie@thereclab.ai"

RECURRING = {
    "podcasts": ["10x Recruiting", "Brainfood", "Offer Accepted",
                 "Recruiting Future", "Building the Talent Machine",
                 "Recruiting Roadshow", "The Debrief", "PromptMates"],
    "tech": ["Lenny's Podcast", "How I AI", "AI & I", "AI For Humans"],
    "newsletters": ["Full Stack Recruiter", "TA Unboxed", "PromptMates Newsletter",
                    "Data Driven Recruiter", "RecOps Collective", "Remade.md",
                    "Ashby Community"],
}
FOLDER = {"podcasts": "library/podcasts/transcripts",
          "tech": "library/tech/transcripts",
          "newsletters": "library/newsletters/transcripts"}


# ---------------------------------------------------------------- helpers

def load(path, problems):
    if not os.path.exists(path):
        problems.append({"phase": 3, "source": os.path.basename(path),
                         "what": "handover file missing",
                         "severity": "degraded", "resolved": "no"})
        return {}
    try:
        text = open(path, encoding="utf-8").read().strip()
        return json.loads(text) if text else {}
    except json.JSONDecodeError as e:
        problems.append({"phase": 3, "source": os.path.basename(path),
                         "what": f"handover file unreadable: {e}",
                         "severity": "degraded", "resolved": "no"})
        return {}


def newest_item_date(project, collection, source):
    """Newest YYYY-MM-DD prefix across the .md files in a source's folder."""
    d = os.path.join(project, FOLDER[collection], source)
    if not os.path.isdir(d):
        return None
    dates = [f[:10] for f in os.listdir(d)
             if f.endswith(".md") and len(f) > 10 and f[:4].isdigit()]
    return max(dates) if dates else None


def weeks_since(datestr, today):
    try:
        d = datetime.date.fromisoformat(datestr)
    except ValueError:
        return None
    return (today - d).days // 7


def counts_line(counts):
    """'Offer Accepted +1, PromptMates +2 (Brainfood, 10x: no new episodes)'"""
    if not counts:
        return "no data"
    got = [f"{k} +{v}" for k, v in sorted(counts.items()) if v]
    none = [k for k, v in sorted(counts.items()) if not v]
    if not got:
        return "none new"
    line = ", ".join(got)
    if none:
        line += f" ({', '.join(none)}: no new items)"
    return line


# ---------------------------------------------------------------- report

def build(project, today):
    problems = []
    run = load(os.path.join(project, "_state", "run-report.json"), problems)
    pub = load(os.path.join(project, "_state", "publish-report.json"), problems)

    iso = today.isoformat()
    for name, data in (("run-report", run), ("publish-report", pub)):
        if data and data.get("date") and data["date"] != iso:
            problems.append({"phase": 3, "source": name,
                             "what": f"stale, dated {data['date']} not {iso}",
                             "severity": "blocked", "resolved": "no"})

    problems += run.get("problems", []) + pub.get("problems", [])

    # Judgement calls are not faults. The run is allowed to decide things the
    # documents did not cover, but every call has to surface where Jamie will
    # actually read it, or it is judgement with no feedback loop. They stay in
    # `problems` so append_log still writes them to RUN_LOG.tsv as a record,
    # and they are pulled out here so they get their own section rather than
    # being counted as things that went wrong.
    decisions = [p for p in problems if p.get("severity") == "decision"]
    zero_from_events = []
    stale = [p for p in problems if "stale" in p.get("what", "")
             or "missing" in p.get("what", "") or "unreadable" in p.get("what", "")]

    # What the tools recorded about themselves beats what anyone remembered.
    # build_index and fetch_transcripts write _state/run-events.jsonl as they go,
    # so counts, warnings and failed fetches never depend on being written down
    # by hand. The run report is still read for the things only the agent knows:
    # which reports were partial, which launches were featured.
    events = runlog.read_events()
    # Added 4 Sep 2026. A record saved with no date is invisible to selection,
    # to the freshness window and to the no-going-backwards check, and it used
    # to be written silently as "0000-". It has to reach Jamie.
    for e in events:
        if e.get("kind") == "missing_date":
            problems.append({"phase": 1, "source": os.path.basename(os.path.dirname(e.get("path", ""))) or "?",
                             "what": "saved with NO DATE, so it is invisible to selection and the 8 week "
                                     "window: " + str(e.get("title", ""))[:70] + ". Recover the date from "
                                     "the source and rename it.",
                             "severity": "degraded", "resolved": "no"})
    ev_index, ev_fetch = {}, {}
    for e in events:
        if e.get("kind") == "index":
            ev_index[e["collection"]] = {"items": e.get("items"),
                                         "missing": e.get("missing", 0),
                                         "blocks": e.get("blocks"),
                                         "warnings": e.get("warnings", [])}
        elif e.get("kind") == "fetch":
            ev_fetch[e["source"]] = e
    for src, e in ev_fetch.items():
        if e.get("outcome") == "listing_failed":
            problems.append({"phase": 1, "source": src,
                             "what": "listing failed, " + str(e.get("detail", ""))[:120],
                             "severity": "degraded", "resolved": "no"})
        elif e.get("outcome") == "bad_destination":
            # Added 3 Sep 2026. A fetch that writes outside the six collections
            # is invisible to selection AND to build_index, so it has to shout.
            problems.append({"phase": 1, "source": src,
                             "what": "REFUSED, invalid destination "
                                     + repr(e.get("destination"))
                                     + ". Nothing was saved for this source this run.",
                             "severity": "blocked", "resolved": "no"})
        elif e.get("outcome") == "scan_limit_clamped":
            problems.append({"phase": 1, "source": src,
                             "what": "scan limit %s clamped to the ceiling of %s. If this "
                                     "source is genuinely behind, run a deliberate backfill "
                                     "with --backfill rather than widening the weekly run."
                                     % (e.get("requested"), e.get("ceiling")),
                             "severity": "decision", "resolved": "yes"})
        elif e.get("outcome") == "listed_empty":
            zero_from_events.append(src)
        if e.get("hit_limit"):
            problems.append({"phase": 1, "source": src,
                             "what": "every listed episode was new, there may be more past the scan limit",
                             "severity": "degraded", "resolved": "no"})

    collections = run.get("collections", {})
    reports = run.get("reports", [])
    if not isinstance(reports, list):
        # Added 10 Sep 2026. run-report.json's "reports" key is documented as a
        # list of {"name","extraction",...} dicts. A run that writes a different
        # shape (e.g. the inbox-processing dict some runs produce instead) must
        # not crash the report - treat it as absent, per this file's own rule
        # that a missing/malformed key is reported, not fatal, and flag it so
        # Phase 1's output gets fixed rather than silently swallowed forever.
        problems.append({"phase": 3, "source": "run-report.json",
                         "what": "the 'reports' key was not a list (got "
                                 + type(reports).__name__ + "), so report "
                                 "reachability could not be shown this week. "
                                 "Check what Phase 1 wrote there.",
                         "severity": "degraded", "resolved": "no"})
        reports = []
    zero = list(run.get("zero_returns", [])) + zero_from_events
    index = run.get("index", {})
    # the tools' own records win over anything written by hand
    for coll, data in ev_index.items():
        index[coll] = data

    needs = []
    # A listing that failed is only recorded after the script has already retried
    # three times, so it means that source genuinely got nothing this week.
    for src, e in ev_fetch.items():
        if e.get("outcome") == "listing_failed":
            needs.append(f"{src}: could not be listed, even after retries. It got nothing this run.")
        if e.get("outcome") == "bad_destination":
            needs.append(f"{src}: the fetch was REFUSED for writing outside the six library "
                         f"collections, so nothing was saved for it. Check how its destination "
                         f"is set in sources.yaml.")
        if e.get("hit_limit"):
            needs.append(f"{src}: every listed episode was new, so there may be more past the "
                         f"scan limit. Rerun it with a bigger limit.")
    for p in stale:
        needs.append(f"Handover file problem: {p['source']} {p['what']}.")
    if not pub.get("published", False):
        why = pub.get("blocked_by")
        if why:
            needs.append("The edition did not publish. " + str(why))
        else:
            needs.append("The edition did not publish.")
        nxt = pub.get("ready_to_publish")
        if isinstance(nxt, dict):
            needs.append("It is built and ready though: " + str(nxt.get("public_copy","")) +
                         " (" + str(nxt.get("checks","")) + "). To finish it, commit that file over " +
                         str(nxt.get("target","")) + " with the message '" +
                         str(nxt.get("commit_message","")) + "', then " +
                         str(nxt.get("record_keeping_still_to_do","")) + ".")
    if pub.get("checks_passed") is False:
        needs.append("A pre-publish check failed.")
    if pub.get("fact_check") == "failed":
        needs.append("The fact-check did not pass.")
    if pub.get("template_restored"):
        needs.append("The template was damaged and restored from backup.")
    for coll, data in index.items():
        for w in (data or {}).get("warnings", []):
            needs.append(f"Index warning ({coll}): {w}")
        # A collection with unsummarised transcripts means Phase 1 did not
        # finish. Nothing used to report this, so a skipped summarising step
        # produced a perfectly healthy looking report.
        miss = (data or {}).get("missing", 0)
        if miss:
            needs.append(f"{coll}: {miss} transcript(s) saved but not summarised. "
                         f"The summarising step did not finish.")

    # quiet feeds, and the pairing that makes one a real break
    quiet = []
    for coll, sources in RECURRING.items():
        for src in sources:
            newest = newest_item_date(project, coll, src)
            wk = weeks_since(newest, today) if newest else None
            if newest is None:
                quiet.append((src, None))
            elif wk is not None and wk >= QUIET_WEEKS:
                quiet.append((src, wk))
    quiet.sort(key=lambda x: (-1 if x[1] is None else -x[1]))
    for src, wk in quiet:
        if src in zero:
            needs.append(f"{src} is quiet AND its source listed empty. Likely a renamed "
                         f"or private channel, check the URL in sources.yaml.")

    L = []
    needs = [n for n in needs if n not in decisions]
    status = "⚠️ Needs attention" if needs else "✅ Healthy"
    version = pub.get("version", "?")
    L.append("**WEEKLY DIGEST HEALTH CHECK**")
    L.append(f"**Status:** {status}")
    L.append(f"**Edition:** Version {version} ({pub.get('edition_date','?')})")
    L.append(f"**Link:** {pub.get('url','https://thereclab.ai/digest')}")
    if pub.get("published", False):
        L.append("**Review & send:** New edition is live for your review. Reply in your "
                 "Cowork chat with any edits or a green light and I'll email it to the "
                 "subscriber list. Nothing goes out until you approve.")
    else:
        L.append("**Review & send:** NOTHING TO REVIEW YET. This edition was built but "
                 "did NOT go live, so the link above still shows the previous edition. "
                 "Nothing has been emailed and nothing can be, until it publishes. "
                 "See Needs attention below.")
    L.append("")
    L.append("**New library items this run**")
    L.append(f"- **Podcasts:** {counts_line(collections.get('podcasts', {}))}")
    L.append(f"- **Newsletters:** {counts_line(collections.get('newsletters', {}))}")

    if reports:
        L.append("- **Reports:** " + ", ".join(
            f"{r['name']} ({r.get('extraction','?')})" for r in reports))
    else:
        L.append("- **Reports:** none new")

    # Added 11 Sep 2026. "none new" used to cover both "nothing material shipped"
    # and "nobody swept", which is how an unswept week shipped looking like a quiet
    # one. Phase 1 now records whether the sweep ran; say so when it did not.
    launches = pub.get("launches", [])
    swept = run.get("launches_swept")
    if launches:
        L.append(f"- **Product launches:** {', '.join(launches)}")
    elif swept is False:
        L.append("- **Product launches:** NOT SWEPT, so this is not a quiet week, "
                 "it is a missing step. See RUN_LOG.")
    elif swept is None:
        L.append("- **Product launches:** unknown, the run report does not say "
                 "whether the sweep ran.")
    else:
        L.append("- **Product launches:** none material this week (sweep ran).")
    L.append(f"- **Tech:** {counts_line(collections.get('tech', {}))}")
    if collections.get("adhoc"):
        L.append(f"- **Adhoc:** {counts_line(collections['adhoc'])}")

    # reports reachability
    full = sum(1 for r in reports if r.get("extraction") == "full")
    part = sum(1 for r in reports if r.get("extraction") == "partial")
    blocked = [r for r in reports if r.get("extraction") == "blocked"]
    L.append("")
    if blocked:
        L.append("**Blocked this week:** " + ", ".join(
            f"[{r['name']}]({r.get('url','')})" for r in blocked))
    if reports and not blocked:
        L.append(f"**Every report was reachable this week**, {full} full, {part} partial.")
    elif reports:
        L.append(f"Of the rest, {full} full, {part} partial.")

    upgrades = [r for r in reports if r.get("extraction") == "partial"] + run.get("to_grab", [])
    if upgrades:
        L.append("To upgrade to full (grab the source and drop it in reports/_inbox):")
        for u in upgrades:
            reason = f" ({u['reason']})" if u.get("reason") else ""
            L.append(f"- [{u['name']}]({u.get('url','')}){reason}")

    if quiet:
        L.append("")
        L.append("**Quiet feeds:** " + ", ".join(
            f"{s} (no items)" if w is None else f"{s} (newest {w}w ago)"
            for s, w in quiet) + ", worth a check for a broken feed.")

    if index:
        bits = ", ".join(
            f"{k} {v.get('items','?')}" + (f" ({v['missing']} unsummarised)" if v.get("missing") else "")
            for k, v in sorted(index.items()))
        warns = sum(len((v or {}).get("warnings", [])) for v in index.values())
        L.append("")
        word = "warning" if warns == 1 else "warnings"
        L.append(f"**Index:** {bits}, " + ("all clean." if not warns else f"{warns} {word}."))

    if decisions:
        L.append("")
        word = "call" if len(decisions) == 1 else "calls"
        L.append(f"**Decisions I made** ({len(decisions)} {word}, nothing needed "
                 f"from you unless you disagree):")
        for d in decisions:
            src = d.get("source", "-")
            L.append(f"- {src}: {d.get('what', '')}")

    if needs:
        L.append("")
        L.append("**Needs attention:**")
        for n in needs:
            L.append(f"- {n}")

    return "\n".join(L), problems, iso


def append_log(project, problems, iso):
    path = os.path.join(project, "_state", "RUN_LOG.tsv")
    if not problems:
        return 0
    with open(path, "a", encoding="utf-8") as f:
        for p in problems:
            f.write("\t".join([
                iso, str(p.get("phase", "")), p.get("source", "-"),
                str(p.get("what", "")).replace("\t", " "),
                str(p.get("severity", "noted")), str(p.get("resolved", "no"))]) + "\n")
    return len(problems)


def plain(msg):
    """Slack bold is litter in an email. Strip it, and drop the top line since
    the subject already says it."""
    out = []
    for line in msg.split("\n"):
        line = line.replace("**", "")
        if line.startswith("# ") or line == "WEEKLY DIGEST HEALTH CHECK":
            continue
        out.append(line)
    return "\n".join(out).strip()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--no-log", action="store_true")
    ap.add_argument("--format", choices=["slack", "email"], default="slack")
    ap.add_argument("--date", default=None, help="override today, YYYY-MM-DD")
    a = ap.parse_args()

    today = datetime.date.fromisoformat(a.date) if a.date else datetime.date.today()
    msg, problems, iso = build(a.project, today)

    if a.format == "email":
        status = "OK" if "Healthy" in msg.split("\n")[1] else "NEEDS ATTENTION"
        version = msg.split("Version ")[1].split(" ")[0] if "Version " in msg else "?"
        print(f"To: {EMAIL_TO}")
        print(f"Subject: Digest health check, Version {version}, {status}")
        print()
        print(plain(msg))
    else:
        print(msg)
    if not a.no_log:
        n = append_log(a.project, problems, iso)
        print(f"\n---\n{n} row(s) written to RUN_LOG.tsv. Send the message above to {SLACK_DM}.",
              file=sys.stderr)
