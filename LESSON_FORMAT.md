# Lesson format contract

Single source of truth for every week. `check_lessons.py` enforces it, `build_anki.py` parses it, `gen_week.py` embeds it in the generation prompt.

## Phone lesson: `docs/week-NN/day-D.md`

Read on a 390 px phone in 20–25 minutes. **Hard cap 800 words** (aim for 650–750). One idea per lesson.

```markdown
---
title: Day 3 · Derivative = sensitivity
terms: [derivative, slope]        # terms INTRODUCED today; each must exist in glossary/terms.jsonl
card: core-calc                   # canvas card id the ledger entry belongs next to
---

# Day 3 · Derivative = sensitivity

<p class="recall" markdown>**Yesterday in one sentence:** … (one line; week 1 day 1 uses "Why this week")</p>

## Idea
One paragraph, plain words, no symbols. Say what problem this idea solves.

## Mechanism
The key formula or mechanism. Math in \( inline \) or \[ display \] form, one formula per display.
Bold each introduced term on first use. Include an analogy from perception / HCI / XR **only where it
is honest**, and say where the analogy breaks. Code, if any: at most one block, ≤ 12 lines, ≤ 60 columns.

## Try it
<div class="visual"><iframe src="../visuals/NAME.html" title="…" loading="lazy"></iframe></div>
Two or three concrete things to try, phrased as predictions ("before you drag, guess …").

## Retrieval
??? question "Question text on one line?"
    Answer, indented four spaces. One to three sentences.

(exactly three of these)

## Sources
- [Title](url): which part, how many minutes. 2–4 links. Prefer a timestamped video segment or one section.

## Ledger prompt
> One line: what to write in the insight ledger, naming the canvas card, e.g. "next to `core-calc`: …"

**Tomorrow:** one-line teaser.
```

Rules
- Section headings are exactly: `## Idea`, `## Mechanism`, `## Try it`, `## Retrieval`, `## Sources`, `## Ledger prompt`.
- Exactly one iframe and exactly three `??? question "…"` blocks. Questions test recall or prediction, not recognition; no yes/no questions.
- No long code walls. Phone lessons explain; the notebook is where code lives.
- Just-in-time math: introduce a math concept only in the lesson that needs it, with the smallest example that works (2×2, three numbers).
- Any link that could not be verified gets "(verify)" after it.

## Glossary: `glossary/terms.jsonl`

One JSON object per line: `{"term", "aliases", "def", "lesson", "card"}`. `build_glossary.py` turns it into tap-to-define
tooltips on every page, the glossary page, and Anki vocab cards.
- Every technical word a lesson uses must have an entry **before** the lesson uses it. When unsure, add it.
- Definitions: ≤ 30 words, plain words, no symbols, must not lean on a term that is defined later. An optional short
  "Like …" analogy from perception/HCI is welcome where honest.
- `aliases` lists plurals and variants that appear in prose (`gradients`, `dot products`). Capitalized forms are automatic.
- Matching is whole-word and case-sensitive, so avoid entries that are common English words with another meaning in prose.
- `lesson` is where the term is first taught; it must also be listed in that lesson's `terms:` front matter.

## Interactive visual: `docs/visuals/NAME.html`

- One self-contained file: inline CSS and JS, canvas or SVG. **No network access of any kind** (no CDN, fonts, fetch, images).
- ≤ 60 KB. Works at 360–390 px wide with no horizontal scroll; touch targets ≥ 44 px; uses pointer events; sliders are native `<input type=range>`.
- Follows the site's dark/light scheme: copy the theme + height-reporting boilerplate from an existing visual
  (reads `data-md-color-scheme` from the parent page, falls back to `prefers-color-scheme`, posts `{learnmlHeight}` to the parent).
- Shows numbers, not only pictures: the learner should be able to check a prediction against a readout.
- Ends with a collapsed "ⓘ Words used here" block defining the 2–4 terms it uses (iframes cannot see the site glossary).
- One interaction, one idea. If it needs instructions longer than two lines, it is too complicated.

## Build day: `docs/week-NN/build.md` + `notebooks/week-NN.ipynb`

`build.md` (≤ 400 words): goal, the Colab badge, the parts with time boxes, "done when", ledger prompt. No iframe or retrieval block required.

Notebook rules
- Opens with the `predict()` / `reveal()` helper cell copied from `notebooks/week-01.ipynb`.
- Every experiment is a pair: a **predict cell** (Colab form fields: prediction text + confidence slider; refuses an empty prediction) and then the experiment cell. Follow with a one-line "surprise?" prompt.
- Code cells ≤ 25 lines, one idea each. Each part starts with a "Words used in this part" markdown cell.
- Runs top to bottom on free Colab in well under 3 hours including thinking time; say explicitly when a GPU is needed.
- Ends with `reveal()` printing the prediction table to paste into the insight ledger, plus the `track.py` command.
