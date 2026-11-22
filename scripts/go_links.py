#!/usr/bin/env python3
"""
Aggregate click counting for the digest email (since 22 November 2026).

Every outside link on an edition's page gets a number, in reading order. The
email sends readers to https://thereclab.ai/go/v<N>/<n>; that page records an
anonymous page view in Vercel Web Analytics and forwards to link <n>. Nothing in
the email identifies the reader, so clicks are counted in total, never per person.

  python3 scripts/go_links.py <edition.html> <site_repo_dir>
    writes <site_repo_dir>/go/v<N>.json   (number -> link; the site forwards from it)
    and    digest/go/v<N>.json            (this repo's copy; build_email.py reads it)

The page forwards ONLY to links in that file, so the counter cannot be used to
send people to an arbitrary address.
"""
import json, os, re, sys
from bs4 import BeautifulSoup

SITE = "https://thereclab.ai"


def edition_version(soup):
    d = soup.select_one(".date")
    m = re.search(r"Version\s+(\d+)", d.get_text(" ", strip=True) if d else "")
    if not m:
        sys.exit("go_links: no 'Version N' on the page, so no file written")
    return "v" + m.group(1)


def page_links(soup):
    """Outside https links, in reading order, each once."""
    seen, out = set(), []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href.startswith("https://"):
            continue
        host = re.sub(r"^https://(www\.)?", "", href).split("/")[0]
        if host == "thereclab.ai":
            continue
        if href not in seen:
            seen.add(href)
            out.append(href)
    return out


def build_map(html):
    soup = BeautifulSoup(html, "html.parser")
    links = page_links(soup)
    return edition_version(soup), {str(i + 1): u for i, u in enumerate(links)}


def go_url(version, n):
    return f"{SITE}/go/{version}/{n}"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    version, m = build_map(open(sys.argv[1], encoding="utf-8").read())
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for path in (os.path.join(sys.argv[2], "go", version + ".json"),
                 os.path.join(here, "digest", "go", version + ".json")):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(m, f, indent=1)
            f.write("\n")
        print(f"wrote {path} ({len(m)} links)")
