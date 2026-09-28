---
title: Lesson 5 · The one-page write-up
terms: [kill/pivot/scale decision]
card: build-step9
---

# Lesson 5 · The one-page write-up

<p class="recall" markdown>**Previously:** rank correlation compares the model's closeness ordering with a confusion table's ordering; this week's table is a synthetic stand-in, and the human study replaces it.</p>

## Idea

The result of an experiment is not the number; it is a page someone else can act on. Five parts in a fixed order: claim, setup, plot, surprise, decision. The order is the discipline: the claim is copied from the plan, not written after the plot, and the decision is read off a rule also written before the run. What remains yours is the surprise, the part a collaborator actually wants.

## Mechanism

The template, which the notebook's last part fills from the run's numbers:

```
CLAIM     A beats B by >= X on M        (copied from the plan)
SETUP     data, rows, seeds, steps, budget spent
RESULT    mean ± sd per row; A − B with 95% CI; ablation cost
PLOT      one figure: rows on x, metric on y, seeds as dots
SURPRISE  the largest gap between a logged prediction and its result
DECISION  kill / pivot / scale up, by the pre-registered rule
ASK       "what baseline would make this go away?"
```

**Claim** already exists. **Setup** is week 7's reproducibility row: data file and seed, the four rows, seeds per row, fixed steps, T4-hours spent. **Result** is mean, sd and n per row plus one interval: the bootstrap 95% CI on A − B. An interval including zero is reported as "no detectable difference at this size", never "A is slightly better".

**Plot**: one figure, not four. Rows on the horizontal axis, the metric on the vertical, every seed a dot, the mean a bar, the pre-registered X a dashed line above B. If the reader cannot see the decision in the plot, the plot is wrong.

**Surprise** is the prediction-table row with the largest gap between what you wrote and what happened. "Predicted the ablation would cost 0.2 at 70%; it cost 0.02" deserves a paragraph: the sound side did nothing, a finding either way.

The **kill/pivot/scale decision** is week 10's rule applied without discussion:

- **Kill** if the gap A − B misses X, or the interval includes zero. Write what was learned; the idea is not dead, the *lever* is.
- **Pivot** if A cleared X but the ablation cost less than half of X: the gain is real but comes from elsewhere; the next plan starts from the ablation row.
- **Scale up** if A cleared X with the interval above zero and the ablation cost what was predicted: 50 shapes, real listeners, lesson 4's prediction.

The outcomes are exhaustive; "run more seeds and see" is not on the list, because it is the fork the plan forbade.

**Ask**: the page ends with one question to an ML collaborator, canvas step 10: "what baseline would make this go away?" Week 9's checklist has the candidates: sound-vector distance under the fixed mapping (no learning), a classifier's penultimate layer, a random encoder of the same size. Whichever is missing from your rows is your next baseline.

**In practice**, the write-up cell's own lines from the SMOKE rehearsal (the full run decides):

```
RESULT    A - B strong = -0.22  95% CI [-0.31, -0.14]
          ablation cost -0.17; B fixed (no learning) +0.78
SURPRISE  D1: predicted "A clears X" at 60%;
          got A below every baseline, even pixels
DECISION  KILL  (rule: gap -0.22 < X 0.2)
```

The analogy is a CHI abstract plus its limitations section. Where it breaks: a paper argues for a conclusion; this page argues for a *next action*, and "kill" is a good outcome for a page that took a week.

## Try it

<div class="visual"><iframe src="../visuals/w12-decision-matrix.html" title="Decision matrix: enter gap, interval and ablation cost; read the decision and its reason" loading="lazy"></iframe></div>

1. Gap 0.25, interval 0.05 to 0.45, X = 0.2, ablation cost 0.2. Does the interval decide, or the ablation?
2. Keep the gap at 0.25, set the ablation cost to 0.0. Predict the decision and the row the next plan starts from.
3. Widen the interval until it includes zero. What changes in RESULT, and what does not change in the rule?

## Retrieval

??? question "A − B = 0.24, interval 0.02 to 0.46, X = 0.2, ablation cost 0.01. Decide, and say which number decided it."
    Pivot. The gain cleared X with the interval above zero, but dropping the sound side cost almost nothing, so hearing carried none of it; the next plan starts from the image–image row.

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

**Next:** the build session: four rows, three or more seeds, predictions logged first, the page filled, the decision made, the question sent.
