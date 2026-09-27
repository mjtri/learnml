---
title: Lesson 5 · Multi-head attention and position encodings
terms: [multi-head attention, positional encoding]
card: core-transformer
---

# Lesson 5 · Multi-head attention and position encodings

<p class="recall" markdown>**Previously:** one head: scores divided by √d, the future masked, a softmax, a weighted sum of values; you computed it for three tokens.</p>

## Idea

One head is one kind of lookup: a single pattern of what asks for what. A sentence needs several at once: which adjective is mine, which verb. **Multi-head attention** runs several small heads side by side on slices of the vector and joins their outputs. The second gap: attention treats the tokens before you as a bag: nothing in \(q \cdot k\) knows *where* a token sat, so "strong left" and "left strong" give the same answer. A **positional encoding** fixes that by adding a per-position vector to each token first.

## Mechanism

Take width 8 and \(h = 2\) heads. Each head gets 4 numbers: its own \(W_q, W_k, W_v\) mapping the 8-vector to 4-vectors, its own \((T, T)\) softmax, its own \((T, 4)\) output. Concatenate to \((T, 8)\), then one final matrix \(W_o\) mixes them:

\[ \text{MultiHead}(x) = \big[\text{head}_1(x); \dots; \text{head}_h(x)\big]\, W_o \]

What changes is the number of independent softmax rows: two heads can say "mostly the adjective" and "mostly the verb" at once, where one row would blur them. The \(\sqrt{d}\) inside each head uses the per-head size: GPT-2 small has 12 heads of 64 in a width of 768, so it divides by 8.

Now the bag. Shuffle the tokens before a head and the set of (key, value) pairs is unchanged, so each token's output is unchanged; only the rows are reordered. The fix: \(x_i = E[\text{token}_i] + P[i]\), where \(P\) is a second lookup table with one row per position. nanoGPT learns \(P\); the 2017 paper used fixed sine waves. One consequence: \(P\) has a fixed number of rows, so the context length is a hard limit; nanoGPT calls it `block_size`.

**In practice.** nanoGPT's forward pass is three lines you can now read completely: `tok_emb = self.transformer.wte(idx)` is \((B, T, d)\), `pos_emb = self.transformer.wpe(pos)` is \((T, d)\), and `x = tok_emb + pos_emb` is week 1's broadcasting, the position rows copied across the batch. Figure 2 of "Attention Is All You Need" is this lesson as a diagram.

The vOICe is the honest analogy for positions. Pitch carries a pixel's row and time carries its column; drop the time channel and the listener gets a bag of pitches with no left or right. A transformer without \(P\) is that listener. Where it breaks: the vOICe keeps content and position in *separate* channels, while the transformer adds them into one vector and relies on the width to hold both. The bag is *right* for unordered sensor readings; there, leaving positions out is a choice.

```python
tok_emb = self.wte(idx)                 # (B, T, d)
pos_emb = self.wpe(torch.arange(T))     # (T, d)
x = tok_emb + pos_emb                   # broadcast over B
q, k, v = self.c_attn(x).split(d, dim=2)
q = q.view(B, T, h, d // h).transpose(1, 2)   # (B, h, T, d/h)
```

## Try it

<div class="visual"><iframe src="../visuals/w04-multi-head-split.html" title="Split one vector into heads; shuffle tokens with and without positions" loading="lazy"></iframe></div>

Predict first, then tap:

1. With 1 head, note which token "pulse" attends to. Predict whether 2 heads show the same row twice, then switch.
2. Positions off: predict whether "pulse"'s output changes when you tap **Shuffle**. Then turn positions on and tap again.
3. Before choosing 4 heads, write the shape line: per-head size, weights per head, concatenated output.

## Retrieval

??? question "A model has width 512 and 8 heads. What is the per-head size, and what number divides the scores inside each softmax?"
    \(512 / 8 = 64\) per head, so the scores are divided by \(\sqrt{64} = 8\), not by \(\sqrt{512}\).

??? question "A model with no positional encoding is trained on 'strong left pulse'. What does it output at the last position for 'left strong pulse', and why?"
    Exactly the same vector. The last token sees the same set of keys and values in a different order, and a weighted sum ignores order.

??? question "Why does a GPT have a hard maximum context length, and where in the code does it live?"
    The position table has one row per position and the model never trained past them. In nanoGPT it is `block_size`, the size of `wpe`.

## Sources

- [3Blue1Brown: Attention in transformers](https://www.3blue1brown.com/lessons/attention): the multi-headed part, about 20 to 24 min.
- [Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/): "The Beast With Many Heads" and "Representing The Order of The Sequence", 10 min.
- [Vaswani et al., Attention Is All You Need](https://arxiv.org/abs/1706.03762): sections 3.2.2 and 3.5, plus figure 2, 10 min.

## Ledger prompt

> Next to `core-transformer` (the "position encodings" bullet): what would break in your own data if a model saw it as a bag instead of a sequence, and one dataset of yours where a bag is the honest representation.

**Next:** the build session: a bigram on a tiny corpus, then one head bolted on, with a shape prediction before every cell.
