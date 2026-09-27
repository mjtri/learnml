---
title: B1 · Apply · Meters, one AGENTS.md, one measured comparison
playbook: budget
---

# B1 · Apply · Meters, one AGENTS.md, one measured comparison

<p class="recall" markdown>**This week in one sentence:** an agent is a loop over a finite context; two subscriptions are two rolling allowances with meters; where a task runs and who verifies it picks the tool.</p>

**Laptop · ~60 min · in the build session, before the Colab notebook.**

## Goal

Leave with (1) the `/usage` habit installed, (2) one AGENTS.md both tools read, and (3) three lines in the playbook that came from numbers, not opinions.

## Steps

1. **Baseline (3 min).** In Claude Code: `/usage`. In ChatGPT: open the usage counter. Write both numbers in a scratch note with the time.
2. **AGENTS.md (15 min).** This repo ships a starter `AGENTS.md` and a `CLAUDE.md` that imports it. Read both. Then, with the agent in plan mode, ask:
   ```
   Goal: tighten AGENTS.md for this repo. Context: read AGENTS.md, LOOP.md, LESSON_FORMAT.md.
   Constraints: under 80 lines, no duplication of LESSON_FORMAT.md, keep the commands section.
   Done when: a fresh session can run the four LOOP.md commands from AGENTS.md alone.
   ```
   Approve or edit the plan, let it run, then check the "done when" yourself.
3. **Same task, two tools (30 min).** Pick a small, self-contained task with an oracle, for example: "add a `--week` filter to `build_anki.py` so `python build_anki.py week-01 --week` prints only question cards; `check_lessons.py` and a manual run must pass." Run it once in Claude Code (local, plan mode) and once as a Codex cloud task or in the Codex CLI, from a clean `git stash` each time. For each, record: wall-clock minutes, usage delta (`/usage` before/after; ChatGPT counter before/after), and a 1–5 quality score after reading the diff. Keep the better diff, discard the other.
4. **Meters again (2 min).** `/usage` and the ChatGPT counter. Compare with step 1: that is the real cost of a build session's warm-up.

## Done when

- `AGENTS.md` is under 80 lines and `CLAUDE.md` starts with `@AGENTS.md`.
- The playbook's **Budget** section has three lines with numbers: the baseline pair, the comparison (minutes / usage / quality per tool), and the warm-up cost.
- `python check_lessons.py` still passes.

## Log it

```bash
python track.py done agentic-01/apply --rating 3 --minutes 60 --note "which tool won the comparison and by how much"
```

## Ledger prompt

> In **Budget**: the comparison line ("task X: Claude 14 min / 6 % / 4; Codex 11 min / 9 msgs / 3") and the one rule it suggests.
