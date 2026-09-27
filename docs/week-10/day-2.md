---
title: Lesson 2 · Baselines that could embarrass you
terms: [baseline, strong baseline, same-compute baseline]
card: build-step5
---

# Lesson 2 · Baselines that could embarrass you

<p class="recall" markdown>**Previously:** an idea changes exactly one lever (data, architecture, objective, optimization, inference), and it becomes an experiment only as "on task T, A beats B by at least X on metric M".</p>

## Idea

A number on its own means nothing; a result is always a *difference* from a **baseline**, the method B in the prediction. Most small ML experiments fool their authors here, not in the model: B was chosen because it was easy to beat. If you would be *embarrassed* to lose to B, it is a real baseline. If losing to it would surprise nobody, you have measured nothing.

## Mechanism

A ladder with three rungs, climbed in order; each answers a different objection.

**Rung 1, the trivial baseline.** Predict the most common class; predict the mean; use raw pixel distance; use the hand-designed mapping you already have. It costs minutes and answers "is the task even hard?" Karpathy's recipe puts it before any model: on 10 shapes, "always say circle" scores 10 %, and a model at 12 % is a broken pipeline, not a result.

**Rung 2, the strong baseline.** The best simple method that already exists for the task, tuned with the *same care* as your method. A **strong baseline** for the week-12 embedding is a plain image encoder trained with the ordinary pixel loss, its learning rate swept exactly as widely as yours. Musgrave's metric-learning check re-ran a decade of "state of the art" with fairly tuned baselines and found the gains had mostly been tuning.

**Rung 3, the same-compute baseline.** Whatever your method spends, give B the same: steps, data passes, model size, tuning budget. A **same-compute baseline** separates "my objective is better" from "I trained longer". Dodge et al. make it a reporting rule: show the best result as a function of compute.

**In practice**, an honest results table for the week-12 default has four rows, and three are baselines:

| Method | Rung | Budget |
|---|---|---|
| pixel distance (no training) | trivial | 0 |
| hand-designed vOICe mapping + fixed encoder | trivial | 0 |
| pixel-loss encoder, tuned | strong, same compute | 5 seeds × 5 min |
| contrastive image–sound encoder (yours) | the claim | 5 seeds × 5 min |

If row 4 does not beat row 3 by the \(X\) you wrote down, the idea is not dead, but the *prediction* is, and the prediction is what you registered.

The user-study analogy is the comparison condition, with one difference. In a study the comparison is "current practice" and reviewers accept it. In ML they ask the sharper question from canvas step 10: *what baseline would make this result go away?* Where the analogy breaks: an ML baseline can be tuned as hard as you like at almost no cost, so "default settings for B" is not neutral, it is a thumb on the scale.
## Try it

<div class="visual"><iframe src="../visuals/w10-baseline-ladder.html" title="Baseline ladder: trivial, strong, same compute" loading="lazy"></iframe></div>

Before dragging, guess the trivial rung's score for the task:

1. Set your method to 18 % on 10 balanced shapes. Does the readout call it a gain over the trivial rung?
2. Drag the baseline's tuning budget up to match yours and watch how much of your margin survives.
3. Give the baseline the same steps. Find the smallest margin that still beats all three rungs.

## Retrieval

??? question "Your sonifier encoder scores 71 % on 10 shapes; the pixel-loss encoder scored 64 % with default settings. Name the two things you must check before calling this a gain."
    Whether the pixel-loss encoder's learning rate and steps were swept as widely as yours, and whether it got the same compute. Until both hold, the 7 points may be tuning or budget.

??? question "What does the trivial baseline protect you from that the strong baseline cannot?"
    A broken pipeline. If "always predict the majority class" scores close to your model, the task is not being learned at all, whatever the strong baseline says.

??? question "Rewrite 'we compare against the original paper's reported number' so it becomes a same-compute baseline."
    Re-run the original method on your data with your model size and step count, sweep its learning rate as widely as yours, and report its mean over the same seeds.

## Sources

- [Musgrave et al.: A metric learning reality check](https://arxiv.org/abs/2003.08505): figure 1 and section 3, how baselines were mistuned, 10 min.
- [Dodge et al.: Show your work](https://arxiv.org/abs/1909.03004): section 3, expected performance as a function of budget, 8 min.
- [Karpathy: A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/): step 2, "get dumb baselines", 4 min.

## Ledger prompt

> Next to `build-step5`: for your week-12 idea, write the three rungs. Then write the sentence a sceptical ML collaborator would say to make your result go away, and whether rung 3 already answers it.

**Next:** with B fixed, how a table of runs shows *which part* of your method carries the gain.
