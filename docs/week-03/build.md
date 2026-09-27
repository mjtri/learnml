---
title: Build · An MLP that generalises, broken and fixed
terms: []
card: core-optim
---

# Build · An MLP that generalises, broken and fixed

<p class="recall" markdown>**This week in one sentence:** the same five-line loop with PyTorch names, scored by surprise, fed in noisy batches, judged on data it never saw, and kept alive by learning rate, init and normalization.</p>

**Laptop · ~3 hours · CPU only (no GPU needed this week).**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-03.ipynb)

If the badge 404s, the repo placeholders are not filled in yet: run `python setup_repo.py <user> <repo>` once, or upload `notebooks/week-03.ipynb` to **Colab** by hand (File → Upload notebook).

## The rule of the session

Every experiment cell is preceded by a **predict cell**. Write what you expect, with a confidence, *before* running; the notebook refuses an empty prediction. Part F is the week's done-when.

A `SMOKE = True` flag near the top shrinks data, model and steps for a quick CPU plumbing check; set it to `False` for the real Colab run.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Load **MNIST**, write a `Dataset` of your own, predict the shapes a `DataLoader` yields | 20 min |
| B | The canonical loop on an MLP: first loss ≈ 2.30, then past 97 % validation accuracy | 30 min |
| C | Softmax and cross-entropy by hand against `F.cross_entropy`; the double-softmax floor | 20 min |
| D | Batch size and optimizers: SGD, momentum and Adam given the same number of steps | 25 min |
| E | Overfit 500 images on purpose, then weight decay, dropout and early stopping | 30 min |
| F | Break it three ways, fix it three ways, predicting which fix works first | 45 min |
| G | Stretch: a twelve-layer tanh MLP with and without residual connections | 15 min |

## Done when

- Your first loss was within 0.05 of 2.303 and you can say why, and validation accuracy passed 97 %.
- In Part F you predicted, before running, which of learning rate, init and normalization would rescue each broken net, and at least two of three were right.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger next to `core-optim`. Mark the biggest surprise.
2. `python track.py done week-03/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 4` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `core-optim`: your three fingerprints and their fixes, for a labmate whose net "just doesn't train". Next to `lin-resnet`: what Part G showed you about depth.
