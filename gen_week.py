"""Print the prompt that (re)generates one week. Generates nothing itself.

    python gen_week.py 2                 # Track A (ML) week 2, human-paste prompt
    python gen_week.py agentic 2         # Track B (agentic workflows) week 2
    python gen_week.py agentic 2 --agent # fan-out prompt for a generation subagent working in a worktree
    python gen_week.py 2 --out prompt.txt

All weeks exist in the finished course; this prints the prompt to rebuild one (for example after low ratings).
"""
from __future__ import annotations

import argparse
import re
import sys

import lml_common as c

CANVAS = r"C:\Users\user\Documents\Git_Repositories\oracle\canvas\AI Research Roadmap.canvas"
NB_PY = r"C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-AI-Projects-LearnML\78565a74-5f28-4904-aed4-9a07db80a72d\scratchpad\nbvenv\Scripts\python.exe"
VENV_PY = r"C:\Users\user\Documents\AI_Projects\LearnML\.venv\Scripts\python.exe"

LEARNER = """\
- HCI researcher (XR, sensory substitution, haptics, Unity VR). Strong research intuition, weak ML/math, comfortable with Python; new to PyTorch at week 1.
- Reads on a phone ~20-25 min per lesson; one ~3 h build session per week on a laptop with free Colab (T4, session limits). Self-paced: a "week" is a unit of content, never a calendar week.
- English only. Goal: read modern papers, fine-tune/modify small models, run small controlled experiments. Not theory.
- Learns fastest when jargon is one tap away: every new term must be in the glossary.
- Wants practical examples: every lesson shows at least one real snippet / tool output / paper figure ("In practice"), ideally from Unity/C#, haptics, XR studies or this repo."""

LEARNER_B = """\
- HCI researcher (XR, sensory substitution, haptics, Unity/C#). Has a Claude Code Max 20x subscription and a ChatGPT Business plan; already uses ChatGPT chat + Codex.
- Wants to stop wasting usage and to run efficient, effective agentic workflows for: Unity/C# XR development, research paperwork (papers, reviewer responses, ETRI TM reports, Korean and English), experiments & data analysis, and the LearnML repo itself.
- Reads on a phone ~15 min per lesson; the 'apply' task (~60 min) happens in the laptop build session. Self-paced.
- Every product claim (feature, limit, price, policy) must cite an official source with a data-checked stamp; third-party claims are marked "(unverified)"."""


