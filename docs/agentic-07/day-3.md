---
title: "B7 · Lesson 3 · Reproducibility: seeds, configs, run logs, and what the agent must never do silently"
terms: [seed/config discipline]
playbook: experiments
---

# B7 · Lesson 3 · Reproducibility: seeds, configs, run logs, and what the agent must never do silently

<p class="recall" markdown>**Previously:** every number comes from an analysis script over the run log, every figure from one command, and the other vendor recomputes one table.</p>

## Idea

An agent will make a run work; reproducibility means it works the same way next month. **Seed/config discipline** is the habit: one config file per run, every random seed set from it, one run log row written by the code with the git hash. The second half matters more: what an agent may do only out loud, never silently.

## How it works

**The convention.** `config.json` holds every knob, `smoke` included. `run.py --config config.json --seed 3` sets the numpy and torch seeds, prints the git hash and whether the tree is dirty, and appends one row to `runs.jsonl`; nothing else writes that file. Versions are pinned in `requirements.txt` and recorded in the row. A dirty-tree run cannot be repeated, and `check.py` rejects it.

```json
{"run_id": "0007", "git": "3f2a9c1", "dirty": false, "config": "config.json",
 "seed": 3, "smoke": false, "metric": "rank_corr", "value": 0.52,
 "minutes": 0.4, "versions": {"torch": "2.8.0", "numpy": "2.3.2"}}
```

**Never silently.** Change a seed or a config value. Drop or filter rows. Edit or delete a test or `check.py`: the harness post calls that "unacceptable" ([effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents){ .src data-checked="2026-09-28" }). Flip `smoke` or shorten a run. Claim a pass without running the check. Retry an approach under Failed approaches. Change a library version. Rewrite CHANGELOG history. Push or merge. Each is allowed with a CHANGELOG line: why, and the run id that shows it.

**Enforce, don't request.** An AGENTS.md instruction is advisory; a hook is deterministic. A PreToolUse hook exiting with code 2 blocks the tool call; a Stop hook exiting 2 keeps the agent working, up to a cap on consecutive blocks; both live in `.claude/settings.json` ([hooks](https://code.claude.com/docs/en/hooks){ .src data-checked="2026-09-28" }). Unattended, `claude -p` with `--allowedTools` scopes the commands and `--permission-prompts none` (v2.1.259 or later) denies anything that would have waited for you ([programmatic runs](https://code.claude.com/docs/en/headless){ .src data-checked="2026-09-28" }). Codex: do-not rules go in AGENTS.md ([Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-28" }); a cloud task returns a diff to read before merging ([Codex cloud](https://learn.chatgpt.com/docs/cloud){ .src data-checked="2026-09-28" }).

**In practice.** Week 10's `SMOKE` flag becomes `smoke` in `config.json`: a smoke row proves the code runs, never the prediction. An agent that flips it to finish faster makes rows `check.py` counts as evidence. The flip is fine; the silence is not.

## Try it

<div class="visual"><iframe src="../visuals/b7-never-silently.html" title="Nine things an agent must never do silently: tap each to record what guards it" loading="lazy"></iframe></div>

Predict how many of the nine your setup catches deterministically, then set each item to the guard you actually have.

**Phone:** list three things an agent changed in a run without telling you; which of the nine were they?
**Laptop:** ask Claude Code for a PreToolUse hook in `.claude/settings.json` that blocks Edit and Write on `experiments/week12/check.py`, then ask it to change that file; you will see the block message instead of an edit.

## Rules of thumb

- Set every seed from the config and write the run log row from the code, never by hand.
- Turn any "never" that has bitten you into a hook; the rest stay one line in AGENTS.md.
- Run unattended only with scoped `--allowedTools` and prompts off, so a stuck run fails loudly.

## Retrieval

??? question "A run log row says dirty: true; what does it mean?"
    The code was never committed, so nobody can check out that version; the row is evidence of nothing and check.py rejects it.

??? question "Instruction or hook: which stops an agent from editing check.py, and why?"
    A hook: it runs every time and exit code 2 blocks the call; an instruction is just another line of context.

??? question "Name four things an agent must never do silently."
    Any four of: change a seed or config, drop rows, edit a check, flip smoke, claim a pass unchecked, retry a logged failure, change a version, push.

## Sources

- [Hooks reference](https://code.claude.com/docs/en/hooks){ .src data-checked="2026-09-28" }
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless){ .src data-checked="2026-09-28" }
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents){ .src data-checked="2026-09-28" }
- [Codex cloud](https://learn.chatgpt.com/docs/cloud){ .src data-checked="2026-09-28" }

## Ledger prompt

> In **Experiments**: your never-silently list and which items are hooks.

**Next:** scaffold the week-12 folder so an agent runs one unit unattended, in both tools, measured.
