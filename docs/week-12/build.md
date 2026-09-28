---
title: Build · Run, compare, decide, write up
terms: []
card: build-step10
---

# Build · Run, compare, decide, write up

<p class="recall" markdown>**This week in one sentence:** four rows over five seeds, predictions logged first, rank correlation against a stand-in confusion table with a bootstrap interval, and a one-page write-up that ends in a decision and one question to a collaborator.</p>

**Laptop · ~3 hours · CPU.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-12.ipynb)

## The rule of the session

Every experiment cell follows a **predict cell**; the notebook refuses empty predictions. The first fixes the rule (\(X\), kill line, ablation floor, pivot target; from `week10_plan.md` when present) and the ablation *before* any data loads. `SMOKE = True` rehearses (three seeds, a minute). `False` is the real run: five seeds, the plan's number, about four minutes of CPU; the plan's 1.7 T4-hours over-budgeted twenty-five-fold.

## The data

Upload `week10_data.npz` and `week10_plan.md` to Colab; if one is missing, Part A regenerates or defaults, and the write-up says so.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Data; rule and ablation; the synthetic confusion table | 25 min |
| B | Trivial baselines: pixel and fixed-mapping distance against the table | 20 min |
| C | Train A once; read the curves | 35 min |
| D | Four rows × five seeds; rank correlation per run, appended to `experiments/week12/runs.jsonl` (`check.py` schema, metric `rank_corr`); bootstrap interval on A − B; one plot | 45 min |
| E | Optional (`RUN_CODEC`): 4×4, 8-level codec, straight-through, against the hand downsampler; the codec plan's pilot | 25 min |
| F | Write-up cell: the page from the numbers; decision by the rule; NEXT, CODEC, ask | 30 min |

## Done when

- `week12_writeup.md` exists: plot, baseline and ablation rows, five seeds per row (SMOKE's three is the rehearsal), logged prediction, surprise, decision.
- The decision came from the rule A0 printed, not from you after the plot, on a run the page shows was healthy.
- `experiments/week12/check.py` says OK.
- The final cell printed your prediction table.

## After the session

1. Paste the prediction table into your ledger, marking the biggest surprise.
2. `python track.py done week-12/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. Canvas step 10: send `week12_writeup.md` to an ML collaborator with the ASK line; log their answer.
4. Track A ends here; next is lesson 4's human study or a new week-10 plan from what NEXT names.

## Ledger prompt

> Next to `build-step10`: the collaborator's answer to the ASK line, and whether it is already one of your rows.
