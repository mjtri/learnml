---
title: Lesson 1 · Pick your partner out of the batch
terms: [contrastive learning, positive/negative pair, InfoNCE]
card: lin-cpc
---

# Lesson 1 · Pick your partner out of the batch

<p class="recall" markdown>**Previously:** a matrix's rank counts the directions it really uses, the SVD sorts them by strength, and LoRA fine-tunes a frozen model by learning only a low-rank change B times A.</p>

## Idea

Labels are expensive; *pairs* are free. A photo arrives with its caption, a depth-camera patch with the vOICe clip you rendered from it. **Contrastive learning** turns such pairs into a training signal: scramble a batch of pairs and make the model match each item with its true partner. The only way to score well is to encode both sides so partners land close and strangers land far. That closeness is the representation you keep, learned from agreement instead of labels.

## Mechanism

Encode a batch of \(B\) pairs into unit-length vectors \(a_i\) (left side) and \(b_i\) (right side). Every \((a_i, b_i)\) is a **positive pair**; every \((a_i, b_j)\) with \(j \ne i\) is a **negative pair**. The batch becomes one \(B \times B\) matrix of cosine similarities, \(S_{ij} = a_i \cdot b_j\), and the job is to make the diagonal win each row.

"Win the row" is a classification you already know: divide the row by a temperature \(\tau\), softmax, cross-entropy against the label "column \(i\)". That loss is **InfoNCE**:

\[ \mathcal{L}_i = -\log \frac{\exp(S_{ii}/\tau)}{\sum_{j=1}^{B} \exp(S_{ij}/\tau)} \]

Temperature at work: row 1 has similarities \((0.9,\ 0.3,\ 0.1)\). At \(\tau = 1\) the softmax is \((0.50,\ 0.27,\ 0.23)\), loss \(0.69\). At \(\tau = 0.1\) the row becomes logits \((9, 3, 1)\), softmax \((0.997,\ 0.002,\ 0.001)\), loss \(0.003\). A small \(\tau\) turns modest gaps into confident choices and decides *which* negatives matter: the gradient concentrates on the hard negatives, those nearly as close as the partner. Too small and one near-duplicate dominates; CLIP learns \(\tau\), clamped above 0.01.

The batch *is* the label set, \(B - 1\) negatives per item, so a bigger batch is a harder exam. The loss is scored both ways, rows and columns, then averaged.

**In practice**, this is CLIP's whole training objective as the paper prints it in figure 3:

```python
logits = np.dot(I_e, T_e.T) * np.exp(t)   # [n, n]
labels = np.arange(n)
loss_i = cross_entropy_loss(logits, labels, axis=0)
loss_t = cross_entropy_loss(logits, labels, axis=1)
loss   = (loss_i + loss_t) / 2
```

`np.exp(t)` is the learned \(1/\tau\); `np.arange(n)` says row \(i\) belongs to column \(i\).

The honest analogy is match-to-sample: a sample, a lineup of \(B\), which one goes with it, scored by log-probability rather than hit rate. Where it breaks: your foils are chosen to be confusable; here they are whatever else was in the batch.

## Try it

<div class="visual"><iframe src="../visuals/w09-contrastive-matrix.html" title="A 4×4 batch: tap a cell, change its similarity, watch the loss" loading="lazy"></iframe></div>

Predict first, then tap:

1. Raise one off-diagonal cell until it equals the diagonal in its row. Before you do, guess that row's loss (two equal candidates).
2. Drag the temperature from 1 to 0.05, matrix unchanged. Which rows' losses fall, and does any row get *worse*?
3. Set diagonals to 1.0 and everything else to 0.0. Predict the total loss at \(\tau = 0.1\), then explain why it is not zero.

## Retrieval

??? question "Row similarities are (0.8, 0.7, 0.1) with the partner in column 1 and τ = 1. Estimate the loss and name the problem."
    The exponentials are about 2.2, 2.0 and 1.1, so the partner's probability is 2.2/5.3 ≈ 0.42 and the loss ≈ 0.87. Column 2 is a hard negative.

??? question "You have 20 shapes, each with one vOICe-style sound. Describe the positives and negatives, and count the negatives per sound in a batch of 8."
    Positive: a shape with its own sound. Negatives: that sound against the other seven shapes in the batch. Seven, not nineteen.

??? question "What does lowering the temperature do to a row's softmax, and why can going too low hurt training?"
    It sharpens: small gaps become confident probabilities and the gradient concentrates on the hardest negatives. Too low, one near-duplicate dominates every update and training stalls.

## Sources

- [CLIP paper (Radford et al. 2021)](https://arxiv.org/abs/2103.00020): section 2.3 and figure 3, the pseudocode above, 10 min.
- [SimCLR (Chen et al. 2020)](https://arxiv.org/abs/2002.05709): figure 2 and section 2.1, the loss with the batch as negatives, 10 min.
- [Lilian Weng: Contrastive Representation Learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/): the "InfoNCE" and "Key ingredients" sections, 12 min.

## Ledger prompt

> Next to `lin-cpc`: the card's dropped assumption is "self-supervision must reconstruct pixels". Name one pairing in your own data that arrives free (a depth patch and its sound). What counts as a negative, and how could a negative accidentally be a positive?

**Next:** two encoders trained this way on 400 million captions, and why the text side becomes a label set you can rewrite at will.
