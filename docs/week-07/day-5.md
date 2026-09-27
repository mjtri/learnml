---
title: Lesson 5 · Reproducibility basics: seeds, configs, run logs
terms: [reproducibility, random seed, run log, git hash]
card: core-tooling
---

# Lesson 5 · Reproducibility basics: seeds, configs, run logs

<p class="recall" markdown>**Previously:** fine-tuning is the ordinary loop on a loaded checkpoint at a tiny learning rate, and it costs about sixteen bytes per parameter, which is why a T4 holds a 360M model but not a 1.7B one.</p>

## Idea

A result you cannot get twice is an anecdote. **Reproducibility** means someone else, or you in a month, gets the same number from the same code, data and settings. Three things drift between two "identical" runs: the random choices, the settings, and the code itself. Each has one pin: a **random seed**, a **config**, a **git hash**. The **run log** is the one row per run that carries all three next to the result. This is the habit that turns a notebook into an experiment.

## Mechanism

**Seed.** Every random choice in a run comes from a generator that starts from one integer: the probe's initial weights, the 80/20 split, the sampled tokens. Same `seed`, same sequence. `transformers.set_seed(0)` sets Python, NumPy and PyTorch at once. What a `seed` does not pin: the arithmetic. GPU kernels add numbers in whatever order is fastest, so two runs on different GPUs agree to a few decimals, not bit for bit; `torch.use_deterministic_algorithms(True)` buys exactness at a speed cost.

**Config.** One dictionary holding everything that changes behaviour: model id and revision, layer, pooling, split fraction, number of examples, learning rate, steps, `seed`. Print it at the start of the run, and never let a setting live only in a cell you edited by hand. It is the run's recipe, as `config.json` is the model's.

**Git hash.** `git rev-parse --short HEAD` prints the id of the code version, and `git status --porcelain` is empty only if nothing is uncommitted. The hash pins what the config cannot: every line of code, including the bug you have not found yet. A run made with uncommitted edits gets the suffix `-dirty`, a warning, not a crime.

**Run log.** Append one row per run to a CSV, never overwrite:

```python
row = dict(time=time.strftime("%Y-%m-%dT%H:%M:%S"),
           git=git_hash(), **cfg, acc=round(acc, 4),
           torch=torch.__version__,
           transformers=transformers.__version__)
with open("runs.csv", "a", newline="") as f:
    csv.DictWriter(f, fieldnames=list(row)).writerow(row)
```

Library versions belong in the row because a Transformers upgrade can change a default, and next month's "same" run will quietly differ. The build session writes this file.

**In practice**, the PyTorch reproducibility notes open with a sentence worth memorising: completely reproducible results are not guaranteed across PyTorch releases, individual commits, or different platforms. The habit that follows: run every reported number with three seeds and quote the spread, not the best one. A probe that scores 0.83, 0.79 and 0.85 is a 0.82 ± 0.03 result, and the ± is the part a reviewer asks about.

The honest analogy is your own methods section: randomisation order, software versions, exact stimulus files. A run log is a methods section written by the code at the moment it ran. Where it breaks: a methods section records what you intended; the log records what actually executed, including the flag you forgot to change back.

## Try it

<div class="visual"><iframe src="../visuals/w07-run-log-builder.html" title="Tap the fields a run log needs; see the row and what a stranger could still not repeat" loading="lazy"></iframe></div>

Predict first, then tap:

1. Before tapping anything, name the three fields you think are worth the most repeatability points, then tap them and read the score.
2. Remove **git hash** only. What in the row still looks complete, and what can no longer be repeated?
3. Build the row for the build session's probe.

## Retrieval

??? question "Same seed, same code, same data, a different GPU: how closely should the two accuracies agree, and what causes the difference?"
    Closely, but not bit for bit. The seed pins the random choices, not the arithmetic; GPU kernels sum in different orders, so the last decimals can differ.

??? question "A colleague sends 'acc = 0.83, seed 1'. Name four more fields you need before you can repeat the run."
    Any four of: model id and revision, layer and pooling, split fraction and example count, learning rate and steps, the git hash, library versions.

??? question "What does the git hash pin that the config does not?"
    The code itself, every line of it, including behaviour no config setting describes and bugs nobody has noticed. The config pins only the settings the code reads.

## Sources

- [PyTorch: Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html): the opening and "Controlling sources of randomness", 6 min.
- [Pineau: The Machine Learning Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf): one page, 4 min.
- [Transformers docs: set_seed](https://huggingface.co/docs/transformers/internal/trainer_utils#transformers.set_seed): the one entry, 1 min.

## Ledger prompt

> Next to `core-tooling`: for the last study you ran, which of seed, config and code version could you produce right now for the analysis behind the headline figure? Write the missing one and where it should have been logged.

**Next:** the build session: load a small model, probe its hidden states layer by layer, and log every run with config, seed and git hash.
