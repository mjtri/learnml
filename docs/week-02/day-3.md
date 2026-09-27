---
title: Lesson 3 · Gradients add, so you must zero them
terms: [gradient accumulation, zero_grad]
card: core-calc
---

# Lesson 3 · Gradients add, so you must zero them

<p class="recall" markdown>**Previously:** the backward pass runs each node's small closure in reverse topological order, starting from `loss.grad = 1`.</p>

## Idea

Two facts, one mechanism. When a value is used in two places, its gradient is the *sum* of what comes back along both paths, so a `_backward` closure must add into `grad`, never overwrite it. That is **gradient accumulation**, and it is correct. But once closures add, they never stop: call backward twice and the second gradient piles onto the first. So every training step starts by clearing the slots: **zero_grad**. Forgetting it is the most common beginner bug in PyTorch. It does not crash; it trains badly.

## Mechanism

Start with the bug that motivates the design. Write the multiply closure with `=`:

```python
def _backward():             # out = self * other
    self.grad  = other.data * out.grad   # wrong: =
    other.grad = self.data  * out.grad
```

Run it on \(L = e \times e\) with \(e = 4\). `self` and `other` are the *same* node. The first line sets `e.grad` to 4; the second overwrites it with 4. The right answer is \(2e = 8\). Everything upstream is off by exactly a factor of two: \(a\) gets \(-12\) instead of \(-24\). The network still learns, more or less, because the direction is right.

Why add? Because that is the chain rule when paths merge. If \(L\) depends on \(e\) by two routes, the sensitivities of the routes add:

\[ \frac{\partial L}{\partial e} = \underbrace{e}_{\text{first factor}} + \underbrace{e}_{\text{second factor}} = 2e \]

A cleaner case: \(y = 3x + x\). Path one contributes 3, path two 1, so \(dy/dx = 4\). Every weight in a real network feeds several neurons, so every weight needs this. The closures say `+=`, and week 1's build-session `Value` already did.

The flip side arrives one training step later. Step 1: backward writes `a.grad = -24`. Update `a`. Step 2: backward *adds* the new gradient, say \(-22\), onto the stale one: `a.grad = -46`. Step 3: \(-66\). The update now uses the sum of every gradient so far, a learning rate that grows every step, and within a few steps the loss curve turns and runs away. The fix is one line at the top of each step: set every parameter's `grad` back to 0.

**In practice.** micrograd's `engine.py` reads `self.grad += other.data * out.grad`, with `+=` on both lines. In PyTorch the accumulation is deliberate and visible:

```python
x = torch.tensor(2.0, requires_grad=True)
(x * 3).backward(); print(x.grad)   # tensor(3.)
(x * 3).backward(); print(x.grad)   # tensor(6.)  added
x.grad.zero_()                      # or: x.grad = None
```

From week 3 one call, `opt.zero_grad()`, does it for every parameter. One detail will confuse you otherwise: modern PyTorch defaults to `set_to_none=True`, so after zeroing `print(w.grad)` shows `None`, not zeros. A memory saving, not a bug.

A haptics analogy is honest here. If each frame's actuator command is *added* to last frame's instead of replacing it, intensity ramps until the driver saturates: a slow, smooth fault rather than a crash. Where it breaks: a stuck integrator drifts with noise, while a stale gradient is an exact, reproducible number, so a numerical-gradient check catches it on the first step.

## Try it

<div class="visual"><iframe src="../visuals/w02-accumulation-bug.html" title="Switch between = and +=, and between zeroing or not, then step the training" loading="lazy"></iframe></div>

Predict first, then step:

1. With `=` instead of `+=`, predict `e.grad` and `a.grad` before pressing **Backward**. By what factor are they wrong?
2. Switch to `+=` and turn zeroing **off**. Predict `a.grad` after three steps, then press **Step ×3** and read the loss.
3. Turn zeroing back on and repeat. At which step do the two loss curves visibly part?

## Retrieval

??? question "y = 3x + x at x = 2: what is dy/dx, and which single character in a micrograd closure makes that come out right?"
    4: the two paths contribute 3 and 1 and they add. The `+=` in `self.grad += ...` does the adding.

??? question "You call loss.backward() every step and never zero. Describe a.grad after three steps and what the loss curve does."
    `a.grad` holds the sum of all three gradients, so the update grows every step, like a learning rate that keeps increasing. The loss falls at first, then oscillates and runs away.

??? question "After zeroing in modern PyTorch, print(w.grad) shows None instead of zeros. Why, and is it a bug?"
    `zero_grad` defaults to `set_to_none=True`, which frees the memory instead of writing zeros. Not a bug; the next backward creates a fresh gradient.

## Sources

- [Karpathy: micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0): about 1:22–1:27, "fixing a backprop bug when one node is used multiple times". The exact bug above, live.
- [PyTorch docs: zero_grad](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html): one page, the `set_to_none` note. 3 min.
- [Olah: Calculus on computational graphs](https://colah.github.io/posts/2015-08-Backprop/): the multi-path chain rule, first two figures. 5 min.

## Ledger prompt

> Next to `core-calc`: name one running total in a system you have built that had to be reset every cycle. What did the failure look like when the reset was missing, and how long did it take to notice?

**Next:** stop pushing single numbers around: a neuron, a layer, an MLP, and the puzzle a straight line cannot solve.
