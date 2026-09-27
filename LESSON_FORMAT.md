# Lesson format contract

Single source of truth for every week. Self-paced: lessons are numbered ("Lesson 3"), recaps say **Previously:** and teasers say **Next:**; nothing refers to days. `check_lessons.py` enforces it, `build_anki.py` parses it, `gen_week.py` embeds it in the generation prompt.

## Phone lesson: `docs/week-NN/day-D.md`

Read on a 390 px phone in 20–25 minutes; the file id stays `day-D.md` but the title says **Lesson D**. **Hard cap 800 words** (aim for 650–750). One idea per lesson.

```markdown
---
title: Lesson 3 · Derivative = sensitivity
terms: [derivative, slope]        # terms INTRODUCED today; each must exist in glossary/terms.jsonl
card: core-calc                   # canvas card id the ledger entry belongs next to
---

# Lesson 3 · Derivative = sensitivity

<p class="recall" markdown>**Previously:** … (one line: the previous lesson, or for lesson 1 the previous week's "This week in one sentence")</p>

## Idea
One paragraph, plain words, no symbols. Say what problem this idea solves.

## Mechanism
The key formula or mechanism. Include one **In practice** paragraph or block: a real snippet, tool output, paper
figure or bug the learner will actually meet ("in nanoGPT this line is …", "the error message reads …"). Math in \( inline \) or \[ display \] form, one formula per display.
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

**Next:** one-line teaser.
```

Rules
- Section headings are exactly: `## Idea`, `## Mechanism`, `## Try it`, `## Retrieval`, `## Sources`, `## Ledger prompt`.
- Exactly one iframe and exactly three `??? question "…"` blocks. Where the mechanism is dynamic (training curves,
  attention weights, sampling) a second visual is welcome; it goes *inside* `## Mechanism` as a second
  `<div class="visual">` only if it is a different mechanism, otherwise fold it into the one visual as a mode.
- Practical over abstract: prefer a worked example from the learner's world (Unity, haptics, a real repo) to a toy. Questions test recall or prediction, not recognition; no yes/no questions.
- No long code walls. Phone lessons explain; the notebook is where code lives.
- Just-in-time math: introduce a math concept only in the lesson that needs it, with the smallest example that works (2×2, three numbers).
- Any link that could not be verified gets "(verify)" after it.

## Track B phone lesson: `docs/agentic-NN/day-D.md`

Read on a 390 px phone in ~15 minutes. **Hard cap 700 words** (aim for 550–650; the retrieval, sources and rules scaffolding is ~200 of them). One habit or mechanism per lesson.
Ratings and ledger entries work like Track A; the ledger is `docs/agentic/playbook.md` instead of the canvas.

