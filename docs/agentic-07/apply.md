---
title: "B7 · Apply · The week-12 harness: one folder, one unit, unattended"
playbook: experiments
---

# B7 · Apply · The week-12 harness: one folder, one unit, unattended

<p class="recall" markdown>**This week in one sentence:** a long-running harness is a progress file, a CHANGELOG with failed approaches, one commit per unit and a check the agent runs before claiming progress; every number and figure comes from an analysis script over the run log; and seeds, configs and run-log rows are written by the code, never changed silently.</p>

**Laptop · ~60 min · in the build session, after `week10_plan.md` exists.**

## Goal

Leave with `experiments/week12/`, a harness an agent can run unattended for one unit, and a measured comparison of both tools doing it.

## Steps

1. **Meters (2 min).** `/usage` and the ChatGPT counter.
2. **Scaffold (15 min).** Claude Code, plan mode:
   ```text
   Goal: create experiments/week12/ with README.md, CHANGELOG.md, progress.md, config.json,
   check.py and an empty runs.jsonl, from the file contents in docs/agentic-07/apply.md and
   the prediction in week10_plan.md. Constraints: standard library only in check.py; nothing
   writes runs.jsonl except run.py (not yet written). Done when: python
   experiments/week12/check.py exits 1 and prints "no runs yet".
   ```
   The files. `README.md` states the falsifiable prediction and the layout:
   ```text
   # Week 12 · cross-modal contrastive embedding
   Prediction (week10_plan.md): on 16×16 shapes ↔ vOICe-style sound, the contrastive
   embedding beats the pixel-loss encoder (B strong) on rank_corr, the rank correlation
   between latent distance and the confusion ordering, by ≥ X (the plan's number) over
   5 seeds; pixel_distance is the trivial rung. Decision: the plan's line (kill under its
   kill line; pivot to the codec if the ablation costs nothing); the notebook adds a CI guard.
   Layout: config.json · run.py · check.py · runs.jsonl · progress.md · CHANGELOG.md · analysis/
   Never silently: change config or seed, drop rows, edit check.py, flip smoke, push.
   ```
   `CHANGELOG.md` has three headings: `## Units done`, `## Failed approaches (do not retry without a new reason)` with the line format `date · what · why · run_id`, and `## Known limitations`. `progress.md` has four lines: status, next unit, blocked on, and "start of session: read CHANGELOG.md, run check.py". `config.json`:
   ```json
   {"option": "contrastive", "data": "week10_data.npz", "seeds": [0, 1, 2, 3, 4],
    "smoke": true, "epochs": 20, "lr": 0.001, "metric": "rank_corr",
    "x": "copied from week10_plan.md", "baseline": "pixel_distance"}
   ```
   `check.py`, the oracle:
   ```python
   import json, sys
   from pathlib import Path
   rows = [json.loads(l) for l in Path(__file__).with_name("runs.jsonl").read_text().splitlines() if l.strip()]
   need = {"run_id", "git", "dirty", "config", "seed", "smoke", "metric", "value"}
   if not rows: sys.exit("FAIL: no runs yet")
   bad = [r.get("run_id") for r in rows if need - r.keys()]
   if bad: sys.exit(f"FAIL: rows missing fields: {bad}")
   dirty = [r["run_id"] for r in rows if r["dirty"]]
   if dirty: sys.exit(f"FAIL: runs from uncommitted code: {dirty}")
   full = {(r["config"], r["seed"]) for r in rows if not r["smoke"]}
   print(f"OK: {len(rows)} rows, {len(full)} full config/seed pairs")
   ```
3. **Oracle check (5 min).** Run `python experiments/week12/check.py`: FAIL. Paste the Lesson 3 row, on one line, into `runs.jsonl` (the week-12 notebook's Part D appends rows in this schema with `metric: "rank_corr"`): OK. Set its `dirty` to `true`: FAIL. Empty the file, commit `Scaffold week12 harness`.
4. **Unit 1, Claude Code (15 min).** Unattended, one line each:
   ```text
   claude update
   claude -p "Read experiments/week12/progress.md and CHANGELOG.md. Do the next unit: write run.py (pixel-distance baseline on week10_data.npz, metric rank_corr against the synthetic confusion table exactly as the week-12 notebook computes it, seeds from config.json, smoke first), append rows, run check.py, update progress.md and CHANGELOG.md, commit." --allowedTools "Read,Edit,Write,Bash(python *),Bash(git add *),Bash(git commit *)" --permission-prompts none
   ```
   `--permission-prompts none` needs Claude Code v2.1.259 or later, hence `claude update` first. Note minutes, `/usage` delta, and a 1–5 quality score after reading the diff.
5. **Unit 1, Codex (15 min).** `git checkout -b codex-unit1 <scaffold hash>` then the same prompt as a Codex cloud task or in the CLI. Note minutes, counter delta, quality. Read both diffs for silent changes: config, seeds, `check.py`, `smoke`.
6. **Keep one (5 min).** Merge the better branch; the loser goes under Failed approaches only if it wrote a wrong row.
7. **Meters (2 min).** `/usage` and the counter again.

## Done when

- `check.py` exits 1 on an empty log, 0 on a valid row, 1 on a `dirty: true` row.
- `runs.jsonl` holds 5 non-smoke `pixel_distance` rows and `git log` shows one commit per unit.
- The playbook's **Experiments** section has the comparison line.

## Log it

```bash
python track.py done agentic-07/apply --rating 3 --minutes 60 --note "which tool ran the unit clean and what it changed silently"
```

## Ledger prompt

> In **Experiments**: the comparison line ("unit 1: Claude 12 min / 7 % / 4, silent: none; Codex 15 min / 1 task / 3, silent: flipped smoke") and the rule it suggests.
