---
title: Lesson 3 · Ablations and controls
terms: [control condition, ablation study]
card: build-step6
---

# Lesson 3 · Ablations and controls

<p class="recall" markdown>**Previously:** a result is a difference from a baseline, and the baseline must climb three rungs: trivial, strong and tuned as hard as your method, and given the same compute.</p>

## Idea

Beating the baseline says your *method* works. It does not say *why*, and a method is usually three or four decisions bundled together. An ML paper owes the reader the unbundling: which part carries the gain, which parts are decoration. The tool is the one you use in a study with a manipulation check: change one thing, hold the rest, measure. In ML the changed-one-thing run is a **control**, and the table of them is an **ablation study**.

## Mechanism

Start from your full method, \(A\). Each ablation row removes or swaps *one* component and re-runs everything else unchanged:

| Row | What changed | Reads as |
|---|---|---|
| A (full) | nothing | the claim |
| A − contrastive loss | pixel loss instead | is the objective the lever? |
| A − sound side | image-only encoder | does the second modality matter? |
| A − jitter | shapes always centred | is the augmentation doing the work? |

Every row is a pair with the full method, and each pair differs in exactly one thing. A row that changes two things, "no jitter and a smaller encoder", is not a control but a second experiment with a confounded answer.

Two kinds of control: A *removal* control deletes a part (drop the sound branch). A *swap* control replaces it with something dumb of the same shape (a random frozen sound encoder). The swap is often more honest, because removal also changes the parameter count, so architecture and objective moved together in one row. Henderson et al. saw the same in deep RL: gains vanished when the method was re-run in a different code base.

**In practice**, the CLIP paper's figure 2 reads like a lab notebook: swap the contrastive objective for predicting the caption's words, same data, same encoder, and transfer to new datasets falls several times over. The number is not the point; the row *structure* is: one column says what was swapped, the rest of the setup is stated once and never varies.

The perception analogy is direct: a control condition in psychophysics is a stimulus identical in everything but the manipulated cue. Where it breaks: participants carry state between conditions (learning, fatigue), so you counter-balance order; a model carries no memory across runs but it *does* carry a seed, which must be the same across rows or the row differs in two things again.

A plan for week 12 needs one ablation, not five: the one that tests your lever directly. If the lever is the objective, the ablation swaps the objective and nothing else. Write it as a prediction too: "removing the contrastive loss costs at least \(Y\)". If it costs nothing, the lever did nothing.
## Try it

<div class="visual"><iframe src="../visuals/w10-confound-checker.html" title="Which pairs of runs are fair comparisons?" loading="lazy"></iframe></div>

Six runs of a shape–sound experiment. Before tapping, guess how many pairs differ in exactly one column.

1. Tap two rows. The readout names every column that differs and says whether the pair is fair.
2. Find the row that looks like an ablation but silently changed the steps too. Fix it with the **steps** button and watch the pair turn fair.
3. Build the smallest row set that isolates the objective lever. How many runs at three seeds each?

## Retrieval

??? question "Your ablation removes the sound branch, which also halves the parameter count. Why is this two levers, and what swap control fixes it?"
    Removing the branch changes objective and architecture at once. Keep the branch but freeze it with random weights: same parameter count, only the learned sound signal is gone.

??? question "Write the one ablation that tests the codec candidate's lever (architecture: a display-shaped code), with a number."
    Replace the 4×4-by-8-level code with an unconstrained one of the same width, everything else fixed. Prediction: shape accuracy from the code drops by at most 3 points.

??? question "A colleague's table has rows 'full' and 'no augmentation', trained for 3000 and 2000 steps. What can the reader conclude?"
    Nothing about augmentation. The rows differ in two things, so the gap could be steps alone. Re-run the second row at 3000 steps with the same seed.

## Sources

- [Lipton & Steinhardt: Troubling trends in ML scholarship](https://arxiv.org/abs/1807.03341): section 3.2 and the ablation discussion, 8 min.
- [Henderson et al.: Deep RL that matters](https://arxiv.org/abs/1709.06560): section 3, implementation differences as hidden changes, 8 min.
- [Radford et al.: CLIP](https://arxiv.org/abs/2103.00020): figure 2 (the objective swap) and the text around it, 5 min.

## Ledger prompt

> Next to `build-step6`: write the single ablation row for your week-12 plan as "A minus what", and the number it should cost.

**Next:** the row that only changes the seed, and why it decides whether any of the other rows mean anything.
