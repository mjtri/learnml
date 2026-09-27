---
title: Lesson 1 · Embeddings: a lookup table that learns
terms: [embedding, lookup table, word2vec, cosine similarity]
card: lin-word2vec
---

# Lesson 1 · Embeddings: a lookup table that learns

<p class="recall" markdown>**Previously:** week 3 moved your engine into PyTorch: `nn.Module`, `Dataset`/`DataLoader`, an optimizer, the standard loop, and a small MLP that generalises. **Why this week:** a transformer is tokens becoming vectors (this lesson) and vectors looking at each other (lessons 3–5).</p>

## Idea

A network eats numbers, and a word is not a number. The old fix was a code with one switch per word: "pulse" is position 4,017 of 50,000, all zeros and a single one. Under that code "buzz" and "vibrate" share nothing. An **embedding** replaces the switch with a short list of learned numbers, a vector, and lets *distance carry meaning*. Whatever the model learns about "buzz" now leaks, usefully, to "vibrate". That is the whole trick: the canvas move discrete → continuous.

## Mechanism

An embedding layer is a **lookup table**: a matrix with one row per token, shape `(V, d)`. Token 4,017 comes back as row 4,017, by index. The surprise is that the table is a **parameter**: the gradient flows into the row that was used, and training moves it.

\[ x = E[i], \qquad E \text{ has shape } (V, d) \]

Nothing in the table says what a direction *means*. Meaning comes from the job the vectors are trained on. **word2vec** (2013) is the cleanest case: predict a word from its neighbours with a tiny model whose only real parameters are the tables. Words used in the same contexts get pushed together, because that is the only way the tiny model can score well. Afterwards nearby vectors are near in meaning, and some directions are consistent: `king − man + woman` lands near `queen`. Nobody annotated that; raw text supervised itself.

How near is near? Take week 1's dot product and divide out length. **Cosine similarity**

\[ \cos(a, b) = \frac{a \cdot b}{\|a\|\,\|b\|} \]

runs from 1 (same direction) through 0 (unrelated) to −1 (opposite). Smallest example: \(a = (1, 2)\), \(b = (2, 4)\). Dot product 10, lengths \(\sqrt{5}\) and \(\sqrt{20}\), cosine \(10 / 10 = 1\): different length, same meaning.

**In practice.** In PyTorch the table is `nn.Embedding(V, d)`; the docs call it exactly that, "a simple lookup table that stores embeddings of a fixed dictionary and size". In Karpathy's GPT code it is `self.transformer.wte(idx)`. Not only for words: a haptics study with twelve stimulus types can give each a row and let the model discover that two of them are effectively the same stimulus.

The honest perceptual analogy is colour space: CIELAB places colours so that distance roughly matches perceived difference. Where it breaks: CIELAB was fitted to human judgements, while word2vec only sees co-occurrence, so "close" means *used in the same slots* and "hot" sits near "cold".

One caution: 64 numbers cannot hold what "left" means in every sentence. The vector is the model's *start*, and the rest is attention's job.

```python
E = torch.nn.Embedding(50_000, 64)     # (V, d), learnable
ids = torch.tensor([[4017, 12, 991]])  # (B=1, T=3) token ids
x = E(ids)                             # (1, 3, 64): one row each
```

## Try it

<div class="visual"><iframe src="../visuals/w04-embedding-space.html" title="Drag words in a 2-D embedding space and read the cosine" loading="lazy"></iframe></div>

Predict first, then drag:

1. Before tapping **Trained**, guess which two of the eight words end up closest by cosine. Check the readout.
2. Drag "buzz" to three times its distance from the origin, same direction. Predict its cosine with "vibrate", and the dot product.
3. Find a pair whose cosine is near 0. What could a model conclude about them?

## Retrieval

??? question "Tokens are numbered 0 to V−1, the embedding size is 32, and a batch holds 8 sequences of 16 tokens. What shape is the table, and what shape comes out?"
    `(V, 32)`; the lookup of an `(8, 16)` batch of ids gives `(8, 16, 32)`: one row per token, batch and sequence axes kept.

??? question "a = (3, 0) and b = (1, 1). Compute the cosine similarity and say what the number means."
    Dot product 3; lengths 3 and \(\sqrt{2}\); cosine \(3 / (3 \sqrt{2}) = 0.71\). The vectors are 45° apart: similar directions, not the same.

??? question "word2vec never sees a similarity label. Explain why similar words end up near each other anyway."
    The task is to predict neighbours and the only parameters are the tables. Words used in the same contexts must give the same predictions, and the cheapest way is nearly the same vector.

## Sources

- [3Blue1Brown: Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt): the "Embedding" section only, about 10 min.
- [Alammar: The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/): "Word Embeddings" to "Language Model Training", 12 min.
- [Mikolov et al., word2vec paper](https://arxiv.org/abs/1301.3781): sections 1 and 3, 10 min.

## Ledger prompt

> Next to `lin-word2vec` (and `move-discrete-continuous`): name one discrete thing in your research you treat as unrelated symbols, a stimulus id or a gesture label. What free supervision from your own logs would push similar ones together?

**Next:** the simplest model that uses a table: predict the next token from the current one, and the loss that scores it.
