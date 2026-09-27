"""Make cross-week recaps exact: each week's first lesson opens with the previous week's
"This week in one sentence" line (from build.md / apply.md). Run after generating or regenerating any week.

    python continuity.py          # rewrite where needed, print what changed
    python continuity.py --check  # exit 1 if any recap is out of date (used by check_lessons.py? no: run it explicitly)
"""
from __future__ import annotations

import argparse
import re
import sys

import lml_common as c

RECALL_RE = re.compile(r'(<p class="recall" markdown>\*\*Previously:\*\*)\s*(.*?)(</p>)', re.S)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    changed, stale = [], []
    for track, t in c.TRACKS.items():
        weeks = sorted({c.week_of(l) for l in c.lesson_ids(track)})
        for n in weeks:
            if n == 1:
                continue
            summary = c.week_summary(c.week_dir(n - 1, track))
            first = c.DOCS / c.week_dir(n, track) / "day-1.md"
            if not summary or not first.exists():
                continue
            text = first.read_text(encoding="utf-8")
            m = RECALL_RE.search(text)
            if not m:
                stale.append(f"{first.relative_to(c.ROOT)}: no Previously recall line")
                continue
            if m.group(2).strip() == summary:
                continue
            stale.append(f"{first.relative_to(c.ROOT)}: recap differs from {c.week_dir(n - 1, track)} summary")
            if not a.check:
                new = text[:m.start(2)] + summary + text[m.end(2):]
                first.write_text(new, encoding="utf-8", newline="\n")
                changed.append(str(first.relative_to(c.ROOT)))
    for s in stale:
        print(("stale:" if a.check else "fixed:"), s)
    if a.check:
        return 1 if stale else 0
    print(f"{len(changed)} recap line(s) rewritten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
