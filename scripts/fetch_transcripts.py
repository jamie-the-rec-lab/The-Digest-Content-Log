#!/usr/bin/env python3
"""
Podcast transcript fetcher (cloud version, November 2026).

Lists a show's newest episodes from YouTube's official RSS feed, gets each new
episode's transcript from TranscriptAPI, and writes one markdown file per
episode into a per-show folder. Re-running skips episodes already saved, so
it's safe to run on a schedule to catch new episodes.

Transcripts include a clickable YouTube timecode at the start of every
paragraph, and a new paragraph wherever the captions mark a change of speaker.

Why not yt-dlp any more: YouTube bot-checks cloud addresses, and getting round
that is something this job does not do. The RSS feed is YouTube's own public
"what's new" list for feed readers, and TranscriptAPI is a paid supplier.
Nothing here talks to YouTube's video or caption servers.

Usage (unchanged, so nothing else in the pipeline had to change):
  python3 fetch_transcripts.py "<url>" "<Podcast Name>" [transcripts_root] [min_date] [scan_limit] [--backfill]
  url               the show's YouTube channel or playlist URL from sources.yaml:
                    .../channel/<UC id>/videos (or /streams), .../playlist?list=<id>,
                    or .../user/<name>/videos. A bare @handle is refused: put the
                    channel id in sources.yaml instead.
  transcripts_root  optional destination relative to library/, and it must
                    be "<collection>/transcripts" for one of the six known
                    collections (podcasts, tech, newsletters, reports,
                    news, adhoc). Default: "podcasts/transcripts".
                    Anything else is refused, nothing is written.
  min_date          optional YYYYMMDD cutoff; skips episodes older than this
  scan_limit        how many of the newest episodes to look at, default 10.
                    The feed only ever shows the newest 15, so that is the
                    ceiling.
  --backfill        not available in the cloud version: the feed cannot go
                    further back than 15 episodes. Accepted so old commands do
                    not break, and recorded so the health report sees it.

Needs: network access to www.youtube.com (feeds only) and transcriptapi.com,
with the TranscriptAPI key in the environment's network secrets. No key is read
or printed here; the environment adds it to each request.
"""

import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runlog

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # scripts/ sits one level down
LIBRARY_DIR = os.path.join(BASE_DIR, "library")

FEED_BASE = "https://www.youtube.com/feeds/videos.xml"
TRANSCRIPT_API = "https://transcriptapi.com/api/v2/youtube/transcript"

SCAN_LIMIT = 10      # a weekly run should never have more new episodes than this
SCAN_CEILING = 15    # the RSS feed only ever lists the newest 15 entries
PAUSE = 1.5          # seconds between transcript requests; nothing here is urgent
FRESH_HOURS = 12     # captions can lag a new upload by hours; younger than this
                     # with no transcript is "pending", not a failure

# The only collections build_index.py walks. A destination outside them is
# invisible to the rest of the pipeline, so writing there loses the episodes
# silently, which is exactly what happened on 3 Sep 2026.
KNOWN_COLLECTIONS = ("podcasts", "tech", "newsletters", "reports", "news", "adhoc")
LIST_RETRIES = 3     # a failed listing is usually a blip, so wait and retry
RETRY_WAIT = 20      # seconds, doubled each attempt

# Failures that waiting will never fix. Retrying these just burns the run's
# time, so fail fast and say why.
PERMANENT_FAILURES = (
    "video_unavailable",
    "not found or unavailable",
    "this video is private",
    "video unavailable",
    "members-only",
    "sign in to confirm",
)


class DestinationError(ValueError):
    """The destination argument does not name a known collection's transcripts
    folder. Fatal, and nothing is written."""


class ListingError(RuntimeError):
    """The feed could not be read. Transient, usually. Retry before concluding
    the feed is broken."""


class TranscriptError(RuntimeError):
    """TranscriptAPI could not return a transcript."""
    def __init__(self, message, status=None, code=None):
        super().__init__(message)
        self.status, self.code = status, code


