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
TERMS = ROOT / "glossary" / "terms.jsonl"

TOTAL_WEEKS = 12
LESSONS_PER_WEEK = 6  # day-1..day-5 + build
WEEK_SLOTS = ["day-1", "day-2", "day-3", "day-4", "day-5", "build"]

# Korea has no DST, so a fixed offset is exact and avoids needing tzdata on Windows.
KST = timezone(timedelta(hours=9), "KST")


def today_kst() -> str:
    return datetime.now(KST).date().isoformat()


def week_dir(n: int) -> str:
    return f"week-{n:02d}"


def lesson_ids() -> list[str]:
    """All lessons that exist on disk, in study order, e.g. 'week-01/day-2'."""
    ids = []
    for wdir in sorted(DOCS.glob("week-[0-9][0-9]")):
        for slot in WEEK_SLOTS:
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
    """Glossary entries: {term, aliases[], def, lesson, card?}."""
    return read_jsonl(TERMS)


def slug(term: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")


def word_count(body: str) -> int:
    """Words a reader actually reads: drops code fences, HTML tags and math delimiters."""
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"https?://\S+", " ", body)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", body))
