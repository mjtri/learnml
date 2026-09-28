---
title: Lesson 5 · Seeds are participants
terms: [standard error, confidence interval, bootstrap]
card: core-prob
---

# Lesson 5 · Seeds are participants

<p class="recall" markdown>**Previously:** a number needs its metric, a held-out split by the unit that repeats, and the dumbest comparison that would have to lose.</p>

## Idea

Train the same model with two random seeds and the accuracy moves: different shuffle, different initialization, different number. One training run is one participant, and you would never report a study with \(n = 1\). Ask of every number *how far would it move if I ran it again*; two cheap tools answer it: several runs give a **standard error**; one run's test set gives a **bootstrap** interval.

## Mechanism

**Seeds.** Run \(k\) seeds. Their mean is the result; their standard deviation \(s\) is the run-to-run spread; \(s/\sqrt{k}\) is the standard error of that mean. Three seeds score 71, 74, 68: mean 71, \(s = 3\), standard error \(3/\sqrt{3} = 1.7\). Report "71.0 ± 1.7 (standard error, 3 seeds)". A rival at 72.5 ± 1.9 differs by 1.5, but the uncertainty of a *difference* is \(\sqrt{1.7^2 + 1.9^2} = 2.6\), so the gap sits inside its own noise. Rule of thumb: two standard errors either side is roughly a 95% **confidence interval**, a range that would cover the true value in most repeats; claim a difference only when the intervals clearly separate.

**Bootstrap.** One run, a test set of \(n\) items each right or wrong: treat it as the population, draw \(n\) items *with replacement*, compute accuracy, repeat a thousand times, take the 2.5th and 97.5th percentiles. Any statistic:

```python
hits = np.array(correct, dtype=float)   # 1 right, 0 wrong
rng = np.random.default_rng(0)
boot = [rng.choice(hits, len(hits), replace=True).mean()
        for _ in range(1000)]
lo, hi = np.percentile(boot, [2.5, 97.5])
print(f"{hits.mean():.2f}  95% [{lo:.2f}, {hi:.2f}]")
```

For accuracy alone there is a shortcut: the standard error of a proportion is \(\sqrt{p(1-p)/n}\). At \(p = 0.8\) and \(n = 64\) that is 0.05, so the interval is about 0.70 to 0.90: twenty points wide.

**In practice**, apply the shortcut to any results table. A bold 76.4 over a rival's 76.1 on ImageNet's 50,000 validation images: \(\sqrt{0.76 \cdot 0.24 / 50000} = 0.0019\), a standard error of 0.19 points, so 0.3 is under two standard errors *before* counting seed variation. Henderson and colleagues showed the same for reinforcement learning: ten seeds of one algorithm, split into two groups of five, looked like two different methods.

Reading a table sceptically: how many seeds? Is the ± a standard deviation or a standard error, over what \(n\)? Does the gap exceed twice the standard error of the difference? And lesson 4's question: what dumb comparison makes the gap go away?

The honest analogy is the title: seeds are participants, and the bootstrap is what you would do with the trials of a single participant. Where it breaks: seeds are free and identically distributed, participants are neither; and seeds capture only training randomness, so a seed interval is a *floor* on the real uncertainty.

## Try it

<div class="visual"><iframe src="../visuals/w09-bootstrap-ci.html" title="Draw a test set, bootstrap it, compare the interval with the formula" loading="lazy"></iframe></div>

Predict first, then draw:

1. \(n = 20\), true accuracy 0.8. Before tapping **draw**, guess the width of the 95% interval.
2. Move \(n\) to 80. Predict how the width changes (hint: square root).
3. Set the comparison line to 0.75 with \(n = 20\). Predict whether the interval excludes it; then find the \(n\) at which it usually does.

## Retrieval

??? question "Three seeds give 71, 74 and 68. Write the result as it should be reported, and say whether a rival at 72.5 ± 1.9 over three seeds is better."
    71.0 ± 1.7 (standard error, 3 seeds). The difference is 1.5 with its own standard error about 2.6, so no claim either way.

??? question "A test set has 64 items and the model gets 80%. Give a 95% interval without a computer and say what the bootstrap adds."
    Standard error \(\sqrt{0.8 \cdot 0.2/64} = 0.05\), so about 0.70 to 0.90. The bootstrap matches here but works for any statistic.

??? question "A table bolds 76.4 over 76.1 on 50,000 test images, one seed each. Is the bold justified, and what number decides it?"
    No. The standard error of a proportion near 0.76 on 50,000 items is about 0.19 points, so 0.3 is within two of them, and seed variation was never measured.

## Sources

- [Henderson et al.: Deep Reinforcement Learning that Matters](https://arxiv.org/abs/1709.06560): section 4, figure 5, the seeds experiment, 8 min.
- [Hesterberg: What Teachers Should Know About the Bootstrap](https://arxiv.org/abs/1411.5279): section 1, 12 min.
- [Seeing Theory: frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html): the confidence-interval animation, 5 min.

## Ledger prompt

> Next to `core-prob`: take a bold number from the last paper you read. Compute its test-set standard error from \(n\), note how many seeds were run, and write whether you would have accepted the same evidence in a user study.

**Next:** the build session: a contrastive model from scratch on shape–sound pairs, then CLIP on CIFAR-10 with prompt ablations and bootstrap intervals.