def is_permanent(message):
    m = (message or "").lower()
    return any(marker in m for marker in PERMANENT_FAILURES)


def resolve_destination(raw_root):
    """Turn the destination argument into an absolute path, or refuse.

    Must be "<collection>/transcripts" for one of KNOWN_COLLECTIONS, relative
    to library/. Never falls back to the default, because a silent fallback is
    how 177 episodes were misfiled and nobody noticed.
    """
    cleaned = (raw_root or "").strip().strip("/")
    parts = [p for p in cleaned.replace("\\", "/").split("/") if p not in ("", ".")]
    if len(parts) == 2 and parts[0] in KNOWN_COLLECTIONS and parts[1] == "transcripts":
        return os.path.join(LIBRARY_DIR, parts[0], parts[1])
    raise DestinationError(
        f"invalid destination {raw_root!r}. Expected \"<collection>/transcripts\" "
        f"relative to library/, where <collection> is one of: "
        f"{', '.join(KNOWN_COLLECTIONS)} (e.g. \"podcasts/transcripts\"). "
        f"A bare show name is not a destination.")


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text).strip("-")[:80]


# ---------------------------------------------------------------- listing ---

def feed_url(url):
    """Map a sources.yaml YouTube URL to its official RSS feed."""
    u = urllib.parse.urlparse(url)
    q = urllib.parse.parse_qs(u.query)
    if "list" in q:
        return f"{FEED_BASE}?playlist_id={q['list'][0]}"
    m = re.search(r"/channel/UC([0-9A-Za-z_-]{22})(/streams)?", u.path)
    if m:
        # YouTube keeps hidden per-channel playlists that mirror the tabs:
        # UULF = the Videos tab (no Shorts), UULV = the Live tab. Same lists the
        # old fetcher read, so Shorts never cost a transcript request.
        return f"{FEED_BASE}?playlist_id={'UULV' if m.group(2) else 'UULF'}{m.group(1)}"
    m = re.search(r"/user/([^/]+)", u.path)
    if m:
        return f"{FEED_BASE}?user={m.group(1)}"
    raise ListingError(f"cannot turn {url!r} into a feed. Use the /channel/<UC id>/videos "
                       f"form in config/sources.yaml (a bare @handle has no feed address).")


def _get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": "TheRecLab-digest/1.0 (feed reader)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8")


def list_episodes(url, limit=SCAN_LIMIT):
    """Return [{id, title, date, channel, description}] newest first, from the
    feed. Raises ListingError if the feed could not be read, so an empty list
    means the source really is empty, not that the call broke."""
    try:
        xml = _get(feed_url(url))
    except urllib.error.HTTPError as e:
        raise ListingError(f"feed returned HTTP {e.code}")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise ListingError(f"feed unreachable: {e}")
    episodes = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        vid = re.search(r"<yt:videoId>(.*?)</yt:videoId>", entry)
        if not vid:
            continue
        def grab(pattern):
            m = re.search(pattern, entry, re.S)
            return html.unescape(m.group(1)).strip() if m else ""
        episodes.append({
            "id": vid.group(1),
            "title": grab(r"<title>(.*?)</title>"),
            "date": grab(r"<published>(\d{4}-\d{2}-\d{2})"),
            "published": grab(r"<published>(.*?)</published>"),
            "channel": grab(r"<author>\s*<name>(.*?)</name>"),
            "description": grab(r"<media:description>(.*?)</media:description>"),
        })
    episodes.sort(key=lambda e: e["date"], reverse=True)
    return episodes[:limit] if limit else episodes


def list_episodes_with_retry(url, limit=SCAN_LIMIT):
    """Speed does not matter here, this runs in the background. So wait and
    try again rather than reporting a working feed as broken."""
    wait = RETRY_WAIT
    for attempt in range(1, LIST_RETRIES + 1):
        try:
            return list_episodes(url, limit)
        except ListingError as e:
            if attempt == LIST_RETRIES or "cannot turn" in str(e):
                raise
            print(f"  listing failed ({e}), waiting {wait}s then retrying "
                  f"({attempt}/{LIST_RETRIES - 1})")
            time.sleep(wait)
            wait *= 2


