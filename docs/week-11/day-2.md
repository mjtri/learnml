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

Tolerance comes from wherever randomness enters, and in the CLIP cell it enters nowhere: fixed weights, the same 10,000 images, no seed. A faithful rerun matches to numerics, about 0.1 point from fp16 or GPU summation order; 89.8 against 91.3 is 150 images classified differently: a recipe gap. When the evaluation *is* seeded (a trained probe, a random split), the band is twice week 10's seed spread, and the paper's number is one draw: the week-10 probe's 71.1 % is a three-seed mean with spread 2.5, so ±5. The test-set standard error answers a third question, how precise the paper's *claim* is on new images:

\[ \sqrt{\frac{p(1-p)}{n}} \]

0.28 points for 91.3 % on 10,000 images, 5.9 for 71.1 % on 60. It says the probe's number was never precise; it does not excuse a gap on the same images.

**In practice**, week 9's notebook loaded `ViT-B-32` with `pretrained="laion2b_s34b_b79k"`: the same architecture, different weights, trained by a different group on different data. OpenCLIP's results table reports 93.6 % on CIFAR-10 for them and 89.8 % for `pretrained="openai"`. Both runs "work"; only one attempts Table 11, and the model line tells them apart before the download.

The analogy is a replication study: same protocol, then the effect lands inside or outside the original's confidence interval. Where it breaks: a replication's noise comes from new participants, so a bigger sample tightens it; a reproduction on the same images has no sampling noise, only seeds, and only more seeds tighten those.

## Try it

<div class="visual"><iframe src="../visuals/w11-tolerance-calculator.html" title="Tolerance calculator: test-set size, seed spread, and whether your number is inside the band" loading="lazy"></iframe></div>

Before moving anything: 91.3 claimed on 10,000 images, your run 89.8 on the same images. Inside or outside?

1. Tap **CLIP cell** and read the band. Then tap **a new sample of n images**, set n to 500: the verdict flips.
2. Tap **week-10 probe** (seed spread 2.5); find the smallest gap the calculator calls real.
3. Give the CLIP case a seed spread of 2 points. What happens to the verdict?

## Retrieval

??? question "Write the five checklist lines for a table cell from memory, and say which one most often takes three sources to fill."
    Data (split, size), preprocessing (transforms, prompts, tokenization), model (architecture, which weights), metric (what is counted), and the claimed number. Preprocessing is assembled from paper, appendix and code.

??? question "A paper reports 84.0 % on 2,000 test images; your run on the same 2,000 images gives 82.9 %. Compute the standard error and say whether it reproduces."
    \(\sqrt{0.84 \times 0.16 / 2000} = 0.0082\), so 0.8 points: the claim is precise to about ±1.6 on new images. On the same images, 1.1 points is 22 images classified differently: outside, a recipe gap, not noise.

??? question "Two runs give 93.6 and 89.8 for 'ViT-B/32 on CIFAR-10'. What checklist line explains the spread, and which run reproduces the paper's 91.3?"
    The model line: same architecture, different weights (LAION-trained versus OpenAI's). Neither lands within tolerance, but only the OpenAI-weights run is a reproduction attempt.

## Sources

- [Radford et al. 2021 (CLIP)](https://arxiv.org/abs/2103.00020): Table 9 (test sizes and metrics), Table 11 (the cell), and §3.1.4, 15 min.
- [OpenCLIP results table](https://raw.githubusercontent.com/mlfoundations/open_clip/main/docs/openclip_results.csv): the `ViT-B-32` rows, `openai` versus `laion2b_s34b_b79k`, 3 min.
- [Pineau et al. 2020](https://arxiv.org/abs/2003.12206): the reproducibility checklist in the appendix, 8 min.

## Ledger prompt

> Next to `core-tooling`: write the tolerance for the number you will reproduce, with its source (numerics or seed spread), before the build session.

**Next:** the repository: where the entry point is, what the config file overrides, and how data flows to the line that prints the number.
