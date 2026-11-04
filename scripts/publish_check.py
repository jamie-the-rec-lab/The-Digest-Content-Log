#!/usr/bin/env python3
"""
Structural checks on a finished digest, before it goes live.

`final_check.py` asks whether it reads well. This asks whether it is BUILT
right: the rules from STYLE.md, SELECTION.md and READER.md that a person would
otherwise catch by eye. With nobody in the loop, every one of those needs a
check somewhere.

    python3 scripts/publish_check.py digest/builds/<file>.html [--public] [--links]

    --public   the copy about to be committed. Adds the checks that only matter
               for what readers see, above all that no Gmail links survived.
    --links    actually request every link and report anything that fails.
               Slower, needs network. Worth it on the public copy.

Exit 0 clean, exit 1 if anything needs a look.
"""

import re, sys, html, datetime, argparse, urllib.request, urllib.error

WINDOW_WEEKS = 8
SECTIONS = ["Recruiting Podcasts", "Recruiting Newsletters",
            "Recruiting reports, product updates, and more", "AI &amp; Tech Picks"]
BRANDS = {"10x Recruiting": "by Metaview", "Offer Accepted": "by Ashby",
          "Recruiting Roadshow": "by Greenhouse", "How I AI": "by Lenny",
          "AI &amp; I": "by Every"}
NEVER_ON_PAGE = ["RecOps Collective", "Elite Recruiter", "Recruitment Mentors"]
MARKETS = ["uk", "us", "eu", "emea", "european", "britain", "british", "america",
           "global", "worldwide", "england", "london", "ireland", "germany"]
MONTHS = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"