# ------------------------------------------------------------- transcript ---

def get_transcript(video_id):
    """Return (segments, length_seconds, language) from TranscriptAPI.
    Retries once or twice on a rate limit or server error; never on anything
    permanent."""
    q = urllib.parse.urlencode({"video_url": f"https://www.youtube.com/watch?v={video_id}",
                                "format": "json"})
    wait = RETRY_WAIT
    for attempt in range(1, 4):
        try:
            d = json.loads(_get(f"{TRANSCRIPT_API}?{q}", timeout=120))
            return d.get("transcript") or [], d.get("length_seconds"), d.get("language", "")
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read().decode("utf-8", "replace")
                info = json.loads(body)
            except Exception:
                info = {}
            code = info.get("code") or ""
            detail = info.get("detail") or body[:200] or f"HTTP {e.code}"
            if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                print(f"    TranscriptAPI HTTP {e.code}, waiting {wait}s")
                time.sleep(wait)
                wait *= 2
                continue
            raise TranscriptError(f"{code or 'http_' + str(e.code)}: {detail}", e.code, code)
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < 3:
                time.sleep(wait)
                wait *= 2
                continue
            raise TranscriptError(f"unreachable: {e}")


def segments_to_paragraphs(segments):
    """Group caption segments into readable paragraphs, each tagged with its
    start second. A new paragraph starts at every '>>' (the captions' mark for a
    change of speaker), at a sentence end past 700 characters, or at a hard cap
    of 1200 characters (captions often lack punctuation)."""
    paras, cur, start, count = [], [], None, 0
    for sg in segments:
        txt = html.unescape(str(sg.get("text", ""))).replace("\n", " ").strip()
        txt = re.sub(r"\[.*?\]", "", txt).strip()        # [Music], [Applause]
        new_speaker = txt.startswith(">>")
        txt = txt.lstrip("> ").strip()
        if new_speaker and cur:
            paras.append((start, " ".join(cur)))
            cur, start, count = [], None, 0
        if not txt:
            continue
        if start is None:
            start = int(float(sg.get("start", 0)))
        cur.append(txt)
        count += len(txt) + 1
        if (count > 700 and txt.endswith((".", "?", "!"))) or count > 1200:
            paras.append((start, " ".join(cur)))
            cur, start, count = [], None, 0
    if cur:
        paras.append((start or 0, " ".join(cur)))
    return paras


