"""
Shared helper. Every script calls this to record what it did, so nothing has to
be remembered or reconstructed afterwards.

Writes one JSON object per line to _state/run-events.jsonl. Phase 3 reads it.

The rule: the tool that knows a fact is the tool that records it. build_index
knows its counts, fetch knows what it saved. Neither the agent nor a later log
analysis should have to work it out.
"""
import json, os, datetime

def _path():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    d = os.path.join(root, "_state")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, "run-events.jsonl")

def record(kind, **fields):
    try:
        row = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "kind": kind}
        row.update(fields)
        with open(_path(), "a", encoding="utf-8") as f:
            f.write(json.dumps(row) + "\n")
    except Exception:
        pass          # recording must never break the run

def read_events():
    p = _path()
    if not os.path.exists(p):
        return []
    out = []
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line:
            try: out.append(json.loads(line))
            except json.JSONDecodeError: pass
    return out

def clear():
    open(_path(), "w").close()
