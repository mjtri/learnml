---
title: "B7 · Lesson 2 · Analysis with an agent: scripts, plots, stats you can defend"
terms: [analysis script, reproducible plot]
playbook: experiments
---

# B7 · Lesson 2 · Analysis with an agent: scripts, plots, stats you can defend

<p class="recall" markdown>**Previously:** a long-running harness is a progress file, a CHANGELOG with failed approaches, a commit per unit, and an oracle run before any claim of progress.</p>

## Idea

An agent produces a plot and an interval in one turn; a reviewer asks where the number came from, and "a chat" is not an answer. The habit: every number in a paper or TM report is printed by an **analysis script** that reads the run log, and every figure is a **reproducible plot** one command regenerates. The chat is the draft; the script is the record.

## How it works

**Script, not chat.** The agent writes `analysis/effect.py`; it does not compute the effect. The script reads `runs.jsonl`, never edits it, prints a table and writes the figure. Ask for evidence: have Claude show "the test output, the command it ran and what it returned" ([best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-28" }). Codex's loop is the same: run the checks, confirm the result, review before you accept ([Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-28" }).

**Stats you can defend.** Three things a reviewer checks, so put them in the prompt: how many random seeds each mean rests on (Track A week 10); an interval, not a bare mean (the resampled interval of Track A week 9, its seed fixed); one dot per seed on the plot. The script prints its assumptions beside the statistic: "n=5 seeds, 2000 resamples". What it cannot print, you cannot defend.

**Second computation.** The script's author is the wrong judge of it; asked to grade its own work, a model tends to praise it ([harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps){ .src data-checked="2026-09-28" }). Give the same `runs.jsonl` and a one-line spec to the other vendor as a Codex cloud task: "print the same table independently". Disagreement is a finding.

**Plots.** A reproducible plot has a script, a named input file, and the git hash in the filename (`effect_3f2a9c1.png`) or caption. Any hand step goes into the script and the CHANGELOG.

**In practice.** Week 10 Part D printed mean ± sd over seeds in a notebook cell; for week 12 it becomes `analysis/seeds.py` over `runs.jsonl`, so the TM report and the paper share one command.

## Try it

### Worked example

```text
Goal: write analysis/effect.py. It reads experiments/week12/runs.jsonl, keeps rows
with smoke=false, and prints per config: n seeds, mean, sd and a 95 % resampled
interval of "value" (2000 resamples, numpy seed 0). It saves fig/effect_<git>.png:
one dot per seed, a bar at the mean. Constraints: numpy and matplotlib only; never
drop or edit rows; fewer than 3 seeds prints "too few seeds" instead of an interval.
Done when: python analysis/effect.py runs from the repo root and its printed table
matches the numbers you quote in your reply.
```

```text
config            n  mean   sd     95 % interval
pixel_distance    5  0.52   0.02   [0.50, 0.54]
contrastive       2  0.71   0.04   too few seeds
wrote fig/effect_3f2a9c1.png   (numpy 2.3.2, matplotlib 3.10.6)
```

The "too few seeds" line is the point: the script refuses to defend a number it cannot.

**Phone:** paste last week's Part D table into ChatGPT: "Which of these claims would a reviewer challenge, and what single extra run settles it?"
**Laptop:** write six fake rows into a scratch `runs.jsonl` (two configs, three seeds), give Claude Code the prompt above, then check one mean by hand; you will see whether the quoted number matches the printed one.

## Rules of thumb

- Ask for a script that prints the number, never for the number, when it will appear in a document.
- Print the seed count and resample count in the table, so the assumption travels with the statistic.
- Have the other vendor recompute one table before a figure goes into a document.

## Retrieval

??? question "Why is 'the agent computed it in the chat' not a source for a table?"
    Nobody can regenerate it, including you; a script over the run log is re-runnable, diffable and reviewable.

??? question "What three things does a defensible statistic carry with it?"
    The seed count behind each mean, an interval with its resample count and fixed seed, and the per-seed points on the plot.

??? question "What makes a plot reproducible?"
    One command regenerates it from a named input file, with the git hash in the filename or caption. Any hand step breaks it.

## Sources

- [Claude Code best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-28" }
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-28" }
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps){ .src data-checked="2026-09-28" }

## Ledger prompt

> In **Experiments**: the naming rule (`analysis/<question>.py` prints, `fig/<question>_<git>.png` is written) and which vendor recomputes.

**Next:** one config, one seed per run, one run-log row written by the code, and what an agent must never do silently.
