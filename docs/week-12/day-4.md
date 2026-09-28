---
title: Lesson 4 · From a distance to a prediction about people
terms: [rank correlation, confusion matrix, JND]
card: build-step7
---

# Lesson 4 · From a distance to a prediction about people

<p class="recall" markdown>**Previously:** read a run against chance (ln B), held-out against training, and the latent spread; report held-out retrieval per seed.</p>

## Idea

The model gives one number per pair of shapes: a latent distance. A listener gives another: how often they mix the two up. The claim is that the first ordering predicts the second. Nobody expects 0.4 to mean "confused 40% of the time", only that the model's closest pairs are the ones listeners confuse most: a statistic that ignores scale and keeps order.

## Mechanism

A **confusion matrix** for 20 shapes has 20 rows (played) and 20 columns (answered); its off-diagonal cells are the confusions. Fold it across the diagonal: one count per pair, 190 pairs. The model side is a distance between class-mean latents for the same 190.

**Rank correlation** (Spearman's) replaces each list by positions, 1 for the closest pair and 1 for the most-confused pair, then correlates the positions. Three pairs:

| pair | model distance | position | confusions | position |
|---|---|---|---|---|
| rising–falling | 0.11 | 1 | 31 | 1 |
| ring–circle | 0.30 | 2 | 12 | 3 |
| plus–X | 0.45 | 3 | 19 | 2 |

Differences \(d = 0, 1, 1\); with \(n\) pairs:

\[ \rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)} = 1 - \frac{12}{24} = 0.5 \]

Why not the plain correlation? Confusion counts are skewed: one extreme pair would dominate. Positions ignore it and any monotone re-scaling, the freedom a model that never promised a scale deserves.

This week's confusions come from a synthetic listener: the sound map blurred to four pitch bands and eight time slices, noise added, answers by nearest class mean. A stand-in of the right shape, so the pipeline runs end to end; its number is not evidence about people.

The human study that replaces it is pairwise, not 20-way: about 20 pairs spread across the winning row's distances, two sounds per trial, "same or different". Each pair's d′, the separation of its two sounds in units of the listener's own noise, is its discriminability. Eight participants × 24 trials per pair is 192 trials per pair. Same \(\rho\), its interval from resampling participants, and the failure line written now: \(\rho\) below 0.4 means the row does not predict listeners. Write it for whichever row won; if that is the fixed sonifier distance, the honest outcome so far, the study needs no trained model.

Your field's **JND** is a threshold on one continuum, found by a staircase; these shapes are categories, so the per-pair number is d′, and rank correlation against a d′ table tests a model that gives no scale. Where it breaks: JNDs are threshold differences; confusions are errors well above threshold under time pressure.

**In practice**, in numpy:

```python
def positions(v):      # argsort twice: ties are broken
    return np.argsort(np.argsort(v)) + 1   # arbitrarily;
def rank_corr(u, v):   # the notebook averages ties
    return float(np.corrcoef(positions(u),
                             positions(v))[0, 1])
rho = rank_corr(dist_pairs, -confusions)
# 1 = closest pair vs 1 = most-confused pair
```

Week 9's bootstrap wraps it, with one change: the 190 pairs share shapes (each sits in 19 of them), so they are not exchangeable. Resample the 20 shapes, rebuild the pairs, recompute \(\rho\) for A and B on each resample, keep the difference; 1000 repeats give the 95% interval on A − B. It covers "which shapes", not the seeds, whose spread is reported beside it.

## Try it

<div class="visual"><iframe src="../visuals/w12-rank-correlation.html" title="Rank-correlation explorer: eight pairs, set the confusions, watch rho" loading="lazy"></iframe></div>

1. Set the sliders so \(\rho\) reads 1.00, then swap the counts of the top two pairs. Predict the drop first.
2. Push one pair's count to the maximum with the rest in order. How far does the plain correlation move, and how far does \(\rho\)?
3. Find a setting where \(\rho\) is near 0 but the three most-confused pairs still match the model's top three. What does that say about a study that only orders 20 pairs?

## Retrieval

??? question "Three pairs: model distance positions 1, 2, 3; confusion positions (1 = most confused) 1, 3, 2. Compute rho."
    \(d = 0, 1, 1\), so \(\sum d^2 = 2\) and \(\rho = 1 - 12/24 = 0.5\).

??? question "Why rho between latent distance and confusion counts, rather than the plain correlation of the raw values?"
    The model promises an ordering, not a scale, and counts are skewed; positions remove both the scale and the pull of one extreme pair.

??? question "The synthetic listener gives rho = 0.6 for the contrastive model. What does that number say about people?"
    Nothing. It shows the pipeline works and gives a number to pre-register against; only the pairwise study with participants is evidence about listeners.

## Sources

- [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient): definition and worked example, 8 min.
- [Kriegeskorte et al.: Representational similarity analysis](https://www.frontiersin.org/articles/10.3389/neuro.06.004.2008/full): figure 1 and the comparing-representations section, 10 min.
- [Nili et al.: A toolbox for representational similarity analysis](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003553): the bootstrap-over-conditions paragraph, 5 min.

## Ledger prompt

> Next to `build-step7`: the human-study prediction as one line with a number, the trials per pair behind each d′, and the confound a listener brings that the synthetic one does not.

**Next:** the one-page write-up: claim, setup, plot, surprise, decision, and the question for an ML collaborator.
