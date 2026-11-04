#!/usr/bin/env python3
"""
Final duplication sweep, run on the finished digest before publishing.

The featured log already stops repeats by exact key: the library path, or the
URL for web-only items. That works for anything with a library file. It fails
for launches and news, where the same release gets linked from a changelog, a
blog post and a release note, so three different URLs point at one thing.

This checks NAMES instead, which is what a person would notice. It compares
every title in the finished digest against everything featured in the last 8
weeks, the same length as the eligibility window, and reports anything that
looks like it has been used before.

    python3 check_duplicates.py digest/<file>.html [--weeks 8]

Exit 0 clean, exit 1 if anything needs a human look. It never blocks on its own
judgement: near matches are reported for a decision, not auto-rejected.
"""

import re, sys, html, datetime, argparse, difflib

STOP = {"the","a","an","and","or","of","for","to","in","on","with","your","you",
        "is","are","how","why","what","open","beta","new","2026","2025"}


def norm(t):
    t = html.unescape(t or "").lower()
    t = re.sub(r"\(.*?\)", " ", t)          # drop parenthetical guest names
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    words = [w for w in t.split() if w not in STOP and len(w) > 2]
    return " ".join(words)


def titles_in_digest(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<span class="src">(.*?)</span>.*?<a class="ttl"[^>]*>(.*?)</a>', s, re.S):
        src = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        out.append((src, re.sub(r"<[^>]+>", "", m.group(2)).strip()))
    # grouped vendor launches: the release name lives in .rt
    for m in re.finditer(r'<span class="src">(.*?)</span>(.*?)</article>', s, re.S):
        src = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        for rt in re.findall(r'<span class="rt">(.*?)</span>', m.group(2)):
            out.append((src, re.sub(r"<[^>]+>", "", rt).strip()))
    # standout rows
    for m in re.finditer(r'<span class="pick">(.*?)</span><span class="body"><a[^>]*>(.*?)</a>', s, re.S):
        out.append(("standout: " + m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()))
    return out


def past(log, weeks):
    cutoff = datetime.date.today() - datetime.timedelta(weeks=weeks)
    rows = []
    for line in open(log, encoding="utf-8"):
        if line.startswith("#"):
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 4:
            continue
        try:
            d = datetime.date.fromisoformat(p[0])
        except ValueError:
            continue
        if d >= cutoff:
            rows.append((d, p[1], p[3]))
    return rows


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("digest")
    ap.add_argument("--log", default="digest/featured-log.tsv")
    ap.add_argument("--weeks", type=int, default=8)
    ap.add_argument("--threshold", type=float, default=0.72)
    a = ap.parse_args()

    old = past(a.log, a.weeks)
    hits = []
    for src, title in titles_in_digest(a.digest):
        n = norm(title)
        if not n:
            continue
        for d, osrc, otitle in old:
            score = difflib.SequenceMatcher(None, n, norm(otitle)).ratio()
            # a short exact-ish name (a product release) counts on containment too
            contained = len(n) > 6 and (n in norm(otitle) or norm(otitle) in n)
            if score >= a.threshold or contained:
                hits.append((src, title, d, osrc, otitle, score))

    if not hits:
        print(f"Duplication sweep: clean. Nothing in this digest resembles the "
              f"{len(old)} items featured in the last {a.weeks} weeks.")
        sys.exit(0)

    print(f"Duplication sweep: {len(hits)} possible repeat(s). Check each before publishing.\n")
    for src, title, d, osrc, otitle, score in sorted(hits, key=lambda x: -x[5]):
        print(f"  THIS WEEK  {src}: {title}")
        print(f"  ALREADY    {d} {osrc}: {otitle}")
        print(f"  similarity {score:.0%}\n")
    sys.exit(1)
