#!/usr/bin/env python3
"""
Regenerate INDEX.md from the transcript files plus episode_summaries.tsv.

episode_summaries.tsv holds one line per episode:
    <podcast>/<filename>.md|||one-line summary|||Company|||tag1, tag2, tag3
Tags must come from TAXONOMY.md so an AI can filter on a consistent set.

Run this after fetching new episodes. New episodes that don't yet have a
summary line will still appear in the index (without a summary/tags) and
are listed at the end so you know which ones to summarise.

Usage:
    python3 build_index.py            # core library (root)
    python3 build_index.py agency     # the "agency" collection subfolder
"""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runlog

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "library")


def load_allowed_tags(root):
    """Tags declared in this collection's TAXONOMY.md (lines starting '- ')."""
    p = os.path.join(root, "TAXONOMY.md")
    allowed = set()
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            st = line.strip()
            if st.startswith("- "):
                tag = st[2:].split("  (")[0].split("(")[0].strip().lower()
                if tag:
                    allowed.add(tag)
    return allowed


def main():
    # Optional first arg: a collection subfolder (e.g. "agency") that has its
    # own transcripts/, episode_summaries.tsv and INDEX.md. Defaults to the
    # core library at the project root.
    root = os.path.join(BASE, sys.argv[1] if len(sys.argv) > 1 else "podcasts")
    summ = {}
    dup_counts = {}
    tsv = os.path.join(root, "episode_summaries.tsv")
    if os.path.exists(tsv):
        for line in open(tsv, encoding="utf-8"):
            line = line.rstrip("\n")
            # A summariser occasionally rewrites the whole file with a line
            # number and tab on the front of every row, which used to make every
            # entry look missing. Real rows start with a folder name, never
            # digits+tab, so stripping it is always safe.
            line = re.sub(r"^\d+\t", "", line)
            if "|||" not in line:
                if line.strip():
                    print("  WARNING skipping malformed line:", line[:80])
                continue
            parts = line.split("|||")
            if len(parts) == 4:
                rel, s, company, tags = parts
            elif len(parts) == 3:  # tolerate old 3-field rows (no company)
                rel, s, tags = parts
                company = ""
            else:  # malformed line — skip rather than crash
                print("  WARNING skipping malformed line:", line[:80])
                continue
            rel = rel.strip()
            dup_counts[rel] = dup_counts.get(rel, 0) + 1
            summ[rel] = (s.strip(), company.strip(), tags.strip())

    coll = sys.argv[1] if len(sys.argv) > 1 else "podcasts"
    titles = {"podcasts": "# Podcast Transcript Index", "agency": "# Agency Transcript Index",
              "newsletters": "# Newsletter Index", "reports": "# Reports Index",
              "adhoc": "# Ad-hoc Library Index"}
    title = titles.get(coll, f"# {coll.title()} Index")
    out = [title, "",
           "Each entry: date, title (links to source), one-line summary, topic tags, and file path.",
           "Use this to find relevant items before opening the full document.", ""]
    total, missing = 0, []
    tdir = os.path.join(root, "transcripts")
    for pod in sorted(os.listdir(tdir)):
        d = os.path.join(tdir, pod)
        if not os.path.isdir(d) or pod.startswith("_"):
            continue
        files = sorted(glob.glob(f"{d}/*.md"))
        out.append(f"## {pod} ({len(files)} episodes)\n")
        rows = []
        for fp in files:
            txt = open(fp, encoding="utf-8").read()
            title = txt.splitlines()[0].lstrip("# ").strip()
            date = (re.search(r"\*\*Date:\*\* (.*)", txt) or [None, ""])[1].strip()
            url = (re.search(r"\*\*URL:\*\* (.*)", txt) or [None, ""])[1].strip()
            rel = f"{pod}/{os.path.basename(fp)}"
            s, company, tags = summ.get(rel, ("", "", ""))
            if not s:
                missing.append(rel)
            rows.append((date, title, url, rel, s, company, tags))
        for date, title, url, rel, s, company, tags in sorted(rows, reverse=True):
            out.append(f"### {date} — [{title}]({url})")
            if s:
                out.append(s)
                if company:
                    out.append(f"Company: {company}")
                out.append(f"Tags: {tags}")
            out.append(f"File: `transcripts/{rel}`")
            out.append("")
            total += 1
    open(os.path.join(root, "INDEX.md"), "w", encoding="utf-8").write("\n".join(out))
    print(f"Wrote INDEX.md with {total} episodes. {len(missing)} missing index lines.")

    # The index line is a one-liner for finding an episode. The SUMMARY BLOCK is
    # the written summary inside the transcript itself, and it is what makes the
    # archive searchable by what was actually said. Nothing used to check it, so
    # a run could write every index line, skip every summary, and look healthy.
    have = 0
    for pod in sorted(os.listdir(tdir)):
        d = os.path.join(tdir, pod)
        if not os.path.isdir(d) or pod.startswith("_"):
            continue
        for fp in glob.glob(f"{d}/*.md"):
            if "<!--SUMMARY-->" in open(fp, encoding="utf-8").read(4000):
                have += 1
    pct = (100 * have // total) if total else 0
    # Summary blocks are for spoken-word transcripts. Newsletters keep the full
    # issue and reports keep their key figures, so they are not expected to have
    # one; the count is shown for information only.
    expected = coll in ("podcasts", "tech", "agency", "adhoc")
    if expected:
        print(f"Summary blocks: {have}/{total} ({pct}%)."
              + ("" if have == total else f" {total - have} transcripts still need one."))
    else:
        print(f"Summary blocks: {have}/{total} (not expected for this collection).")
    for m in missing:
        print("  needs summary:", m)

    # ---- integrity checks (warn only, never crash) ----
    warnings = []
    actual = {f"{pod}/{os.path.basename(fp)}"
              for pod in os.listdir(tdir) if os.path.isdir(os.path.join(tdir, pod)) and not pod.startswith("_")
              for fp in glob.glob(os.path.join(tdir, pod, "*.md"))}

    # 1. unknown tags (not declared in this collection's TAXONOMY.md)
    allowed = load_allowed_tags(root)
    if allowed:
        bad_tags = {}
        for rel, (s, company, tags) in summ.items():
            for t in tags.split(","):
                t = t.strip().lower()
                if t and t not in allowed:
                    bad_tags.setdefault(t, []).append(rel)
        for t, files in sorted(bad_tags.items()):
            warnings.append(f"unknown tag '{t}' in {len(files)} file(s), e.g. {files[0]}")

    # 2. duplicate TSV lines for the same path
    for rel, n in sorted(dup_counts.items()):
        if n > 1:
            warnings.append(f"duplicate TSV line: {rel} ({n}x)")

    # 3. TSV entries pointing at a file that no longer exists
    for rel in sorted(summ):
        if rel not in actual:
            warnings.append(f"TSV summary points at missing file: {rel}")

    # 4. near-duplicate source folders (e.g. 'Korn Ferry' vs 'KornFerry')
    norm = {}
    for pod in os.listdir(tdir):
        if os.path.isdir(os.path.join(tdir, pod)) and not pod.startswith("_"):
            norm.setdefault(re.sub(r"[^a-z0-9]", "", pod.lower()), []).append(pod)
    for names in norm.values():
        if len(names) > 1:
            warnings.append(f"near-duplicate folders: {sorted(names)}")

    runlog.record("index", collection=coll, items=total, missing=len(missing),
                  blocks=have, warnings=warnings)
    if warnings:
        print(f"CHECK: {len(warnings)} warning(s):")
        for w in warnings:
            print("  WARN:", w)
    else:
        print("CHECK: clean (tags valid, no duplicate/orphan TSV lines, no near-dup folders).")


if __name__ == "__main__":
    main()
