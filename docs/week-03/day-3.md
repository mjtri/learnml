---
title: Lesson 3 · Mini-batches, momentum, Adam
terms: [mini-batch, SGD, momentum, Adam]
card: core-optim
---

# Lesson 3 · Mini-batches, momentum, Adam

<p class="recall" markdown>**Previously:** softmax turns scores into probabilities, cross-entropy charges the model for its surprise at the right label, and the gradient at the logits is probabilities minus one-hot.</p>

## Idea

The real loss averages over all 60,000 training images, so its gradient does too. Computing that for every step is wasteful: a random handful of 64 images gives a gradient that points roughly the same way at a thousandth of the cost. Gradient descent on handfuls is **SGD**. The price is noise. Two optimizers handle the noise, and week 1's ravines, by remembering the past: **momentum** averages recent gradients; **Adam** also averages their squares and gives every parameter its own step size.

## Mechanism

A **mini-batch** gradient is the mean of the per-example gradients in the batch. The mean of \(B\) noisy things has spread proportional to \(1/\sqrt{B}\): a batch of 64 is 8× less noisy than one example, but 256 is only 2× better than 64 while costing 4× more per step. You know the curve from estimating a detection threshold: doubling the trials shrinks the confidence interval by 1.4×, not 2×. Where the comparison breaks: in a study, trials are scarce; here examples are nearly free and compute per step is what you pay.

Momentum keeps a running average of the gradient and steps along it:

\[ v \leftarrow \beta v + g, \qquad \theta \leftarrow \theta - \eta v \]

With \(\beta = 0.9\), \(v\) remembers roughly the last \(1/(1-\beta) = 10\) gradients. Noise averages out; a direction that keeps agreeing builds up to 10× the push. This is the exponential moving average you would write to smooth a head-tracker signal, the same line. Where it breaks: a tracker filter smooths a signal that exists; here the "true" gradient changes as you move, so a long memory carries you past the valley floor and up the far wall.

<div class="visual"><iframe src="../visuals/w03-optimizer-ravine.html" title="SGD, momentum and Adam on the same ravine" loading="lazy"></iframe></div>

Adam keeps two averages, \(m\) of the gradient (\(\beta_1 = 0.9\)) and \(v\) of its square (\(\beta_2 = 0.999\)), and steps each parameter by

\[ \theta \leftarrow \theta - \eta \, \frac{m}{\sqrt{v} + \epsilon} \]

Dividing by the typical gradient size means a parameter with huge gradients and one with tiny gradients both move about \(\eta\) per step. The ravine's wall and floor get the same stride. So the two learning rates mean different things: for SGD, distance per unit of slope; for Adam, roughly distance per step. Typical values follow: 0.01 to 0.1 for SGD, 0.001 to 0.0003 for Adam.

**In practice.** In nanoGPT the optimizer line reads `torch.optim.AdamW(optim_groups, lr=learning_rate, betas=(0.9, 0.95))`. The betas are the two memory lengths, about 10 steps for direction and 20 for size, the second shortened from the paper's 0.999 because a language model's gradient scale drifts fast. Those betas plus the learning rate are the whole interface.

## Try it

<div class="visual"><iframe src="../visuals/w03-batch-noise.html" title="Mini-batch gradient noise versus batch size" loading="lazy"></iframe></div>

Predict first, then draw:

1. Batch size 1: draw ten batches. How often does the estimate point *uphill*? Now batch size 16.
2. Predict the spread at batch 64 from the spread at 16, then check the readout. A quarter, or a half?
3. On the ravine above, learning rate 0.05: which of the three arrives first, and which last? Then set 0.15 and predict which one diverges.

## Retrieval

??? question "Batch size 16 gives a gradient with spread s. What spread do you expect at 256, and how much more does each step cost?"
    Spread \(s/4\), since \(\sqrt{256/16} = 4\). Each step costs 16× as much compute.

??? question "Write the momentum update and say what β = 0.9 means in steps. What goes wrong if β is too high?"
    \(v \leftarrow \beta v + g\); \(\theta \leftarrow \theta - \eta v\). The average remembers about ten steps. Too much memory carries the walk past the valley floor, and it oscillates or diverges.

??? question "Why can Adam use one learning rate for parameters whose gradients differ by 100×, when SGD cannot?"
    Adam divides each parameter's step by an estimate of its own gradient size, so every parameter moves about the learning rate per step. SGD's step is proportional to the gradient, so the steep direction sets the limit.

## Sources

- [Goh: Why momentum really works](https://distill.pub/2017/momentum/): the first two sections and the interactive ravine, 12 min.
- [Kingma & Ba: Adam](https://arxiv.org/abs/1412.6980): abstract and Algorithm 1 only, 8 min.
- [d2l 12.6 Momentum](https://d2l.ai/chapter_optimization/momentum.html): sections 12.6.1 and 12.6.2, 10 min.

## Ledger prompt

> Next to `core-optim`: where in your pipeline do you already average a noisy signal over time (a filter on tracking data, a running mean over trials)? What memory length did you pick, and what broke when it was too long?

**Next:** why a loss of 0.01 proves nothing, and the data you must hide from the model.
