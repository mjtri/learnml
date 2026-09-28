---
title: Lesson 3 · Ablations and controls
terms: [control condition, ablation study]
card: build-step6
---

# Lesson 3 · Ablations and controls

<p class="recall" markdown>**Previously:** a result is a difference from a baseline, and the baseline must climb three rungs: trivial, strong and tuned as hard as your method, and given the same compute.</p>

## Idea

Beating the baseline says your *method* works. It does not say *why*; a method is usually three or four decisions bundled together. An ML paper owes the reader the unbundling: which part carries the gain, which parts are decoration. The tool is the one a study uses: change one thing, hold the rest, measure. In ML the changed-one-thing run is a **control condition**, and the table of them is an **ablation study**.

## Mechanism

Start from your full method, \(A\). Each ablation row removes or swaps *one* component and re-runs the rest unchanged:

| Row | What changed | Reads as |
|---|---|---|
| A (full) | nothing | the claim |
| A − contrastive loss | pixel loss instead | is the objective the lever? |
| A − sound side | image-only encoder | does the second modality matter? |
| A − jitter | shapes always centred | is the augmentation doing the work? |

Each row pairs with the full method and differs from it in exactly one thing. A row that changes two things, "no jitter and a smaller encoder", is not a control but a second experiment with a confounded answer.

Two kinds of control: A *removal* control deletes a part (drop the sound branch). A *swap* control replaces it with something dumb of the same shape (a random frozen sound encoder). The swap is often more honest: removal also changes the parameter count, so architecture and objective moved together in one row.

**In practice**, the CLIP paper's figure 2 reads like a lab notebook: same data, same image encoder, three objectives. Predicting the caption's bag of words reaches a given zero-shot ImageNet accuracy with 3× fewer images than predicting the exact caption; the contrastive objective needs 4× fewer again. The number is not the point; the row *structure* is: one column says what was swapped, everything else is stated once.

The perception analogy is direct: a control condition in psychophysics is a stimulus identical in everything but the manipulated cue. Where it breaks: participants carry state between conditions (learning, fatigue), so you counter-balance order; a model carries no memory across runs but *does* carry a seed, which must be the same across rows or the row differs in two things again.

A plan for week 12 needs one ablation, not five: the one that tests your lever without repeating a baseline row. Swapping the objective for pixel loss *is* lesson 2's strong baseline, so the default ablation is the swap control: a frozen random sound encoder, nothing else changed. Write it as a prediction: "A − sound side costs at least \(Y\)". If it costs nothing, the sound signal did nothing.

## Try it

<div class="visual"><iframe src="../visuals/w10-confound-checker.html" title="Which pairs of runs are fair comparisons?" loading="lazy"></iframe></div>

Six runs of a shape–sound experiment. Before tapping, guess how many pairs differ in exactly one column.

1. Tap two rows. The readout names every column that differs and says whether the pair is fair.
2. Find the row that looks like an ablation but silently changed the steps too. Fix it with the **steps** button and watch the pair turn fair.
3. Which two of the six rows form the pair that isolates the objective lever, and how many runs at three seeds?

## Retrieval

??? question "Your ablation removes the sound branch, which also halves the parameter count. Why is this two levers, and what swap control fixes it?"
    Removing the branch changes objective and architecture at once. Keep the branch but freeze it with random weights: same parameter count, only the learned sound signal is gone.

??? question "Write the one ablation that tests the codec candidate's lever (architecture: a display-shaped code), with a number."
    Replace the 4×4-by-8-level code with an unconstrained one of the same width, everything else fixed. Prediction: the unconstrained code beats the 4×4×8 code by at most 3 points, so the constraint costs little.

??? question "A colleague's table has rows 'full' and 'no augmentation', trained for 3000 and 2000 steps. What can the reader conclude?"
    Nothing about augmentation. The rows differ in two things, so the gap could be steps alone. Re-run the second row at 3000 steps with the same seed.

## Sources

- [Lipton & Steinhardt: Troubling trends in ML scholarship](https://arxiv.org/abs/1807.03341): section 3.2 and the ablation discussion, 8 min.
- [Henderson et al.: Deep RL that matters](https://arxiv.org/abs/1709.06560): section 3, implementation differences as hidden changes, 8 min.
- [Radford et al.: CLIP](https://arxiv.org/abs/2103.00020): figure 2 (the objective swap) and the text around it, 5 min.

## Ledger prompt

> Next to `build-step6`: write the single ablation row for your week-12 plan as "A minus what", and the number it should cost.

**Next:** the row that only changes the seed, and why it decides whether any of the other rows mean anything.
