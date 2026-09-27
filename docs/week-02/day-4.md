---
title: Lesson 4 · Neuron → layer → MLP, and why the bend matters
terms: [neuron, activation function, nonlinearity, ReLU, tanh, MLP, hidden layer, XOR]
card: core-calc
---

# Lesson 4 · Neuron → layer → MLP, and why the bend matters

<p class="recall" markdown>**Previously:** gradients add where paths merge, so closures use `+=`, so every step starts by zeroing them.</p>

## Idea

Now build something worth training out of Values. A **neuron** is a weighted sum of its inputs, plus an offset, pushed through a bend. A layer is several neurons reading the same inputs: week 1's matmul, one row per neuron. An **MLP** is layers stacked. The bend is the point: without it, any stack of layers collapses into one matrix, and one matrix cannot learn the four-point puzzle called **XOR**. With it, two layers can.

## Mechanism

One neuron with two inputs:

\[ y = \tanh(w_1 x_1 + w_2 x_2 + b) \]

**tanh** is the bend, an **activation function**: a fixed S-curve that squashes any number into \((-1, 1)\), steep near 0 and flat far out. Its flat ends pass almost no gradient back (week 1, lesson 3: the saturated knob cannot be felt). The other bend you will meet most is **ReLU**, \(\max(0, x)\): cheaper, slope exactly 0 or 1, never saturating on the positive side, which is why most large models use it. Both are a **nonlinearity**: anything that is not a plain weighted sum.

A layer of 4 neurons on 2 inputs is a \(4 \times 2\) weight matrix, 4 offsets, and tanh on each result. Feed those into 1 more neuron and you have a 2–4–1 MLP: 8 + 4 + 4 + 1 = 17 parameters. The middle layer is a **hidden layer**: its four numbers are not data and not answers, but learned in-between features nobody labelled.

Why the bend is not optional. Two linear layers with nothing between them: \(W_2 (W_1 x) = (W_2 W_1)\, x\), one matrix. Now XOR: \((0,0) \to 0\), \((0,1) \to 1\), \((1,0) \to 1\), \((1,1) \to 0\). A single neuron's decision boundary is a straight line, and no line puts the two diagonal 1s on one side and the two 0s on the other: three of four at best. With a hidden layer of two tanh neurons, each hidden unit draws its own line, roughly "at least one input on" and "both on", and the output neuron combines them: *one or the other, and not both*.

**In practice.** Open nanoGPT's `model.py` and find `class MLP`: a linear layer from width 768 to 3072, a bend called GELU (a smoothed ReLU), a linear layer back to 768: this lesson's 2–4–1, wider, inside every block of a large text model. The micrograd neuron as typed in the video (the repo's `nn.py` later swaps tanh for ReLU):

```python
class Neuron:
    def __init__(self, n_in):
        self.w = [Value(random.uniform(-1, 1))
                  for _ in range(n_in)]
        self.b = Value(0.0)
    def __call__(self, x):
        s = sum((wi * xi for wi, xi in zip(self.w, x)),
                self.b)
        return s.tanh()
```

The perception analogy needs care. A single detector with a linear receptive field cannot signal "either, but not both"; an intermediate stage must compute the pieces first. Where it breaks: the word "neuron" is inherited, not earned. A real neuron has time, spikes and feedback; this one is a weighted sum and a bend.

## Try it

<div class="visual"><iframe src="../visuals/w02-xor-neuron.html" title="One neuron versus a small MLP on the four XOR points" loading="lazy"></iframe></div>

Predict first, then try:

1. **1 neuron**: drag the three sliders and try to get all four points right. Predict the best score you can reach before you start.
2. **Hidden 2, tanh**: press Train. Predict how many steps until 4 of 4, then watch the readout.
3. **Hidden 2, no bend**: press Train again. Predict the final score before pressing, and explain it with \(W_2 W_1\).

## Retrieval

??? question "Two linear layers with no activation function between them: what can they represent that one linear layer cannot?"
    Nothing. \(W_2 W_1\) is one matrix, so the stack is one linear layer with extra parameters. The bend is what makes depth mean anything.

??? question "In one sentence, why can a single neuron not fit XOR?"
    Its decision boundary is a straight line, and XOR's two 1s sit on one diagonal with the two 0s on the other, so no line separates them.

??? question "A 2–4–1 MLP with offsets: count its parameters, layer by layer."
    Hidden layer: 4 × 2 weights + 4 offsets = 12. Output neuron: 4 weights + 1 offset = 5. 17 in total.

## Sources

- [Karpathy: micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0): about 0:52–1:09, "manual backpropagation example #2: a neuron", then 1:43–1:51, "building out a neural net library (MLP)".
- [micrograd `nn.py`](https://github.com/karpathy/micrograd/blob/master/micrograd/nn.py): `Neuron`, `Layer`, `MLP`. 5 min.
- [3Blue1Brown: But what is a neural network?](https://www.3blue1brown.com/lessons/neural-networks): the first half, layers of neurons as weighted sums and bends. 10 min.

## Ledger prompt

> Next to `core-calc`: write one XOR-shaped rule from your own research, true when exactly one of two conditions holds. What hidden quantity would a system have to compute first to make that rule a straight line?

**Next:** put the pieces together and watch it learn: five lines, repeated, and the curve they draw.
