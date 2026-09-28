---
title: Lesson 2 · From paper to checklist
terms: [reproduction, tolerance]
card: core-tooling
---

# Lesson 2 · From paper to checklist

<p class="recall" markdown>**Previously:** a paper is read in three passes with one question each, and the recipe for a number is scattered across appendix tables, the repository, footnotes and cited papers.</p>

## Idea

A **reproduction** is the same number from the same recipe, and "same recipe" must be written down before the run, or the run decides what the recipe was. Five lines cover almost any table cell: data, preprocessing, model, metric, and the claimed number. The fifth needs a companion most reproductions skip: a **tolerance**, how far off you may land and still call it the same number. Without it, 89.8 versus 91.3 is an argument; with it, a verdict.

## Mechanism

The checklist for the CLIP cell:

| Line | For the CLIP cell | Found in |
|---|---|---|
| data | CIFAR-10 *test* split, 10,000 images, 10 classes | Table 9 |
| preprocessing | resize and centre-crop to 224, CLIP normalisation (the shipped `preprocess`); 18 prompt templates averaged | code, `data/prompts.md`, §3.1.4 |
| model | ViT-B/32, OpenAI's released weights | Table 11 row |
| metric | top-1 accuracy over the 10,000 images | Table 9 |
| number | 91.3 | Table 11 |

Preprocessing came from three places; it is where most gaps start.

Tolerance has two sources; take the larger. First, a finite test set: an accuracy \(p\) measured on \(n\) images has a standard error of

\[ \sqrt{\frac{p(1-p)}{n}} \]

For 91.3 % on 10,000 images that is 0.28 points, a band of ±0.6 at two standard errors; 89.8 is five standard errors away, a real gap. Second, seed spread, from week 10: if the number depends on random choices, the standard deviation across seeds is the band, and the paper's number is one draw from it. CLIP's zero-shot evaluation has no seed. The week-10 probe you will reproduce in the build's rehearsal has one: 71.1 % on 60 held-out images has a standard error of 5.9 points and its three seeds spread by 2.5, so the band is about ±12 and almost anything reproduces. That is not a comfort; it is the finding that the number was never precise.

**In practice**, week 9's notebook loaded `ViT-B-32` with `pretrained="laion2b_s34b_b79k"`: the same architecture, different weights, trained by a different group on different data. OpenCLIP's results table reports 93.6 % on CIFAR-10 for them and 89.8 % for `pretrained="openai"`. Both runs "work"; only one attempts Table 11, and the model line tells them apart before the download.

The analogy is a replication study: same protocol, then the effect lands inside or outside the original's confidence interval, temptations included. Where it breaks: a replication's noise comes from new participants, so a bigger sample tightens it; a reproduction's comes from a fixed test set and from seeds, and only more seeds tighten the second.

## Try it

<div class="visual"><iframe src="../visuals/w11-tolerance-calculator.html" title="Tolerance calculator: test-set size, seed spread, and whether your number is inside the band" loading="lazy"></iframe></div>

Before moving anything: 91.3 claimed on 10,000 images, your run 89.8. Inside or outside?

1. Enter that case, then shrink the test set to 500 images and watch the verdict flip.
2. Set 71.1 claimed on 60 images with a seed spread of 2.5; find the smallest gap the calculator calls real.
3. Give the CLIP case a seed spread of 2 points. What happens to the verdict?

## Retrieval

??? question "Write the five checklist lines for a table cell from memory, and say which one most often takes three sources to fill."
    Data (split, size), preprocessing (transforms, prompts, tokenization), model (architecture, which weights), metric (what is counted), and the claimed number. Preprocessing is assembled from paper, appendix and code.

??? question "A paper reports 84.0 % accuracy on 2,000 test images. Compute the standard error and say whether your 82.9 % reproduces it."
    \(\sqrt{0.84 \times 0.16 / 2000} = 0.0082\), so 0.8 points; two standard errors give ±1.6. 82.9 is 1.1 below: inside the band, so it reproduces.

??? question "Two runs give 93.6 and 89.8 for 'ViT-B/32 on CIFAR-10'. What checklist line explains the spread, and which run reproduces the paper's 91.3?"
    The model line: same architecture, different weights (LAION-trained versus OpenAI's). Neither lands within tolerance, but only the OpenAI-weights run is a reproduction attempt.

## Sources

- [Radford et al. 2021 (CLIP)](https://arxiv.org/abs/2103.00020): Table 9 (test sizes and metrics), Table 11 (the cell), and §3.1.4, 15 min.
- [OpenCLIP results table](https://raw.githubusercontent.com/mlfoundations/open_clip/main/docs/openclip_results.csv): the `ViT-B-32` rows, `openai` versus `laion2b_s34b_b79k`, 3 min.
- [Pineau et al. 2020](https://arxiv.org/abs/2003.12206): the reproducibility checklist in the appendix, 8 min.

## Ledger prompt

> Next to `core-tooling`: write the tolerance for the number you will reproduce, with its source (test-set size, seed spread, or both), before the build session.

**Next:** the repository: where the entry point is, what the config file overrides, and how data flows to the line that prints the number.
