---
title: B4 · Apply · Two commands per week, and the other vendor grades
playbook: delegation
---

# B4 · Apply · Two commands per week, and the other vendor grades

<p class="recall" markdown>**This week in one sentence:** delegate to subagents, skills and worktrees so the main window stays small, pay for each spawned window knowingly, and let a different agent, ideally a different vendor, grade the work.</p>

**Laptop · ~60 min · in the build session.**

## Goal

Leave with (1) `/gen-week` generating a week in an isolated worktree, (2) a `week-reviewer` subagent that grades without editing, and (3) one Codex adversarial review of a Claude-made week, with what it caught in the playbook.

## Steps

1. **Meters (3 min).** `/usage` and the ChatGPT counter, with the time. Then `git push`, so `main` is on the remote, or put `"worktree": {"baseRef": "head"}` in `.claude/settings.json`: worktrees branch from the remote default branch otherwise.
2. **The skill (10 min).** Create `.claude/skills/gen-week/SKILL.md`:
   ```markdown
   ---
   name: gen-week
   description: Generate one LearnML week in a worktree subagent, then run the checks
   argument-hint: "[agentic] <week>"
   disable-model-invocation: true
   ---
   Run `python gen_week.py $ARGUMENTS --agent --out .claude/gen-week-prompt.txt`.
   Spawn one general-purpose subagent with isolation set to worktree; its task is
   that file's full text plus: commit on your branch once every self-check is clean.
   When it reports, run `python check_lessons.py --only <week-dir>` here and show
   me its report, its branch name and its worktree path. Do not merge.
   ```
   `/reload-skills`, then `/gen-week agentic 2` (or any week whose ratings were low). Note wall-clock time.
3. **The reviewer (10 min).** Create `.claude/agents/week-reviewer.md`:
   ```markdown
   ---
   name: week-reviewer
   description: Grades a generated LearnML week; read-only, every finding with evidence
   tools: Read, Grep, Glob, Bash, WebFetch
   model: sonnet
   ---
   You are the grader, not the doer. Read LESSON_FORMAT.md, then every file in the
   week directory you are given. Run `python check_lessons.py --only <week-dir>`.
   Re-fetch each stamped source and quote the sentence that supports each claim,
   or say it does not. Report at most 15 findings as `file:line · blocks|nit ·
   evidence`. Never edit a file.
   ```
   Ask: `@week-reviewer grade the week at <worktree path>`. It starts with no memory of the generation, which is the point.
4. **The other vendor (25 min).** `/plugin marketplace add openai/codex-plugin-cc`, `/plugin install codex@openai-codex`, `/codex:setup`. Open a session in the worktree and run `/codex:adversarial-review --base main --wait product claims that overstate the cited page; lessons that break LESSON_FORMAT.md`. For comparison, run `/code-review medium` on the same branch. For each grader record: minutes, usage delta (`/usage` or the ChatGPT counter), a 1–5 quality score, and each finding tagged real or noise. Fix the real ones in the worktree, rerun the checker, merge.
5. **Meters (2 min).** `/usage` and the ChatGPT counter again: the cost of one generated and twice-graded week.

## Done when

- `/gen-week agentic N` yields a committed week on a `worktree-*` branch with the checker green, and `@week-reviewer` returns a findings list without touching a file.
- The Codex adversarial review caught at least one real issue, logged with both meters' deltas.
- `python check_lessons.py` passes on `main` after the merge.

## Log it

```bash
python track.py done agentic-04/apply --rating 3 --minutes 60 --note "what Codex caught that /code-review missed"
```

## Ledger prompt

> In **Delegation**: the comparison line ("week 2: /code-review medium 3 min / 4 % / 1 real; Codex adversarial 6 min / 5 msgs / 2 real") and the pipeline rule it supports.
