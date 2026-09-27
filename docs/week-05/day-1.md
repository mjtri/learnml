---
title: Lesson 1 · The residual stream
terms: [residual stream, transformer block, nanoGPT, tiny Shakespeare, character-level model]
card: lin-resnet
---

# Lesson 1 · The residual stream

<p class="recall" markdown>**Previously:** words became vectors, similar direction meant similar meaning, and attention let each token mix in the vectors of the tokens before it, weighted by relevance.</p>

## Idea

A transformer is not a pipeline in which each layer swallows its input and hands on something new. It is a **running sum**. One vector per token starts as the token's embedding; every block *reads* it, computes a small update, and *adds* it back. Nothing is overwritten. That sum is the **residual stream**; the unit that reads and writes it is the **transformer block**. ResNet's motivation: before 2015, deeper networks trained *worse*, because every layer had to relearn "pass the input through". Making identity the default, so each layer learns only a correction, fixed it.

## Mechanism

For one token, with stream width \(d\), the update rule is

\[ x_{l+1} = x_l + f_l(x_l) \]

where \(f_l\) is whatever block \(l\) computes. Unroll it and the sum shows itself:

\[ x_L = x_0 + f_1(x_0) + f_2(x_1) + \dots + f_L(x_{L-1}) \]

The final vector is the original embedding *plus* one contribution per block. Three numbers: \(x_0 = (1.0,\ 0.0,\ 2.0)\). Block 1 writes \((0.2,\ -0.1,\ 0.0)\); the stream is now \((1.2,\ -0.1,\ 2.0)\). Block 2 writes \((0.0,\ 0.3,\ -0.5)\), giving \((1.2,\ 0.2,\ 1.5)\). The original \((1, 0, 2)\) is still legible inside the result. Without the adds, after ten blocks the embedding has been laundered ten times.

Two consequences carry the week.

1. **The gradient has a highway.** The sensitivity of \(x_{l+1}\) to \(x_l\) is the identity plus a small term. Multiply twelve of those and the identity survives, so the loss still "feels" block 1. Without the add, twelve small terms multiply: week 1's vanishing chain.
2. **The stream width never changes.** Every block maps \((T, d)\) to \((T, d)\). That width is the model's working memory per token: the first number on any model's spec sheet.

A block holds two readers-and-writers in sequence: attention moves information *between* tokens; a small per-token network, the MLP, processes each token *alone*. Each adds its result to the stream.

**In practice**, this is the entire `Block.forward` in **nanoGPT**'s `model.py`, the code you will run in the build session on **tiny Shakespeare** as a **character-level model**:

```python
def forward(self, x):
    x = x + self.attn(self.ln_1(x))
    x = x + self.mlp(self.ln_2(x))
    return x
```

Two `x = x + ...` lines: that *is* the residual stream. The rest of the file is what goes inside `attn` and `mlp`; `ln_1` and `ln_2` are the next lesson.

The honest analogy is a shared scratchpad passed down a line of reviewers: each writes a note in the margin and passes it on; nobody erases. Where it breaks: the pad is a fixed-width vector, so notes are *added into the same numbers*, not kept on separate lines, and blocks writing to the same directions interfere.

## Try it

<div class="visual"><iframe src="../visuals/w05-residual-stream.html" title="Add and remove blocks on a running sum" loading="lazy"></iframe></div>

Predict first, then tap:

1. With **residual on**, add four blocks. Guess the cosine similarity between the final stream and \(x_0\). Then add four more.
2. Switch **residual off** and repeat. At which block does the similarity fall below 0.5?
3. Remove a middle block with residual on. Predict which numbers in the final stream change.

## Retrieval

??? question "Three blocks write u1, u2, u3 onto an embedding e. Write the final stream, then say what is lost if block 2 has no add."
    \(e + u_1 + u_2 + u_3\). Without the add, block 2 emits only \(u_2\): \(e\) and \(u_1\) vanish from every later block.

??? question "Stream width 768, 12 blocks, a 256-token input. What shape enters block 7, and how do you know without reading block 6?"
    (256, 768). Every block maps the stream to the same shape, so the width at any block is the width everywhere.

??? question "In week 1's chain-rule language, why does the residual stream keep the loss sensitive to block 1 of a deep model?"
    Each block's local derivative is identity plus a small term. A product of such terms keeps the identity part, so the gradient reaching block 1 does not shrink to nothing.

## Sources

- [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=5195s): from about 1:26:35, "residual connections", 6 min.
- [ResNet paper (He et al. 2015)](https://arxiv.org/abs/1512.03385): figure 1 only, deeper plain nets doing worse, 4 min.
- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html): "The residual stream as a communication channel", 8 min.

## Ledger prompt

> Next to `lin-resnet`: name one system you have built where a stage *replaced* its input instead of adding a correction. What was lost downstream, and would "identity by default" have helped?

**Next:** what the two sub-blocks calculate, and why a LayerNorm sits in front of each one.
