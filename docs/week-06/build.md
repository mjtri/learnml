---
title: Build · BPE from scratch, one ablation, one scaling line
terms: []
card: core-transformer
---

# Build · BPE from scratch, one ablation, one scaling line

<p class="recall" markdown>**This week in one sentence:** text becomes tokens by learned merges, loss falls as a straight line on log–log axes, and a component removed on purpose tells you what it was for.</p>

**Laptop · ~3 hours · T4 for parts C–E (Runtime → Change runtime type). `SMOKE = True` runs everything on a CPU in minutes at toy size; set it to `False` for the real run.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-06.ipynb)

If the badge 404s, run `python setup_repo.py <user> <repo>` once, or upload the notebook to **Colab** by hand.

## The rule of the session

Every experiment cell is preceded by a **predict cell**. This week the rule *is* the deliverable: `core-transformer` is done when you have ablated one component and explained the loss change, prediction logged first. An ablation without a prior prediction is a demo.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | A 20-line BPE trainer: `aaabdaaabac` by hand, then 300 merges on tiny Shakespeare | 30 min |
| B | GPT-2's real tokenizer on the lesson-2 table (optional, needs `tiktoken`) | 15 min |
| C | A nanoGPT-mini with four switches; the untouched model, twice | 25 min |
| D | **The ablation:** one component, two random starts, effect vs seed spread; then the mask | 60 min |
| E | Three sizes, same tokens: loss vs parameters on log–log axes, fitted slope, 6ND | 40 min |
| Wrap | `reveal()` and the ledger | 10 min |

## Done when

- Your BPE trainer reproduces the lesson-1 example (`aa`, `ab`, `ZY`) and reports bytes per token on Shakespeare.
- One component ablated with two runs each way, and a sentence on the loss change *relative to the seed spread*.
- The mask ablation did what lesson 5 said, or you found out why not.
- A three-point scaling line with a fitted slope and the 6ND count per size.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger next to `core-transformer`. Mark the biggest surprise.
2. `python track.py done week-06/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 7` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `core-transformer`: the component you removed, the loss change, the seed spread, and what the component was *for*. Next to `move-scale`: your fitted slope, and whether three points on a line convinced you of anything.
