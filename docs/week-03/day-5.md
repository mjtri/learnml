---
title: Lesson 5 · When training breaks
terms: [initialization, normalization, BatchNorm, LayerNorm, vanishing gradient, exploding gradient, residual connection]
card: core-optim
---

# Lesson 5 · When training breaks

<p class="recall" markdown>**Previously:** the gap between training and validation curves is the diagnosis, and regularization is anything that closes it.</p>

## Idea

A network that will not train fails in a handful of ways, and each leaves a fingerprint. Loss shooting into the hundreds, or NaN, within a few steps: the learning rate. First loss 27 instead of 2.3, or stuck at 2.3 forever: the **initialization**. Trains with three layers and refuses with twenty: depth, cured by **normalization** and **residual connections**. Read the fingerprint and predict the fix: this week's done-when.

## Mechanism

Start with the spread of the numbers inside the net. A unit sums \(n\) inputs times weights; if the inputs have spread 1 and the weights spread \(\sigma\), the sum has spread

\[ \sigma\sqrt{n} \]

With \(n = 784\) and \(\sigma = 1\) that is 28: every tanh unit saturates and the first loss reads 27. With \(\sigma = 1/\sqrt{n}\) the spread stays 1 layer after layer: **LeCun** initialization. ReLU switches off half its units, so **Kaiming** uses \(\sqrt{2/n}\). That is the whole theory of init: keep the spread near 1 everywhere.

Backwards, the same product runs in reverse. Ten layers each shrinking the signal by 0.5 leave a thousandth: a **vanishing gradient**, and the early layers never learn. Ten layers each doubling it: an **exploding gradient**.

Think of ten amplifier stages: gain 0.5 per stage buries the signal in noise, gain 2 clips, and keeping each stage near unity gain is what normalization does for a network. **BatchNorm** rescales each unit's output to mean 0 and spread 1 across the batch, then learns a scale and shift back. **LayerNorm** does it across the features of one example, independent of the batch, which is why transformers use it. Both make the init scale nearly irrelevant. Normalize the inputs too: in week 1's notebook, inputs in millimetres made lr 0.1 diverge.

The last fix is structural. A **residual connection** computes \(y = x + f(x)\). Its sensitivity is \(1 + f'(x)\), and a product of many "one plus small" does not vanish: the gradient has a wire straight back through every block. The 2015 ResNet paper showed a 56-layer plain net with *higher training error* than a 20-layer one, a failure to optimize, not overfitting; with residual connections they trained 152 layers. Every transformer block is residual. Where the amplifier analogy breaks: its gain is fixed; a residual block learns its correction, and can learn zero.

The fix order. Loss explodes within a few steps: divide the learning rate by 10. First loss far above \(\log 10\): init scale. Shallow trains and deep does not: normalization or residual connections.

**In practice.** `nn.Linear` initializes itself with `init.kaiming_uniform_(self.weight, a=math.sqrt(5))`, a spread of \(1/\sqrt{3n}\): smaller than Kaiming's \(\sqrt{2/n}\), kept for compatibility. In makemore 3, one gain number decides whether a six-layer tanh net collapses to zero or pins at ±1; after BatchNorm it barely matters.

## Try it

<div class="visual"><iframe src="../visuals/w03-init-histogram.html" title="Init scale and the spread of activations through eight layers" loading="lazy"></iframe></div>

Predict first, then drag:

1. Weight scale 1.0: predict the spread at layer 8 and the fraction of tanh units saturated.
2. Find the scale that keeps the spread near 1 through all eight layers. Compare it with \(1/\sqrt{64} = 0.125\).
3. Switch on normalization, then set the scale to 0.02 and to 3. Does layer 8 still care?

## Retrieval

??? question "Ten classes, and the first printed loss is 27. What is wrong, and what is the fix?"
    The weight scale is too big for the number of inputs, so the logits are huge. Shrink the initialization to about \(1/\sqrt{n}\), or normalize the layer.

??? question "Each of ten layers scales the gradient by 0.6 on the way back. By what factor does the first layer's gradient shrink, and what are two fixes?"
    \(0.6^{10} \approx 0.006\): a vanishing gradient. Fixes: initialization that keeps the spread at 1, normalization layers, or residual connections.

??? question "In the ResNet paper the 56-layer plain network had higher training error than the 20-layer one. Why does that rule out overfitting?"
    Overfitting is low training error with high validation error; here the *training* error was worse, so the deeper net could not be optimized.

## Sources

- [He et al.: Deep residual learning](https://arxiv.org/abs/1512.03385): abstract, figure 1 and section 3.1, 10 min.
- [Karpathy: makemore 3](https://www.youtube.com/watch?v=P6sfmUTpUmc): from the start to about 0:40, initial loss, saturated tanh, the gain.
- [d2l 5.4 Numerical stability and initialization](https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html): 5.4.1 and 5.4.2, 12 min.

## Ledger prompt

> Next to `lin-resnet`: why deeper plain nets trained *worse*, and where the residual wire returns in week 5. Next to `core-optim`: your fix order as three fingerprints.

**Next:** build the MLP, get it past 97 %, then break it three ways and fix it three ways, predicting each fix first.
