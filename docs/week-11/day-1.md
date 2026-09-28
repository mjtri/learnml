---
title: Lesson 1 · Read a paper in three passes
terms: [three-pass reading]
card: lin-clip
---

# Lesson 1 · Read a paper in three passes

<p class="recall" markdown>**Previously:** one lever, a baseline that could embarrass you, one ablation, seeds chosen from the spread, all on a pre-registered page; the week-12 experiment is the cross-modal contrastive embedding (rendered shapes ↔ vOICe-style sound), with the learned image→touch codec as the alternative.</p>

## Idea

This week's deliverable is one number from a published table, produced again by you, with a written account of the gap. A paper read front to back gives you a story; read for reproduction it gives a recipe, and the recipe is scattered: the claim in a figure, the number in an appendix table, the preprocessing in a code repository, the split size in a footnote. **Three-pass reading** is the habit of reading with one question per pass, so the recipe is collected instead of stumbled on.

## Mechanism

Keshav's three passes, with reproduction as the question:

| Pass | Time | Read | You leave with |
|---|---|---|---|
| 1 | 10 min | title, abstract, headings, captions, conclusion | the claim, and which table holds *your* cell |
| 2 | 1 h | figures, tables, method, appendix headings; skip proofs | five checklist lines with a page each: data, preprocessing, model, metric, number |
| 3 | 3 h+ | appendix, footnotes, the repository, keyboard open | the recipe re-assembled and running |

Pass 1 answers "which cell?": a paper reports hundreds of numbers; you reproduce one. Pass 2 hunts the details and notes where each one was *not*: an empty line after pass 2 means the detail lives in the code, or nowhere. Pass 3 is the build session. Most papers deserve pass 1 only.

**In practice**, the CLIP paper (Radford et al. 2021) is 48 pages. The claim is Figure 5 on page 8. Your cell, 91.3 % zero-shot accuracy on CIFAR-10 with ViT-B/32, is Table 11 on page 43; the test-set size (10,000 images) and the metric (accuracy, not mean per class) are Table 9 on page 39; the 18 prompt templates averaged for CIFAR-10 are in no table: they sit in `data/prompts.md` in the repository. Section 3.1.4 says only that 80 templates gave +3.5 points on ImageNet. Five lines, four places, one outside the PDF.

Where details hide, most often first:

1. **Appendix tables.** The main text carries averages and plots; per-dataset numbers are appendix rows.
2. **The repository.** Preprocessing, prompt wording, the seed, the checkpoint; "standard augmentation" in the paper is a named function in the code.
3. **Footnotes and captions.** "Evaluated on the validation split"; "mean of three runs".
4. **A cited paper.** "We follow the protocol of X": one more pass 2, on X.

You already do pass 1 when reviewing for CHI: abstract, figures, contributions, decide. The difference is where the method lives: an HCI method section describes the study in full; an ML paper's method is the code, and the section summarises it. Where the analogy breaks: an HCI study cannot be re-run from its paper; a reproduction expects to be, and treats a missing detail as a finding.

## Try it

<div class="visual"><iframe src="../visuals/w11-paper-sections.html" title="Tap the sections of the CLIP paper: which pass reads them, which checklist line they fill" loading="lazy"></iframe></div>

Before tapping, guess how many of the five checklist lines the PDF completes without the repository.

1. Tap sections in the order you would read them; watch the pass and the minute count.
2. Find the line no PDF section completes. Where does the visual say it lives?
3. Tap only what a pass-1 reader sees. Which lines stay empty?

## Retrieval

??? question "After pass 2, your 'preprocessing' checklist line is still empty. What does that tell you, and where do you look next?"
    The paper does not state it; it lives in the repository (a transform, a prompt file, a config) or nowhere. Pass 3 opens the code; if absent there too, the gap becomes a line of your report.

??? question "The CLIP paper's headline figure says zero-shot CLIP matches a linear probe. Why is that not the number you reproduce, and what is?"
    A figure of averages across datasets cannot be checked to a tolerance. You reproduce one cell with a metric and a test set: Table 11, ViT-B/32, CIFAR-10, 91.3 %.

??? question "Name the four places, most likely first, where a reproduction detail hides outside the main text."
    Appendix tables, the code repository, footnotes and captions, and a cited paper whose protocol is 'followed'.

## Sources

- [Keshav: How to read a paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf): section 2, the three passes, 8 min.
- [Radford et al. 2021 (CLIP)](https://arxiv.org/abs/2103.00020): pass 1 of the PDF, then Table 9 (page 39) and Table 11 (page 43), 25 min.
- [CLIP repository: data/prompts.md](https://github.com/openai/CLIP/blob/main/data/prompts.md): the CIFAR-10 block, 3 min.

## Ledger prompt

> Next to `lin-clip`: name the checklist line you expect to be hardest to find for the CLIP cell and where you guess it is; correct the guess after pass 2.

**Next:** the five-line checklist, and the number that decides whether "close" counts: the tolerance.
