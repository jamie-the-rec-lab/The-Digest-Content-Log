#!/usr/bin/env python3
"""
Podcast transcript fetcher.

Pulls YouTube auto-captions for every episode of a channel/playlist,
cleans them into readable prose, and writes one markdown file per
episode into a per-podcast folder. Re-running skips episodes already
saved, so it's safe to run on a schedule to catch new episodes.

Transcripts include a clickable YouTube timecode at the start of every
paragraph.

Usage:
    python3 fetch_transcripts.py "<url>" "<Podcast Name>" [transcripts_root] [min_date] [scan_limit] [--backfill]
      transcripts_root  optional destination relative to library/, and it must
                        be "<collection>/transcripts" for one of the six known
                        collections (podcasts, tech, newsletters, reports,
                        news, adhoc). Default: "podcasts/transcripts".
                        Anything else is refused, nothing is written.
      min_date          optional YYYYMMDD cutoff; skips episodes older than
                        this (newest-first, stops once well past the cutoff)
      scan_limit        how many of the newest episodes to LIST, default 10.
                        Capped at SCAN_CEILING (50) unless --backfill is passed;
                        without it a bigger request is clamped and recorded.
      --backfill        opt in to scanning past the ceiling ("all" or >50).
                        A deliberate backfill job, never a weekly run.
"""

import html
import json
import os
import re
import subprocess, time
import sys
from datetime import datetime

# Folder where transcripts live. When run in the sandbox this maps to
# the user's "Podcast Project" folder.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import runlog

def _resolve_ytdlp():
    """Find a working yt-dlp, however it happens to be installed.

    The machine this runs on does not always keep installed packages between
    runs, and when pip does install it the binary can land somewhere that is
    not on PATH. So: try the command, then the module, then install and try
    the module again. Returns the command prefix as a list.
    """
    import shutil
    # Added 9 Oct 2026. --impersonate needs curl_cffi; the workspace resets each
    # run, so make sure it is present or every caption fetch is 429-blocked.
    try:
        import curl_cffi  # noqa: F401
    except ImportError:
        print("curl_cffi missing, installing yt-dlp[default,curl-cffi]...", flush=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                        "--break-system-packages", "yt-dlp[default,curl-cffi]"],
                       capture_output=True, text=True)
    if shutil.which("yt-dlp"):
        return ["yt-dlp"]
    probe = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                           capture_output=True, text=True)
    if probe.returncode == 0:
        return [sys.executable, "-m", "yt_dlp"]
    print("yt-dlp not found, installing it...", flush=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                    "--break-system-packages", "yt-dlp"],
                   capture_output=True, text=True)
    probe = subprocess.run([sys.executable, "-m", "yt_dlp", "--version"],
                           capture_output=True, text=True)
    if probe.returncode == 0:
        return [sys.executable, "-m", "yt_dlp"]
    sys.exit("FATAL: yt-dlp is not available and could not be installed. "
             "No transcripts can be fetched. Stop the run and report this.")


YTDLP = _resolve_ytdlp()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # scripts/ sits one level down
LIBRARY_DIR = os.path.join(BASE_DIR, "library")
TRANSCRIPTS_DIR = os.path.join(LIBRARY_DIR, "podcasts", "transcripts")


