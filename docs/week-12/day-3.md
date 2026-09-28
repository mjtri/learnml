---
title: Lesson 3 · Learning, memorising, or broken
terms: []
card: build-step6
---

# Lesson 3 · Learning, memorising, or broken

<p class="recall" markdown>**Previously:** a bottleneck shaped like the display (4×4, 8 levels) trains through rounding with the straight-through estimator; a VAE shapes it with noise instead.</p>

## Idea

The build session prints a loss every 50 steps and a plot at the end; the diagnosis lives in the curves, not the final number. Three questions, in order: is the loss below chance, is the held-out number following the training number, is the space alive?

## Mechanism

**Chance first.** InfoNCE with batch \(B\) starts at \(\ln B\), and a broken model stays there. For \(B = 64\), 4.16. A run sitting at 4.1 for 300 steps is a wiring bug: mismatched pairs (images shuffled, sounds not), a temperature of 1.0 that flattens every softmax, or a learning rate that saturates the encoders.

**Train against held-out.** Every 50 steps the notebook also measures retrieval on the 25% of pairs never trained on: for each held-out image, is its own sound the nearest held-out sound? Four shapes:

| training loss | held-out retrieval | reading |
|---|---|---|
| falls to about 1 | rises to 60–90% | learning |
| falls to about 0 | peaks, then falls | memorising the training pairs |
| stuck near \(\ln B\) | stays near 1 / held-out count | broken |
| falls fast, then jumps | drops to chance | learning rate too high |

Memorising looks like success on the training curve alone; the stopping rule (fixed steps) forbids stopping at the peak; the honest fix is more data or a smaller latent, for every row. The SMOKE run shows the opposite trap: loss 0.01 by step 100, held-out retrieval 100% from step 50. Not memorising: *too easy*. The spectrogram is nearly a linear picture of the image, so a perfect retrieval curve says nothing about the claim; the number that counts is Part D's rank correlation, where A lost in the SMOKE rehearsal; predict the full run anyway.

**Is the space alive?** Under InfoNCE, all latents pointing the same way is a stationary point, not one training is pulled toward; when it happens it is a symptom (dead units, a learning rate too high), and the loss sits at \(\ln B\) although nothing is mis-wired (SimSiam's collapse is the no-negatives regime). The check is one number: the standard deviation of the unit-length latents across the held-out set, averaged over dimensions. Alive is about \(1/\sqrt{d}\), 0.18 for \(d = 32\); collapsed is under 0.02.

**In practice**, the SMOKE run's print-out (seed 0, 300 steps):

```
step    50  loss 0.13  held-out retrieval 100%  latent sd 0.17
step   100  loss 0.01  held-out retrieval 100%  latent sd 0.17
step   300  loss 0.00  held-out retrieval 100%  latent sd 0.17
```

With the pairs shuffled the same cell prints `loss 4.15` on every line and `latent sd 0.17`: alive, with nothing to learn.

The analogy is a participant's learning curve: flat at chance, the mapping was not understood; rising then falling, fatigue. Where it breaks: a participant at chance may be learning something the task misses; a model at \(\ln B\) has learned nothing.

Report held-out numbers per row and seed, not the training loss, which is only what was optimised. Before writing KILL, show the run was healthy (loss well below chance, space alive): a kill from a broken run is a bug report.

## Try it

<div class="visual"><iframe src="../visuals/w12-curve-reader.html" title="Curve reader: pick a diagnosis, then reveal the run's numbers" loading="lazy"></iframe></div>

1. Read the chance line for \(B = 64\) off the plot. Find the runs where the loss never leaves it and name each bug before revealing.
2. Find the run whose training curve looks best; check held-out and latent sd before calling it best.
3. Two runs end near the same loss. Which would you report, and which number decides?

## Retrieval

??? question "Training loss 0.05 at step 3000, held-out retrieval 20% and falling since step 800. Diagnose, and name the fix the plan allows."
    Memorising. More data or a smaller latent, applied to every row; not stopping at step 800, because the stopping rule is fixed.

??? question "Loss stuck at 4.15 with batch 64 and latent sd 0.17. Which two wiring bugs would you check first?"
    Pairs out of order (images and sounds shuffled separately) and a temperature near 1. The space is alive, so it is not collapse.

??? question "Why report held-out retrieval per seed rather than the final training loss?"
    The loss can be driven to zero by memorising; held-out retrieval measures what the claim is about, and its spread across seeds is the noise band the gap must clear.

## Sources

- [Karpathy: A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/): sections 2 and 3, 12 min.
- [Wang & Isola: alignment and uniformity](https://arxiv.org/abs/2005.10242): figure 1 and section 4.1, 8 min.
- [SimSiam paper](https://arxiv.org/abs/2011.10566): section 4.1, collapse without negatives, 5 min.

## Ledger prompt

> Next to `build-step6`: the three numbers you read before believing any run (chance level, held-out peak against final, latent sd) and the value of each that makes you stop and debug.

**Next:** the model gives a distance; the human study needs a prediction: rank correlation against a table of confusions.
