---
title: Lesson 4 · Sampling, temperature and top-k
terms: [sampling, temperature, top-k, greedy decoding]
card: core-transformer
---

# Lesson 4 · Sampling, temperature and top-k

<p class="recall" markdown>**Previously:** the model is embeddings, \(N\) identical blocks and a head; a block costs about \(12d^2\) parameters, and the count predicts memory and speed.</p>

## Idea

A trained model does not output the next character. It outputs a probability for *every* character in the alphabet, 65 numbers that sum to one. Turning that list into one character is **sampling**, a separate step after the model that you control with two knobs. This is why the same model gives different text on every run, why "the model said X" describes one draw from a distribution, and why a study that puts a language model in front of participants must report those knobs.

## Mechanism

The head produces logits \(z\), one per character. Divide by a **temperature** \(T\), then softmax:

\[ p_i = \frac{e^{z_i / T}}{\sum_j e^{z_j / T}} \]

Three logits, \(z = (2, 1, 0)\):

| \(T\) | probabilities | behaviour |
|---|---|---|
| 0.5 | (0.87, 0.12, 0.02) | sharper: nearly always the favourite |
| 1.0 | (0.67, 0.24, 0.09) | the model's own belief |
| 2.0 | (0.51, 0.31, 0.19) | flatter: the tail gets its turn |

As \(T \to 0\) the favourite gets everything: that is **greedy decoding**, deterministic and prone to loops (`the the the`). As \(T\) grows the distribution flattens towards uniform, and text degrades into spelling noise, because a character-level model has a long tail of slightly-plausible letters.

**Top-k** attacks that tail directly: keep only the \(k\) largest logits, set the rest to \(-\infty\) (probability zero), then softmax. With \(k = 2\) above, the third option vanishes and the first two are renormalised to (0.74, 0.26) at \(T = 1\). Temperature reshapes; top-k truncates. Most systems use both.

Generation is a loop: draw one character, append it to the context, run the model again. So errors compound, a bad draw feeding every later step, and the context is cropped to the model's window, so a long sample forgets its own beginning.

**In practice**, the whole thing is five lines of nanoGPT's `generate`, and the same lines sit behind the `temperature` field of every chat API you have called:

```python
logits = logits[:, -1, :] / temperature
if top_k is not None:
    v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
    logits[logits < v[:, [-1]]] = -float('Inf')
probs = F.softmax(logits, dim=-1)
idx_next = torch.multinomial(probs, num_samples=1)
```

`multinomial` is the draw. Replace it with `argmax` and you have greedy decoding.

The analogy here is exact rather than loose: softmax with a temperature *is* the Luce choice rule from psychophysics. If you have fitted a softmax decision model to participants' choices, you have already fitted a temperature. Where it breaks: a participant's logits come from evidence; a model's come from a matrix multiply, and nothing forces them to be calibrated.

For your own experiments the rule is short: fix the temperature, fix \(k\), fix the random `seed`, and write all three down beside the result. Otherwise two runs of the "same" model are two different stimuli.

## Try it

<div class="visual"><iframe src="../visuals/w05-sampling-playground.html" title="Temperature and top-k on a tiny distribution" loading="lazy"></iframe></div>

Predict first, then drag:

1. At \(T = 1\), guess the share of draws the favourite character gets. Press **draw 50** and compare with the readout.
2. Slide \(T\) to 0.2. Predict how many *different* characters appear in 50 draws. Then try \(T = 3\).
3. Set \(T = 1\) and \(k = 3\). Predict the favourite's new probability before the bars redraw.

## Retrieval

??? question "Logits (3, 1, 1) at temperature 1 give roughly (0.79, 0.11, 0.11). Without computing, say what happens to each number at temperature 0.5 and at temperature 4."
    At 0.5 the gap doubles in logit space, so the favourite rises towards 0.97 and the others fall. At 4 the gaps shrink to a quarter, so all three approach one third.

??? question "A model keeps producing the same sentence in loops. Which knob is set wrong, and what does changing it trade away?"
    The temperature is at or near zero: greedy decoding. Raising it breaks the loops but admits occasional low-probability characters, so spelling errors appear.

??? question "Why does top-k with k = 1 make temperature irrelevant?"
    Only the largest logit survives, so after softmax it has probability one whatever the temperature. k = 1 is greedy decoding by another name.

## Sources

- [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=2100s): 0:35 to 0:42, the first `generate` loop with `multinomial`, 7 min.
- [nanoGPT `model.py`](https://github.com/karpathy/nanoGPT/blob/master/model.py): the `generate` method at the end of the file, 3 min.
- [Holtzman et al., The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751): figure 1 and section 3 only, greedy loops and the tail, 8 min.

## Ledger prompt

> Next to `core-transformer`: think of one study you could run where an LLM generates stimuli. Write the three numbers you would have to report for another lab to reproduce the stimuli, and where in your current pipeline they would get lost.

**Next:** read *Attention Is All You Need* with a map from every box in figure 1 to a line you have now seen.
