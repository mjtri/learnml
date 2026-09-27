---
title: Build · Rebuild micrograd, train it on XOR and moons
terms: []
card: core-calc
---

# Build · Rebuild micrograd, train it on XOR and moons

<p class="recall" markdown>**This week in one sentence:** a Value remembers its history, the backward walk fills every gradient, and five repeated lines turn an MLP into a learner.</p>

**Laptop · ~3 hours · CPU only, no GPU needed.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-02.ipynb)

If the badge 404s, run `python setup_repo.py <user> <repo>` once, or upload `notebooks/week-02.ipynb` to Colab by hand.

## The rule of the session

Every experiment cell is preceded by a **predict cell**. Write what you expect, with a confidence, *before* running; the notebook refuses an empty prediction. One extra rule: Part A is written **from memory**. Close the lessons, write `Value`, run the checks. If it fails, fix it and note in the ledger which piece you had forgotten.

A `SMOKE` switch near the top shrinks data and step counts so the notebook runs in minutes on CPU. Set it to `False` for the real session.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | `Value` from memory: `+`, `×`, `tanh`, `backward`; a test cell says PASS or FAIL | 40 min |
| B | Every gradient of a small graph checked three ways: yours, a PyTorch twin, nudge-and-measure | 25 min |
| C | Cause the accumulation bug on purpose, twice: with `=` and with no zeroing | 15 min |
| D | `Neuron` → `Layer` → `MLP`; XOR with and without the bend, plus a one-neuron control | 40 min |
| E | Moons: a 2–8–1 MLP, loss curve, decision boundary; PyTorch twin agrees to 1e-9 | 45 min |
| F | Stretch: swap tanh for ReLU and sweep the learning rate | 15 min |

## Done when

- Part A's test cell prints PASS on a `Value` you wrote without looking.
- Your 2-layer MLP scores 4 of 4 on XOR, and the same model with the bend removed does not.
- `torch.allclose` says your engine and PyTorch agree on every gradient in Part E.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger next to `core-calc`. Mark the biggest surprise.
2. `python track.py done week-02/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 3` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `move-discrete-continuous`: Part D's XOR needed a soft bend and a soft loss. Pick one hard rule from a study you ran (an inclusion threshold, a hit/miss criterion): what becomes possible, and what becomes fuzzier, once it is differentiable?
