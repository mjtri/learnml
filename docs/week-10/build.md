---
title: Build · Two candidates, one plan, one pipeline
terms: []
card: build-step6
---

# Build · Two candidates, one plan, one pipeline

<p class="recall" markdown>**This week in one sentence:** one lever, a baseline that could embarrass you, one ablation, seeds chosen from the spread, all on a pre-registered page; the week-12 experiment is the cross-modal contrastive embedding (rendered shapes ↔ vOICe-style sound), with the learned image→touch codec as the alternative.</p>

**Laptop · ~3 hours · CPU only.**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mjtri/learnml/blob/main/notebooks/week-10.ipynb)

## The rule of the session

Every experiment cell is preceded by a **predict cell**; the notebook refuses an empty prediction. A `SMOKE` flag near the top keeps the notebook under five minutes on CPU; `False` runs the full sweep, still under a minute of compute.

## The choice

The data pipeline **defaults to the cross-modal contrastive embedding** (`OPTION = "contrastive"`): 16×16 rendered shapes → vOICe-style sonifier → pitch-by-time energy vectors. The alternative (`OPTION = "codec"`) feeds the same shapes to a 4×4, 8-level haptic-grid downsampler. Both go into `week10_data.npz`, the file weeks 11–12 and Track B week 7 read.

## Parts

| Part | What you do | Time |
|---|---|---|
| A | Render 20 shape classes at 16×16 with jitter; both candidates through canvas steps 1–5 | 30 min |
| B | Sonifier: image → column snippets → pitch-by-time energy vector; round-trip check | 35 min |
| C | Haptic-grid downsampler: 16×16 → 4×4 × 8 levels; count code collisions | 20 min |
| D | Seeds vs noise: a tiny probe per representation; mean ± sd (and SE) over seeds, effect size, \(16/\Delta^2\) | 45 min |
| E | Choose; fill the one-page plan; budget computed; save `week10_plan.md` | 30 min |
| F | Stretch: week 12's trivial baseline, pixel distance vs sound distance over shape pairs | 20 min |

## Done when

- `week10_data.npz` exists and Part B's round-trip check passes at the threshold you predicted.
- Part D printed mean ± sd (and SE) over seeds for two representations.
- `week10_plan.md` names task, metric, baseline B, a prediction with a number, one ablation, seeds, a compute budget ≤ a few T4-hours, and the chosen option.

## After the session

1. Paste the prediction table into your insight ledger.
2. Commit `week10_plan.md`: the commit hash is your pre-registration time-stamp.
3. `python track.py done week-10/build --rating <1-5> --minutes 180 --note "biggest surprise"`
4. `python gen_week.py 11` and paste the printed prompt into Claude Code.

## Ledger prompt

> Next to `build-step6`: which Move Library card does your chosen candidate use (`move-free-supervision` for contrastive, `move-inductive-bias` for the codec)? Write the ablation that would show the move was unnecessary.
