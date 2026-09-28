---
title: "Lesson 3 · Scaling laws: reading a log–log plot"
terms: [scaling law, power law, log–log plot]
card: lin-kaplan
---

# Lesson 3 · Scaling laws: reading a log–log plot

<p class="recall" markdown>**Previously:** a token is an opaque id, so spelling, digit chunks and the price of Korean are set by the tokenizer, not the model.</p>

## Idea

Before 2020 nobody could say what a model ten times bigger would do; you built it and found out. Kaplan and colleagues trained hundreds of language models across seven orders of magnitude and found that loss falls *smoothly and predictably* with parameters, with data and with compute, each as a **power law**. That is a **scaling law**: train small models, fit a line, read off what the big one will reach. Your skill: read the plot, because every scaling paper draws the same one.

## Mechanism

A power law says loss is proportional to size raised to a fixed negative power. Kaplan's fit for parameters \(N\):

\[ L(N) = \left(\frac{N_c}{N}\right)^{0.076}, \qquad N_c \approx 8.8 \times 10^{13} \]

The exponent is the whole story. Each tenfold increase in \(N\) multiplies the loss by \(10^{-0.076} \approx 0.84\): 16% lower per decade, wherever you start. Same shape for data, \(D^{-0.095}\), and for compute, \(C^{-0.050}\).

Take the logarithm of both sides:

\[ \log L = 0.076 \log N_c - 0.076 \log N \]

A straight line in \(\log N\) with slope \(-0.076\). So on a **log–log plot**, where each axis tick is ten times the last, a power law *is* a straight line and its slope *is* the exponent. Reading one is three checks: are both axes really ×10 per tick, over how many decades is the line straight, what is the slope. A bend downward at the right means the law is breaking; a flat floor means an irreducible loss from the noise in the text itself.

**In practice.** Figure 1 of the Kaplan paper is three panels, loss against compute, data and parameters, each a straight line on log–log axes. Figure 3.1 of the GPT-3 paper repeats it for eight sizes up to 175 billion parameters. In the build you make the same plot with three sizes: two decades instead of seven, noisier, and a steeper slope because everything is tiny. The point is that a line appears at all.

Shape barely matters at fixed \(N\): twice as deep and half as wide moves the loss a few percent. And Kaplan concluded that as compute grows you should grow the model faster than the data, \(D \propto N^{0.74}\). The next lesson corrects that one.

The psychophysics analogy is Stevens' power law: perceived intensity grows as stimulus intensity to a fixed power, and the exponent (0.33 for brightness, 3.5 for electric shock) is read off a log–log plot exactly as here. Both are empirical fits over a range. Where it breaks: Stevens' exponents shift with task and observer, and the argument here is about resources, not sensation.

## Try it

<div class="visual"><iframe src="../visuals/w06-loglog-plotter.html" title="Log–log scaling-law plotter" loading="lazy"></iframe></div>

Predict first, then drag:

1. Kaplan preset, exponent 0.076: predict the loss at \(10^{9}\) parameters from the loss at \(10^{6}\), then switch to linear axes and watch the hockey stick.
2. Add a floor of 1.7. Predict where the straight line starts to bend, then find it.
3. Put the two markers one decade apart. Predict the ratio the readout will show for exponents 0.05 and 0.2, then look.

## Retrieval

??? question "The exponent for parameters is 0.076. How much lower is the loss after 10× more parameters, and after 100×?"
    About 16% per decade (multiply by 0.84), so about 29% after two decades (0.84 × 0.84 ≈ 0.71).

??? question "Losses of 3.0 at ten million parameters and 2.4 at a billion lie on a straight log–log line. Predict the loss at a hundred billion."
    2.4/3.0 = 0.8 per two decades, so the next two decades give 2.4 × 0.8 ≈ 1.9.

??? question "A scaling curve on log–log axes goes flat at the right. Give two different explanations you would check."
    An irreducible floor: the loss cannot go below the noise in the text. Or the data ran out, so bigger models repeat examples instead of learning from new ones.

## Sources

- [Kaplan et al., Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361): figures 1–4 and section 1.2, 20 min.
- [Brown et al., GPT-3](https://arxiv.org/abs/2005.14165): figure 3.1 and its caption only, 5 min.
- [Wikipedia: Stevens's power law](https://en.wikipedia.org/wiki/Stevens%27s_power_law): the table of exponents, 5 min.

## Ledger prompt

> Next to `lin-kaplan`: one quantity in your own studies that you have only ever plotted on linear axes. If it were a power law, what slope would you expect, and what would a bend mean?

**Next:** the 2022 correction: for a fixed compute budget, models were too big and saw too little data.
