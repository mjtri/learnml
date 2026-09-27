---
title: Lesson 3 · Stacking blocks and counting parameters
terms: [parameter count, checkpoint]
card: core-transformer
---

# Lesson 3 · Stacking blocks and counting parameters

<p class="recall" markdown>**Previously:** the MLP block thinks per token, LayerNorm rescales per token, and pre-norm keeps the residual stream a clean sum.</p>

## Idea

A whole model is four things: an embedding table in, \(N\) identical transformer blocks, one final LayerNorm, and a linear layer out. Once you can count the weights in one block by hand, a model's spec sheet becomes arithmetic: how much memory it needs, how long a step takes, and which knob (depth or width) bought what. The **parameter count** is the first thing to check before downloading anything.

## Mechanism

Let \(d\) be the stream width, \(V\) the alphabet size, \(T\) the context length. Count matrices; biases and LayerNorm add a few thousand and can be ignored.

**One block.** Attention holds four \(d \times d\) matrices: query, key, value and the output projection. The MLP holds \(d \times 4d\) and \(4d \times d\). So

\[ \text{per block} \approx 4d^2 + 8d^2 = 12d^2 \]

**Outside the blocks.** Token embeddings \(V \times d\), position embeddings \(T \times d\), and the output layer \(d \times V\), which nanoGPT *ties* to the token embedding so it costs nothing extra.

**Worked example**, nanoGPT's tiny Shakespeare settings: \(N = 6\), \(d = 384\), \(T = 256\), \(V = 65\). Per block \(12 \times 384^2 = 1.77\)M; six blocks 10.6M; embeddings \(65 \times 384 + 256 \times 384 = 0.12\)M. Total about 10.7M. The script prints `number of parameters: 10.65M`. For the smallest 2019 OpenAI model (\(N = 12\), \(d = 768\), \(V = 50257\)): \(12 \times 12 \times 768^2 = 85\)M in blocks plus 38.6M of token embeddings, hence its familiar 124M.

**Depth or width?** Doubling \(N\) doubles the block count. Doubling \(d\) *quadruples* it, because every matrix is \(d^2\). Width is the expensive knob.

**Where the arithmetic goes.** Every weight is used once per token per forward pass, so multiply-adds per token are roughly the parameter count; the backward pass costs about twice that again. Attention adds a second bill that grows with \(T\), comparing every token with every earlier one, but at \(T = 256\) it is a rounding error next to the \(12d^2\) matrices. It stops being one at long contexts: next week's story.

**Memory.** Four bytes per weight in 32-bit: 10.7M weights is 43 MB; the 124M model is 500 MB; a 7-billion-parameter model is 28 GB, which is why it does not fit a free T4.

**In practice**, counting is one line, and a **checkpoint** (the saved weights) is the same numbers on disk:

```python
n = sum(p.numel() for p in model.parameters())
print(f"{n/1e6:.2f}M parameters")
for name, m in model.named_children():
    k = sum(p.numel() for p in m.parameters())
    print(f"{name:10s} {k/1e6:6.2f}M")
torch.save(model.state_dict(), "ckpt.pt")  # ~4 bytes per weight
```

In the build session the breakdown prints `blocks 10.62M`, `wte 0.02M`, `wpe 0.10M`; the arithmetic above predicts it before you run it. The honest analogy from your lab: a haptic display with 6 actuators at 3 levels versus 16 at 8 has a "parameter count" too, and it bounds which stimuli the device can express. Where it breaks: a model's weights are learned and shared across inputs; actuator settings are chosen per stimulus.

## Try it

<div class="visual"><iframe src="../visuals/w05-param-counter.html" title="Count parameters from a model's settings" loading="lazy"></iframe></div>

Predict first, then slide:

1. Load the **tiny Shakespeare** preset. Before looking, estimate the share of parameters inside the blocks versus the embeddings.
2. Double \(d\) to 768 and predict the total; then double \(N\) instead. Which costs more?
3. Pick the **124M** preset and predict the 32-bit checkpoint size in megabytes.

## Retrieval

??? question "Stream width 512, 6 blocks, alphabet 65, context 128. Estimate the parameter count and state which term dominates."
    Per block \(12 \times 512^2 = 3.1\)M; six blocks 18.9M; embeddings \(65 \times 512 + 128 \times 512 \approx 0.1\)M. About 19M, nearly all in the blocks.

??? question "You must halve a model's memory. Which single change does it, halving depth or shrinking width, and what does width have to become?"
    Halving depth halves the block parameters directly. Shrinking width must reach \(d/\sqrt{2}\) (about 0.71d), since block parameters scale with \(d^2\).

??? question "The 124M model of 2019 keeps only 85M parameters in its blocks. Where are the rest, and why does nanoGPT's tiny Shakespeare model not have that problem?"
    In the token embedding: 50257 tokens × 768. With a 65-character alphabet the table is 65 × 384, negligible next to the blocks.

## Sources

- [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=5869s): 1:37:49 "scaling up the model", the settings and printed count, 5 min.
- [nanoGPT `model.py`](https://github.com/karpathy/nanoGPT/blob/master/model.py): `GPTConfig` and `get_num_params`, 5 min.
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): count the matrices in one block yourself, 8 min.

## Ledger prompt

> Next to `core-transformer`: write the parameter-count formula in your own words, then apply it to one model you might train further later (its spec sheet lists \(N\), \(d\), \(V\)). Does it fit a T4?

**Next:** the model outputs probabilities, not characters; choosing one is a separate step with knobs you control.
