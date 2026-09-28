---
title: Lesson 4 · When the number does not match
terms: [debugging order]
card: core-tooling
---

# Lesson 4 · When the number does not match

<p class="recall" markdown>**Previously:** read a repository through four stations, entry point, config file, data flow, metric line, and copy every unstated setting into the checklist.</p>

## Idea

Your number is 89.8, the paper's 91.3. The reflex is to change the thing you understand least, usually the model, until something lands near 91.3, at which point you have tuned to a target, not reproduced anything. A **debugging order** replaces the reflex: a fixed sequence of checks, cheapest and likeliest first, each with a symptom that says whether to stop.

## Mechanism

The gap's *size* names the first suspect:

| Gap | First suspect |
|---|---|
| near chance (10 % on 10 classes) | labels, class order, the metric reading the wrong thing |
| tens of points | wrong split, wrong weights, eval mode off |
| a few points | preprocessing: transforms, prompts, tokenization; or weights from another source |
| a fraction of a point | seeds, library versions, fp16 versus fp32, GPU numerics |

The order, at most one cheap run per step:

1. **Same metric?** Percentage versus fraction, top-1 versus mean per class, test versus validation split. Zero runs.
2. **Same data?** Count the examples and classes; print five labels next to five images.
3. **Same preprocessing?** One example printed after every transform: size, value range, the exact prompt strings.
4. **Same model?** Weight source and version, `model.eval()`, dtype.
5. **Same randomness?** Three seeds; if the paper's number sits inside your spread, stop: the gap was one draw.
6. **Same code and libraries?** Git hash of the repo, versions of the libraries on the data path.
7. **Same hardware numerics?** GPU versus CPU, mixed precision. A few tenths at most; check last.

A step that changes nothing is a report line ("ruled out: data, 10,000 test images confirmed"); a step that moves the number is a candidate explanation, recorded with how much.

**In practice**, the swap from week 9's `laion2b_s34b_b79k` weights to `openai` is step 4 and moves CIFAR-10 by about four points: 93.6 is *not* a reproduction of 91.3, it is a better model. In the rehearsal, week 10's probe reported 71.1 % as the mean of seeds 0, 1, 2; seeds 0 to 9 give 66 % with a spread of 8. Step 5 explains the gap and re-describes the claim: three draws from a wide distribution, and the honest number is the ten-seed one.

The analogy to a failed replication holds: you check the dependent-variable coding before the sample, the sample before the apparatus, because cheap checks are also frequent culprits. It breaks on cost: a replication cannot re-run for free, so its order is fixed by plausibility alone; yours weights each step by run time too, which pushes seeds before versions before hardware.

```python
print(len(ds), ds[0][0].shape, ds[0][0].min(), ds[0][0].max())
print(ds.classes[:3], model.training, next(model.parameters()).dtype)
```

Steps 2 to 4 in two lines, before any re-run.

## Try it

<div class="visual"><iframe src="../visuals/w11-debug-order.html" title="Debugging order: enter the gap, walk the checks in order, see what each rules out" loading="lazy"></iframe></div>

Before tapping: your run gives 47.0 % where the paper says 91.3 %. Which step do you expect to stop at?

1. Enter that gap and walk the steps in order; note where the visual says "likely here".
2. Enter 89.8 against 91.3 with no seed spread. Which steps remain, and what do they cost?
3. Enter 66 against 71.1 with a seed spread of 8. What does the verdict say about the paper's number?

## Retrieval

??? question "Your reproduction lands at 10.2 % on a 10-class task. Which step of the order do you go to, and what single print statement do you run?"
    Near chance means the labels or the metric are misaligned: step 1 or 2. Print five predicted labels next to five true labels and check the class order.

??? question "Why does the debugging order put preprocessing before model weights, when weights feel more important?"
    Preprocessing checks cost one print and explain most few-point gaps; a weight mismatch is rarer and its check (downloading another checkpoint) costs more.

??? question "A gap of 0.3 points remains after steps 1–5 confirm everything. Do you keep going, and what do you write?"
    Only if the tolerance says 0.3 is real. Otherwise write 'residue 0.3, within tolerance, not pursued'; if outside, steps 6 and 7 cost one run each.

## Sources

- [Karpathy: A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/): sections 1–2, "become one with the data" and "overfit one batch", 12 min.
- [Bouthillier et al. 2021: Accounting for variance in machine learning benchmarks](https://arxiv.org/abs/2103.03098): abstract and Figure 1, where the variance comes from, 8 min.
- [OpenCLIP results table](https://raw.githubusercontent.com/mlfoundations/open_clip/main/docs/openclip_results.csv): compare the two `ViT-B-32` rows, 2 min.

## Ledger prompt

> Next to `core-tooling`: write your own debugging order for the target you chose, seven lines, with the cost of each step in minutes; the build session will test it.

**Next:** turning the run, the verdict and the ruled-out list into one paragraph someone else can act on.
