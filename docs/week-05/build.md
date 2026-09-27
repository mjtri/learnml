---
title: Build · A character-level model on tiny Shakespeare
terms: []
card: move-inductive-bias
---

# Build · A character-level model on tiny Shakespeare

<p class="recall" markdown>**This week in one sentence:** one running sum, read and written by identical blocks of attention and MLP, trained to guess the next character and then sampled with a temperature.</p>

**Laptop · ~3 hours · T4 for Part D (Colab: Runtime → Change runtime type → T4).** Everything else runs on CPU.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-05.ipynb)

If the badge 404s, upload `notebooks/week-05.ipynb` to **Colab** by hand.

## The rule of the session

Every experiment cell is preceded by a **predict cell**; the notebook refuses an empty prediction. Near the top is a `SMOKE` flag: leave it `True` for a two-minute CPU dress rehearsal, then set it `False`, switch to the T4, and run again for real (~15 min of training).

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Download tiny Shakespeare, build the character alphabet, make (input, target) batches | 20 min |
| B | Write attention and the transformer block; push a vector through eight untrained blocks with and without the residual add | 25 min |
| C | Assemble the model; predict its parameter count from lesson 3's formula, then check the breakdown | 30 min |
| D | Train; read the loss curve; save a checkpoint; log validation loss with `cfg` and `seed` | 50 min |
| E | Sample: greedy, temperature 0.3 / 1 / 2, top-k; reproduce a sample exactly from its `seed` | 25 min |
| F | Map every box of figure 1 to a line you ran; stretch: pre-norm vs post-norm, loss per depth | 30 min |

## Done when

- Your predicted parameter count for Part C is within 5% of the printed one, and you can say where the difference lives.
- `week05_runs.jsonl` holds a line with `cfg`, `seed`, steps and final validation loss; the checkpoint file exists.
- For every box of figure 1 you can name the class or line that implements it, or say "not in this model".
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger. Mark the biggest surprise.
2. `python track.py done week-05/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 6` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `move-inductive-bias`: the residual add is a structural prior ("identity is the default"); Part F measured what changing it costs. Name one prior baked into a device or pipeline of your own, and what removing it would let the data decide.
