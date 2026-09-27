---
title: Lesson 5 · Reading the Transformer paper with a map
terms: []
card: lin-transformer
---

# Lesson 5 · Reading the Transformer paper with a map

<p class="recall" markdown>**Previously:** the model outputs a probability per character; sampling with a temperature and top-k turns that into text, and the knobs belong in your notes.</p>

## Idea

You have now met every part of *Attention Is All You Need* (2017) as code. Reading the paper is no longer learning; it is *mapping*: put your finger on each box in figure 1 and name the line in nanoGPT that does it. The map also shows the three places where the paper and the code you run differ, the source of most confusion about "the transformer". Read in this order: figure 1, section 3 with the figure beside it, the parameter count; skip the translation results on this pass.

## Mechanism

Figure 1 has two stacks. The left one reads the source sentence, the right one writes the translation. nanoGPT keeps only the right stack, and drops the middle box that let it read the left one. Every remaining box is a line you have seen:

| Figure 1 box | nanoGPT line | Shape, tiny Shakespeare |
|---|---|---|
| Output Embedding | `self.wte(idx)` | (B, T) → (B, T, 384) |
| Positional Encoding | `self.wpe(pos)`, added | (T, 384) |
| Masked Multi-Head Attention | `CausalSelfAttention` | (B, T, 384) → same |
| Add & Norm | `x = x + ...`, `ln_1`/`ln_2` | same |
| Feed Forward | `MLP` | 384 → 1536 → 384 |
| N× | `for block in self.transformer.h` | 6 times |
| Linear | `self.lm_head` | (B, T, 384) → (B, T, 65) |
| Softmax | `F.softmax` inside `generate` | (B, 65) |

The formula in section 3.2.1 is one line of the attention class:

\[ \text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) V \]

```python
att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
att = att.masked_fill(self.bias[:,:,:T,:T] == 0, float('-inf'))
att = F.softmax(att, dim=-1)
y = att @ v
```

**Three honest differences.** First, *Add & Norm* in the figure is post-norm; nanoGPT and nearly every model since are pre-norm (lesson 2). Second, the paper's positions are fixed sine waves (section 3.5); nanoGPT learns a position table instead. Third, the paper has the left stack and the cross-attention box that reads it; nanoGPT has neither, so about a third of the figure has no counterpart in your code.

**In practice**, check the paper's own numbers with lesson 3's formula. The base model has \(N = 6\), \(d = 512\), 37,000 shared word pieces. A left-stack block is \(12d^2 = 3.1\)M; a right-stack block has one extra attention, \(16d^2 = 4.2\)M. Six of each is 44M; the shared embedding table is \(37000 \times 512 = 18.9\)M. Total 63M against the 65M in table 3; the rest is biases. When a phone-sized formula reproduces a 2017 table within three percent, you are reading the paper, not looking at it.

The analogy from your world is a cockpit's controls-and-displays diagram versus its wiring: the diagram is faithful about *what connects to what*, but the wiring has changed since. Where it breaks: a cockpit diagram is descriptive; the figure was prescriptive, and the code deliberately departed from it.

## Try it

<div class="visual"><iframe src="../visuals/w05-figure1-map.html" title="Tap a box of figure 1 to see its line and its shapes" loading="lazy"></iframe></div>

Predict first, then tap:

1. Before tapping **Feed Forward**, write the two shapes it moves through for \(d = 384\).
2. Tap **Add & Norm**. Predict which order the panel marks as "the paper" and which as "the code".
3. Find the box with **no** line of code in nanoGPT. Guess how many parameters it would add per block (hint: another attention).

## Retrieval

??? question "Name the three differences between figure 1 and nanoGPT, and say which one changes the residual stream."
    Post-norm versus pre-norm, sinusoidal versus learned positions, and the missing left stack plus cross-attention. Only the norm placement changes the stream: post-norm rescales the running sum after every block.

??? question "The base Transformer has stream width 512 and six right-stack blocks. Estimate their parameters and explain the extra term."
    \(16 \times 512^2 \approx 4.2\)M per block, 25M for six. The extra \(4d^2\) is the cross-attention that reads the left stack, which nanoGPT does not have.

??? question "Which line of code is the √d_k in the attention formula, and what goes wrong without it?"
    The `1.0 / math.sqrt(k.size(-1))` factor. Without it the dot products grow with head size, the softmax saturates towards one-hot, and its gradients vanish.

## Sources

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762): figure 1, section 3 up to 3.5, and table 3, 25 min.
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/): the section on the two stacks, code beside the figure, 10 min.
- [LLM Visualization (Brendan Bycroft)](https://bbycroft.net/llm): walk the smallest model shown once, following one token through a block, 10 min.

## Ledger prompt

> Next to `lin-transformer`: the card says the dropped assumption was "sequence models need recurrence". Name the figure-1 box that replaces recurrence, and why that is the `move-inductive-bias` move.

**Next:** the build session: train on tiny Shakespeare, log validation loss with `cfg` and `seed`, and sample.
