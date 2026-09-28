---
title: Build · Run, compare, decide, write up
terms: []
card: build-step10
---

# Build · Run, compare, decide, write up

<p class="recall" markdown>**This week in one sentence:** four rows over three or more seeds, predictions logged first, rank correlation against a stand-in confusion table with a bootstrap interval, and a one-page write-up that ends in kill, pivot or scale up and one question to a collaborator.</p>

**Laptop · ~3 hours · CPU is enough.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-12.ipynb)

## The rule of the session

Every experiment cell is preceded by a **predict cell**; the notebook refuses an empty prediction. The first asks for the pre-registered \(X\) and the sharpened ablation *before* any data loads. `SMOKE = True` keeps the notebook under five minutes on CPU; `False` is the real run, about five minutes on CPU.

## The data

Upload `week10_data.npz` and `week10_plan.md` to Colab's Files panel. If either is missing, Part A regenerates the data with week 10's code and seed and uses the default plan; the write-up says so.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Load or regenerate the data; log \(X\) and the ablation; the synthetic confusion table | 25 min |
| B | Trivial baselines: pixel distance and fixed-mapping distance against the table | 20 min |
| C | Train the contrastive model once; read the curves | 35 min |
| D | Four rows × seeds; rank correlation per run; bootstrap interval on A − B; one plot | 45 min |
| E | Optional (`RUN_CODEC`): 4×4, 8-level bottleneck with the straight-through trick against the hand downsampler | 25 min |
| F | Write-up cell: the page filled from the numbers, the decision by the rule, the ask | 30 min |

## Done when

- `week12_writeup.md` exists with the plot, the baseline rows, the ablation row, at least three seeds per row, the logged prediction, the surprise, and a decision.
- The decision came from lesson 5's rule, not from you after seeing the plot.
- The final cell printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger; mark the biggest surprise.
2. `python track.py done week-12/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. Canvas step 10: send `week12_writeup.md` to an ML collaborator with the question; log their answer.
4. Track A ends here; the next page is lesson 4's human-study plan, or a new week-10 plan from the row the decision named.

## Ledger prompt

> Next to `build-step10`: the collaborator's answer to "what baseline would make this go away?", and whether it is already one of your rows.
