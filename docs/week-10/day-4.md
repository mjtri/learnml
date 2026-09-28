---
title: Lesson 4 · Seeds, variance and honest tables
terms: [effect size, variance across seeds]
card: core-tooling
---

# Lesson 4 · Seeds, variance and honest tables

<p class="recall" markdown>**Previously:** an ablation study is a table of controls, each row differing from the full method in exactly one thing, and the one ablation that matters is the one that tests your lever.</p>

## Idea

Two runs of the *same* code with a different random seed (weights, data order, dropout) give different numbers. Until you know how far apart those repeats land, you cannot say whether a 3-point gain is your idea or the dice. You know this problem by another name: participants. Nobody reports a user study with one participant per condition, and one seed per method is the same mistake.

## Mechanism

Measure the **variance across seeds** first: run your baseline three to five times changing only the seed, and take the standard deviation \(\sigma\) of the metric.

An **effect size** is the gain in units of that spread:

\[ \Delta = \frac{\bar{A} - \bar{B}}{\sigma} \]

A 3-point gain with \(\sigma = 1\) is \(\Delta = 3\), enormous. The same 3 points with \(\sigma = 4\) is \(\Delta = 0.75\), which five seeds per method show about one time in five. This is Cohen's \(d\).

The math is the rule you use for participants. The mean of \(n\) seeds wanders by about \(\sigma/\sqrt{n}\), so the difference of two such means wanders by about \(\sigma\sqrt{2/n}\). To see an effect \(\Delta\) reliably, the rule of thumb per method is

\[ n \approx \frac{16}{\Delta^2} \]

\(\Delta = 2\) needs 4 seeds; \(\Delta = 1\) needs 16; \(\Delta = 0.5\) needs 64, which is why half-a-spread gains reported with three seeds are usually noise. For week 12 read it backwards: 5 seeds per method detect only \(\Delta \gtrsim 1.8\), so predict at least that or call it a pilot.

**In practice**, an honest row is mean ± standard deviation over named seeds:

```
method            acc (mean ± sd, n=5)   seeds
pixel-loss enc.   64.2 ± 2.9             0-4
contrastive enc.  71.0 ± 3.1             0-4
```

The gap is 6.8 and \(\sigma \approx 3\), so \(\Delta \approx 2.3\): five seeds is enough. Week 9 reported ± standard error; this table shows the standard deviation because \(\Delta\) needs it, and either is honest when labelled. Swap the 3.1 for 1.4 without saying so and the table lies by omission, because 1.4 is the spread divided by \(\sqrt{5}\).

The part people skip: **tune the baseline as hard as your method**. Six learning rates for you and one for the baseline is six draws against one, and the best of six is higher by construction. Same sweep, same seeds, same steps, or the spread column is fiction.

Where the participant analogy breaks: people differ, but seeds vary because *you* left something random, so seed variance can be reduced (fixed data order, larger batches). Reducing it is progress; hiding it is not.

## Try it

<div class="visual"><iframe src="../visuals/w10-seeds-vs-noise.html" title="How many seeds to see an effect" loading="lazy"></iframe></div>

Before pressing **run 100 experiments**, guess how often A will appear to beat B.

1. Gain 3, spread 3, one seed each. Predict A's share of wins, then run. Now three seeds each.
2. Spread 1, gain 1. Find the smallest seed count that shows the effect in at least 80 % of experiments; compare with \(16/\Delta^2\).
3. Switch to **effect vs noise** and read off the gain your week-12 budget of 5 seeds can detect.

## Retrieval

??? question "Baseline seeds score 62, 65, 61, 64; your method scores 68 with one seed. What is the spread, the effect size, and what do you do next?"
    Spread about 1.8, so the 5-point gap is \(\Delta \approx 2.8\), promising; but one seed says nothing about your method's own spread. Run it four more times.

??? question "You can afford 10 runs in total, two methods. What is the smallest effect size you can expect to detect, and what does that mean for your prediction?"
    Five seeds each: \(\Delta \approx \sqrt{16/5} \approx 1.8\). Predict a gain at least 1.8 spreads wide, or call the run a pilot that measures \(\sigma\).

??? question "A table shows 71.0 ± 0.4 over five seeds. What two questions do you ask before trusting the ± 0.4?"
    Is 0.4 the standard deviation across seeds or the spread divided by \(\sqrt{5}\)? And did the baseline row get the same seeds and tuning sweep?

## Sources

- [Henderson et al.: Deep RL that matters](https://arxiv.org/abs/1709.06560): section 4 and figure 5, ten seeds split in two, 8 min.
- [Bouthillier et al.: Accounting for variance in ML benchmarks](https://arxiv.org/abs/2103.03098): figure 1 and section 2, which randomness dominates, 10 min.
- [Dodge et al.: Show your work](https://arxiv.org/abs/1909.03004): section 4, results that reverse with budget, 6 min.

## Ledger prompt

> Next to `core-tooling`: write the seed count you will use in week 12 and the smallest effect it can detect, next to one study of yours where the same arithmetic set the participant count.

**Next:** everything from this week on one page, written before the first run so the run cannot rewrite it.
