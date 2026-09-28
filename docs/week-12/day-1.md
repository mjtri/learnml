---
title: Lesson 1 · The chosen family in one page
terms: [sonification, spectrogram, latent]
card: bridge-crossmodal
---

# Lesson 1 · The chosen family in one page

<p class="recall" markdown>**Previously:** read for one table cell, write its five-line checklist and a tolerance, walk the repo from entry point to metric, reproduce, and when the number is off, check cheapest first and write the gap down.</p>

## Idea

The week-10 plan chose the cross-modal contrastive embedding, and this week runs it. The whole family fits on one page: two small networks, one loss, one space. The experiment does not ask whether a network can learn the vOICe mapping (a matrix can). It asks whether the *space it learns* orders shape pairs the way a listener confuses them: a claim about a person, tested first against a stand-in.

## Mechanism

Start from the data, since the objective needs pairs. **Sonification** is a fixed rule from data to sound; the vOICe rule scans a 16×16 image left to right, one 60 ms snippet per column, one pitch per row, brightness as loudness. Week 10's notebook folded each snippet back into a **spectrogram**: 16 pitch bands by 16 time slices. Every image gets a partner sound for free, with no labelling.

Two encoders: \(f\) maps the 256 pixels to a short vector, \(g\) maps the 256 spectrogram numbers to one of the same length. Each vector is a **latent**: what the network kept. Both are scaled to unit length, so the similarity of image \(i\) and sound \(j\) is a cosine, \(s_{ij} = f(x_i) \cdot g(a_j)\).

InfoNCE from week 9, in a batch of \(B\) pairs, is a softmax over the row:

\[ \mathcal{L}_i = -\log \frac{\exp(s_{ii}/\tau)}{\sum_{j=1}^{B} \exp(s_{ij}/\tau)} \]

Pick your partner out of the batch, averaged over rows and columns. Chance is \(\ln B\): 4.16 for \(B = 64\), the number to read the first loss curve against. The temperature \(\tau\) sharpens the softmax; 0.07 is CLIP's, a knob you fix, not tune.

Why not a classifier? One trained on 20 shape names learns 20 boundaries and nothing about which shapes are *near*. The contrastive space must spread the classes so their sounds can be told apart in a batch; two shapes whose sounds collide (a rising and a falling line use the same pitch bands in reversed order) stay close, because no batch can separate them. That nearness is the prediction.

**In practice**, the four rows the build session runs, from `week10_plan.md`:

```
A          contrastive image<->sound, 32-d latent
B strong   pixel-loss autoencoder, same encoder, same steps
B trivial  pixel distance between class means
ablation   contrastive image<->image (no sound side)
```

The ablation was sharpened from week 10's plan, where the pixel-loss swap was both the strong baseline and the ablation. Dropping the *sound side* asks what the claim needs: does the agreement come from hearing, or from any contrastive training on these shapes? It is logged in the notebook's first predict cell, before any run, next to the pre-registered \(X = 0.2\).

Your field's version: a discrimination experiment orders stimulus pairs without any model; this model *predicts* that ordering from the mapping alone. Where it breaks: a listener has working memory and a learning curve, the model has neither, so a mismatch may only mean the listener has not finished learning. Lineage: CLIP with text in place of sound; Perceiver with one encoder for every modality.

## Try it

<div class="visual"><iframe src="../visuals/w12-sonifier.html" title="Draw a 16×16 image, hear it, and see its spectrogram" loading="lazy"></iframe></div>

Predict each spectrogram before drawing:

1. A rising diagonal, then a falling one. Will the two spectrograms share pitch bands, time slices, both, or neither?
2. A small dot top-left, then the same dot bottom-right. Which of pitch and time moves?
3. A full column, then a full row. Which sounds like a chord and which like a sweep? Check the active-bands readout.

## Retrieval

??? question "Batch size 64, InfoNCE loss after 50 steps reads 4.1. Is the model learning yet, and what number are you comparing against?"
    Not yet: chance is ln 64 ≈ 4.16. Learning shows as the loss falling clearly below that line.

??? question "Two shapes sound nearly identical under the vOICe rule. Where do their latents end up, and why does the loss allow it?"
    Close together. InfoNCE can only push apart pairs that a batch can distinguish; if the sounds carry no difference, no gradient separates them.

??? question "Why does the plan drop the sound side as the ablation rather than swapping the contrastive loss for a pixel loss?"
    The pixel-loss swap is already the strong baseline. Dropping the sound side tests whether hearing, not contrastive training alone, produces the agreement.

## Sources

- [CLIP paper](https://arxiv.org/abs/2103.00020): section 2.3 and figure 3, the pseudocode, 10 min.
- [The vOICe](https://www.seeingwithsound.com/): the description of the mapping, 5 min.
- [Perceiver paper](https://arxiv.org/abs/2103.03206): figure 1 only, 3 min.

## Ledger prompt

> Next to `bridge-crossmodal`: the one sentence a reviewer must believe for this experiment to matter, and the one measurement (not a model number) that would settle it.

**Next:** the alternative path: an autoencoder whose bottleneck is a 4×4 display, and the trick that trains through rounding.
