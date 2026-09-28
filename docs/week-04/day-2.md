---
title: "Lesson 2 · Next-token prediction: the bigram model and its loss"
terms: [sequence, next-token prediction, language model, bigram, context length]
card: core-prob
---

# Lesson 2 · Next-token prediction: the bigram model and its loss

<p class="recall" markdown>**Previously:** an embedding is a lookup table whose rows are learned, and cosine similarity reads how alike two rows are.</p>

## Idea

A **language model** has one job: given the tokens so far, put a probability on every possible next token. Any text is training data, because every position in a **sequence** is a labelled example: the label is the token that came next. Generation is asking the same question repeatedly and feeding each answer back in. This lesson builds the smallest version, the **bigram**, which looks at one token only; everything after it is "look further back, better".

## Mechanism

**Next-token prediction** with a **context length** of 1: the model sees the current token and nothing else. Make a table with one row and one column per token, \(N[a, b]\) = how often \(b\) followed \(a\). Divide each row by its sum and the row is a probability distribution: numbers at or above zero that sum to 1. Three tokens: after "left" you saw "pulse" 6 times, "buzz" 3, "left" 1, so the row is \((0.6, 0.3, 0.1)\).

The loss is week 3's. Find the probability \(p\) the model gave to the token that actually came next, take \(-\log p\), average over positions:

\[ L = -\frac{1}{T}\sum_{t} \log p(\text{token}_{t+1} \mid \text{token}_t) \]

Read it as *surprise at the right answer*: \(p = 0.6\) costs 0.51, \(p = 0.1\) costs 2.30, \(p = 1\) costs nothing. The log makes surprises add across a sequence instead of multiplying. One number to memorise: spreading probability evenly over \(V\) tokens scores exactly \(\log V\). That is the "knows nothing" line: 3.30 for 27 characters, 10.8 for a 50,000-token model.

The learned version replaces counts with a table of scores, pushes each row through a softmax, and lets gradient descent lower the loss. It arrives at the same table the counting found, which makes counting your sanity check in the build session. Notice what the learned table *is*: an embedding with `d = V`, row \(a\) holding the scores for what follows \(a\). Lesson 1's lookup table, used as the whole model.

**In practice.** Karpathy's makemore trains a bigram on 32,000 names split into characters, 27 tokens with a boundary marker: loss about 2.45 against the 3.30 line. Read it as "knows something, not much", and read any paper's loss the same way.

Your phone keyboard is a language model with a short context length. When the suggestion strip proposes "the the", that is a bigram's blindness: it answered from one token. The analogy breaks where the keyboard is also personalised and rule-filtered.

Why not count longer contexts? A context of \(k\) tokens needs \(V^k\) rows: 14 million at \(V = 27\), \(k = 5\), nearly all never seen; hopeless at \(k = 2\) for 50,000 tokens. Counting cannot look back. The next lesson looks back without a table.

```python
N = torch.zeros(V, V)
for a, b in zip(ids[:-1], ids[1:]):
    N[a, b] += 1
P = N / N.sum(1, keepdim=True)              # each row sums to 1
loss = -P[ids[:-1], ids[1:]].log().mean()   # surprise, averaged
```

## Try it

<div class="visual"><iframe src="../visuals/w04-bigram-counts.html" title="Bigram counts become probabilities; the loss is the surprise" loading="lazy"></iframe></div>

Predict first, then tap:

1. Before tapping any row, guess which token has the most uncertain next token. Check: which row is closest to even?
2. Add the line "weak left pulse" and predict whether the average loss goes up or down, and why.
3. Find a next token whose count is 0. What loss would it get, and what does **+1 smoothing** do to it?

## Retrieval

??? question "After 'buzz' the counts are: left 2, pulse 2, stop 4. Give the three probabilities and the loss if the next token is actually 'left'."
    Probabilities 0.25, 0.25, 0.5. The loss at that position is \(-\log 0.25 = 1.39\).

??? question "A model over 64 possible tokens reports a loss of 4.16. What does that number tell you about what it learned?"
    Nothing was learned: \(\log 64 = 4.16\), so it does exactly as well as spreading probability evenly. Learning shows as a loss below that line.

??? question "Why does a context of 5 tokens make the counting approach collapse, in numbers?"
    One row per possible context: \(V^5\), about 14 million for 27 tokens. Almost every row is never seen, so the table stays empty.

## Sources

- [Karpathy: makemore part 1, bigrams](https://www.youtube.com/watch?v=PaCmpygFfXo): from the start to about 1:03: counting, normalising rows, the loss.
- [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY): about 0:14 to 0:28, the bigram as an embedding table.
- [3Blue1Brown: Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt): the "Softmax" section, 5 min.

## Ledger prompt

> Next to `core-prob` (the cross-entropy bullet): write the "knows nothing" line, \(\log V\), for one prediction task in your own work, and the loss you would need to see before believing the model learned something.

**Next:** a lookup that looks back: the token asks, every earlier token answers, and a softmax decides how much of each to mix in.
