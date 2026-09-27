---
title: Build · LoRA by hand, then with PEFT, then a rank ablation
terms: []
card: lin-lora
---

# Build · LoRA by hand, then with PEFT, then a rank ablation

<p class="recall" markdown>**This week in one sentence:** a matrix's rank counts the directions it really uses, the SVD sorts them by strength, and LoRA fine-tunes a frozen model by learning only a low-rank change B times A.</p>

**Laptop · ~3 hours · T4 for Part E (Runtime → Change runtime type → T4).** Parts A to D run on CPU.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-08.ipynb)

If the badge 404s, upload `notebooks/week-08.ipynb` to **Colab** by hand.

## The rule of the session

Every experiment cell is preceded by a **predict cell**; the notebook refuses an empty prediction. A `SMOKE` flag near the top: `True` is a five-minute CPU rehearsal on a tiny sensor-glove model; `False` on the T4 runs Part E for real.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Rank and SVD in numbers: count a rank-2 matrix, compress an image at k = 1, 4, 16 | 25 min |
| B | Write `LoRALinear` by hand; adapt a frozen glove-gesture model to a new user; count what trains | 35 min |
| C | Same model through PEFT: match the count, check the weight merge to floating-point noise | 20 min |
| D | Rank ablation r ∈ {1, 4, 16} × 2 seeds on the tiny model; plant forgetting and leakage | 35 min |
| E | T4: LoRA-tune SmolLM2-360M on 400 instruction rows; before/after loss on unseen rows; same ablation | 60 min |
| F | Stretch: attach the adapter to one layer only, rerun the ablation | 15 min |

## Done when

- Your hand count of trainable parameters (Part B) matches `print_trainable_parameters()` (Part C) exactly.
- You wrote the r ordering *before* Part D ran, and can say whether the gaps beat the seed spread.
- The leakage check printed `0 test items also in train`, and you can point at the planted leak's loss.
- Part E logged a before/after loss on unseen rows, with `cfg`, `seed` and `r`, in `week08_runs.jsonl`.
- The final cell has printed your prediction table.

## After the session

1. Paste the prediction table into your insight ledger. Mark the biggest surprise.
2. `python track.py done week-08/build --rating <1-5> --minutes 180 --note "biggest surprise"`
3. `python gen_week.py 9` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `lin-lora`: the ablation ordering and seed spread in one line, then the smallest r you would use and why. Next to `bridge-adaptation`: which planted failure would be hardest to detect in a human study?