```markdown
---
title: B1 · Lesson 2 · What you actually pay for
terms: [usage window, weekly cap]     # terms INTRODUCED today; each must exist in glossary/terms.jsonl
playbook: budget                       # playbook section the ledger line belongs in
---

# B1 · Lesson 2 · What you actually pay for

<p class="recall" markdown>**Previously:** …</p>

## Idea
One paragraph: the habit or mechanism, and the waste or failure it prevents.

## How it works
How the tool actually behaves, with numbers where they exist. Every product claim (feature, limit, price, policy)
links to the official page with a checked stamp:
`[usage limits](https://support.claude.com/...){ .src data-checked="2026-09-27" }`.
Third-party or anecdotal claims end with "(unverified)". Bold each introduced term on first use.
One **In practice** example from the learner's work (Unity/C#, paperwork, experiments, or this repo).

## Try it
Exactly one of: an iframe visual, or a `### Worked example` card (a real prompt or command and its result, ≤ 12 lines).
Then two variants, both mandatory:
**Phone:** something doable now in the Claude app Code tab / Remote Control / Codex Remote, or a 2-minute reflection.
**Laptop:** the real exercise, ≤ 10 minutes, with a concrete "you will see …" outcome.

## Rules of thumb
- exactly three bullets, each one line, each actionable ("Do X when Y")
- …
- …

## Retrieval
??? question "…"
    …
(exactly three)

## Sources
- Official docs first (stamped), then engineering posts; 2–4 links. Third-party links say "(unverified)".

## Ledger prompt
> One line to add to the playbook, naming its section: "In **budget**: …"

**Next:** one-line teaser.
```

Rules
- Headings exactly: `## Idea`, `## How it works`, `## Try it`, `## Rules of thumb`, `## Retrieval`, `## Sources`, `## Ledger prompt`.
- Claims are dated, not eternal: stamps older than 60 days raise a warning; `python gen_refresh.py` prints the re-check prompt.
- Cover both subscriptions in every lesson where it is honest to: what Claude Code does, what Codex/ChatGPT does, when to use which.
- Never invent a limit or price. If the official page gives no number, say so ("OpenAI publishes no number; check the in-product counter").

## Track B apply task: `docs/agentic-NN/apply.md`

≤ 400 words, done in the build session (~60 min). Opens with `**This week in one sentence:**` like Track A's build page. Sections: goal, the steps (numbered, each with the exact command or prompt),
"done when", what to log (`track.py done agentic-NN/apply --minutes 60 …`) and a ledger prompt for the playbook. Where a step
runs the same task in Claude Code and in Codex, ask for time, usage delta (`/usage` before/after, or the ChatGPT counter) and a
1–5 quality score so the playbook accumulates evidence, not opinions.

## Styling rule: prose stays inline

Every glossary term in a page becomes its own `<abbr>` element, and every backtick becomes a `<code>` element, so a
sentence is many inline nodes. **Never put `display: flex` or `display: grid` on an element that contains prose**
(paragraphs, list items, `summary` titles, table cells, admonition titles). Flex/grid turns each node into a separate box and
the words scatter across the line. Get tap-target height from `padding` or `min-height` alone. Flex/grid belong only on
layout containers whose children are blocks (`.stats`, `.bar`, button rows). `check_lessons.py` fails the build if
`extra.css` breaks this.

## Glossary: `glossary/terms-<week-dir>.jsonl` shards

One shard per week (plus `terms-core.jsonl` for forward references); `glossary/OWNERSHIP.md` says which week defines which term. One JSON object per line: `{"term", "aliases", "def", "lesson", "card"}`. `build_glossary.py` turns it into tap-to-define
tooltips on every page, the glossary page, and Anki vocab cards.
- Every technical word a lesson uses must have an entry **before** the lesson uses it. When unsure, add it.
- Definitions: ≤ 30 words, plain words, no symbols, must not lean on a term that is defined later. An optional short
  "Like …" analogy from perception/HCI is welcome where honest.
- `aliases` lists plurals and variants that appear in prose (`gradients`, `dot products`). Capitalized forms are automatic.
- Matching is whole-word and case-sensitive, so avoid entries that are common English words with another meaning in prose.
- `lesson` is where the term is first taught; it must also be listed in that lesson's `terms:` front matter, and the row must live in that week's shard.
- A term is defined once in the whole course. A lesson may use a term defined later in the *same* week (tap-to-define covers it) but never one owned by a later week: use plain words instead.

## Interactive visual: `docs/visuals/wNN-NAME.html` (Track A) / `bN-NAME.html` (Track B)

- Filename prefixed with the week (`w05-attention-heatmap.html`, `b3-hook-builder.html`); the checker rejects unprefixed files.
- One self-contained file: inline CSS and JS, canvas or SVG. **No network access of any kind** (no CDN, fonts, fetch, images).
- ≤ 60 KB. Works at 360–390 px wide with no horizontal scroll; touch targets ≥ 44 px; uses pointer events; sliders are native `<input type=range>`.
- Follows the site's dark/light scheme: copy the theme + height-reporting boilerplate from an existing visual
  (reads `data-md-color-scheme` from the parent page, falls back to `prefers-color-scheme`, posts `{learnmlHeight}` to the parent).
- Shows numbers, not only pictures: the learner should be able to check a prediction against a readout.
- Ends with a collapsed "ⓘ Words used here" block defining the 2–4 terms it uses (iframes cannot see the site glossary).
- One interaction, one idea. If it needs instructions longer than two lines, it is too complicated.

## Build day: `docs/week-NN/build.md` + `notebooks/week-NN.ipynb`

`build.md` (≤ 400 words): opens with `<p class="recall" markdown>**This week in one sentence:** …</p>` (the next week's first lesson reuses it), then goal, the Colab badge, the parts with time boxes, "done when", ledger prompt. No iframe or retrieval block required.

Notebook rules
- Opens with the `predict()` / `reveal()` helper cell copied from `notebooks/week-01.ipynb`.
- Every experiment is a pair: a **predict cell** (Colab form fields: prediction text + confidence slider; refuses an empty prediction) and then the experiment cell. Follow with a one-line "surprise?" prompt.
- Code cells ≤ 25 lines, one idea each. Each part starts with a "Words used in this part" markdown cell.
- Runs top to bottom on free Colab in well under 3 hours including thinking time; say explicitly when a GPU is needed.
- Ends with `reveal()` printing the prediction table to paste into the insight ledger, plus the `track.py` command.
