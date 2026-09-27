---
title: Build · Probe a small language model and log the run
terms: []
card: core-tooling
---

# Build · Probe a small language model and log the run

<p class="recall" markdown>**This week in one sentence:** a checkpoint is config plus weights plus tokenizer; load it, read the shapes, probe its hidden states with the weights frozen, and log every run with config, seed and git hash.</p>

**Laptop · ~3 hours · CPU is enough; a T4 only for Part D's memory measurement.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-07.ipynb)

If the badge 404s, upload `notebooks/week-07.ipynb` to **Colab** by hand.

## The rule of the session

Every experiment cell is preceded by a **predict cell**; the notebook refuses an empty prediction. Near the top is a `SMOKE` flag: `True` is a five-minute CPU rehearsal with a 14M-parameter model and 200 sentences; `False` is the real pass with SmolLM2-135M and 800 sentences (a few minutes, even on CPU).

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Load model and tokenizer; read the config; predict the parameter count, then check it | 20 min |
| B | Tokenize a padded batch, fix the pad-token error, forward pass with hidden states, generate twice from one seed | 30 min |
| C | Fetch labelled sentences, pool hidden states with the mask, fit a linear probe per layer, then shuffle the labels | 50 min |
| D | Memory arithmetic: predict the footprints, then measure one fine-tuning step on a GPU if you have one | 30 min |
| E | Reproducibility: one seed twice, three seeds, write `week07_runs.csv` with config, seed and git hash | 30 min |
| F | Stretch: last-token pooling vs the mean | 20 min |

## Done when

- From `config.json` alone you can state the shapes of `input_ids`, one hidden state and `logits`, and the parameter count within 10 %.
- Your per-layer probe curve has a best layer and the shuffled-label check sits at chance.
- `week07_runs.csv` holds four rows with git hash, seed, model, layer, versions and accuracy; two same-seed rows agree.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger. Mark the biggest surprise.
2. `python track.py done week-07/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 8` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `core-tooling`: the card says "clone a paper repo, reproduce one table row, log your own run with config + seed". Which can you now do, and what would the paper repo need to give you for the middle one?
