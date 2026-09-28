---
title: "Lesson 3 · Attention as soft lookup: query, key, value"
terms: [attention, query vector, key vector, value vector, attention weights]
card: lin-attention
---

# Lesson 3 · Attention as soft lookup: query, key, value

<p class="recall" markdown>**Previously:** a language model scores the next token by its surprise, and a bigram's context length of 1 caps what it can know.</p>

## Idea

To predict well, a token needs information from earlier tokens, but *which* ones depends on the token. In "the pulse on the left hand was ___", "pulse" and "left" matter and "the" does not. **Attention** is a lookup in which each token *asks* for what it needs, every token *advertises* what it has, and the strength of the match decides how much of each token's *content* is copied over. It is soft: instead of picking one row it takes a weighted mix, and a mix is differentiable, so the asking and the advertising can be learned. Discrete → continuous again.

## Mechanism

Each token's embedding \(x\) becomes three vectors through three learned matrices:

\[ q = W_q x, \qquad k = W_k x, \qquad v = W_v x \]

The **query** \(q\) is what this token is looking for. The **key** \(k\) is what it offers. The **value** \(v\) is what it hands over once matched. Token \(i\) scores token \(j\) by the dot product \(q_i \cdot k_j\), large when question matches offer. A softmax over one row's scores gives the **attention weights**, at or above zero and summing to 1, and the output for token \(i\) is the weighted sum of the values.

Smallest example: three tokens, two numbers each, "strong left pulse":

| token | \(q\) | \(k\) | \(v\) |
|---|---|---|---|
| strong | (0, 1) | (2, 0) | (3, 0) |
| left | (1, 0) | (0, 2) | (0, 3) |
| pulse | (2, 0) | (1, 1) | (1, 1) |

"pulse" asks with \(q = (2, 0)\). Against the three keys: \(4, 0, 2\). The visual also divides scores by \(\sqrt{2}\) before the softmax (the next lesson says why), giving weights \(0.77, 0.05, 0.19\): "pulse" mostly reads "strong", a little of itself, almost nothing of "left". The output is \(0.77\,(3,0) + 0.05\,(0,3) + 0.19\,(1,1) = (2.5, 0.3)\): "pulse" now carries "strong" inside it.

Why three matrices? Because *what I look for*, *what I offer* and *what I hand over* are different things. "pulse" looks for an intensity word; "strong" advertises "I am an intensity word" and hands over "intensity: high".

**In practice.** The head you build this week is Karpathy's `Head.forward`, minus the ÷√d and mask lines the next lesson adds:

```python
k = self.key(x)                 # (B, T, hs)
q = self.query(x)               # (B, T, hs)
wei = q @ k.transpose(-2, -1)   # (B, T, T) scores
wei = F.softmax(wei, dim=-1)    # rows sum to 1
v = self.value(x)               # (B, T, hs)
out = wei @ v                   # (B, T, hs) weighted mix
```

The nearest analogy is a dictionary lookup: match the key, return the value. Two honest differences: every key answers a little, and it returns a blend, never one entry. Selective attention at a party breaks worse: human attention is a capacity limit, while every token here attends to every other, in parallel.

## Try it

<div class="visual"><iframe src="../visuals/w04-attention-heatmap.html" title="Edit Q, K, V for three tokens and watch the softmax weights" loading="lazy"></iframe></div>

Predict first, then edit:

1. Before touching anything, read the queries and keys and predict which token "left" attends to most. Tap its row to check.
2. Change the key of "left" to (2, 0), identical to "strong"'s key. Predict the "pulse" row before it updates. Do the values matter to the weights?
3. Set every query to (0, 0). Predict every row, then the outputs: what has attention become?

## Retrieval

??? question "In your own words: what does each of Q, K and V contribute to the output for one token?"
    The query says what this token wants; the keys say what each token offers, and query·key scores the match; the values are what gets mixed into the output, in proportion to those scores.

??? question "Two tokens have identical keys but different values. A query matches them. What are their weights, and what does the output contain?"
    Equal weights, whatever the values are. The output holds the average of their values at that shared weight: attention cannot tell them apart.

??? question "For one query the scores against three keys are (1, 1, 1). What are the weights, and what is the output?"
    Softmax of equal numbers is uniform, 1/3 each. The output is the plain mean of the three values; no lookup happened.

## Sources

- [3Blue1Brown: Attention in transformers](https://www.3blue1brown.com/lessons/attention): from the start through "Queries" and "Keys", about 13 min.
- [Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/): "Self-Attention at a High Level" and "Self-Attention in Detail", 10 min.
- [Bahdanau et al., Neural machine translation by jointly learning to align and translate](https://arxiv.org/abs/1409.0473): sections 1–3, skim in 15 min; figure 3 is the point.

## Ledger prompt

> Next to `lin-attention`: Bahdanau dropped the assumption that compressing the input into one fixed vector (the `lin-seq2seq` bottleneck) is necessary. Name one pipeline in your work where a summary is computed early and used late, and what "look back at the raw thing with learned weights" would mean there.

**Next:** the two details that make the lookup trainable: divide by √d, and blank out the future.
