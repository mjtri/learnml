---
title: B5 · Lesson 1 · Three clocks: /loop, desktop tasks, cloud routines
terms: [/loop, desktop scheduled task, cloud routine, trigger]
playbook: automation
---

# B5 · Lesson 1 · Three clocks: /loop, desktop tasks, cloud routines

<p class="recall" markdown>**Previously:** delegate to subagents, skills and worktrees so the main window stays small, pay for each spawned window knowingly, and let a different agent, ideally a different vendor, grade the work.</p>

## Idea

A scheduled prompt is an agent turn nobody watches. Three clocks can fire it, differing in where the run happens, what it can touch, and what it costs while you sleep. A forgotten timer spends the same weekly cap as a session you sit in.

## How it works

**`/loop` (inside a session).** **`/loop`** re-runs a prompt while the session stays open: `/loop 5m check the deploy`; with no interval, Claude picks the wait itself. Session-scoped: a new conversation clears it, it fires only while Claude Code is idle, and it expires after 7 days ([scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks){ .src data-checked="2026-09-27" }). Every fire re-sends the whole conversation; `/usage` shows a Loops row with tokens per run ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }).

**Desktop scheduled task (your machine, no session).** Desktop app › Code › Routines › New routine › Local. A **desktop scheduled task** starts a fresh session with your files, only while the app is open and the computer awake; a missed day gets one catch-up run on wake, so a 9 am task may run at 11 pm ([desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks){ .src data-checked="2026-09-27" }). "Always allow" its tools after a manual run, or later runs stall unanswered.

**Cloud routine (laptop closed).** A **cloud routine** is a saved prompt plus repositories, run as a cloud session when a **trigger** fires: a schedule (hourly at most), an HTTP call, or a GitHub event such as a pull request opening. Each run clones the repo fresh, asks no permissions, and pushes to `claude/` branches. Research preview; it draws normal subscription usage under a daily cap on runs (one-off runs exempt) ([routines](https://code.claude.com/docs/en/routines){ .src data-checked="2026-09-28" }). Create it with `/schedule`, a few minutes past the hour.

**Codex.** ChatGPT's scheduled tasks are the same idea on the other pool, fired by a schedule or by Gmail, Slack or GitHub events; in the desktop app, "keep the computer on and the app running" ([Codex scheduled tasks](https://learn.chatgpt.com/docs/automations.md){ .src data-checked="2026-09-27" }). OpenAI publishes no per-run usage figure.

**In practice.** This site's daily deploy is a fourth clock: a GitHub Actions workflow running the checker with no model, right for a script. The weekly "fix what the checker flags, open a deployable PR" needs an agent: a cloud routine.

## Try it

<div class="visual"><iframe src="../visuals/b5-three-clocks.html" title="Pick a clock and an interval; read where it runs and what a week of fires costs" loading="lazy"></iframe></div>

Predict first: a 10-minute check for one evening, and a weekly build with the laptop closed. Which clock survives each?

**Phone:** open claude.ai/code/routines and note the remaining daily runs, the apply task's ceiling.
**Laptop:** `/loop 2m say the time`, two fires, then `/usage`: you will see a Loops row, and the second fire re-sending the whole context.

## Rules of thumb

- Use `/loop` only while you are at the keyboard anyway; cancel it before you `/clear`.
- Put a task on the desktop clock when it needs your files; run it once by hand first.
- Put a task in a cloud routine when it must run with the laptop closed; scope its repo and connected services.

## Retrieval

??? question "Why does a `/loop` in a long session cost more each time it fires?"
    Each fire re-sends the entire conversation: a session holding 100k tokens pays about 100k per fire.

??? question "A desktop task was due at 9 am while the laptop slept all day. What happens at 11 pm?"
    One catch-up run for the most recent missed time; older misses are dropped.

??? question "Which clock runs without permission prompts, and what bounds its cost?"
    A cloud routine: normal subscription usage under a daily cap on runs; one-off runs are exempt.

## Sources

- [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks){ .src data-checked="2026-09-27" }: 8 min.
- [Scheduled tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks){ .src data-checked="2026-09-27" }: 5 min.
- [Automate work with routines](https://code.claude.com/docs/en/routines){ .src data-checked="2026-09-28" }: 10 min.
- [Codex: scheduled tasks](https://learn.chatgpt.com/docs/automations.md){ .src data-checked="2026-09-27" }: 3 min.

## Ledger prompt

> In **Automation**: one line per clock naming the task you would give it, or "none yet".

**Next:** driving the laptop from the couch: Remote Control, Codex Remote and cloud sessions, and what the phone cannot do.
