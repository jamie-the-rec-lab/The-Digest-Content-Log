#!/usr/bin/env python3
"""
Quality check on the summary blocks in the library.

Run after every backfill batch. With 1,600 transcripts to get through, a fault
in the instructions produces hundreds of bad blocks before anyone notices.

    python3 scripts/check_summaries.py            everything
    python3 scripts/check_summaries.py podcasts   one collection
    python3 scripts/check_summaries.py --list     print the bad file paths only
    python3 scripts/check_summaries.py --fix      repair what can be repaired

--fix does two mechanical things and nothing clever:
  * replaces em and en dashes in our own prose with a comma, leaving quotes alone
  * strips any block that is far too short, so the backfill picks it up again

Anything needing judgement is left for a human or a rerun.

Exit 0 clean, exit 1 if anything is off.
"""
import glob, re, sys, os, collections

REQUIRED = ["## Actionable summary", "**Show:**", "**Tags:**",
            "**When to use this:**", "**Big idea:**", "**Steal this"]
COLLECTIONS = ["podcasts", "tech", "adhoc"]


def problems(path):
    s = open(path, encoding="utf-8").read()
    if "<!--SUMMARY-->" not in s:
        return None                      # no block yet, that is the backfill's job
    out = []
    if not s.startswith("<!--SUMMARY-->"):
        out.append("block is not at the top of the file")
    i, j = s.index("<!--SUMMARY-->"), s.index("<!--/SUMMARY-->")
    if j < i:
        return ["closing marker before the opening one"]
    b = s[i:j]
    for n in REQUIRED:
        if n not in b:
            out.append("missing " + n)
    # a guest OR a host, never neither, and it has to say who they are
    if "**Guest:**" not in b and "**Host:**" not in b:
        out.append("no Guest or Host line")
    else:
        m = re.search(r"\*\*(?:Guest|Host):\*\*\s*(.+?)(?:·|\n)", b)
        person = m.group(1).strip() if m else ""
        if len(person.split()) < 3 or ("," not in person and "@" not in person):
            out.append("Guest or Host line does not say who they are")

    # Every figure in a block must appear in the transcript underneath it.
    # Catches the exact failure measured on 27 August: a "3x engagement" stat
    # that nobody said, invented to make a play land harder. Pushing for useful
    # is precisely when numbers get made up.
    body = s[s.index("<!--/SUMMARY-->"):].lower()
    body_digits = set(re.findall(r"\d[\d,.]*", body.replace(",", "")))
    ghosts = []
    for n in set(re.findall(r"\d[\d,.]*", b.replace(",", ""))):
        clean = n.rstrip(".")
        if len(clean) < 2:                      # single digits are too noisy
            continue
        if re.match(r"^(19|20)\d\d$", clean):   # years, usually the episode date
            continue
        if clean not in body_digits and clean not in body:
            ghosts.append(clean)
    if ghosts:
        out.append("figure not in the transcript: " + ", ".join(sorted(ghosts)[:4]))

    # A play is a method you could run, not a principle you already know. The
    # spec asks for the worked example, exact step or number behind it. Without
    # a specific, the summary tells you what the episode was about rather than
    # what was said in it, which is the failure this whole archive exists to
    # avoid. Measured 27 August: a third of blocks failed this.
    fr = re.search(r"\*\*Frameworks & plays:\*\*(.*?)(?:\n\*\*|\Z)", b, re.S)
    plays = re.findall(r"^- (.+)$", fr.group(1), re.M) if fr else []
    if plays:
        specific = sum(1 for p in plays if re.search(r"\d|[A-Z][a-z]+ [A-Z]|\"|\'[a-z]", p))
        if specific < max(1, len(plays) // 2):
            out.append("plays are generic, %d of %d carry a number, name or quote"
                       % (specific, len(plays)))
    # dashes are allowed inside a verbatim quote, never in our own prose
    prose = re.sub(r'"[^"]*"', "", b)
    if re.search(r"[—–]", prose):
        out.append("em or en dash outside a quote")
    if s.count("<!--SUMMARY-->") > 1:
        out.append("more than one block")
    if len(b.split()) < 200:
        out.append("block is only %d words, spec is 250 to 450" % len(b.split()))

    # Scraped from the episode description instead of read from the transcript.
    # The description's "what you'll learn" list is topic labels, not methods,
    # and a summary built from it tells you what an episode is about rather than
    # what was said in it. That is the whole difference this archive exists for.
    desc = ""
    m = re.search(r"## Episode description(.*?)(?=\n## |\Z)", s, re.S)
    if m:
        desc = m.group(1).lower()
    if desc:
        lifted = 0
        for line in re.findall(r"^- (.{30,})$", b, re.M):
            probe = " ".join(line.split()[:6]).strip(",.").lower()
            if len(probe) > 20 and probe in desc:
                lifted += 1
        if lifted >= 2:
            out.append("%d bullets lifted from the episode description, not the transcript" % lifted)
    return out


def fix(path):
    """Mechanical repairs only."""
    s = open(path, encoding="utf-8").read()
    if "<!--SUMMARY-->" not in s:
        return None
    i, j = s.index("<!--SUMMARY-->"), s.index("<!--/SUMMARY-->") + len("<!--/SUMMARY-->")
    b = s[i:j]
    probs = problems(path) or []
    if any(x.startswith("block is only") or x.startswith("bullets lifted")
           or x.startswith("plays are generic") or x.startswith("Guest or Host line does not")
           for x in probs):
        open(path, "w", encoding="utf-8").write((s[:i] + s[j:]).lstrip("\n"))
        return "stripped and requeued, below spec"
    parts = re.split(r'("[^"]*")', b)          # keep quotes untouched
    for k in range(0, len(parts), 2):
        parts[k] = re.sub(r"\s*[—–]\s*", ", ", parts[k])
    nb = "".join(parts)
    nb = re.sub(r",\s*,", ",", nb)
    if nb != b:
        open(path, "w", encoding="utf-8").write(s[:i] + nb + s[j:])
        return "dashes replaced with commas"
    return None


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--fix" in sys.argv:
        n = collections.Counter()
        for c in (args or COLLECTIONS):
            for f in glob.glob(f"library/{c}/transcripts/*/*.md"):
                if "/_teasers/" in f: continue
                if problems(f):
                    r = fix(f)
                    if r: n[r] += 1
        for k, v in n.most_common(): print(f"  {v:4}  {k}")
        print("done, rerun without --fix to confirm")
        sys.exit(0)
    listing = "--list" in sys.argv
    colls = args or COLLECTIONS
    counts = collections.Counter()
    bad_files = []
    total = withblock = 0
    for c in colls:
        for f in glob.glob(f"library/{c}/transcripts/*/*.md"):
            if "/_teasers/" in f:
                continue
            total += 1
            p = problems(f)
            if p is None:
                continue
            withblock += 1
            if p:
                bad_files.append(f)
                for x in p:
                    counts[x] += 1
    if listing:
        print("\n".join(bad_files)); sys.exit(1 if bad_files else 0)
    print(f"{withblock} of {total} transcripts have a summary block.")
    if not bad_files:
        print("Summary check: clean.")
        sys.exit(0)
    print(f"\n{len(bad_files)} block(s) with problems:\n")
    for k, v in counts.most_common():
        print(f"  {v:4}  {k}")
    print("\nRerun with --list to get the file paths.")
    sys.exit(1)
