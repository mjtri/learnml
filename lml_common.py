"""Shared helpers for the LearnML scripts. Standard library only."""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Windows consoles often default to a legacy code page (cp949/cp1252); lesson titles contain → and ·.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
LOG = ROOT / "progress" / "log.jsonl"      # committed: date, lesson, minutes, rating
NOTES = ROOT / "progress" / "notes.jsonl"  # git-ignored: date, lesson, note
GLOSSARY_DIR = ROOT / "glossary"   # terms-<week-dir>.jsonl shards + terms-core.jsonl

# Two parallel tracks. A lesson id is "<dir>/<slot>", e.g. "week-01/day-2" or "agentic-01/apply".
TRACKS = {
    "ml": {"label": "Track A · ML", "prefix": "week", "weeks": 12,
           "slots": ["day-1", "day-2", "day-3", "day-4", "day-5", "build"], "long": "build"},
    "agentic": {"label": "Track B · Agentic workflows", "prefix": "agentic", "weeks": 8,
                "slots": ["day-1", "day-2", "day-3", "apply"], "long": "apply"},
}
# Backwards-compatible aliases for the ML track.
TOTAL_WEEKS = TRACKS["ml"]["weeks"]
LESSONS_PER_WEEK = len(TRACKS["ml"]["slots"])
WEEK_SLOTS = TRACKS["ml"]["slots"]

# Korea has no DST, so a fixed offset is exact and avoids needing tzdata on Windows.
KST = timezone(timedelta(hours=9), "KST")


def today_kst() -> str:
    return datetime.now(KST).date().isoformat()


def week_dir(n: int, track: str = "ml") -> str:
    return f"{TRACKS[track]['prefix']}-{n:02d}"


def track_of(lesson_id: str) -> str:
    prefix = lesson_id.split("-", 1)[0]
    for name, t in TRACKS.items():
        if t["prefix"] == prefix:
            return name
    raise ValueError(f"unknown track for lesson id {lesson_id!r}")


def week_of(lesson_id: str) -> int:
    return int(lesson_id.split("/")[0].rsplit("-", 1)[1])


def lesson_ids(track: str | None = None) -> list[str]:
    """Lessons that exist on disk, in study order, e.g. 'week-01/day-2'. ML track first, then agentic."""
    ids = []
    for name, t in TRACKS.items():
        if track and name != track:
            continue
        for wdir in sorted(DOCS.glob(f"{t['prefix']}-[0-9][0-9]")):
            for slot in t["slots"]:
                if (wdir / f"{slot}.md").exists():
                    ids.append(f"{wdir.name}/{slot}")
    return ids


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def done_lessons() -> set[str]:
    return {r["lesson"] for r in read_jsonl(LOG)}


def split_front_matter(text: str) -> tuple[dict, str]:
    """Tiny front-matter reader: 'key: value' and 'key: [a, b]' lines only."""
    meta: dict = {}
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return meta, text
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            meta[key.strip()] = [v.strip().strip("\"'") for v in val[1:-1].split(",") if v.strip()]
        else:
            meta[key.strip()] = val.strip("\"'")
    return meta, text[m.end():]


def read_lesson(lesson_id: str) -> tuple[dict, str]:
    return split_front_matter((DOCS / f"{lesson_id}.md").read_text(encoding="utf-8"))


def lesson_title(lesson_id: str) -> str:
    meta, body = read_lesson(lesson_id)
    m = re.search(r"^# (.+)$", body, re.M)
    return m.group(1).strip() if m else meta.get("title", lesson_id)


RETRIEVAL_RE = re.compile(r'^\?\?\? question "(.+?)"\s*\n((?:(?: {4}|\t).*\n?|\s*\n)+)', re.M)


def retrieval_questions(body: str) -> list[tuple[str, str]]:
    """(question, answer) pairs from `??? question "..."` blocks."""
    out = []
    for q, a in RETRIEVAL_RE.findall(body):
        answer = " ".join(line.strip() for line in a.splitlines() if line.strip())
        out.append((q.strip(), answer))
    return out


def load_terms() -> list[dict]:
    """Glossary entries from every shard: {term, aliases[], def, lesson, card?, shard}."""
    out = []
    for shard in sorted(GLOSSARY_DIR.glob("terms*.jsonl")):
        for row in read_jsonl(shard):
            row["shard"] = shard.name
            out.append(row)
    return out


def lesson_index(lesson_id: str) -> tuple[str, int, int]:
    """Sortable position of a lesson inside its track: (track, week, slot index)."""
    track = track_of(lesson_id)
    slot = lesson_id.split("/")[1]
    return track, week_of(lesson_id), TRACKS[track]["slots"].index(slot)


def week_title(week_dir: str) -> str:
    """Human title of a week from curriculum.md, e.g. 'Tensors → gradients'."""
    track = track_of(week_dir + "/x")
    n = int(week_dir.rsplit("-", 1)[1])
    head = rf"^## Week {n} — (.+)$" if track == "ml" else rf"^## B{n} — (.+)$"
    m = re.search(head, (ROOT / "curriculum.md").read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else week_dir


def week_summary(week_dir: str) -> str:
    """The 'This week in one sentence' line from build.md / apply.md, or ''."""
    track = track_of(week_dir + "/x")
    path = DOCS / week_dir / f"{TRACKS[track]['long']}.md"
    if not path.exists():
        return ""
    m = re.search(r"\*\*This week in one sentence:\*\*\s*(.+?)</p>", path.read_text(encoding="utf-8"))
    return m.group(1).strip() if m else ""


def slug(term: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")


def word_count(body: str) -> int:
    """Words a reader actually reads: drops code fences, HTML tags and math delimiters."""
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"https?://\S+", " ", body)
    body = re.sub(r"\{[^}\n]*\}", " ", body)  # attr_list stamps like { .src data-checked="..." }
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", body))
