---
title: B2 · Apply · An instruction file the Unity project can build from
playbook: instructions
---

# B2 · Apply · An instruction file the Unity project can build from

<p class="recall" markdown>**This week in one sentence:** one short instruction file that both tools read, a plan before any edit, a four-part prompt, and memory kept for preferences rather than rules.</p>

**Laptop · ~60 min · in the build session, before the Colab notebook.**

## Goal

A fresh session in either tool can build and test the Unity project from the instruction file alone, and one of your own prompts has a measured before/after.

## Steps

1. **Draft (15 min).** In the Unity repo, Claude Code in plan mode:
   ```
   Goal: write AGENTS.md for this project.
   Context: the folder tree, ProjectSettings/ProjectVersion.txt, the test assemblies.
   Constraints: under 60 lines; sections Commands, Folder map, Conventions, Never touch;
   nothing the code already says.
   Done when: a fresh session can run the EditMode tests from this file alone.
   ```
   Approve or edit the plan. Add a `CLAUDE.md` whose first line is `@AGENTS.md`. The test command follows Unity's own form ([test framework CLI](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/reference-command-line.html){ .src data-checked="2026-09-27" }):
   ```
   Unity.exe -runTests -batchmode -projectPath . -testPlatform EditMode -testResults results.xml
   ```
2. **Prove it, twice (20 min).** New session, Claude Code: "Using only the instruction file, run the EditMode tests. Report the command and the result." Then the Codex CLI in the same repo, same prompt. Record for each: minutes, usage delta (`/usage` before/after, or the ChatGPT counter), and 1–5 for how much help it needed. If a tool asked you for the command, the file failed its done-when: fix the file, not the prompt.
3. **One prompt, two shapes (20 min).** Take the vague prompt from Lesson 2's phone task. Run it as written in one tool, then its four-part version in the same tool, in plan mode, from the same commit both times (`git stash` between runs). Record minutes, usage delta, a 1–5 quality score after reading the diff, and how many corrections you typed.
4. **Prune (5 min).** `/memory` in Claude Code: delete stale lines; move any rule that must always apply into `AGENTS.md`.

## Done when

- Both tools ran the EditMode tests from the instruction file alone.
- `AGENTS.md` is under 60 lines and `CLAUDE.md` starts with `@AGENTS.md`.
- The playbook's **Instructions** section has three lines with numbers: the two build runs, the prompt comparison, and the prune (lines moved in / out).

## Log it

```bash
python track.py done agentic-02/apply --rating 3 --minutes 60 --note "which tool built from the file alone; vague vs four-part delta"
```

## Ledger prompt

> In **Instructions**: the comparison line ("vague: 18 min / 7 % / 2 corrections; four-part: 9 min / 4 % / 0") and the plan-mode rule it supports.
