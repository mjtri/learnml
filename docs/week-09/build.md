---
title: Build · A contrastive model from scratch, then CLIP with error bars
terms: []
card: bridge-crossmodal
---

# Build · A contrastive model from scratch, then CLIP with error bars

<p class="recall" markdown>**This week in one sentence:** pairs are free labels, so each item learns to pick its partner out of the batch, and a number becomes a result only with a metric, a held-out split and an interval against something dumb.</p>

**Laptop · ~3 hours · CPU for Parts A–D; T4 for Parts E–F.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-09.ipynb)

If the badge 404s, upload `notebooks/week-09.ipynb` to **Colab** by hand.

## The rule of the session

Every experiment cell is preceded by a **predict cell**; the notebook refuses an empty prediction. Near the top is a `SMOKE` flag: leave it `True` for a five-minute CPU rehearsal of Parts A–D (E–F are skipped), then set it `False` on the T4 to run everything, including a 600 MB CLIP download.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Make 8×8 shape images and their vOICe-style "sound" vectors; the pairing is free | 20 min |
| B | Two small encoders and InfoNCE from scratch; similarity matrix before and after; held-out retrieval accuracy against chance | 40 min |
| C | Ablations: temperature, batch size, and the shuffled-pairing run that must sit at chance | 25 min |
| D | Three seeds as three participants, mean ± sd (and SE); a bootstrap interval on held-out pairs | 25 min |
| E | OpenCLIP zero-shot CIFAR-10 on the T4: bare labels versus three prompt templates, with bootstrap intervals | 40 min |
| F | Image↔text retrieval on a small custom set: your own XR or haptics screenshots | 30 min |

## Done when

- Part B's held-out retrieval accuracy is well above \(1/B\) and Part C's shuffled-pairing run sits at chance.
- Part D is written as "mean ± sd (and SE) over 3 seeds" plus a bootstrap interval.
- Part E compares templates as intervals, not bare numbers.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger. Mark the biggest surprise.
2. `python track.py done week-09/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 10` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `bridge-crossmodal`: the card's small experiment is Part B at toy scale. Write what changes for real depth patches and real vOICe clips: which pairing arrives free, which unit you would split by, and which dumb comparison has to lose before embedding distance may predict human discrimination.
