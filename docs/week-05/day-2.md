---
title: Lesson 2 · The MLP block and where LayerNorm goes
terms: [MLP block, feed-forward, pre-norm]
card: core-transformer
---

# Lesson 2 · The MLP block and where LayerNorm goes

<p class="recall" markdown>**Previously:** a transformer is a running sum; each block reads the residual stream, computes a small update and adds it back, so the original embedding stays reachable.</p>

## Idea

Attention is the only place in a transformer where tokens talk to each other. The **MLP block** is everything else: the same small two-layer network applied to every position on its own, the per-token "thinking" about what attention just delivered. Before either sub-block reads the stream, a LayerNorm puts the numbers on a standard scale. *Where* it sits decides whether the residual stream stays a clean sum, and is the biggest way the 2017 paper differs from the code you will run.

## Mechanism

**The MLP block.** For one token's vector \(x\) of width \(d\):

\[ \text{MLP}(x) = W_2\, \text{gelu}(W_1 x) \]

\(W_1\) widens from \(d\) to \(4d\), a nonlinearity bends, \(W_2\) narrows back to \(d\) so the result can be added to the stream. The paper calls this the **feed-forward** layer: information flows straight through, no mixing across positions. It is a plain week-2 MLP applied to \((T, d)\) as \(T\) independent rows. Karpathy's phrase: attention is *communication*, the MLP is *computation*.

**LayerNorm, just in time.** LayerNorm takes one token's vector, subtracts its mean, divides by its standard deviation, then applies a learned scale and shift. Three numbers: \(x = (1, 3, 5)\). Mean 3. Deviations \((-2, 0, 2)\), variance \((4 + 0 + 4)/3 = 2.67\), standard deviation 1.63. Normalised: \((-1.22,\ 0,\ 1.22)\). Per token: nothing is averaged across the batch or across positions.

**Placement.** Two orders are in use:

\[ \text{pre-norm:}\quad x \leftarrow x + f(\text{LN}(x)) \qquad\quad \text{post-norm:}\quad x \leftarrow \text{LN}(x + f(x)) \]

With **pre-norm** the LayerNorm sits on the *branch*: the stream itself is never normalised, so it remains exactly lesson 1's sum and the gradient highway is untouched. With post-norm the sum is rescaled after every block, which weakens the identity path; the original Transformer needed a careful warm-up to train at all. nanoGPT and nearly every model since 2018 use pre-norm. The 2017 figure shows post-norm: honest about 2017, not about the code you will run.

**In practice**, nanoGPT's MLP is nine lines:

```python
class MLP(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.c_fc   = nn.Linear(config.n_embd, 4 * config.n_embd)
        self.gelu   = nn.GELU()
        self.c_proj = nn.Linear(4 * config.n_embd, config.n_embd)
    def forward(self, x):
        return self.c_proj(self.gelu(self.c_fc(x)))
```

`n_embd` is the stream width \(d\); the `4 *` is the standard widening; `c_proj` is the write back onto the stream. `nn.Linear` acts on the *last* axis: `(B, T, d)` in, `(B, T, 4d)` out, no loop over tokens.

An honest analogy from your analysis pipeline: z-scoring each participant's ratings before pooling across a study, so a "4" means the same thing for everyone. LayerNorm does that per token, per block. Where it breaks: LayerNorm then multiplies by a learned gain and adds a learned offset, so it can undo itself for directions the model wants kept large; your z-score never learns.

## Try it

<div class="visual"><iframe src="../visuals/w05-layernorm-placement.html" title="Normalise one token, then choose where LayerNorm sits" loading="lazy"></iframe></div>

Predict first, then tap:

1. Set the four numbers to \((2, 2, 2, 2)\). Guess what LayerNorm outputs before you look. Then change one number to 10.
2. Switch to **placement** and pick **pre-norm**. Predict how the size of the stream grows over eight blocks, then compare with post-norm.
3. In post-norm, guess the "share of \(x_0\)" readout after block 3, then check.

## Retrieval

??? question "Normalise (2, 4, 6) with LayerNorm, before the learned scale and shift. Which number changes if the vector is (20, 40, 60)?"
    Mean 4, deviations (−2, 0, 2), standard deviation 1.63, result (−1.22, 0, 1.22). None: scaling every input by 10 scales mean and standard deviation by 10 too.

??? question "A block's MLP has stream width 256. Give the shapes of its two weight matrices and of the output for 8 sequences of 64 tokens."
    \(W_1\) is 1024 × 256, \(W_2\) is 256 × 1024 (out × in, week 1's convention). Output (8, 64, 256), the same as the input, ready to be added to the stream.

??? question "Why does pre-norm keep the residual stream 'a clean sum' while post-norm does not?"
    In pre-norm the LayerNorm sits on the branch, so the stream is only ever changed by additions. In post-norm it is applied to the sum itself, rescaling everything earlier blocks wrote.

## Sources

- [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=5098s): 1:24:58 "feedforward layers", then 1:32:25 "layernorm", 10 min.
- [On Layer Normalization in the Transformer Architecture (Xiong et al. 2020)](https://arxiv.org/abs/2002.04745): figure 1 only, the two block diagrams, 3 min.
- [PyTorch LayerNorm docs](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html): the first paragraph, 3 min.

## Ledger prompt

> Next to `core-transformer`: where in your own pipelines do you normalise per item (per trial, participant or frame) before a later stage reads it? Which of those would you *not* want a learned gain to undo?

**Next:** stack the blocks, count the parameters by hand, and see where the arithmetic goes.
