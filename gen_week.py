"""Print the exact prompt to paste into Claude Code to generate week N. Generates nothing itself.

    python gen_week.py 2            # refuses unless week 1 is >= 80% done
    python gen_week.py 2 --force    # print anyway
    python gen_week.py 2 --out prompt.txt
"""
from __future__ import annotations

import argparse
import re
import sys

import lml_common as c

CANVAS = r"C:\Users\user\Documents\Git_Repositories\oracle\canvas\AI Research Roadmap.canvas"

LEARNER = """\
- HCI researcher (XR, sensory substitution, haptics, Unity VR). Strong research intuition, weak ML/math, comfortable with Python; new to PyTorch at week 1.
- Reads on a phone ~20-25 min/day; one ~3 h build session per week on a laptop with free Colab (T4, session limits).
- English only. Goal: read modern papers, fine-tune/modify small models, run small controlled experiments. Not theory.
- Learns fastest when jargon is one tap away: every new term must be in the glossary."""


def curriculum_section(n: int) -> str:
    text = (c.ROOT / "curriculum.md").read_text(encoding="utf-8")
    m = re.search(rf"^## Week {n}\b.*?(?=^#{{1,2}} |^---$|\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"curriculum.md has no '## Week {n}' section")
    return m.group(0).strip()


def build_prompt(n: int) -> str:
    wk = c.week_dir(n)
    visuals = sorted(p.name for p in (c.DOCS / "visuals").glob("*.html"))
    terms = sorted(e["term"] for e in c.load_terms())
    ratings = [r for r in c.read_jsonl(c.LOG) if r["lesson"].startswith(c.week_dir(n - 1))]
    rating_line = ", ".join(f"{r['lesson'].split('/')[1]}={r['rating']}" for r in ratings) or "none logged"
    fmt = (c.ROOT / "LESSON_FORMAT.md").read_text(encoding="utf-8").strip()

    return f"""\
Generate Week {n} of my LearnML course in this repo. Generate ONLY week {n}, then stop for my review.

## Learner
{LEARNER}

## Last week's self-ratings (1 = lost, 5 = easy)
{rating_line}
If any rating is <= 2, open the matching day this week with a 3-sentence repair of that idea before moving on.
Also read progress/notes.jsonl if it exists (local surprise notes) and reuse my own words where they help.

## What week {n} must cover (from curriculum.md)
{curriculum_section(n)}

## Files to create
- docs/{wk}/day-1.md ... day-5.md and docs/{wk}/build.md, following LESSON_FORMAT.md below exactly.
- One new interactive visual per phone lesson in docs/visuals/. Do not duplicate existing ones: {", ".join(visuals)}
- notebooks/{wk}.ipynb with "predict before you run" cells (same helper pattern as notebooks/week-01.ipynb), sized for a free Colab T4 in under 3 h.
- Append new terms to glossary/terms.jsonl (one JSON object per line). Reuse existing definitions; existing terms: {", ".join(terms)}
- Add the week to `nav:` in mkdocs.yml.
- Ledger prompts must name the canvas card id they belong next to. The canvas is read-only: {CANVAS}

## Then run and fix until clean
python check_lessons.py
python build_today.py
python build_anki.py {wk}
mkdocs build --strict
Open every new visual at a 390 px wide viewport (headless or the built-in browser) and confirm it renders, responds to touch, and has no horizontal scroll.
Check every external link resolves; mark any you cannot verify with "(verify)".

## Lesson format contract (LESSON_FORMAT.md)
{fmt}

Stop after week {n}. Summarize what to review. Do not commit or push.
"""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("week", type=int)
    p.add_argument("--force", action="store_true", help="print even if the previous week is under 80 percent done")
    p.add_argument("--out", help="also write the prompt to this file")
    a = p.parse_args()

    if not 2 <= a.week <= c.TOTAL_WEEKS:
        print(f"week must be 2..{c.TOTAL_WEEKS}")
        return 1
    if (c.DOCS / c.week_dir(a.week)).exists() and not a.force:
        print(f"docs/{c.week_dir(a.week)} already exists. Use --force to print the prompt anyway.")
        return 1

    prev = [f"{c.week_dir(a.week - 1)}/{s}" for s in c.WEEK_SLOTS]
    n_done = len(c.done_lessons() & set(prev))
    frac = n_done / c.LESSONS_PER_WEEK
    if frac < 0.8 and not a.force:
        missing = [l for l in prev if l not in c.done_lessons()]
        print(f"Week {a.week - 1} is {n_done}/{c.LESSONS_PER_WEEK} done ({frac:.0%}); need >= 80% before generating week {a.week}.")
        print("Still open: " + ", ".join(missing))
        print("Finish those (python track.py done ...), or rerun with --force.")
        return 2

    prompt = build_prompt(a.week)
    if a.out:
        with open(a.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(prompt)
    print("=" * 72)
    print(f"Paste everything below this line into Claude Code (run from {c.ROOT}):")
    print("=" * 72)
    print(prompt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
