---
title: Build · Bigram to one attention head
terms: []
card: core-transformer
---

# Build · Bigram to one attention head

<p class="recall" markdown>**This week in one sentence:** tokens become learned vectors, and each token mixes in the earlier tokens it asks for, weighted by a softmax over query·key scores.</p>

**Laptop · ~3 hours · CPU is enough (GPU only for the stretch).**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-04.ipynb)

If the badge 404s, run `python setup_repo.py <user> <repo>` once, or upload `notebooks/week-04.ipynb` to **Colab** by hand.

## The rule of the session

Every experiment cell is preceded by a **predict cell**; most predictions this week are *shapes*. Write the shape you expect, with a confidence, before running. A `SMOKE` flag near the top shrinks everything so the notebook runs on a CPU in minutes; set it to `False` for the real run.

The corpus is a synthetic log of haptic cues such as `L:2,3,1;L`: the opening letter fixes the digit range and must be echoed at the end. A bigram can know neither; one head can.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Tokens and the corpus: characters to ids, `(N,)` to `(B, T)` windows, the \(\log V\) line | 20 min |
| B | **Bigram** by counting, then the same table by gradient descent | 40 min |
| C | Lesson 4's three tokens in `torch`: unscaled, scaled, masked | 25 min |
| D | Position vectors plus one head; train; loss per context; read the weights | 45 min |
| E | Break it three ways: no mask, no positions, no √d; predict the ranking first | 30 min |
| F | Stretch: the same model on real downloaded text (GPU recommended) | 20 min |

## Done when

- You predicted the shape at every step in Parts C and D.
- The bigram loss sits between \(\log V\) and the head's loss, and you can say which positions the head fixed.
- You can name the no-mask bug from its symptom: training loss near zero, generated lines nonsense.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger next to `core-transformer`.
2. `python track.py done week-04/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 5` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `core-transformer`: what each of Q, K and V contributed in Part D, and one experiment on your own logs where "which earlier event matters depends on the current event" is the question.