def curriculum_section(track: str, n: int) -> str:
    text = (c.ROOT / "curriculum.md").read_text(encoding="utf-8")
    head = rf"^## Week {n}\b" if track == "ml" else rf"^## B{n}\b"
    m = re.search(head + r".*?(?=^#{1,2} |^---$|\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"curriculum.md has no section matching {head!r}")
    return m.group(0).strip()


def curriculum_objectives(track: str, n: int) -> str:
    """One-line digest of a week: its title plus the first objective bullet."""
    sec = curriculum_section(track, n)
    title = sec.splitlines()[0].lstrip("# ").split("—", 1)[-1].strip()
    m = re.search(r"\*\*Objectives\*\*\n- (.+)", sec)
    return f"{title}: {m.group(1).strip()}" if m else title


def format_section(track: str) -> str:
    """The part of LESSON_FORMAT.md that applies to this track, plus the shared sections."""
    fmt = (c.ROOT / "LESSON_FORMAT.md").read_text(encoding="utf-8")
    # Split at '## ' headings, but not at the '## Idea' etc. lines inside the ```markdown templates.
    parts, in_fence = [""], False
    for line in fmt.splitlines(keepends=True):
        if line.startswith("```"):
            in_fence = not in_fence
        if line.startswith("## ") and not in_fence:
            parts.append("")
        parts[-1] += line
    keep = []
    for part in parts:
        title = part.splitlines()[0] if part.strip() else ""
        if track == "ml" and title.startswith("## Track B"):
            continue
        if track == "agentic" and (title.startswith("## Phone lesson") or title.startswith("## Build day")):
            continue
        keep.append(part)
    return "".join(keep).strip()


def ownership(track: str) -> dict[int, tuple[str, str]]:
    """{week: (owned terms, visual topics)} from glossary/OWNERSHIP.md."""
    text = (c.ROOT / "glossary" / "OWNERSHIP.md").read_text(encoding="utf-8")
    head = "## Track A" if track == "ml" else "## Track B"
    block = text.split(head, 1)[1].split("\n## ", 1)[0]
    out = {}
    for line in block.splitlines():
        m = re.match(r"\|\s*(\d+)[^|]*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", line)
        if m:
            out[int(m.group(1))] = (m.group(2), m.group(3))
    return out


def build_prompt(track: str, n: int, agent: bool) -> str:
    t = c.TRACKS[track]
    wk = c.week_dir(n, track)
    prefix = f"w{n:02d}-" if track == "ml" else f"b{n}-"
    existing_visuals = sorted(p.name for p in (c.DOCS / "visuals").glob("*.html"))
    existing_terms = sorted({e["term"] for e in c.load_terms() if not (e.get("lesson") or "").startswith(wk + "/")})
    own = ownership(track)
    owned, visual_topics = own.get(n, ("(see curriculum)", "(one per lesson)"))
    reserved = "; ".join(f"week {k}: {v[0]}" for k, v in sorted(own.items()) if k > n)
    brief = "\n".join(f"- Week {k}: {curriculum_objectives(track, k)}" for k in range(1, n))
    prev_summary = c.week_summary(c.week_dir(n - 1, track)) if n > 1 else ""
    prev_line = prev_summary or f"(week {n - 1} has no build/apply summary yet; write a one-line recap of its objectives above)"
    ratings = [r for r in c.read_jsonl(c.LOG) if r["lesson"].startswith(c.week_dir(n - 1, track) + "/")]
    rating_line = ", ".join(f"{r['lesson'].split('/')[1]}={r['rating']}" for r in ratings) or "none logged"
    fmt = format_section(track)

    if track == "ml":
        learner, label = LEARNER, f"Week {n} of Track A (ML)"
        anchors = "docs/week-01/day-3.md, docs/week-01/build.md, docs/visuals/w01-slope-slider.html, and the first 4 cells of notebooks/week-01.ipynb (the setup/predict/record/reveal helper cell must be copied byte-for-byte)"
        files = f"""\
- docs/{wk}/day-1.md … day-5.md (titles "Lesson N · …") and docs/{wk}/build.md, following the lesson contract below exactly.
- One interactive visual per phone lesson at docs/visuals/{prefix}<slug>.html (a second one only where the mechanism is dynamic). Topics reserved for this week: {visual_topics}. Existing visuals, do not duplicate: {", ".join(existing_visuals)}
- notebooks/{wk}.ipynb: same helper pattern as week 1; a `SMOKE = True` flag near the top shrinks data/model/steps so the whole notebook runs on CPU in under 5 minutes (set False for the real Colab run); GPU-only parts guarded with `torch.cuda.is_available()`; weeks 7–9 use the smallest viable models (e.g. SmolLM2-135M, openai/clip-vit-base-patch32). Every experiment cell is preceded by a predict cell; the last cell is `reveal()`; code cells ≤ 25 lines.
- Ledger prompts name the canvas card id they belong next to. The canvas is read-only: {CANVAS}"""
    else:
        learner, label = LEARNER_B, f"Week {n} of Track B (agentic workflows)"
        anchors = "docs/agentic-01/day-2.md, docs/agentic-01/apply.md, docs/visuals/b1-usage-windows.html"
        files = f"""\
- docs/{wk}/day-1.md, day-2.md, day-3.md (titles "B{n} · Lesson N · …") and docs/{wk}/apply.md, following the Track B contract below exactly.
- One interactive visual OR one '### Worked example' per phone lesson; visuals at docs/visuals/{prefix}<slug>.html. Topics reserved for this week: {visual_topics}. Existing visuals: {", ".join(existing_visuals)}
- Every product claim cites an official page with {{ .src data-checked="YYYY-MM-DD" }} using the REAL date you fetched it (WebFetch each page first; never cite from memory). Unreachable page → say so and mark the sentence "(verify)". Third-party sources get "(unverified)".
- Ledger prompts ask for a line in docs/agentic/playbook.md, naming the playbook section. Do NOT edit playbook.md or changelog.md; put changelog bullets in your report instead."""

    common_rules = f"""\
## Glossary rules (shards; one definition per term in the whole course)
- Write ONLY glossary/terms-{wk}.jsonl. One JSON object per line: {{"term", "aliases", "def", "lesson", "card"?}} with "lesson" one of this week's ids ({", ".join(f"{wk}/{s}" for s in t["slots"])}); each term must also appear in that lesson's `terms:` front matter.
- You OWN these terms; define them here: {owned}
- Already defined, reuse freely, never redefine: {", ".join(existing_terms)}
- Reserved for later weeks; do NOT define them, use plain words instead: {reserved or "(none)"}
- Definitions ≤ 30 plain words; aliases = plurals/variants only; never an alias that is an ordinary English word with another meaning.

## Continuity (self-paced wording, enforced by the checker)
- Lesson 1 opens: <p class="recall" markdown>**Previously:** {prev_line}</p>
- Every later lesson opens with **Previously:** = one line recapping the previous lesson. No "Yesterday", "Tomorrow", "Day N", "today's lesson" anywhere.
- Each lesson ends with **Next:** one-line teaser. {t["long"]}.md opens with **This week in one sentence:** … (the next week's agent reuses it verbatim).
- Course so far, one line per earlier week (keep references consistent with these):
{brief or "- (this is week 1)"}"""

    selfcheck = f"""\
## Self-check: run until clean (Windows; use these exact interpreters)
1. "{VENV_PY}" check_lessons.py --only {wk}
2. "{VENV_PY}" build_today.py   then   "{VENV_PY}" -m mkdocs build --strict
3. Visuals: each docs/visuals/{prefix}*.html ≤ 60 KB, no network access, contains the theme/height boilerplate (copy it from the anchor visual), a collapsed "ⓘ Words used here" block, works at 360–390 px wide with no horizontal scroll (check with the browser tool at a 390×844 viewport if available, else reason from the CSS), touch targets ≥ 44 px, never `display:flex/grid` on an element holding prose.
4. Notebook (Track A): `json.load` succeeds; every code cell parses with `ast.parse` and is ≤ 25 lines; execute it headlessly with "{NB_PY}" (has torch CPU, nbclient, ipykernel: use the run pattern `nbformat.read` → stub every `prediction = ""` to "test" → `NotebookClient(nb, timeout=600).execute()` with MPLBACKEND=Agg). If a download is too large or a step needs a GPU, guard it and report "not executed: <reason>".
5. Links: WebFetch every URL in every `## Sources` section; a URL you cannot confirm gets " (verify)" after it.
6. Word counts per lesson within the caps and above the floors printed by the checker.

## Report back (≤ 40 lines, this exact order)
files created; per-lesson word counts; terms added; terms you wanted but were reserved; proposed WATCHLIST additions for check_lessons.py; the {t["long"]}.md "This week in one sentence"; links marked (verify); notebook executed yes/no (+reason); visual sizes; {"changelog bullets for outdated claims found in earlier weeks; " if track == "agentic" else ""}anything you could not satisfy."""

    if agent:
        head = f"""\
You are generating {label} of the LearnML course, working in THIS git worktree only. Write only these paths:
docs/{wk}/*, docs/visuals/{prefix}*.html, {"notebooks/" + wk + ".ipynb, " if track == "ml" else ""}glossary/terms-{wk}.jsonl.
Never touch mkdocs.yml, check_lessons.py, curriculum.md, LESSON_FORMAT.md, docs/agentic/*, other weeks, generated files (docs/index.md, docs/glossary.md, docs/curriculum.md, includes/, docs/javascripts/glossary-map.js, anki/). Do not commit. Do not run gen_week.py.
Study the style anchors first: {anchors}. Match their voice, density, "In practice" placement and the visual's code structure.
Read AGENTS.md and glossary/OWNERSHIP.md for repo conventions."""
    else:
        head = f"""\
Generate {label} of my LearnML course in this repo. Generate ONLY this week, then stop for my review.
Style anchors to match: {anchors}."""

    return f"""\
{head}

## Learner
{learner}

## Ratings for the previous week (1 = lost, 5 = easy)
{rating_line}
If any rating is <= 2, open the matching lesson this week with a 3-sentence repair of that idea before moving on.

## What this week must cover (from curriculum.md)
{curriculum_section(track, n)}

## Files to create
{files}

{common_rules}

{selfcheck}

## Lesson format contract (from LESSON_FORMAT.md)
{fmt}
"""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("args", nargs="+", help="[track] week, e.g. '2' or 'agentic 2'")
    p.add_argument("--agent", action="store_true", help="fan-out prompt for a worktree subagent")
    p.add_argument("--force", action="store_true", help="print even if the week already exists")
    p.add_argument("--out", help="also write the prompt to this file")
    a = p.parse_args()

    track = "ml"
    if len(a.args) == 2:
        track = a.args[0]
        if track not in c.TRACKS:
            print(f"unknown track '{track}'; use one of: {', '.join(c.TRACKS)}")
            return 1
    try:
        week = int(a.args[-1])
    except ValueError:
        print(__doc__)
        return 1
    t = c.TRACKS[track]
    if not 1 <= week <= t["weeks"]:
        print(f"{t['label']}: week must be 1..{t['weeks']}")
        return 1
    if (c.DOCS / c.week_dir(week, track)).exists() and not (a.force or a.agent):
        print(f"docs/{c.week_dir(week, track)} already exists. Use --force to print a regeneration prompt anyway.")
        return 1

    prompt = build_prompt(track, week, a.agent)
    if a.out:
        with open(a.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(prompt)
    if not a.agent:
        print("=" * 72)
        print(f"Paste everything below this line into Claude Code (run from {c.ROOT}):")
        print("=" * 72)
    print(prompt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
