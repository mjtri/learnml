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

**Sonification** is a fixed rule from data to sound; the vOICe rule scans a 16×16 image left to right, one 60 ms snippet per column, one pitch per row, brightness as loudness. Week 10's notebook folded each snippet back into a **spectrogram**: 16 pitch bands by 16 time slices. Every image gets a partner sound for free.

Two encoders: \(f\) maps the 256 pixels to a short vector, \(g\) maps the 256 spectrogram numbers to one of the same length. Each vector is a **latent**: what the network kept. Both are scaled to unit length, so the similarity of image \(i\) and sound \(j\) is a cosine, \(s_{ij} = f(x_i) \cdot g(a_j)\).

InfoNCE from week 9, in a batch of \(B\) pairs, is a softmax over the row:

\[ \mathcal{L}_i = -\log \frac{\exp(s_{ii}/\tau)}{\sum_{j=1}^{B} \exp(s_{ij}/\tau)} \]

Pick your partner out of the batch, averaged over rows and columns. Chance is \(\ln B\): 4.16 for \(B = 64\), the number to read the first loss curve against. The temperature \(\tau\) sharpens the softmax; CLIP learns it from 0.07; here it is fixed there.

Look at a *pair*. A rising and a falling line give a diagonal and an anti-diagonal spectrogram: distinct pictures, and lesson 3 shows the spectrogram is nearly a linear picture of the image: the mapping is close to one-to-one. A listener's confusions come from the listener (a blurred ear of a few pitch bands, a short memory), not from the sound, so a model trained on exact spectrograms has no reason to inherit them. And the no-learning baseline, sound-vector distance under the fixed mapping, is nearly the stand-in listener's own ruler, since the listener is built from that map. Remember this when the notebook prints its decision.

**In practice**, the notebook's rows; the ablation is sharpened from the plan's and logged in A0:

```
A          contrastive image<->sound, 32-d latent
B strong   pixel-loss autoencoder, same encoder, same steps
B trivial  pixel distance between class means
ablation   contrastive image<->image (no sound side)
```

Week 10's plan used the pixel-loss swap as both strong baseline and ablation; dropping the *sound side* asks what the claim needs: hearing, or any contrastive training. A0 logs it before any run, next to the plan's \(X\).

Your field's version: a discrimination experiment orders stimulus pairs without any model; this model *predicts* that ordering. Where it breaks: a listener has working memory and a learning curve, the model has neither, so a mismatch may only mean the listener has not finished learning. Lineage: CLIP with text for sound; Perceiver, one encoder for every modality.

## Try it

<div class="visual"><iframe src="../visuals/w12-sonifier.html" title="Draw a 16×16 image, hear it, and see its spectrogram" loading="lazy"></iframe></div>

Predict before drawing:

1. A rising diagonal, then a falling one. Will the two spectrograms share pitch bands, time slices, both, or neither?
2. A small dot top-left, then the same dot bottom-right. Which of pitch and time moves?
3. A full column, then a full row. Which sounds like a chord and which like a sweep? Check the active-bands readout.

## Retrieval

??? question "What loss value separates learning from chance at B = 64, and why?"
    ln 64 ≈ 4.16, the loss of a softmax spreading equal weight over 64 candidates. A run at 4.1 has not started; learning is the loss falling clearly below that line.

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
