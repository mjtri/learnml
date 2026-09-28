---
title: Lesson 5 · The one-paragraph reproduction report
terms: [reproduction report]
card: lin-clip
---

# Lesson 5 · The one-paragraph reproduction report

<p class="recall" markdown>**Previously:** a debugging order walks the checks cheapest and likeliest first, metric, data, preprocessing, model, seeds, versions, hardware, and each ruled-out step becomes a line in the report.</p>

## Idea

The run is over and a number is on the screen. By itself it is worth nothing: next month you will not remember which weights it used, and nobody else can tell whether 89.8 was a failure or a success. A **reproduction report** is one paragraph, six sentences in a fixed order, that carries the number, its recipe, its verdict and the honest remainder. Committed next to the config and the seed, it is the `core-tooling` criterion: your own run, logged, comparable.

## Mechanism

The six sentences, in order, each answering one question:

| # | Sentence | Answers |
|---|---|---|
| 1 | **Target.** paper, table, cell, claimed number | what was reproduced |
| 2 | **Setup.** weights, data and size, preprocessing, code hash, library versions, hardware, seed | the five checklist lines, as run |
| 3 | **Result.** your number, and the tolerance with its source | what happened |
| 4 | **Verdict.** inside or outside the band, by how much | the one-word answer |
| 5 | **Explanation.** what was ruled out, what moved the number, by how much | the debugging order's output |
| 6 | **Residue.** what remains unexplained and what the next check costs | where to start next time |

Sentences 1 to 4 are facts; a reader who stops there knows the result. Sentence 5 is the only one with judgement in it, and it must quote measured moves, not guesses: "single template instead of 18 costs 1.2 points (measured)" is a sentence; "prompts probably matter" is not. Sentence 6 is the one people leave out and the one that makes the report reusable: an unexplained residue *stated* is a result; an unexplained residue *hidden* is a claim.

**In practice**, the paragraph for the CLIP cell, with the numbers the build session prints in the gaps:

```
Target: Radford et al. 2021, Table 11, ViT-B/32,
zero-shot CIFAR-10, 91.3. Setup: open_clip <ver>,
pretrained=openai, 10,000 test images, shipped
preprocess, 18 templates averaged, T4 fp32, commit
<hash>, no seed (deterministic). Result: <acc>,
tolerance +-0.1 (same images, numerics only; the
claim's test-set SE is 0.28). Verdict: <in/out>
by <gap>. Explanation: 1 template instead of 18
moves it <d1>; laion2b weights instead of openai
move it <d2> (ruled out as the cause). Residue:
<r> points unexplained; next check: resize method,
10 min.
```

The same paragraph for week 10's probe fits in four lines, and its explanation sentence is "seeds 0–9 give (the build's mean ± spread); the claimed 71.1 was the mean of three draws".

Where it goes: `week11_report.md` beside `week10_plan.md`, plus one row in `week11_runs.jsonl`, week 7's run log, with the same commit hash. The report says what the number means; the run log says how to get it again.

A registered report's results section is the analogy: the plan was fixed, so the results are written against it, and "did not replicate" is publishable because the protocol was. It holds through sentence 4 and breaks at sentence 5: a replication rarely gets to explain its gap by re-running with one thing changed; you can, for a few minutes each, so your explanation sentence is expected to contain measurements.

## Try it

<div class="visual"><iframe src="../visuals/w11-report-template.html" title="Report template: fill six fields, get a verdict and the paragraph to commit" loading="lazy"></iframe></div>

Before filling: guess which of the six fields the template will refuse most often.

1. Fill the CLIP case with 89.8 against 91.3 on 10,000 images. Read the verdict the template computes and the paragraph it prints.
2. Leave the residue field empty and tap **check**. What does it say?
3. Tap **week-10 case** (a ten-seed rerun with a wider spread). Does the explanation sentence change the verdict?

## Retrieval

??? question "List the six sentences of a reproduction report in order, and say which one must contain a measured number rather than a guess."
    Target, setup, result, verdict, explanation, residue. The explanation must quote how much each change moved the number, from a run; a guess belongs in the residue sentence as the next check.

??? question "What is the difference between the reproduction report and the run-log row, and why keep both?"
    The report interprets: verdict, explanation, residue. The run-log row is the recipe: commit hash, config, seed, versions, result. The row lets you rerun; the report tells you whether to.

??? question "Your reproduction is 1.5 points outside tolerance and you have no explanation. Write the residue sentence."
    'Residue: 1.5 points unexplained after ruling out data, metric and weights; next check is the preprocessing transform (resize and interpolation), about 10 minutes.'

## Sources

- [ReScience C](https://rescience.github.io/): the front page: a journal for explicit replications, and what it asks for, 5 min.
- [Pineau et al. 2020](https://arxiv.org/abs/2003.12206): section 4, the reproducibility checklist and what reports omit, 8 min.
- [Dodge et al. 2019: Show your work](https://arxiv.org/abs/1909.03004): section 5, the reporting checklist, 5 min.

## Ledger prompt

> Next to `lin-clip`: write sentences 1 and 2 of your report now, before the build session; only sentences 3–6 may be written after the run.

**Next:** the build session: the checklist filled from the paper, the number reproduced (rehearsal on CPU, then CLIP on the T4), the debugging order run, the report committed.
