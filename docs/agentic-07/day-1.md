---
title: B7 · Lesson 1 · The long-running harness: progress file, changelog, commit per unit
terms: [long-running harness, progress file, CHANGELOG, commit per unit, unattended run]
playbook: experiments
---

# B7 · Lesson 1 · The long-running harness: progress file, changelog, commit per unit

<p class="recall" markdown>**Previously:** a literature review is search in both tools, dedupe, a scripted citation verification and only then a summary; Projects hold the standing instructions (TM template, reviewer-response table, KR↔EN glossary); and the plan's training policy decides where an unpublished draft may live.</p>

## Idea

A week-long experiment cannot live in one context window; every restart is a new engineer with no memory of the last shift. A **long-running harness** puts the memory on disk: a **progress file**, a **CHANGELOG** whose best section is failed approaches, a **commit per unit** so any step rolls back, and an oracle run before any claim of progress. Without it an **unattended run** retries old dead ends, declares victory early, or runs out of context halfway.

## How it works

**Three failure modes.** Anthropic's harness post: context loss between sessions ("engineers working in shifts"), declaring the job done after partial progress, and one-shotting the whole app until context runs out. Its answer: an initializer session writes `claude-progress.txt` and a feature list with `passes: false`; every later session reads the progress file, runs the tests, does one feature and commits it ([effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents){ .src data-checked="2026-09-28" }).

**Failed approaches.** The scientific-computing post keeps one `CHANGELOG.md`, "a sort of lab notes": status, failed approaches and why, accuracy tables. "Without them, successive sessions will re-attempt the same dead ends." The oracle is a reference implementation or a test suite; commit after every meaningful unit ([long-running Claude](https://www.anthropic.com/research/long-running-Claude){ .src data-checked="2026-09-28" }). This course uses `progress.md` for status and `CHANGELOG.md` for history. Do not let the working agent grade itself; a separate, skeptical evaluator is "far more tractable" ([harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps){ .src data-checked="2026-09-28" }).

**In the tools.** Claude Code: a Stop hook can block the turn from ending until your check passes (up to a cap of consecutive blocks), and `claude -p` runs a unit unattended ([best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-28" }). Codex: one chat per coherent unit of work, worktrees for scheduled tasks, and ask it to run the checks before you accept ([Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-28" }).

**In practice.** This week's pages came from a worktree agent that lands one commit; if it dies, the branch is the record. Week 12: `progress.md` says "next unit: pixel-distance baseline, 5 seeds"; `CHANGELOG.md` says "cosine on raw spectrogram: failed, collapses to 0.05, run 0007".

## Try it

<div class="visual"><iframe src="../visuals/b7-harness-anatomy.html" title="Tap each part of a long-running harness to see what breaks without it" loading="lazy"></iframe></div>

Predict first which missing part wastes the most usage over five sessions, then remove parts one at a time.

**Phone:** open your longest session in the Claude app's Code tab: could a fresh session continue it from files alone? Name the missing file.
**Laptop:** ask Claude Code: "Write `progress.md` for this repo from `git log --oneline -20`: status, next unit, blocked on, under 15 lines." Then `/clear` and ask "What is the next unit?"; you will see whether the file is enough.

## Rules of thumb

- Open every agent session with "read progress.md and CHANGELOG.md, run the check".
- Log a failed approach in the CHANGELOG the moment it fails, with its run id, so no session retries it.
- Commit after each unit; never let an agent edit or delete a test to make a unit pass.

## Retrieval

??? question "Three failure modes of long-running agents: which harness part answers each?"
    Context loss: progress file and CHANGELOG. Premature done: the oracle before the claim. Over-ambition: one unit, one commit per session.

??? question "Why is the failed-approaches section worth more than completed tasks?"
    Completed work is visible in git; a dead end is not, so a fresh session re-attempts it and pays again.

??? question "Why not let the working agent grade its own unit?"
    Asked to judge its own output it praises it; a separate evaluator or a script is easier to make skeptical.

## Sources

- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents){ .src data-checked="2026-09-28" }
- [Long-running Claude for scientific computing](https://www.anthropic.com/research/long-running-Claude){ .src data-checked="2026-09-28" }
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps){ .src data-checked="2026-09-28" }
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-28" }

## Ledger prompt

> In **Experiments**: the three files every experiment folder gets, and the sentence every agent session starts with.

**Next:** analysis scripts that regenerate every number and plot, and statistics a reviewer cannot knock down.
