---
title: Lesson 5 · Pre-registration for yourself
terms: [pre-registration, compute budget]
card: build-step5
---

# Lesson 5 · Pre-registration for yourself

<p class="recall" markdown>**Previously:** measure the spread across seeds first, report gains as effect sizes against it, plan about \(16/\Delta^2\) seeds per method, and tune the baseline as hard as your own method.</p>

## Idea

Everything this week is a decision made *before* the first run: the lever, the baseline, the ablation, the seeds, the number \(X\). Writing them on one page is not bureaucracy. A result, once seen, quietly rewrites the question: the metric that happened to move becomes "the metric", the seed that worked becomes "the run". You know the cure from psychology's reform decade as **pre-registration**. Nobody will audit the page; its audience is you in two weeks, wanting to move the goalposts.

## Mechanism

The one-page plan has eight lines, each a word you met this week:

| Line | Fill in | From |
|---|---|---|
| intuition | one plain sentence, no jargon | canvas step 1 |
| lever | one of five | lesson 1 |
| task \(T\), metric \(M\) | runnable this month; one number | lesson 1 |
| baseline \(B\) | the three rungs; which one you report against | lesson 2 |
| prediction | "A beats B by ≥ X on M", X a number | lesson 1 |
| ablation | one "A minus what", with the cost it should show | lesson 3 |
| seeds | count per method, from \(16/\Delta^2\) | lesson 4 |
| compute budget | rows × seeds × minutes, in T4-hours | here |

The **compute budget** is the line most people leave out and the one that keeps the others honest: rows (methods plus ablations) × seeds × minutes per run. Four rows × 5 seeds × 6 minutes is 2 T4-hours, a Colab afternoon. Four rows × 5 seeds × 40 minutes is 13 hours, which the free tier will not give you in one sitting, so the model shrinks, or the seeds drop (and \(\Delta\) must rise), or it is not yet a plan. The canvas card for step 6 caps it at "a few GPU-hours".

Two more lines, because a result tempts you to change them: the *stopping rule* (a fixed number of steps, never "until it looked converged") and the *decision rule* for each outcome: kill, pivot or scale up, canvas step 9.

**In practice**, the default week-12 plan as the build session's notebook prints it:

```
lever       objective (contrastive image-sound loss)
task/metric 20 rendered shapes; agreement between
            embedding-distance and confusion orderings
baseline    pixel distance (trivial); pixel-loss
            encoder, same sweep and steps (strong)
prediction  beats pixel-loss encoder by >= 0.2
ablation    swap contrastive for pixel loss: >= 0.2
seeds       5 per row (detects delta >= 1.8)
budget      4 rows x 5 seeds x 5 min = 1.7 T4-h
```

The analogy to a pre-registered study holds line for line, with one difference: a registry makes the plan public and time-stamped; your page is a file in the repo, and its commit hash is the time-stamp. Where it weakens: pilots are cheap in ML, so a *pilot run* to measure \(\sigma\) before fixing \(X\) is the standard move, as long as the pilot's seeds are not reused in the registered run.

The page prevents Gelman's garden of forking paths: at each fork (metric, seed, stopping point) an honest researcher picks the branch that looks best, and the branches multiply into a result that would not survive a fresh run.

## Try it

<div class="visual"><iframe src="../visuals/w10-plan-builder.html" title="One-page plan builder with a compute budget readout" loading="lazy"></iframe></div>

Before touching the seeds and minutes sliders, guess the budget in T4-hours.

1. Rows 4, seeds 5, minutes 5. Read the budget and the smallest detectable effect.
2. Push minutes to 40. Find the seed count that brings the budget under 3 hours, and what it costs in detectable effect.
3. Leave the prediction's number blank and tap **check**. Every blank is a fork.

## Retrieval

??? question "A plan reads 'train until the validation curve flattens, then compare'. Which line is missing, and what goes wrong without it?"
    The stopping rule. Flattening is judged by eye after seeing the numbers, so each method stops where it looks best; fix a step count for every row.

??? question "Your budget is 4 rows × 5 seeds × 25 min. Compute it in T4-hours and name two ways to bring it under 3 hours, with their cost."
    About 8.3 hours. Halve the model or steps (the result may not transfer), or cut to 3 seeds (only effects above \(\Delta \approx 2.3\) stay detectable).

??? question "Why is a pilot run to measure the seed spread allowed before pre-registering X, and what rule must it follow?"
    X must be stated as an effect size, which needs \(\sigma\), and \(\sigma\) is cheap to measure. The pilot's seeds must not be reused as evidence in the registered run.

## Sources

- [Center for Open Science: Preregistration](https://www.cos.io/initiatives/prereg): the "what" section and the template list, 6 min.
- [Gelman & Loken: The garden of forking paths](https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf): sections 1–2, 10 min.
- [Dodge et al.: Show your work](https://arxiv.org/abs/1909.03004): section 5, the reporting checklist with budget, 5 min.

## Ledger prompt

> Next to `build-step5`: write the prediction line of your plan exactly as it will be committed, then the one fork you are most likely to take after seeing the result, and the sentence on the page that forbids it.

**Next:** the build session: both candidates through canvas steps 1–5, one chosen, the plan committed, the data pipeline built and sanity-checked.