def _fmt_ts(secs):
    secs = int(secs or 0)
    h, rem = divmod(secs, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def hours_old(ep):
    """Hours since the feed says the episode was published. Unknown counts as old,
    so a missing timestamp can never hide a real failure."""
    try:
        pub = datetime.fromisoformat(ep.get("published", "").replace("Z", "+00:00"))
        return (datetime.now(pub.tzinfo) - pub).total_seconds() / 3600
    except (ValueError, TypeError):
        return 1e9


# ------------------------------------------------------------------ save ---

def already_saved(title, dest_dir, teaser_dir):
    """Fast skip: the filename is keyed off the title slug, so an episode saved
    before (by this script or the old yt-dlp one) is found with no network call.
    Skip only if it already has timecode links; otherwise re-fetch and upgrade.
    Reads the whole file: a summary block above the title can push the first
    timecode past any fixed window (the 4 Sep 2026 fault)."""
    slug = slugify(title)
    for scan_dir in (dest_dir, teaser_dir):
        if not os.path.isdir(scan_dir):
            continue
        for existing in os.listdir(scan_dir):
            if existing.endswith(f"-{slug}.md"):
                body = open(os.path.join(scan_dir, existing), encoding="utf-8").read()
                return "&t=" in body
    return False


def fetch_one(ep, dest_dir, min_date=None):
    # Teasers, trailers and short promo clips live in a sibling "_teasers/<Show>"
    # folder that build_index ignores, so they never flag as missing summaries.
    teaser_dir = os.path.join(os.path.dirname(dest_dir), "_teasers", os.path.basename(dest_dir))
    title = ep["title"] or ep["id"]

    if already_saved(title, dest_dir, teaser_dir):
        return ("skip", title, None)
    # Date gate before spending a transcript request.
    if min_date and ep["date"] and ep["date"].replace("-", "") < min_date:
        return ("old", title, None)

    try:
        segments, length, lang = get_transcript(ep["id"])
    except TranscriptError as e:
        if e.code in ("live_not_started", "live_in_progress", "upcoming"):
            return ("upcoming", title, "live stream not aired yet")
        if hours_old(ep) < FRESH_HOURS:
            return ("pending", title, f"released {hours_old(ep):.0f}h ago, captions not ready")
        status = "gone" if is_permanent(str(e)) else "failed"
        return (status, title, str(e))
    paragraphs = segments_to_paragraphs(segments)
    if not paragraphs:
        if hours_old(ep) < FRESH_HOURS:
            return ("pending", title, f"released {hours_old(ep):.0f}h ago, captions not ready")
        return ("nosubs", title, None)

    url = f"https://www.youtube.com/watch?v={ep['id']}"
    date = ep["date"]
    fname = f"{date or '0000'}-{slugify(title)}.md"
    wordcount = sum(len(t.split()) for _, t in paragraphs)
    lt = title.lower()
    is_teaser = ("trailer" in lt) or ("preview" in lt) or ("#shorts" in lt) or (wordcount < 700)
    target_dir = teaser_dir if is_teaser else dest_dir
    os.makedirs(target_dir, exist_ok=True)
    fpath = os.path.join(target_dir, fname)
    if not is_teaser:
        # run_check uses this to confirm everything saved this run also got
        # summarised.
        runlog.record("saved", path=fpath)

    # A rewrite must never destroy hand-written archive work. If this file
    # already exists and carries a SUMMARY block, lift it out first and put it
    # back on top of the fresh transcript.
    preserved_summary = ""
    if os.path.exists(fpath):
        prior = open(fpath, encoding="utf-8").read()
        m = re.search(r"<!--SUMMARY-->.*?<!--/SUMMARY-->", prior, re.S)
        if m:
            preserved_summary = m.group(0) + "\n\n"
            runlog.record("summary_preserved", path=fpath)

    # A record with no date is invisible to every date-based rule. Still save
    # it, never throw work away, but say so.
    if not date:
        runlog.record("missing_date", path=fpath, title=title, url=url)

    duration = _fmt_ts(length) if length else _fmt_ts(segments[-1].get("start", 0) if segments else 0)
    with open(fpath, "w", encoding="utf-8") as f:
        if preserved_summary:
            f.write(preserved_summary)
        f.write(f"# {title}\n\n")
        f.write(f"- **Podcast:** {os.path.basename(dest_dir)}\n")
        f.write(f"- **Channel:** {ep.get('channel', '')}\n")
        f.write(f"- **Date:** {date}\n")
        f.write(f"- **Duration:** {duration}\n")
        f.write(f"- **URL:** {url}\n")
        f.write(f"- **Fetched:** {datetime.now():%Y-%m-%d}\n")
        f.write(f"- **Source:** YouTube captions via TranscriptAPI ({lang})\n\n")
        desc = ep.get("description", "")
        if desc:
            f.write("## Episode description\n\n" + desc[:1500] + "\n\n")
        f.write("## Transcript\n\n")
        f.write("Each paragraph starts with a timecode linking to that moment on YouTube. "
                "A new paragraph marks a change of speaker where the captions show one "
                "(speaker names are not available).\n\n")
        for start, text in paragraphs:
            f.write(f"**[{_fmt_ts(start)}]({url}&t={start}s)** {text}\n\n")
    return (("teaser" if is_teaser else "saved"), title, None)


# ------------------------------------------------------------------ main ---

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    argv = [a for a in sys.argv[1:] if a != "--backfill"]
    backfill = "--backfill" in sys.argv[1:]
    url, podcast = argv[0], argv[1]
    raw_root = argv[2] if len(argv) > 2 else "podcasts/transcripts"
    # GUARD 1: refuse anything that is not a known collection's transcripts
    # folder. Exit non-zero, write nothing, do not fall back to the default.
    try:
        root = resolve_destination(raw_root)
    except DestinationError as e:
        runlog.record("fetch", source=podcast, outcome="bad_destination",
                      destination=raw_root, detail=str(e)[:300])
        print(f"{podcast}: REFUSED, {e}")
        sys.exit(3)
    min_date = argv[3] if len(argv) > 3 and argv[3] not in ("", "-") else None
    raw = argv[4] if len(argv) > 4 else str(SCAN_LIMIT)
    scan_limit = SCAN_CEILING if raw.lower() in ("all", "0") else int(raw)
    # GUARD 2: the feed only goes back 15 episodes. Anything more, including a
    # backfill, is clamped and recorded so the health report can see it.
    clamped = False
    if backfill or scan_limit > SCAN_CEILING or raw.lower() in ("all", "0"):
        clamped = True
        print(f"{podcast}: asked for {raw}{' with --backfill' if backfill else ''}, but the feed "
              f"only lists the newest {SCAN_CEILING}. A deeper backfill needs a different "
              f"source and is a deliberate job, not part of a weekly run.")
        runlog.record("fetch", source=podcast, outcome="scan_limit_clamped",
                      requested=raw, ceiling=SCAN_CEILING, applied=SCAN_CEILING)
        scan_limit = SCAN_CEILING
    dest = os.path.join(root, podcast)
    os.makedirs(dest, exist_ok=True)

    try:
        eps = list_episodes_with_retry(url, scan_limit)
    except ListingError as e:
        # A failed listing is NOT the same as an empty source.
        runlog.record("fetch", source=podcast, outcome="listing_failed", detail=str(e)[:200])
        print(f"{podcast}: LISTING FAILED, retry before assuming it is broken. {e}")
        sys.exit(2)
    print(f"{podcast}: found {len(eps)} videos")
    if not eps:
        print(f"{podcast}: the feed read cleanly and is genuinely empty. "
              f"Likely a renamed or private channel.")
    counts, failures, pending = {}, [], []
    for i, ep in enumerate(eps, 1):
        status, title, detail = fetch_one(ep, dest, min_date=min_date)
        counts[status] = counts.get(status, 0) + 1
        print(f"  [{i}/{len(eps)}] {status:6} {title[:60]}" + (f"  ({detail[:80]})" if detail else ""))
        if status == "pending":
            pending.append(title)
            runlog.record("captions_pending", source=podcast, title=title[:80], id=ep["id"],
                          published=ep.get("published", ""))
        if status in ("failed", "gone"):
            failures.append({"title": title[:80], "id": ep["id"], "detail": (detail or "")[:160],
                             "permanent": status == "gone"})
        if status not in ("skip", "old", "upcoming"):
            time.sleep(PAUSE)
    # If nothing was skipped, every episode listed was new, so there may be
    # more beyond the list. Say so loudly rather than let it pass.
    hit_limit = bool(scan_limit and counts.get("saved", 0) >= scan_limit)
    if hit_limit:
        print(f"{podcast}: WARNING, all {scan_limit} listed episodes were new. "
              f"There may be more past what the feed shows.")
    for fl in failures:
        runlog.record("transcript_failed", source=podcast, **fl)
    runlog.record("fetch", source=podcast, outcome="ok" if eps else "listed_empty",
                  saved=counts.get("saved", 0), skipped=counts.get("skip", 0),
                  failed=len(failures), pending=len(pending), destination=raw_root, scan_limit=scan_limit,
                  backfill=backfill, clamped=clamped,
                  more_beyond_limit=hit_limit, hit_limit=hit_limit)
    print(f"Done. {dict(counts)}")


if __name__ == "__main__":
    main()
