---
title: Lesson 5 · The one-page write-up
terms: [kill/pivot/scale decision]
card: build-step9
---

# Lesson 5 · The one-page write-up

<p class="recall" markdown>**Previously:** rank correlation compares the model's distance ordering with a confusion table's ordering; this week's table is a synthetic stand-in, and a pairwise study with participants replaces it.</p>

## Idea

The result of an experiment is not the number; it is a page someone else can act on. Five parts in a fixed order: claim, setup, plot, surprise, decision. The order is the discipline: the claim is copied from the plan and the decision is read off a rule also written before the run. What remains yours is the surprise, the part a collaborator wants.

## Mechanism

The template, which the notebook's last part fills from the run's numbers:

```
CLAIM     A beats B by >= X on M        (copied from the plan)
RULE      kill line, ablation floor, pivot target (from the plan)
SETUP     data, rows, seeds, steps, minutes spent, run health
RESULT    mean ± sd per row; A − B with 95% CI; ablation cost
PLOT      one figure: rows on x, metric on y, seeds as dots
SURPRISE  the largest gap between a logged prediction and its result
DECISION  kill / pivot / scale up, by the rule
NEXT      what the decision names; CODEC: Part E's number
ASK       one question to a collaborator
```

**Claim** and **rule** are copied from `week10_plan.md` (\(X\), kill line, ablation floor, pivot target) before any data loads. **Setup** is week 7's reproducibility row (data and seed, rows, seeds, fixed steps, minutes) plus one line showing the run was healthy: a kill from a broken run is a bug report. **Result** is mean, sd and n per row and the bootstrap 95% CI on A − B, naming the noise it covers: the notebook resamples the 20 shapes, so the interval is about "which shapes"; the seed spread stands beside it. An interval including zero is "no detectable difference at this size", never "A is slightly better".

**Plot**: one figure. Rows on x, the metric on y, every seed a dot, the mean a bar, \(X\) a dashed line above B. If the reader cannot see the decision in it, the plot is wrong.

**Surprise** is the prediction-table row with the largest gap between prediction and result. A negative ablation cost (dropping the sound side *helped*) is a finding, not noise to explain away.

The **kill/pivot/scale decision** is your plan's rule applied without discussion, numbers copied, not remembered:

- **Kill** if the gap is under your plan's kill line, the interval includes zero, or the gap never reaches \(X\). The idea is not dead, the *lever* is.
- **Pivot** if the gap survived but the ablation cost less than your plan's floor: the gain is real but not for the claimed reason; the next plan starts from the plan's pivot target.
- **Scale up** if the gap cleared \(X\) with the interval above zero and the ablation cost its floor.

The outcomes are exhaustive; "run more seeds and see" is the fork the plan forbade.

**Reading a kill.** The honest outcome here is a kill: healthy curves, the fixed sonifier distance (no learning) above every trained row, a negative ablation cost. A kill names no row, so the next plan is the pre-registered alternative, the codec; Part E was its pilot and the CODEC line carries its number. The **ask** flips: a no-learning baseline beat A, so ask "what would make the sonifier-plus-ruler baseline lose?".

**In practice**, the write-up cell's own lines from the SMOKE rehearsal (the full run decides):

```
RESULT    A - B strong = -0.22  95% CI [-0.40, -0.06]
          ablation cost -0.17 (negative: dropping sound helped)
          B fixed (no learning) +0.78
DECISION  KILL  (rule: gap -0.22 < kill line 0.1)
NEXT      the plan's alternative (codec); Part E was its pilot
CODEC     learned - hand downsampler = -32.8 probe points
ASK       what would make the sonifier-plus-ruler baseline lose?
```

## Try it

<div class="visual"><iframe src="../visuals/w12-decision-matrix.html" title="Decision matrix: enter gap, interval and ablation cost; read the decision and its reason" loading="lazy"></iframe></div>

1. Gap 0.25, interval 0.05 to 0.45, \(X = 0.2\), kill line 0.1, floor 0.05, ablation cost 0.2. Interval or ablation: which decides?
2. Keep the gap at 0.25, set the ablation cost to 0.0. Predict the decision and where the next plan starts.
3. Widen the interval until it includes zero. What changes in RESULT, and what does not change in the rule?

## Retrieval

??? question "A − B = 0.24, interval 0.02 to 0.46, X = 0.2, kill line 0.1, ablation floor 0.05, ablation cost 0.01. Decide, and say which number decided it."
    Pivot. The gap survived the kill line with the interval above zero, but the ablation cost 0.01, under the floor: hearing carried none of it; the next plan starts from the pivot target.

??? question "Why is 'run more seeds and look again' not one of the three outcomes?"
    It is the fork pre-registration forbids: seeds added after seeing a result get added until the result appears. A new seed count needs a new plan.

??? question "Name two baselines an ML collaborator might propose that would make a contrastive result go away, and what each one tests."
    Sound-vector distance under the fixed mapping: whether learning added anything. A random encoder of the same size: whether the architecture alone orders the pairs.

## Sources

- [Lipton & Steinhardt: Troubling trends in machine learning scholarship](https://arxiv.org/abs/1807.03341): section 3, 10 min.
- [The machine learning reproducibility checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf): one page, 5 min.
- [Dodge et al.: Show your work](https://arxiv.org/abs/1909.03004): section 5, the reporting checklist, 5 min.

## Ledger prompt

> Next to `build-step9`: the decision rule as three lines with numbers, written before opening the notebook; afterwards, the decision it printed and whether you wanted to argue.

**Next:** the build session: four rows, five seeds, predictions logged first, the page filled, the decision made, the question sent.
