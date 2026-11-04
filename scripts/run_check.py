#!/usr/bin/env python3
"""
Did the run actually do what a run does?

Every other check looks at the finished page. This looks at the RUN: the state
the project should be in once a week has completed properly. It is the check
that catches a phase quietly not happening, which no artefact check ever will,
because a digest built from a stale library looks perfectly fine.

    python3 scripts/run_check.py            after publishing
    python3 scripts/run_check.py --pre      before publishing, skips the publish checks

Exit 0 clean, exit 1 if something did not happen.
"""

import os, sys, json, glob, datetime, argparse, subprocess

COLLECTIONS = ["podcasts", "tech", "adhoc", "newsletters", "reports", "news"]
SUMMARISED = ["podcasts", "tech", "adhoc"]


def today():
    return datetime.date.today()


def mdate(p):
    return datetime.date.fromtimestamp(os.path.getmtime(p)) if os.path.exists(p) else None


def check(pre):
    bad, note = [], []
    t = today()

    # --- the tools ran at all -------------------------------------------
    ev = "_state/run-events.jsonl"
    if not os.path.exists(ev) or os.path.getsize(ev) == 0:
        bad.append(("nothing recorded", "run-events.jsonl is empty, so no script reported doing anything"))
    elif mdate(ev) != t:
        bad.append(("stale events", f"run-events.jsonl last written {mdate(ev)}, not today"))

    # --- the handover files are this week's ------------------------------
    for f in ["run-report.json", "publish-report.json"]:
        p = os.path.join("_state", f)
        if pre and f == "publish-report.json":
            continue
        if not os.path.exists(p) or os.path.getsize(p) == 0:
            bad.append(("missing handover", f"_state/{f} is empty"))
            continue
        try:
            d = json.load(open(p))
            if d.get("date") != t.isoformat():
                bad.append(("stale handover", f"_state/{f} is dated {d.get('date')}, not {t}"))
        except json.JSONDecodeError:
            bad.append(("unreadable handover", f"_state/{f}"))

    # --- every index rebuilt today ---------------------------------------
    for c in COLLECTIONS:
        idx = f"library/{c}/INDEX.md"
        if not os.path.exists(idx):
            bad.append(("no index", c)); continue
        if mdate(idx) != t:
            bad.append(("index not rebuilt", f"{c}: INDEX.md last written {mdate(idx)}"))

    # --- everything SAVED THIS RUN got summarised -------------------------
    # Modification time is not good enough here: a backfill edits old files too.
    # fetch_transcripts records exactly what it saved, so use that.
    saved = []
    try:
        sys.path.insert(0, "scripts"); import runlog
        for e in runlog.read_events():
            if e.get("kind") == "saved":
                saved.append(e["path"])
    except Exception:
        pass
    unsummarised = [p for p in saved if os.path.exists(p)
                    and "<!--SUMMARY-->" not in open(p, encoding="utf-8").read(200)]
    if unsummarised:
        bad.append(("saved but not summarised",
                    f"{len(unsummarised)} of {len(saved)} episodes saved this run have no "
                    f"summary block, e.g. {os.path.basename(unsummarised[0])}"))
    elif saved:
        note.append(f"{len(saved)} episodes saved this run, all summarised")

    # --- indexes are clean ------------------------------------------------
    for c in COLLECTIONS:
        try:
            out = subprocess.run([sys.executable, "scripts/build_index.py", c],
                                 capture_output=True, text=True, timeout=180).stdout
            if "CHECK: clean" not in out:
                n = [l for l in out.splitlines() if "WARN" in l]
                bad.append(("index warnings", f"{c}: {len(n)} warning(s), first is {n[0].strip() if n else '?'}"))
            for l in out.splitlines():
                if "missing index lines" in l and not l.strip().startswith("Wrote INDEX.md with 0"):
                    if " 0 missing index lines" not in l:
                        bad.append(("missing index lines", f"{c}: {l.strip()}"))
        except Exception as e:
            bad.append(("could not rebuild index", f"{c}: {e}"))

    if pre:
        return bad, note

    # --- the publish actually happened -----------------------------------
    builds = [f for f in glob.glob("digest/builds/*.html") if "_TRIAL" not in f]
    if len(builds) != 1:
        bad.append(("builds folder", f"{len(builds)} build files, should be exactly 1 (this week's)"))
    elif mdate(builds[0]) != t:
        bad.append(("build not from today", os.path.basename(builds[0])))

    pubs = sorted(glob.glob("digest/published/*.html"))
    if not pubs:
        bad.append(("nothing archived", "digest/published/ is empty"))
    elif mdate(pubs[-1]) != t:
        bad.append(("no edition archived today", f"newest is {os.path.basename(pubs[-1])}"))

    try:
        v = int(open("digest/version.txt").read().strip())
        pub = json.load(open("_state/publish-report.json"))
        if pub.get("version") != v:
            bad.append(("version not written back",
                        f"version.txt says {v}, this run published {pub.get('version')}"))
    except Exception as e:
        bad.append(("version file", str(e)))

    rows = [l for l in open("digest/featured-log.tsv", encoding="utf-8")
            if not l.startswith("#") and l.startswith(t.isoformat())]
    if not rows:
        bad.append(("nothing logged as featured",
                    "no rows dated today in featured-log.tsv, so next week will repeat this week's items"))
    else:
        note.append(f"{len(rows)} items logged as featured")

    return bad, note


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pre", action="store_true", help="before publishing")
    a = ap.parse_args()
    bad, note = check(a.pre)
    for n in note:
        print("  " + n)
    if not bad:
        print("Run check: clean. The run did everything a run should.")
        sys.exit(0)
    print(f"\nRun check: {len(bad)} thing(s) did not happen.\n")
    for kind, detail in bad:
        print(f"  [{kind}]\n    {detail}\n")
    sys.exit(1)
