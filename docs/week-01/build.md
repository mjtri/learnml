---
title: Build · Gradients by hand, then by machine
terms: [MSE, Colab]
card: core-calc
---

# Build · Gradients by hand, then by machine

<p class="recall" markdown>**This week in one sentence:** tensors in boxes, mixed by matrices, nudged downhill along the gradient.</p>

**Laptop · ~3 hours · CPU is enough (no GPU needed this week).**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-01.ipynb)

If the badge 404s, the repo placeholders are not filled in yet: run `python setup_repo.py <user> <repo>` once, or upload `notebooks/week-01.ipynb` to **Colab** by hand (File → Upload notebook).

## The rule of the session

Every experiment cell is preceded by a **predict cell**. Write what you expect, with a confidence, *before* running. The notebook refuses to continue on an empty prediction. The gap between prediction and result is the thing you are here to collect (canvas steps 7–8).

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Shape drills: predict result shapes and one silent broadcasting bug | 25 min |
| B | Build a vOICe-style image→sound **matrix**, play the sound, then squash it | 35 min |
| C | Nudge-and-measure vs autograd on the same function | 20 min |
| D | Day 4's graph by hand on paper, then checked three ways | 30 min |
| E | Fit a line with hand-written gradient descent and an **MSE** loss; then break it with the learning rate | 45 min |
| F | Stretch: a 25-line `Value` class with `+` and `×` that does its own backward pass (next week's seed) | 25 min |

## Done when

- Your hand-computed gradients for Part D match autograd *and* the numerical check.
- You predicted, before running, roughly which learning rate makes Part E diverge, and you can explain the actual threshold.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger. Mark the biggest surprise.
2. `python track.py done week-01/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 2` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `lin-bitter` (after reading the essay): Part B's matrix was designed by hand. Which part of a sensory-substitution mapping would you *not* want to hand over to learning, and what would you need to measure to be proved wrong?
