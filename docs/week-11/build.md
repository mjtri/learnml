---
title: Build · Reproduce one number
terms: []
card: core-tooling
---

# Build · Reproduce one number

<p class="recall" markdown>**This week in one sentence:** read for one table cell, write its five-line checklist and a tolerance, walk the repo from entry point to metric, reproduce, and when the number is off, check cheapest first and write the gap down.</p>

**Laptop · ~3 hours · CPU for Parts A–D and F; T4 for Part E.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-11.ipynb)

## The rule of the session

Every experiment cell is preceded by a **predict cell**; the notebook refuses an empty prediction. `SMOKE = True` reproduces a number from *this course* (week 10's sound-probe accuracy) on CPU in under five minutes, so the whole workflow is rehearsed with no download; `False` on a T4 adds Part E, OpenCLIP zero-shot CIFAR-10 against Table 11.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Three passes over the target; five checklist lines as form fields, a source for each | 25 min |
| B | Load `week10_data.npz` (regenerated if missing) and check it against the checklist | 20 min |
| C | Run the reproduction; tolerance from seed spread (or numerics); verdict | 25 min |
| D | Debugging order: seeds 0–9; probe steps 200 → 500 as the deliberate optimisation change; one deliberate preprocessing mismatch | 35 min |
| E | T4: OpenCLIP ViT-B/32, `openai` weights, CIFAR-10 test set; 1 template versus 18; the `laion2b` swap as a ruled-out cause | 45 min |
| F | The six-sentence report from the recorded numbers, saved as `week11_report.md`, plus a row in `week11_runs.jsonl` | 20 min |

## Done when

- Part A has a source for every line; Part B flagged every mismatch between file and checklist.
- Part C printed a verdict with its tolerance, not a bare number.
- Part D moved the number at least once, and you wrote by how much.
- `week11_report.md` has six sentences and a residue line, and the final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger; mark the biggest surprise.
2. Commit `week11_report.md` with the `week11_runs.jsonl` row; the hash goes into the report's setup sentence.
3. `python track.py done week-11/build --rating <1-5> --minutes 180 --note "biggest surprise"`
4. `python gen_week.py 12` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `core-tooling`, with a copy next to `lin-clip`: paste the report's verdict and residue sentences, then one line on which checklist line you would have got wrong without the rehearsal.
