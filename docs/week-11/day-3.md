---
title: Lesson 3 · Reading someone else's repo
terms: [entry point, config file, data flow]
card: core-tooling
---

# Lesson 3 · Reading someone else's repo

<p class="recall" markdown>**Previously:** five checklist lines (data, preprocessing, model, metric, number) plus a tolerance from test-set size or seed spread turn "close" into a verdict.</p>

## Idea

A research repository is read the way the paper was: in passes, with a question. The question is "which line prints the number?" and the route to it always has the same four stations: the **entry point** (the script the README tells you to run), the **config file** (the settings that script reads), the **data flow** (how examples travel from disk to metric), and the metric line itself. Read those four and you can change one thing at a time; read the whole repo and you learn its author's habits.

## Mechanism

The order:

1. **README first, for the command.** `python train.py config/train_shakespeare_char.py` names the entry point and the config; both are checklist evidence.
2. **Entry point, top to bottom, once.** Usually under 300 lines: defaults, config, data, model, loop, evaluation, print. Note line numbers.
3. **Config file, against your checklist.** Every setting either matches a checklist line or is a detail the paper never mentioned. The second kind is where gaps hide: `dropout = 0.2`, `eval_iters = 200`, `dtype = 'bfloat16'`.
4. **Data flow, backwards from the metric.** Find the line that computes accuracy or loss; ask where its inputs came from; repeat until you reach a file on disk. Every function on that path is preprocessing, whatever it is called.

**In practice**, nanoGPT (week 5) is the cleanest example. Entry point `train.py`; the config `config/train_shakespeare_char.py` is a Python file whose assignments overwrite `train.py`'s globals through `configurator.py`, so `max_iters = 5000` there replaces the default of 600,000. The data flow: `data/shakespeare_char/prepare.py` writes `train.bin` and `val.bin`; `get_batch()` reads random windows; `model(X, Y)` returns logits and loss; `estimate_loss()` averages `eval_iters` batches and prints `val loss`. The README's number for this config, 1.4697, is that printed value at the best step. Three files, one chain, fifteen minutes. OpenCLIP's zero-shot path is shorter and stranger: `create_model_and_transforms()` returns the model *and* the preprocessing transform, and the class-name templates are supplied by you, from another repository. Whatever you pass there is the preprocessing line.

The Unity analogy is honest: opening someone's project you find the entry scene, the `ScriptableObject` holding the tunables, and the `Update()` chain from input to screen, and read nothing else. It breaks in one place: the inspector shows config values live; a Python config shows only what is *written*, and the defaults it never mentions are in the entry point.

```bash
grep -rn "accuracy\|val loss" --include="*.py" .
git log -1 --format="%h %ad" --date=short
```

The first finds the metric line; the second records the code version, for the report.

## Try it

<div class="visual"><iframe src="../visuals/w11-repo-map.html" title="Repo map: entry point, config, data, model, metric for three repositories" loading="lazy"></iframe></div>

Before tapping, guess which of the three repositories keeps its preprocessing furthest from its entry point.

1. Walk nanoGPT from entry point to metric; count the files on the path.
2. Switch to the OpenCLIP zero-shot path. Which station holds the prompt templates, and is it a file at all?
3. Open the week-10 notebook's map. Which cell prints the rehearsal number, and which cell is its config?

## Retrieval

??? question "You have the README's command. Name the four stations you read next, in order, and the question each answers."
    Entry point (what runs, in what order), config file (which settings the paper never mentioned), data flow backwards from the metric (what counts as preprocessing), and the metric line (what exactly is counted).

??? question "A config file sets dropout = 0.2 and the paper never mentions dropout. What do you do with a config setting the paper never mentions?"
    Treat it as a checklist line: an unstated setting the run depends on. Copy it into your model line with the file name, and treat any change to it as a candidate gap explanation.

??? question "In nanoGPT, why does max_iters = 5000 in a config file change the run, when train.py sets max_iters = 600000?"
    The config file is executed after the defaults and its assignments overwrite the globals, so the last assignment wins.

## Sources

- [nanoGPT README](https://github.com/karpathy/nanoGPT): the "quick start" block and the reported validation loss, 8 min.
- [nanoGPT train.py](https://github.com/karpathy/nanoGPT/blob/master/train.py): the first 100 lines: defaults, then the `configurator.py` line, 10 min.
- [OpenCLIP README](https://github.com/mlfoundations/open_clip): the usage snippet with `create_model_and_transforms` and `get_tokenizer`, 5 min.

## Ledger prompt

> Next to `core-tooling`: for the repository you will reproduce from, write the four stations as file:line, and mark the one setting that appears in the config but not in the paper.

**Next:** the number comes out wrong; the order in which to suspect things, cheapest and likeliest first.
