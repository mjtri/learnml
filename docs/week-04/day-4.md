---
title: Lesson 4 · Scaled dot-product attention by hand; the causal mask
terms: [scaled dot-product, √d scaling, causal mask]
card: core-transformer
---

# Lesson 4 · Scaled dot-product attention by hand; the causal mask

<p class="recall" markdown>**Previously:** attention is a soft lookup: queries ask, keys advertise, a softmax over their dot products weights the values.</p>

## Idea

Two engineering details make attention trainable, both inside one line of code. Dot products grow with the number of dimensions, so raw scores get huge, the softmax becomes a hard pick and the gradient dies: divide by \(\sqrt{d}\). And in next-token prediction a token must not see the future, or training is cheating: blank the future before the softmax. This lesson does the full computation on paper for three tokens.

## Mechanism

**Scaled dot-product** attention, with the queries, keys and values stacked as rows of \(Q\), \(K\), \(V\), each \((T, d)\):

\[ \text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{Q K^{\top}}{\sqrt{d}}\right) V \]

\(QK^{\top}\) is \((T, T)\), row \(i\) = token \(i\)'s scores. Divide, softmax each row, multiply by \(V\): \((T, d)\) out, one mixed vector per token. With the previous lesson's numbers (\(T = 3\), \(d = 2\)):

\[ QK^{\top} = \begin{pmatrix} 0 & 2 & 1 \\ 2 & 0 & 1 \\ 4 & 0 & 2 \end{pmatrix} \]

Row 3, "pulse", by hand: \((4, 0, 2) / \sqrt{2} = (2.83, 0, 1.41)\). Exponentials \(16.9, 1, 4.1\), sum \(22.0\). Weights \((0.77, 0.05, 0.19)\). Output \(0.77\,(3,0) + 0.05\,(0,3) + 0.19\,(1,1) = (2.49, 0.32)\). Do rows 1 and 2 yourself.

**√d scaling.** If the entries of \(q\) and \(k\) are around size 1 and unrelated, \(q \cdot k\) adds \(d\) terms with random signs, and such a sum has typical size \(\sqrt{d}\): scores near 1.4 at \(d = 2\), near 8 at \(d = 64\), near 23 at \(d = 512\). Softmax of \((23, 0, 12)\) is \((1.00, 0.00, 0.00)\): a hard pick, through which almost no gradient flows, so the head never learns. Dividing by \(\sqrt{d}\) keeps typical scores near 1 whatever \(d\) is. Any divisor here acts as a temperature, sharp when small and flat when large; \(\sqrt{d}\) keeps it moderate.

**Causal mask.** Before the softmax, set every score with \(j > i\) to \(-\infty\). \(e^{-\infty} = 0\), so the row renormalises over the past only and the weight matrix comes out lower-triangular. Rows 1 and 2 become \((1, 0, 0)\) and \((0.80, 0.20, 0)\); row 3 already sees only the past. Why it is not optional: training predicts all \(T\) positions in one pass, and without the mask position \(i\) reads token \(i + 1\), its own label. The loss collapses toward zero while generation produces garbage; you do this bug on purpose in the build session.

**In practice.** nanoGPT's `CausalSelfAttention.forward` is the formula, one line each; the fused `F.scaled_dot_product_attention(q, k, v, is_causal=True)` does the same, faster:

```python
att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
att = att.masked_fill(self.bias[:, :, :T, :T] == 0, float('-inf'))
att = F.softmax(att, dim=-1)
```

The signal-processing analogy is a causal filter: a real-time vibrotactile renderer can only use past samples. It breaks because the mask is not about latency; the model computes on the whole sequence at once. The mask keeps the label out of the input.

## Try it

<div class="visual"><iframe src="../visuals/w04-causal-mask.html" title="Four tokens: what dividing by sqrt(d) and the causal mask do to the rows" loading="lazy"></iframe></div>

Predict first, then slide:

1. At \(d = 2\), note the largest weight in the "pulse" row on the unscaled side. Predict it at \(d = 64\), then slide and compare with the scaled side.
2. Turn the mask on. Before looking, write down row 1 and where row 2's removed mass goes.
3. With the mask on, does every row still sum to 1? Why?

## Retrieval

??? question "One query scores (2, 0, −2) against three keys, with d = 4. Compute the attention weights."
    Divide by \(\sqrt{4} = 2\): \((1, 0, -1)\). Exponentials \(2.72, 1, 0.37\), sum \(4.09\). Weights \((0.665, 0.245, 0.090)\).

??? question "In a causal attention over 4 tokens, which entries of row 2 can be non-zero, and what do they sum to?"
    Only columns 1 and 2, the token itself and the one before it. They sum to 1: the softmax renormalises over whatever is not masked.

??? question "Why does training without the mask give a near-zero loss but a useless generator?"
    Each position reads the next token through the values, so predicting it is trivial. At generation time the next token does not exist yet.

## Sources

- [3Blue1Brown: Attention in transformers](https://www.3blue1brown.com/lessons/attention): "The Attention Pattern" and the masking part, about 13 to 20 min.
- [Vaswani et al., Attention Is All You Need](https://arxiv.org/abs/1706.03762): section 3.2.1 only, one page.
- [nanoGPT model.py](https://github.com/karpathy/nanoGPT/blob/master/model.py): `CausalSelfAttention.forward`, 5 min.
- [PyTorch docs: scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html): the `is_causal` and `scale` arguments, 3 min.

## Ledger prompt

> Next to `core-transformer`: write the three-token computation once from memory, scores → ÷√d → mask → softmax → weighted sum, with the shape at every step, and which step you got wrong first.

**Next:** several heads at once, and the position vector that tells "strong left" from "left strong".
