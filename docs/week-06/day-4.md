---
title: "Lesson 4 · Chinchilla: compute-optimal for a small lab"
terms: [FLOPs, compute-optimal, Chinchilla]
card: lin-chinchilla
---

# Lesson 4 · Chinchilla: compute-optimal for a small lab

<p class="recall" markdown>**Previously:** loss falls as a power law in parameters, data and compute; on log–log axes that is a straight line whose slope is the exponent.</p>

## Idea

The field followed Kaplan and spent on parameters: GPT-3 had 175 billion and saw 300 billion tokens, under two per parameter. In 2022 DeepMind re-ran the experiment more carefully and got a different answer: for a fixed budget, grow parameters and data *together*, about 20 tokens per parameter. They proved it with **Chinchilla**, 70 billion parameters on 1.4 trillion tokens, the same compute as their own 280-billion Gopher, and it won. The lesson for a small lab: "bigger" is a budget decision, and budgets can be spent wrong.

## Mechanism

Compute is counted in **FLOPs**, floating-point operations. The rule of thumb for training a transformer is

\[ C \approx 6\,N\,D \]

for \(N\) parameters and \(D\) training tokens. The 6: in the forward pass every parameter does one multiply and one add per token, so 2; the backward pass costs about twice the forward, so 4 more. Check it on GPT-3: \(6 \times 1.75\times10^{11} \times 3\times10^{11} = 3.15\times10^{23}\) FLOPs, which is 3,640 petaflop-days, the paper's own figure.

**Compute-optimal** means: for this \(C\), which split of \(N\) and \(D\) gives the lowest loss? Chinchilla fitted

\[ L(N, D) = 1.69 + \frac{406}{N^{0.34}} + \frac{411}{D^{0.28}} \]

(1.69 is the floor from the previous lesson) and minimised it under \(6ND = C\). Both exponents come out near one half: ten times the compute means about 3.2× the parameters *and* 3.2× the tokens, which lands near 20 tokens per parameter.

| Model | \(N\) | \(D\) | tokens per parameter |
|---|---|---|---|
| GPT-3 | 175 B | 300 B | 1.7 |
| Gopher | 280 B | 300 B | 1.1 |
| Chinchilla | 70 B | 1.4 T | 20 |
| Llama 3 8B | 8 B | 15 T | 1,900 |

The last row is not a mistake. Compute-optimal counts only *training*; a model that answers millions of requests pays \(2N\) FLOPs per token forever, so if inference dominates you want a smaller model trained far past the optimum.

**In practice.** nanoGPT's `model.py` estimates its own compute in `estimate_mfu`: `flops_per_token = 6*N + 12*L*H*Q*T`, where the second term is attention's extra cost, negligible at short sequence lengths, which is why 6ND works. For you: a T4 promises \(65\times10^{12}\) FLOPs per second in half precision; at 25% utilisation, about \(6\times10^{16}\) per hour. GPT-2 small (124 million parameters) trained Chinchilla-style on 2.5 billion tokens is \(1.9\times10^{18}\) FLOPs: about 32 T4-hours. Your build model, 350 thousand parameters on 3 million tokens, is \(6\times10^{12}\): seconds of arithmetic.

The experiment-design analogy: fixed lab hours split between participants and trials each; one split minimises your confidence interval, and all-trials-one-participant wastes hours as all-parameters-no-data did. Where it breaks: that trade-off follows a variance formula; \(N\) against \(D\) follows an empirical fit valid only inside the tested range.

## Try it

<div class="visual"><iframe src="../visuals/w06-compute-calculator.html" title="6ND compute calculator with the Chinchilla rule" loading="lazy"></iframe></div>

Predict first, then slide:

1. Preset **GPT-2 small**. Estimate the T4-hours for 20 tokens per parameter before reading the readout.
2. Preset **Gopher**, lock compute, then drag \(N\) down to 70 B. Predict how far \(D\) rises and which way the fitted loss moves.
3. Preset **your build model**, 9 tokens per parameter. Predict what the fit says happens to loss if you double the steps, then check.

## Retrieval

??? question "State the 6ND rule and apply it to 175 billion parameters and 300 billion tokens, in FLOPs and in petaflop-days."
    Training compute ≈ 6 × parameters × tokens = 3.15 × 10²³ FLOPs, about 3,600 petaflop-days.

??? question "Gopher and Chinchilla cost the same compute. Give both models' parameter and token counts, and say why Chinchilla won."
    Gopher: 280 B parameters, 300 B tokens. Chinchilla: 70 B, 1.4 T. Same budget, but Gopher was four times too big and had seen four times too little data.

??? question "Llama 3 8B saw about 1,900 tokens per parameter, far past 20. Why is that a sensible choice rather than an error?"
    Compute-optimal minimises training cost only. A model served millions of times pays 2N FLOPs per token forever, so a smaller model trained past the optimum is cheaper overall.

## Sources

- [Hoffmann et al., Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556): abstract, figure 1 and table 1, 15 min.
- [EleutherAI: Transformer Math 101](https://blog.eleuther.ai/transformer-math/): the "Compute requirements" section for where 6ND comes from, 10 min.
- [nanoGPT `model.py`](https://github.com/karpathy/nanoGPT/blob/master/model.py): search for `estimate_mfu`, 3 min.

## Ledger prompt

> Next to `lin-chinchilla`: a resource split in your own lab you set by habit (participants vs trials, headsets vs sessions). What would its compute-optimal-style curve look like, and which side of the optimum are you on?

**Next:** the same block used two ways: read everything at once, or read only the past.