def resolve_destination(raw_root):
    """Turn the destination argument into an absolute path, or refuse.

    Must be "<collection>/transcripts" for one of KNOWN_COLLECTIONS, relative
    to library/. Returns the absolute path. Raises DestinationError otherwise:
    never falls back to the default, because a silent fallback is how 177
    episodes were misfiled and nobody noticed.
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


class DestinationError(ValueError):
    """The destination argument does not name a known collection's transcripts
    folder. Fatal, and nothing is written."""


class ListingError(RuntimeError):
    """yt-dlp could not list the source. Transient, usually. Retry before
    concluding the feed is broken."""


SCAN_LIMIT = 10       # a weekly run should never have more new episodes than this
SCAN_CEILING = 50     # hard ceiling on how many episodes one run will LIST.
                      # A weekly run escalating to 100+ pulled months of back
                      # catalogue on 3 Sep 2026. Past this needs --backfill.

# The only collections build_index.py walks. A destination outside them is
# invisible to the rest of the pipeline, so writing there loses the episodes
# silently, which is exactly what happened on 3 Sep 2026.
KNOWN_COLLECTIONS = ("podcasts", "tech", "newsletters", "reports", "news", "adhoc")
LIST_RETRIES = 3      # a failed listing is usually a rate limit, so wait and retry
RETRY_WAIT = 20       # seconds, doubled each attempt

# Failures that waiting will never fix. A rate limit clears by itself; a bot
# check does not, it wants credentials we deliberately do not supply. Tested
# 27 Aug 2026: a datacentre IP is refused on the first request, every time.
# Retrying these just burns the run's time, so fail fast and say why.
PERMANENT_FAILURES = (
    "sign in to confirm",
    "confirm you\u2019re not a bot",
    "confirm you're not a bot",
    "this video is private",
    "video unavailable",
    "members-only",
)


def is_permanent(message):
    m = (message or "").lower()
    return any(marker in m for marker in PERMANENT_FAILURES)


def list_episodes(url, limit=SCAN_LIMIT):
    """Return a list of {id, title} for every video on the channel/playlist.

    Raises ListingError if yt-dlp itself failed. An empty list therefore means
    the source really is empty, not that the call broke. Without this, a rate
    limit and a dead channel both looked like "found 0 videos", and the health
    report could not tell a real break from a blip.
    """
    cmd = YTDLP + ["--flat-playlist", "--dump-json"]
    if limit:
        # Only list the newest N. YouTube lists newest first, so a weekly run
        # never needs more, and this turns a 456-video walk into one short call.
        cmd += ["--playlist-end", str(limit)]
    out = subprocess.run(cmd + [url], capture_output=True, text=True)
    episodes = []
    for line in out.stdout.strip().splitlines():
        try:
            d = json.loads(line)
            episodes.append({"id": d["id"], "title": d.get("title", d["id"])})
        except (json.JSONDecodeError, KeyError):
            continue
    if not episodes and out.returncode != 0:
        err = (out.stderr or "").strip().splitlines()
        raise ListingError(err[-1] if err else f"yt-dlp exited {out.returncode}")
    return episodes


def list_episodes_with_retry(url, limit=SCAN_LIMIT):
    """Speed does not matter here, this runs in the background. So wait and try
    again rather than reporting a working feed as broken."""
    wait = RETRY_WAIT
    for attempt in range(1, LIST_RETRIES + 1):
        try:
            return list_episodes(url, limit)
        except ListingError as e:
            if is_permanent(str(e)):
                print(f"  listing failed permanently ({e}). Not retrying: "
                      f"waiting cannot fix this one.")
                raise
            if attempt == LIST_RETRIES:
                raise
            print(f"  listing failed ({e}), waiting {wait}s then retrying "
                  f"({attempt}/{LIST_RETRIES - 1})")
            time.sleep(wait)
            wait *= 2


def meta_from_info(d):
    """Build our metadata dict from a yt-dlp info-json dict."""
    raw = d.get("upload_date", "")
    date = f"{raw[:4]}-{raw[4:6]}-{raw[6:]}" if len(raw) == 8 else ""
    return {
        "title": d.get("title", ""),
        "date": date,
        "channel": d.get("channel", d.get("uploader", "")),
        "duration": d.get("duration_string", ""),
        "url": d.get("webpage_url", ""),
        "description": (d.get("description") or "").strip(),
    }


def _ts_to_secs(t):
    """'00:14:32.120' -> 872 (int seconds)."""
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + int(float(s))


def parse_vtt(vtt_path):
    """Return de-duplicated [(start_seconds, text_line), ...] preserving cue timing."""
    blocks, cur_time = [], None
    with open(vtt_path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = re.match(r"(\d\d:\d\d:\d\d\.\d+)\s*-->", line)
            if m:
                cur_time = _ts_to_secs(m.group(1))
                continue
            if line.strip() in ("WEBVTT", "") or line.startswith(("Kind:", "Language:")):
                continue
            txt = re.sub(r"<[^>]+>", "", line)        # inline timing tags
            txt = html.unescape(txt)                   # &gt;&gt; -> >>, &amp; -> &
            txt = re.sub(r"\[.*?\]", "", txt).strip()  # [Music] etc
            if txt and cur_time is not None:
                blocks.append((cur_time, txt))
    deduped = []
    for t, txt in blocks:
        if not deduped or deduped[-1][1] != txt:
            deduped.append((t, txt))
    return deduped


def vtt_to_paragraphs(vtt_path):
    """Group caption lines into ~700-char paragraphs, each tagged with its start second."""
    blocks = parse_vtt(vtt_path)
    paras, cur, start, count = [], [], None, 0
    for t, txt in blocks:
        if start is None:
            start = t
        cur.append(txt)
        count += len(txt) + 1
        # break at a sentence end past 700 chars, or hard-cap at 1200 (captions
        # often lack punctuation, so the hard cap stops runaway paragraphs)
        if (count > 700 and txt.endswith((".", "?", "!"))) or count > 1200:
            paras.append((start, " ".join(cur)))
            cur, start, count = [], None, 0
    if cur:
        paras.append((start or 0, " ".join(cur)))
    return paras


def _fmt_ts(secs):
    h, rem = divmod(secs, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fetch_one(video_id, title_hint, dest_dir, min_date=None):
    # Teasers/trailers/short promo clips live in a sibling "_teasers/<Show>"
    # folder that build_index ignores, so they never flag as missing summaries.
    teaser_dir = os.path.join(os.path.dirname(dest_dir), "_teasers", os.path.basename(dest_dir))

    # Fast skip: filename is keyed off the title slug only, so we can detect an
    # already-saved episode (in either the show or teaser folder) with no network call.
    if title_hint:
        for scan_dir in (dest_dir, teaser_dir):
            if not os.path.isdir(scan_dir):
                continue
            for existing in os.listdir(scan_dir):
                if existing.endswith(f"-{slugify(title_hint)}.md"):
                    # Already saved. Skip only if it already has timecode links;
                    # otherwise fall through to re-fetch and upgrade it in place.
                    #
                    # Fixed 4 Sep 2026. This used to read only the first 4000
                    # bytes. A SUMMARY_SPEC block is 250 to 450 words and sits
                    # ABOVE the title, which pushes the first timecode link past
                    # that window. The fetcher then decided the file needed
                    # upgrading, re-fetched it, and overwrote the summary. In
                    # other words, writing a good summary made the file a target
                    # for having that summary destroyed, and the longer the
                    # summary the likelier it was. Six were lost this way before
                    # it was spotted. Read the whole file: these are ~50KB.
                    existing_path = os.path.join(scan_dir, existing)
                    body = open(existing_path, encoding="utf-8").read()
                    if "&t=" in body:
                        return ("skip", title_hint)
                    break

    tmp = f"/tmp/{video_id}"
    # One call: write subtitles AND the info-json, so we avoid a second
    # round-trip just to read metadata.
    subprocess.run(
        YTDLP + ["--impersonate", "chrome", "--sleep-subtitles", "3",
         "--write-auto-subs", "--write-subs", "--sub-langs", "en.*",
         "--sub-format", "vtt", "--skip-download", "--convert-subs", "vtt",
         "--write-info-json",
         "-o", f"{tmp}.%(ext)s", f"https://www.youtube.com/watch?v={video_id}"],
        capture_output=True, text=True,
    )
    # Added 7 Oct 2026. YouTube now 429s the "en" track on some videos while
    # "en-orig" (the original auto captions) downloads fine, and the 429 aborts
    # the whole call, which used to be logged as "nosubs". Retry en-orig alone.
    if not any(os.path.exists(f"{tmp}.{l}.vtt") for l in ("en", "en-orig")):
        subprocess.run(
            YTDLP + ["--impersonate", "chrome", "--write-auto-subs",
             "--sub-langs", "en-orig", "--sub-format", "vtt", "--skip-download",
             "--write-info-json",
             "-o", f"{tmp}.%(ext)s", f"https://www.youtube.com/watch?v={video_id}"],
            capture_output=True, text=True,
        )
    meta = {}
    if os.path.exists(f"{tmp}.info.json"):
        with open(f"{tmp}.info.json", encoding="utf-8") as f:
            meta = meta_from_info(json.load(f))
        os.remove(f"{tmp}.info.json")
    title = meta.get("title") or title_hint or video_id
    # date gate (for back-catalogue slicing, e.g. only 2024 onwards)
    if min_date and meta.get("date") and meta["date"].replace("-", "") < min_date:
        for cand in (f"{tmp}.en.vtt", f"{tmp}.en-orig.vtt"):
            if os.path.exists(cand):
                os.remove(cand)
        return ("old", title)
    fname = f"{meta.get('date','0000')}-{slugify(title)}.md"

    # prefer manual en, fall back to auto en-orig
    vtt = None
    for cand in (f"{tmp}.en.vtt", f"{tmp}.en-orig.vtt"):
        if os.path.exists(cand):
            vtt = cand
            break
    if not vtt:
        return ("nosubs", title)

    base_url = meta.get("url", "") or f"https://www.youtube.com/watch?v={video_id}"
    sep = "&" if "?" in base_url else "?"
    paragraphs = vtt_to_paragraphs(vtt)
    # Route trailers/previews and very short promo clips into the ignored
    # "_teasers/<Show>" folder so they never pollute the index.
    wordcount = sum(len(t.split()) for _, t in paragraphs)
    lt = title.lower()
    is_teaser = ("trailer" in lt) or ("preview" in lt) or (wordcount < 700)
    target_dir = teaser_dir if is_teaser else dest_dir
    os.makedirs(target_dir, exist_ok=True)
    fpath = os.path.join(target_dir, fname)
    if not is_teaser:
        # Recorded here, where the real filename exists. run_check uses this to
        # confirm everything saved this run also got summarised. Reconstructing
        # the name outside this function was fragile and got it wrong.
        runlog.record("saved", path=fpath)
    # Added 4 Sep 2026. A rewrite must never destroy hand-written archive work.
    # If this file already exists and carries a SUMMARY_SPEC block, lift the
    # block out first and put it back on top of the fresh transcript. The
    # transcript is cheap and reproducible; the summary is not, and it is the
    # thing the library exists for.
    preserved_summary = ""
    if os.path.exists(fpath):
        prior = open(fpath, encoding="utf-8").read()
        m = re.search(r"<!--SUMMARY-->.*?<!--/SUMMARY-->", prior, re.S)
        if m:
            preserved_summary = m.group(0) + "\n\n"
            runlog.record("summary_preserved", path=fpath)

    # A record with no date is invisible to every date-based rule we have:
    # selection, the freshness window, the no-going-backwards check. It used to
    # be written silently as "0000-" and nothing flagged it. Three turned up on
    # 4 Sep 2026. Still save the transcript, never throw work away, but say so.
    if not meta.get("date"):
        runlog.record("missing_date", path=fpath, title=title, url=meta.get("url", ""))

    with open(fpath, "w", encoding="utf-8") as f:
        if preserved_summary:
            f.write(preserved_summary)
        f.write(f"# {title}\n\n")
        f.write(f"- **Podcast:** {os.path.basename(dest_dir)}\n")
        f.write(f"- **Channel:** {meta.get('channel','')}\n")
        f.write(f"- **Date:** {meta.get('date','')}\n")
        f.write(f"- **Duration:** {meta.get('duration','')}\n")
        f.write(f"- **URL:** {meta.get('url','')}\n")
        f.write(f"- **Fetched:** {datetime.now():%Y-%m-%d}\n\n")
        desc = meta.get("description", "")
        if desc:
            f.write("## Episode description\n\n" + desc[:1500] + "\n\n")
        f.write("## Transcript\n\n")
        f.write("Each paragraph starts with a timecode linking to that moment on YouTube.\n\n")
        for start, text in paragraphs:
            f.write(f"**[{_fmt_ts(start)}]({base_url}{sep}t={start}s)** {text}\n\n")
    for cand in (f"{tmp}.en.vtt", f"{tmp}.en-orig.vtt"):
        if os.path.exists(cand):
            os.remove(cand)
    return ("teaser", title) if is_teaser else ("saved", title)


def main():
    # Usage: fetch_transcripts.py <url> "<Podcast>" [transcripts_root] [min_date YYYYMMDD]
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
    min_date = argv[3] if len(argv) > 3 else None
    # 5th arg: how many of the newest episodes to look at. "all" or 0 scans the
    # whole channel, which is only needed for a first fetch or a backfill.
    raw = argv[4] if len(argv) > 4 else str(SCAN_LIMIT)
    scan_limit = 0 if raw.lower() in ("all", "0") else int(raw)
    # GUARD 2: a weekly run must not walk hundreds of videos. "all" or anything
    # above the ceiling needs an explicit --backfill; otherwise it is clamped
    # and the clamp is recorded so the health report can see it.
    clamped = False
    if (scan_limit == 0 or scan_limit > SCAN_CEILING) and not backfill:
        clamped = True
        print(f"{podcast}: scan limit {raw} exceeds the ceiling, clamped to "
              f"{SCAN_CEILING}. Pass --backfill to scan further; that is a "
              f"deliberate backfill job, not a weekly run.")
        runlog.record("fetch", source=podcast, outcome="scan_limit_clamped",
                      requested=raw, ceiling=SCAN_CEILING, applied=SCAN_CEILING)
        scan_limit = SCAN_CEILING
    dest = os.path.join(root, podcast)
    os.makedirs(dest, exist_ok=True)

    try:
        eps = list_episodes_with_retry(url, scan_limit)
    except ListingError as e:
        # A failed listing is NOT the same as an empty source. Say so plainly,
        # so the health report does not report a working feed as broken.
        runlog.record("fetch", source=podcast, outcome="listing_failed", detail=str(e)[:200])
        print(f"{podcast}: LISTING FAILED, retry before assuming it is broken. {e}")
        sys.exit(2)
    print(f"{podcast}: found {len(eps)} videos")
    if not eps:
        print(f"{podcast}: the source listed cleanly and is genuinely empty. "
              f"Likely a renamed or private channel.")
    counts = {}
    consec_old = 0
    for i, ep in enumerate(eps, 1):
        status, title = fetch_one(ep["id"], ep["title"], dest, min_date=min_date)
        counts[status] = counts.get(status, 0) + 1
        print(f"  [{i}/{len(eps)}] {status:6} {title[:60]}")
        # videos are newest-first; once we've seen a run of pre-cutoff episodes
        # we can stop rather than walking the whole back catalogue
        if status == "old":
            consec_old += 1
            if consec_old >= 12:
                print("  reached pre-cutoff back catalogue, stopping.")
                break
        else:
            consec_old = 0
    # If nothing was skipped, every episode on the list was new, which means the
    # list probably ran out before the already-saved ones started, and there may
    # be more beyond it. Silently missing those is the one real risk of a scan
    # limit, so say so loudly rather than let it pass.
    hit_limit = bool(scan_limit and counts.get("saved", 0) >= scan_limit)
    if hit_limit:
        print(f"{podcast}: WARNING, all {scan_limit} listed episodes were new. "
              f"There may be more past the scan limit. Rerun with a bigger "
              f"limit, e.g. 50, or 'all' with --backfill.")
    # Two different conditions, two different responses: "more_beyond_limit"
    # means episodes may have been missed and the show needs a rerun;
    # "clamped" means this run asked for more than the ceiling allows.
    runlog.record("fetch", source=podcast, outcome="ok" if eps else "listed_empty",
                  saved=counts.get("saved", 0), skipped=counts.get("skip", 0),
                  destination=raw_root, scan_limit=scan_limit,
                  backfill=backfill, clamped=clamped,
                  more_beyond_limit=hit_limit,
                  hit_limit=hit_limit)
    print(f"Done. {dict(counts)}")


if __name__ == "__main__":
    main()
