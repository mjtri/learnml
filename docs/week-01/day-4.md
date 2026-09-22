---
title: Day 4 · Chain rule on a graph
terms: [chain rule, computation graph, forward pass, backward pass, gradient, local derivative, autograd, backpropagation, inference]
card: core-calc
---

# Day 4 · Chain rule on a graph

<p class="recall" markdown>**Yesterday in one sentence:** a derivative is a local sensitivity; nudge-and-measure finds it, but costs one model run per knob.</p>

## Idea

A network is a long chain of simple operations. We want the sensitivity of the final error to *every* knob, including ones at the very start of the chain. The **chain rule** says sensitivities multiply along a path. **Autograd** turns that into a procedure: record the calculation as a graph while it runs, then walk the graph backward once, reusing work as you go. That backward walk is **backpropagation**, and the whole field runs on it.

## Mechanism

Take a calculation small enough to hold in your head:

\[ d = a \times b \qquad e = d + c \qquad L = e^2 \]

Drawn as boxes and arrows this is a **computation graph**. The **forward pass** fills in values. With \(a=2,\ b=-3,\ c=10\): \(d=-6\), \(e=4\), \(L=16\).

The **backward pass** starts at the output and asks of each value, "how sensitive is \(L\) to you?"

1. \(L\) to itself: 1.
2. \(L = e^2\), so \(\partial L/\partial e = 2e = 8\).
3. \(e = d + c\). Nudging \(d\) or \(c\) by 1 nudges \(e\) by 1, so both inherit 8.
4. \(d = a \times b\). Nudging \(a\) moves \(d\) by \(b\). So \(\partial L/\partial a = 8 \times (-3) = -24\), and \(\partial L/\partial b = 8 \times 2 = 16\).

Every step used one rule:

\[ \text{gradient of my input} = \textbf{local derivative} \times \text{gradient of my output} \]

Each box only needs to know its own tiny derivative (yesterday's table). The graph does the rest. The full list of sensitivities, \((-24, 16, 8)\) here, is the **gradient** of \(L\).

Two patterns cover most of what you will see. **Add distributes:** it copies the incoming gradient to both inputs unchanged. **Multiply swaps:** each input receives the incoming gradient times the *other* input's value. So if \(b = 0\), \(a\) gets gradient 0: it has no way to influence the result right now, and cannot learn.

Here the analogy is the same mathematics, not just a likeness. Think of a signal chain: tracker → filter → renderer → display. The end-to-end sensitivity of what the eye sees to a head movement is the product of the stage gains. One stage with zero gain (saturated, clipped) and nothing upstream matters. Several stages with gain above 1 and small changes blow up. Deep networks suffer both: vanishing and exploding gradients.

Why walk backward rather than nudging forward? One backward pass yields the sensitivity of **one output** to **everything**, at about the cost of a second forward pass. Nudging yields the effect of one knob per run. We have millions of knobs and one number we care about, the error. Backward wins by a factor of millions; it is also why training needs a single scalar to differentiate. At **inference** time none of this runs: only the forward pass.

```python
import torch
a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(-3.0, requires_grad=True)
c = torch.tensor(10.0, requires_grad=True)
L = (a * b + c) ** 2      # forward: graph is recorded
L.backward()              # backward: chain rule, once
print(a.grad, b.grad, c.grad)   # -24, 16, 8
```

## Try it

<div class="visual"><iframe src="../visuals/chain-rule-graph.html" title="Step through a backward pass" loading="lazy"></iframe></div>

Predict first, then step:

1. With the default values, write down all five gradients, then press **Backward step** until they are revealed.
2. Set \(b = 0\). Predict \(\partial L/\partial a\) before stepping. Why can \(a\) not influence \(L\) right now?
3. Press **Nudge a**: \(a\) grows by 0.01. Predict the change in \(L\) from the gradient, then compare with the measured change.

## Retrieval

??? question "For L = (a·b + c)² with a = 2, b = −3, c = 10, compute ∂L/∂a step by step."
    Forward: \(d=-6,\ e=4\). Backward: \(\partial L/\partial e = 2e = 8\); the add passes 8 to \(d\); the multiply swaps: \(8 \times b = -24\).

??? question "How does a gradient pass through an add box, and through a multiply box?"
    Add copies the incoming gradient to both inputs unchanged. Multiply gives each input the incoming gradient times the other input's value.

??? question "Why does backpropagation run backward from the error instead of nudging each parameter?"
    One backward pass gives the sensitivity of the single output to every parameter for about the cost of one more forward pass. Nudging needs a separate run per parameter, which is millions of runs per learning step.

## Sources

- [Karpathy: micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0): about 0:20–1:10, manual backpropagation on a graph just like today's. The most valuable 50 minutes of the week; split it over two days if needed.
- [Olah: Calculus on computational graphs](https://colah.github.io/posts/2015-08-Backprop/): 10 min read, the clearest account of why backward beats forward.
- [3Blue1Brown: What is backpropagation really doing?](https://www.3blue1brown.com/lessons/backpropagation): 13 min, for intuition at network scale.

## Ledger prompt

> Next to `core-calc`: draw a three-stage pipeline from your own work as a graph. If the last stage saturates (local derivative ≈ 0), what upstream can no longer be tuned by feedback?

**Tomorrow:** we have the gradient. Now use it to learn.
