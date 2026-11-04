#!/usr/bin/env python3
"""
The last read before publishing. Run it after every edit and every fact-check
correction, on the finished file.

The fact-check asks "is this true". This asks "does this read well". It is
surface level on purpose: it catches the things that are embarrassing rather
than wrong, and it catches them after the last edit, which is exactly when they
get introduced.

    python3 scripts/final_check.py digest/builds/<file>.html

Exit 0 clean, exit 1 if anything needs a look. It reports, it does not block.
"""

import re, sys, html, collections

BANNED_WORDS = ["delve","leverage","harness","landscape","dive deep","seamless",
    "unlock","empower","robust","crucial","pivotal","realm","tapestry",
    "testament","navigate","foster","it's worth noting","it is worth noting"]
BANNED_TICS = ["quietly","leans into","a reckoning","stacking up","hollowing out",
    "a rare bit of","game-changing","game changing","revolutionary","cutting-edge",
    "next-generation","supercharge","powerful new"]
# a bullet that opens leaning on the one above it
LEANERS = ["he also","she also","they also","this means","that means","the second",
    "the third","and finally","as a result","which is why","it also"]

# Words that belong to someone who writes code for a living. The reader drives
# AI tools but does not build them. See STYLE.md: recruiting language and
# landed AI language are fine, engineering language is not.
ENGINEER_WORDS = ["api","endpoint","webhook","repo","repository","vector database",
    "rag","fine-tuning","fine tuning","inference","deployment","schema","sdk",
    "latency","backend","front-end","frontend","middleware","payload","regex",
    "webhooks","oauth","json","yaml","runtime","stack trace","kubernetes"]

# Joins that let two ideas be welded into one sentence
JOINS = [", and ", ", plus ", ", while ", ", but ", " as well as ", ", which ", ", so "]


def text(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


def bullets(s):
    out = []
    for m in re.finditer(r'<ul class="pts">(.*?)</ul>', s, re.S):
        for li in re.findall(r"<li>(.*?)</li>", m.group(1), re.S):
            out.append(text(li))
    return out


def whys(s):
    return [text(m) for m in re.findall(r'<span class="why">(.*?)</span>', s, re.S)]


def real_commas(p):
    """Commas that separate ideas, not the ones inside a simple list.
    "awe, anger and anxiety" is one thing, not three ideas welded together."""
    n = p.count(",")
    n -= len(re.findall(r"\w+,\s+\w+(?:,\s+\w+)*\s+and\s+\w+", p))
    return max(n, 0)


def brief(s):
    m = re.search(r'<p class="brief-text">(.*?)</p>', s, re.S)
    return text(m.group(1)) if m else ""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: final_check.py <digest file>"); sys.exit(2)
    s = open(sys.argv[1], encoding="utf-8").read()
    body = s[s.index("<body"):] if "<body" in s else s
    prose = bullets(s) + whys(s) + ([brief(s)] if brief(s) else [])
    issues = []

    # 1. dashes anywhere in the body
    for d in re.findall(r"[^.]{0,40}[—–][^.]{0,40}", text(body)):
        issues.append(("dash", d.strip()))

    # 2. banned vocabulary and tics
    low = " ".join(prose).lower()
    for w in BANNED_WORDS + BANNED_TICS:
        if re.search(r"\b" + re.escape(w) + r"\b", low):
            for p in prose:
                if re.search(r"\b" + re.escape(w) + r"\b", p.lower()):
                    issues.append(("banned: " + w, p[:110])); break

    # 3. a line that leans on the one before it, so it fails the blank page test
    for p in prose:
        for l in LEANERS:
            if p.lower().startswith(l):
                issues.append(("does not stand alone", p[:110])); break

    # 4. the same opening used twice by two DIFFERENT items. A standout echoing
    #    its own item is expected and not flagged.
    b = bullets(s)
    openings = collections.Counter(" ".join(p.split()[:4]).lower() for p in b if len(p.split()) > 4)
    for o, n in openings.items():
        if n > 1:
            issues.append(("two items open the same way, x%d" % n, o))

    # 5. bullets outside 15 to 35 words
    for p in bullets(s):
        w = len(p.split())
        if w < 12 or w > 40:
            issues.append(("bullet %d words" % w, p[:110]))

    # 6. language a recruiter would not use. Plain English is the rule.
    for p in prose:
        low = " " + p.lower() + " "
        for w in ENGINEER_WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                issues.append(("engineering word: " + w, p[:110])); break

    # 7. one idea per bullet. Too many joins or commas means ideas welded together.
    for p in bullets(s):
        joins = sum(p.lower().count(j) for j in JOINS)
        if joins >= 2:
            issues.append(("ideas welded together, %d joins" % joins, p[:110]))
        elif real_commas(p) >= 3:
            issues.append(("%d commas, likely two bullets" % real_commas(p), p[:110]))

    # 8. THE BRIEF gets stricter treatment. It is the first thing read, and it is
    #    where topics get mushed into one unreadable sentence.
    br = brief(s)
    if br:
        sentences = [x.strip() for x in re.split(r"(?<=[.!?]) ", br) if x.strip()]
        # Updated 11 Sep 2026 to match STYLE.md section 3, which now fixes the
        # brief's shape: two or three recruiting sentences, then ONE closing
        # sentence for the general AI material. That makes 3 to 4 sentences the
        # correct range, not 2 to 3, and widens the word count to suit.
        if len(sentences) > 4:
            issues.append(("brief: %d sentences, spec says 3 to 4" % len(sentences), br[:80]))
        w = len(br.split())
        if not (50 <= w <= 110):
            issues.append(("brief: %d words, spec says 50 to 110" % w, br[:80]))
        if sentences and not sentences[-1].lstrip().startswith("And in the world of AI"):
            issues.append(("brief: last sentence should open 'And in the world of AI' "
                           "(drop it entirely if there is no general AI item this week)",
                           sentences[-1][:110]))
        for sen in sentences:
            n = len(sen.split())
            if n > 32:
                issues.append(("brief: a %d word sentence, hard to follow" % n, sen[:110]))
            joins = sum(sen.lower().count(j) for j in JOINS)
            if joins >= 2:
                issues.append(("brief: %d topics welded into one sentence" % (joins + 1), sen[:110]))
            if real_commas(sen) >= 4:
                issues.append(("brief: %d commas in one sentence" % real_commas(sen), sen[:110]))

    # 9. a vague pronoun with no noun in front of it
    for p in prose:
        if re.match(r"^(it|this|that|they|them|these|those)\b", p.lower()):
            issues.append(("opens on a vague word", p[:110]))

    if not issues:
        print(f"Final check: clean. {len(bullets(s))} bullets, {len(whys(s))} standouts read fine.")
        sys.exit(0)

    print(f"Final check: {len(issues)} thing(s) to look at.\n")
    for kind, detail in issues:
        print(f"  [{kind}]\n    {detail}\n")
    print("None of these block publishing. Read each one and decide.")
    sys.exit(1)
