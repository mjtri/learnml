"""Export a week's retrieval questions and new glossary terms as Anki cards.

    python build_anki.py week-01      ->  anki/week-01.txt

Import in Anki: File > Import, the header lines set tab separator, HTML and the tags column.
"""
from __future__ import annotations

import html
import re
import sys

import lml_common as c


def clean(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text.replace("\t", " ").strip()


def main() -> int:
    if len(sys.argv) != 2 or not re.fullmatch(r"week-\d\d", sys.argv[1]):
        print(__doc__)
        return 1
    week = sys.argv[1]
    lessons = [l for l in c.lesson_ids() if l.startswith(week + "/")]
    if not lessons:
        print(f"No lessons found for {week}")
        return 1

    rows = []
    for lesson in lessons:
        _, body = c.read_lesson(lesson)
        tag = f"learnml {week} {week}-{lesson.split('/')[1]}"
        for q, a in c.retrieval_questions(body):
            rows.append((clean(q), clean(a), tag))
    n_q = len(rows)
    for e in c.load_terms():
        if e.get("lesson", "").startswith(week + "/"):
            front = f"What does <b>{html.escape(e['term'])}</b> mean?"
            rows.append((front, html.escape(" ".join(e["def"].split())), f"learnml {week} vocab"))

    out = c.ROOT / "anki" / f"{week}.txt"
    out.parent.mkdir(exist_ok=True)
    lines = ["#separator:tab", "#html:true", "#tags column:3"]
    lines += ["\t".join(r) for r in rows]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"{out.relative_to(c.ROOT)}: {n_q} question cards + {len(rows) - n_q} vocab cards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
