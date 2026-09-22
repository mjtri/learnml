---
title: Day 5 · Gradient descent
terms: [loss, gradient descent, learning rate, converge, diverge, local minimum, loss surface, training, model, NaN]
card: core-optim
---

# Day 5 · Gradient descent

<p class="recall" markdown>**Yesterday in one sentence:** one backward pass through the graph gives the sensitivity of the output to every knob: the gradient.</p>

## Idea

Give the model's wrongness a single number, the **loss**. Yesterday's machinery tells us, for every parameter, which way makes the loss go *up*. So step the other way, a little. Then do it again, thousands of times. That is **gradient descent**; everything from a line fit to a large language model is trained by a variant of it. The size of the step, the **learning rate**, is the single most important knob you will tune in the next eleven weeks.

## Mechanism

\[ \theta \leftarrow \theta - \eta \, \nabla_\theta L \]

\(\theta\) is every parameter of the **model**; \(\nabla_\theta L\) is the gradient of the loss with respect to them (day 4); \(\eta\) is the learning rate. The minus sign is day 3's "move against the sign". **Training** is this loop: forward pass → loss → backward pass → update → repeat.

Picture the **loss surface**: each position is one setting of the parameters, height is the loss. Gradient descent is walking downhill blindfolded, feeling only the tilt of the ground under your feet. You have local information, no map. Two consequences follow.

**You find a nearby valley, not the best one.** Start somewhere else and you may **converge** to a different **local minimum**. (For large networks this turns out to matter less than the 2-D picture suggests; flat plateaus and narrow ravines are the practical trouble.)

**Step length decides everything.** Too short and you crawl. Too long and you step clean across the valley onto the opposite wall, higher than where you started; the next step is bigger still, and the loss **diverges**, typically ending in **NaN**. You know this behaviour from control loops: a tracking correction with too much gain oscillates and then runs away. That comparison is exact. On a bowl-shaped loss, gradient descent *is* a discrete feedback loop, stable only while \(\eta\) times the curvature stays below 2.

That gives you a number to test. For \(L = x^2\) the gradient is \(2x\), so each update multiplies \(x\) by \((1 - 2\eta)\). With \(\eta = 0.1\) that factor is 0.8: smooth decay. At \(\eta = 0.5\) you land on the minimum in one step. At \(\eta = 1\) the factor is −1: you bounce between two walls forever. Above 1, every bounce is bigger.

Now the **ravine**: \(L = x^2 + 10y^2\), steep across, shallow along. The steep direction caps the learning rate at 0.1; at that cap the shallow direction barely moves. The path zig-zags across the ravine while creeping along it. Real loss surfaces are full of ravines, which is why week 3 introduces momentum and Adam.

Where the picture breaks: real models have millions of dimensions, and real gradients are noisy estimates from small batches. The cartoon still predicts what your loss curves will do.

```python
w = torch.tensor([3.0, -2.0], requires_grad=True)
for step in range(100):
    loss = w[0]**2 + 10 * w[1]**2    # the ravine
    loss.backward()
    with torch.no_grad():            # the update is not part of the graph
        w -= 0.05 * w.grad
        w.grad.zero_()               # gradients accumulate: reset them
```

## Try it

<div class="visual"><iframe src="../visuals/gradient-descent-2d.html" title="Gradient descent on a 2D loss surface" loading="lazy"></iframe></div>

Predict first, then run:

1. **Bowl**, learning rate 0.1, then 0.5, then 1.0, then 1.05. Predict each path from the \((1 - 2\eta)\) factor before pressing Run.
2. **Ravine**: predict the largest learning rate that does not diverge, then find it. Watch which direction misbehaves first.
3. **Two valleys**: tap two different start points. Do they end in the same place? Can a *large* learning rate jump you out of the shallow valley?

## Retrieval

??? question "Write the gradient descent update from memory and name every symbol."
    \(\theta \leftarrow \theta - \eta \nabla_\theta L\): parameters; learning rate (step size); gradient of the loss with respect to the parameters. Minus because the gradient points uphill.

??? question "A loss curve reads 2.1, 1.9, 2.6, 4.8, 31, NaN. What happened, and what is the first thing to try?"
    Training diverged: steps overshoot the valley and each overshoot is larger. Lower the learning rate by 3–10× first.

??? question "Why is plain gradient descent slow in a ravine?"
    The steep direction limits how large the learning rate can be; at that rate the shallow direction makes tiny progress, so the path zig-zags across while creeping along.

## Sources

- [3Blue1Brown: Gradient descent, how neural networks learn](https://www.3blue1brown.com/lessons/gradient-descent): 21 min.
- [d2l 12.3 Gradient descent](https://d2l.ai/chapter_optimization/gd.html): sections 12.3.1–12.3.2, the learning-rate pictures, 10 min.
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/), chapter 6 "Fitting models", section 6.1.
- Lineage read for the week: Sutton, [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), 5 min.

## Ledger prompt

> Next to `core-optim`: where in your own systems is there a "learning rate", a gain or adaptation step that crawls when too low and oscillates when too high? How did you tune it?

**Tomorrow (build day):** do all five days by hand in Colab, then let PyTorch do it for you.
