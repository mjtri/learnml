---
title: Day 3 · Derivative = sensitivity
terms: [function, derivative, slope, numerical gradient]
card: core-calc
---

# Day 3 · Derivative = sensitivity

<p class="recall" markdown>**Yesterday in one sentence:** a layer is a matrix multiply, each output a weighted mix of the inputs, and learning means choosing the weights.</p>

## Idea

To improve a model we need to know, for each of its millions of weights: *if I turn this knob up a hair, does the error go up or down, and how fast?* That number is a **derivative**. It is a sensitivity, measured at the current setting, and nothing more mystical than that. Today: one knob.

## Mechanism

Take any **function** \(f\). The recipe is *nudge and measure*:

\[ \frac{df}{dx} \approx \frac{f(x+h) - f(x)}{h} \qquad \text{for a small } h \]

Try \(f(x) = x^2\) at \(x = 3\) with \(h = 0.01\): \((9.0601 - 9)/0.01 = 6.01\). The exact answer is \(2x = 6\). Geometrically this is the **slope** of the curve at that point: shrink \(h\) and the line through the two points settles onto the tangent.

Three facts to keep:

1. **It is local.** At \(x=3\) the slope of \(x^2\) is 6; at \(x=0\) it is 0; at \(x=-2\) it is −4. A derivative is always "at this setting".
2. **The sign is a direction.** Positive means raising \(x\) raises \(f\). To *lower* \(f\), move \(x\) against the sign.
3. **The size is leverage.** It also gives a forecast: \(f(x + \Delta) \approx f(x) + \text{slope} \cdot \Delta\). The forecast is only good for small \(\Delta\): the root reason models learn in many small steps.

The perception analogy is psychophysics. On a stimulus–response curve, the slope at the operating point says how much the response changes per unit of stimulus: steep means small differences are discriminable, flat (saturation) means changes go unnoticed. A model has the same problem: where the derivative is zero it cannot "feel" that knob, so it gets no learning signal from it. Where the analogy breaks: a JND is the threshold of a noisy observer, while a derivative is an exact, noiseless slope.

The nudge recipe works on anything, even a whole network treated as a black box; the result is called a **numerical gradient**. Its flaw is cost: one extra run of the model *per knob*, so a million weights means a million runs per learning step. Tomorrow's trick gets them all from roughly one extra run. The numerical version survives as the gold-standard check; you will use it on build day.

Slopes worth knowing by heart; software handles the rest.

| \(f(x)\) | slope | in words |
|---|---|---|
| \(a \cdot x\) | \(a\) | a gain is its own sensitivity |
| \(x^2\) | \(2x\) | steeper further out |
| \(\max(0, x)\) (ReLU) | 0 or 1 | off, or passes changes through |
| \(\tanh x\) | \(1 - \tanh^2 x\) | flat at both ends: saturates |

```python
def f(x): return x**2
x, h = 3.0, 1e-4
print((f(x + h) - f(x)) / h)   # 6.0001
```

## Try it

<div class="visual"><iframe src="../visuals/slope-slider.html" title="Nudge and measure: secant becomes tangent" loading="lazy"></iframe></div>

Predict first, then drag:

1. \(f = x^2\) at \(x = 1.5\): predict the slope. Then shrink \(h\) from 1 to 0.01 and watch the estimate close in on it.
2. Switch to **ReLU**. Where is the slope exactly 0? If this were a unit in a network sitting there, what would it learn from this input?
3. On **sin**, find an \(x\) where the slope is 0. The top of a hill: to first order, nudging does nothing.

## Retrieval

??? question "Estimate the derivative of f(x) = x³ at x = 2 using h = 0.1. What does the number mean?"
    \((2.1^3 - 2^3)/0.1 = (9.261 - 8)/0.1 = 12.61\) (exact: 12). Near \(x = 2\), the output changes about 12 times as fast as the input.

??? question "The derivative at the current setting is −4. Which way do you move x to lower f, and what do you expect from a step of 0.1?"
    Raise \(x\). The slope is negative, so increasing \(x\) decreases \(f\): you move against the sign. Forecast: \(f\) drops by about \(4 \times 0.1 = 0.4\).

??? question "Why not train networks with numerical gradients, and what are they still good for?"
    They cost one extra run of the model per parameter, which is hopeless with millions of parameters. They remain the trusted way to check that a faster gradient method is correct.

## Sources

- [3Blue1Brown: The paradox of the derivative](https://www.3blue1brown.com/lessons/derivatives): 17 min.
- [Karpathy: micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0): from about 0:08 to 0:20, "derivative of a simple function".
- [d2l 2.4 Calculus](https://d2l.ai/chapter_preliminaries/calculus.html): section 2.4.1 only, 8 min.

## Ledger prompt

> Next to `core-calc`: name one quantity in your own research that is really a sensitivity (output change per input change). Where is its flat region, and what cannot be learned or perceived there?

**Tomorrow:** many knobs in a chain, and the trick that makes deep learning affordable.