def txt(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


def articles(s):
    """(section label, src, date, title, guest, [bullets]) per item."""
    out = []
    for sec in re.finditer(r'<span class="lbl">(.*?)</span>.*?<div class="sbody">(.*?)\n  </div>', s, re.S):
        label = sec.group(1)
        for a in re.finditer(r"<article[^>]*>(.*?)</article>", sec.group(2), re.S):
            body = a.group(1)
            src = re.search(r'<span class="src">(.*?)</span>', body, re.S)
            cd = re.search(r'<span class="cdate">(.*?)</span>', body, re.S)
            ttl = re.search(r'<a class="ttl"[^>]*>(.*?)</a>', body, re.S)
            vg = re.search(r'<div class="vgroup-title">(.*?)</div>', body, re.S)
            guest = re.search(r'<div class="guest">(.*?)</div>', body, re.S)
            pts = re.findall(r"<li>(.*?)</li>", body, re.S)
            out.append({"section": label,
                        "src": src.group(1) if src else "",
                        "date": txt(cd.group(1)) if cd else "",
                        "title": txt(ttl.group(1)) if ttl else (txt(vg.group(1)) if vg else ""),
                        "guest": txt(guest.group(1)) if guest else None,
                        "bullets": [txt(p) for p in pts],
                        "grouped": bool(vg)})
    return out


def parse_date(d):
    for fmt in ("%d %b %Y", "%b %Y"):
        try:
            return datetime.datetime.strptime(d, fmt).date()
        except ValueError:
            pass
    return None


def check(path, public, do_links):
    s = open(path, encoding="utf-8").read()
    arts = articles(s)
    bad = []
    today = datetime.date.today()

    # ---- what readers see -------------------------------------------------
    if public:
        for m in re.findall(r'href="(https://mail\.google\.com[^"]*)"', s):
            bad.append(("GMAIL LINK ON THE PUBLIC PAGE", m))
        if "_TRIAL" in path:
            bad.append(("trial file", "this is a trial build, not for publishing"))

    # ---- structure --------------------------------------------------------
    labels = re.findall(r'<span class="lbl">(.*?)</span>', s)
    for l in labels:
        if l not in SECTIONS:
            bad.append(("section label reworded", l))
    if labels != [x for x in SECTIONS if x in labels]:
        bad.append(("sections out of order", " | ".join(labels)))

    for sec in re.finditer(r'<span class="lbl">(.*?)</span><span class="cnt">(\d+)</span>(.*?)\n  </div>', s, re.S):
        actual = len(re.findall(r"<article", sec.group(3)))
        if int(sec.group(2)) != actual:
            bad.append(("count says %s, actually %d" % (sec.group(2), actual), sec.group(1)))

    # ---- per item ---------------------------------------------------------
    seen_dates = {}
    for a in arts:
        who = f"{txt(a['src'])}: {a['title'][:44]}"

        if not a["grouped"] and not (2 <= len(a["bullets"]) <= 3):
            bad.append(("%d bullets, should be 2 or 3" % len(a["bullets"]), who))

        if re.search(r"\b(Ep|Episode)\s*\.?\s*\d+\s*[:\-]", a["title"], re.I):
            bad.append(("episode number left in the title", a["title"][:70]))

        if a["date"] and not re.fullmatch(r"(\d{1,2} )?(%s) \d{4}" % MONTHS, a["date"]):
            bad.append(("date format", f"{who} -> {a['date']}"))

        d = parse_date(a["date"])
        if d and (today - d).days > WINDOW_WEEKS * 7 + 31:
            bad.append(("older than the %d week window" % WINDOW_WEEKS, f"{who} -> {a['date']}"))
        if d:
            seen_dates.setdefault(a["section"], []).append((d, who))

        if a["guest"] is not None and not re.search(r".+ · .+ @ .+", a["guest"]):
            bad.append(("guest line format", a["guest"][:70]))

        src_plain = txt(a["src"])
        for show, credit in BRANDS.items():
            plain_show = html.unescape(show)
            if src_plain.startswith(plain_show) and credit.replace("by ", "") not in src_plain:
                bad.append(("missing brand credit, expected '%s'" % credit, src_plain))
        for never in NEVER_ON_PAGE:
            if never in src_plain:
                bad.append(("library name on the page, use the display name", src_plain))

        # Market data has to say which market. This applies to REPORTS and NEWS,
        # where a figure describes a market. A figure about one company, like
        # "SentiLink hired 60% more", is not market data and needs no label.
        if re.search(r"·\s*(report|news)", src_plain):
            for b in a["bullets"]:
                if re.search(r"[£$€]\s?[\d,]|(\d+(\.\d+)?%)", b):
                    if not any(re.search(r"\b" + m, b.lower()) for m in MARKETS):
                        bad.append(("market figure with no market named", b[:100]))

    # Freshest first inside each section, EXCEPT the reports section.
    #
    # Added 3 Sep 2026. This rule fired on that section every single week,
    # including on the published v1, because SELECTION.md orders it by TYPE
    # (reports, then events, then launches, then essays) and not by date. Two
    # deliberate rules that cannot both hold. A check that always fails is not a
    # check: it trains everyone to skim past it, and the week a real ordering
    # problem shows up it looks exactly like the usual noise.
    #
    # Stated positively, only these sections are genuinely date-ordered.
    # Match SECTIONS above, which carries the label exactly as it appears in the
    # HTML, so the ampersand is escaped. Getting this wrong would silently stop
    # checking the tech section rather than failing loudly.
    DATE_ORDERED = ("Recruiting Podcasts", "Recruiting Newsletters", "AI &amp; Tech Picks")
    assert all(x in SECTIONS for x in DATE_ORDERED), "DATE_ORDERED drifted from SECTIONS"
    for sec, ds in seen_dates.items():
        if sec not in DATE_ORDERED:
            continue
        if ds != sorted(ds, key=lambda x: x[0], reverse=True):
            bad.append(("not freshest first", sec))

    # ---- selection rules --------------------------------------------------
    launches = [a for a in arts if "· launch" in txt(a["src"])]
    vendors = {txt(a["src"]).split("·")[0].strip() for a in launches}
    if len(vendors) > 2:
        bad.append(("%d launch blocks, maximum is 2" % len(vendors), ", ".join(sorted(vendors))))

    pod_standout = re.search(r'<span class="pick">Podcast</span>.*?<a[^>]*>(.*?)</a>', s, re.S)
    if pod_standout and "Brainfood" in pod_standout.group(1):
        bad.append(("Brainfood as the podcast standout", "never allowed, see SELECTION.md"))

    # ---- links ------------------------------------------------------------
    if do_links:
        urls = sorted(set(re.findall(r'href="(https?://[^"]+)"', s)))
        urls = [u for u in urls if "mail.google.com" not in u]
        for u in urls:
            try:
                r = urllib.request.Request(u, method="HEAD",
                                           headers={"User-Agent": "Mozilla/5.0"})
                code = urllib.request.urlopen(r, timeout=12).status
                if code >= 400:
                    bad.append(("link returns %d" % code, u))
            except urllib.error.HTTPError as e:
                if e.code not in (403, 405, 429):   # bot blocks, not broken links
                    bad.append(("link returns %d" % e.code, u))
            except Exception as e:
                bad.append(("link failed: %s" % type(e).__name__, u))

    return arts, bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("digest")
    ap.add_argument("--public", action="store_true")
    ap.add_argument("--links", action="store_true")
    a = ap.parse_args()
    arts, bad = check(a.digest, a.public, a.links)
    if not bad:
        print(f"Publish check: clean. {len(arts)} items across "
              f"{len(set(x['section'] for x in arts))} sections.")
        sys.exit(0)
    print(f"Publish check: {len(bad)} thing(s) to look at.\n")
    for kind, detail in bad:
        print(f"  [{kind}]\n    {detail}\n")
    sys.exit(1)
