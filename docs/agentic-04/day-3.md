---
title: "B4 · Lesson 3 · Doer ≠ grader: /code-review, ultrareview, adversarial review"
terms: [doer/grader, adversarial review, ultrareview, codex-plugin-cc]
playbook: delegation
---

# B4 · Lesson 3 · Doer ≠ grader: /code-review, ultrareview, adversarial review

<p class="recall" markdown>**Previously:** worktrees give each parallel agent its own files; background sessions and teams each pay a full context window.</p>

## Idea

An agent grading its own work keeps the blind spots it had while doing it: same context, assumptions and prompt. The **doer/grader** split fixes the mechanism, not the model: the grader starts from a fresh context and, better still, is another vendor's model. The oracle catches what a test can express; a grader catches what only a reader notices.

## How it works

**`/code-review` (Claude, local).** Reviews your branch's commits ahead of upstream plus uncommitted changes. It runs as a background subagent with its own context, so the grader never inherits the doer's conversation ([code review](https://code.claude.com/docs/en/code-review){ .src data-checked="2026-09-27" }). `low` and `medium` effort report only confident findings; `high` to `max` widen coverage and admit doubtful ones. `--fix` applies findings. It reads `CLAUDE.md`, not `REVIEW.md`, and counts as normal plan usage. GitHub-side automatic review is Team and Enterprise only.

**Ultrareview (Claude, cloud).** `/code-review ultra` runs a fleet of reviewers in a cloud sandbox and reproduces every finding before reporting it ([ultrareview](https://code.claude.com/docs/en/ultrareview){ .src data-checked="2026-09-27" }). 5 to 10 minutes; up to 500 files and 8,000 changed lines; Max includes three free runs, once, then $5 to $25 in usage credits per run, estimated before you confirm. A run you stop still counts; it never starts on its own.

**Codex as the grader.** **codex-plugin-cc** is OpenAI's plugin for Claude Code: `/plugin marketplace add openai/codex-plugin-cc`, `/plugin install codex@openai-codex`, `/codex:setup`. It needs Node 18.18+ and your ChatGPT sign-in; "usage will contribute to your Codex usage limits", so the grader spends the other pool ([codex-plugin-cc](https://github.com/openai/codex-plugin-cc){ .src data-checked="2026-09-28" }). `/codex:review --base main` is a read-only review. `/codex:adversarial-review` is an **adversarial review**: it argues against the chosen design, takes focus text, and does not fix code. Inside Codex, `/review` offers the same presets without touching the tree ([Codex code review](https://learn.chatgpt.com/docs/code-review.md){ .src data-checked="2026-09-27" }). OpenAI publishes no per-review number.

**In practice.** Reply to reviewers due: Claude drafts it from the manuscript and the reviews; a ChatGPT session given only the reviewers' comments and the draft lists every point the draft dodges. It knows nothing about why you dodged them, which is the point.

## Try it

<div class="visual"><iframe src="../visuals/b4-reviewer-pipeline.html" title="Build a review pipeline and read its time, cost and independence" loading="lazy"></iframe></div>

Predict first: for a one-file docs change, which two stages give an independent grader for the least usage? Then build one for a twelve-file Unity refactor.

**Phone:** paste a paragraph you wrote with Claude into the ChatGPT app and ask for its three weakest claims. Is any real?
**Laptop:** on a branch with a diff, run `/code-review medium` and then `/codex:review --base main --wait`; you will see two lists, and the overlap tells you what the second vendor adds.

## Rules of thumb

- Never let the session that made a change grade it: at least `/code-review`, at best the other vendor.
- Use `low` or `medium` effort for routine diffs; save `ultra` for changes you would be embarrassed to ship wrong.
- Log what each grader caught; drop a grader with zero real catches in five runs.

## Retrieval

??? question "Why is `/code-review` in the same terminal still a different grader from the doer?"
    It runs as a background subagent with its own context, so it never sees the doer's conversation or assumptions.

??? question "What does ultrareview cost on Max, and when does a run count?"
    Three free runs that never refresh, then $5 to $25 in usage credits. A run counts once the cloud session starts, even if stopped.

??? question "Which pool pays for `/codex:adversarial-review`, and what does it refuse to do?"
    Your ChatGPT/Codex usage, not the Claude plan. It is read-only: it never edits.

## Sources

- [Code review](https://code.claude.com/docs/en/code-review){ .src data-checked="2026-09-27" }: 6 min.
- [Find bugs with ultrareview](https://code.claude.com/docs/en/ultrareview){ .src data-checked="2026-09-27" }: pricing table, 6 min.
- [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc){ .src data-checked="2026-09-28" }: OpenAI-maintained README, 3 min.
- [Codex code review](https://learn.chatgpt.com/docs/code-review.md){ .src data-checked="2026-09-27" }: 2 min.

## Ledger prompt

> In **Delegation**: your default review pipeline per change size, and the pool each stage spends.

**Next:** the apply task: a `/gen-week` skill, a reviewer subagent, and Codex grading a Claude-made week.
