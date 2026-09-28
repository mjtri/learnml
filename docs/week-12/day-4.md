---
title: Lesson 4 · From a distance to a prediction about people
terms: [rank correlation, confusion matrix, JND]
card: build-step7
---

# Lesson 4 · From a distance to a prediction about people

<p class="recall" markdown>**Previously:** read a run against chance (ln B), the held-out curve against the training curve, and the latent spread; report held-out retrieval per seed.</p>

## Idea

The model gives one number per pair of shapes: a latent distance. A listener gives a different kind: how often they mix the two up. The claim is that the first ordering predicts the second. Ordering is the right word: nobody expects a distance of 0.4 to mean "confused 40% of the time", only that the model's closest pairs are the ones listeners confuse most. That calls for a statistic that ignores scale and keeps order.

## Mechanism

A **confusion matrix** for 20 shapes has 20 rows (what was played) and 20 columns (what was answered); its off-diagonal cells are the confusions. Fold it across the diagonal: one count per pair, 190 pairs. The model side is a distance between class-mean latents for the same 190.

**Rank correlation** (Spearman's) replaces each list by positions, 1 for the smallest upward, then correlates the positions. Three pairs:

| pair | model closeness | position | confusions | position |
|---|---|---|---|---|
| rising–falling | 0.89 | 1 | 31 | 1 |
| ring–circle | 0.70 | 2 | 12 | 3 |
| plus–X | 0.55 | 3 | 19 | 2 |

Position differences \(d = 0, 1, 1\), and with \(n\) pairs:

\[ \rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)} = 1 - \frac{12}{24} = 0.5 \]

Why not the plain correlation on raw values? Confusion counts are skewed: a few pairs carry most confusions and one would dominate. Positions ignore one extreme pair and any monotone re-scaling, exactly the freedom a model that never promised a scale deserves.

This week's confusions come from a synthetic listener: the sound map blurred to four pitch bands and eight time slices, noise added, answers by nearest class mean over many trials. It is a stand-in: a 20×20 table of the right shape, so the pipeline from model to \(\rho\) runs end to end; its number is not evidence about people. The human study that replaces it: a participant hears a sonified shape and picks from 20 pictures; 20 shapes × 10 repeats × 8 participants is 1600 trials, about 8 per pair, enough to order the 20 most-confused pairs, not 190. The prediction it tests, written now: \(\rho\) at least 0.4, and at least 0.2 above pixel closeness.

Your field's JND table is the same object. A **JND** is the smallest stimulus difference a participant reliably detects; a table of JNDs over pairs is a discriminability ordering, and rank correlation against it is the standard test of a perceptual model that gives no scale. Where the analogy breaks: JNDs are measured at threshold with staircases; confusions are errors well above threshold under time pressure.

**In practice**, the notebook's whole statistic is six lines of numpy:

```python
def positions(v):
    return np.argsort(np.argsort(v)).astype(float)
def rank_corr(u, v):
    return float(np.corrcoef(positions(u), positions(v))[0, 1])
rho = rank_corr(-dist_pairs, confusions)  # closeness vs confusions
```

Week 9's bootstrap wraps it: resample the 190 pairs with replacement, recompute \(\rho\) for A and B on the same resample, keep the difference; 1000 repeats give the 95% interval on A − B.

## Try it

<div class="visual"><iframe src="../visuals/w12-rank-correlation.html" title="Rank-correlation explorer: eight pairs, set the confusions, watch rho" loading="lazy"></iframe></div>

1. Set the sliders so \(\rho\) reads 1.00, then swap the counts of the top two pairs. Predict the drop first.
2. Push one pair's count to the maximum with the rest in order. How far does the plain correlation move, and how far does \(\rho\)?
3. Find a setting where \(\rho\) is near 0 but the three most-confused pairs still match the model's top three. What does that say about a study that only orders 20 pairs?

## Retrieval

??? question "Three pairs: model closeness positions 1, 2, 3; listener confusion positions 1, 3, 2. Compute rho."
    \(d = 0, 1, 1\), so \(\sum d^2 = 2\) and \(\rho = 1 - 12/24 = 0.5\).

??? question "Why is rho between latent closeness and confusion counts the right statistic, rather than the plain correlation of the raw values?"
    The model promises an ordering, not a scale, and confusion counts are skewed; positions remove the scale and the pull of one extreme pair.

??? question "The synthetic listener gives rho = 0.6 for the contrastive model. What does that number say about people?"
    Nothing. It shows the pipeline from latent distance to \(\rho\) works and gives a number to pre-register against; only the identification study is evidence about listeners.

## Sources

- [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient): definition and worked example, 8 min.
- [Kriegeskorte et al.: Representational similarity analysis](https://www.frontiersin.org/articles/10.3389/neuro.06.004.2008/full): figure 1 and the comparing-representations section, 12 min.
- [Just-noticeable difference](https://en.wikipedia.org/wiki/Just-noticeable_difference): the Quantification section (Weber's law), 5 min.

## Ledger prompt

> Next to `build-step7`: the human-study prediction as one line with a number, the trials per pair needed to order the top 20 pairs, and the confound a listener brings that the synthetic one does not.

**Next:** the one-page write-up: claim, setup, plot, surprise, decision, and the question you send to an ML collaborator.
