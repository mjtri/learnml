---
title: B8 · Lesson 1 · Reading your own meters: what a week of usage says
terms: [usage report, /insights]
playbook: weekly review
---

# B8 · Lesson 1 · Reading your own meters: what a week of usage says

<p class="recall" markdown>**Previously:** week 7 set up a harness for long-running agent work: a progress file, a CHANGELOG of failed approaches, a commit per unit, and test oracles.</p>

## Idea

Seven weeks of rules and still the same Sunday question: where did the usage go? A **usage report** is six numbers written down once a week from meters you already have; the pattern in them, not the total, says what to change. Without it the playbook stays opinion.

## How it works

**Claude: `/usage`.** The plan bars (5-hour window, weekly cap, model limits) come from your account. The rest is "computed from local session history on this machine": attribution (skills, subagents, plugins, each MCP server), behavior flags (long context, cache misses, flagged at 10 % or more of recent usage), and a Loops row per scheduled task with tokens per run. Press `w` for the last 7 days; other devices and claude.ai are excluded ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }).

**Claude: `/insights`.** **`/insights`** writes an HTML report "on how you work rather than how many tokens you've used": friction points and suggestions. It analyzes up to 200 unseen sessions, writes `~/.claude/usage-data/report.html` (deleted with other session data after 30 days by default), spends plan tokens, and is not available in cloud sessions ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }, [commands](https://code.claude.com/docs/en/commands){ .src data-checked="2026-09-28" }). Monthly is enough.

**Codex and ChatGPT.** `/status` shows "session configuration and token usage"; `/usage daily`, `/usage weekly` or `/usage cumulative` show account token activity ([developer commands](https://learn.chatgpt.com/docs/developer-commands){ .src data-checked="2026-09-28" }). The usage dashboard in Settings shows the exhausted allowance and reset time; "a long-running task can use substantially more than a short request", so count tasks, not messages ([Codex with your plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan){ .src data-checked="2026-09-28" }).

**The six numbers.** Claude weekly % and worst window %; the top attribution item with its share; any flag; Codex weekly %; credits spent, both tools. Readings: worst window near 100 % with weekly under 50 % is bunched sessions; a subagent or MCP share over a third means delegation is the bill; a cache-miss flag means cold restarts after long breaks.

**In practice.** This repo, one week: weekly 58 %, worst window 92 % (the Saturday build), attribution "subagents 31 %", flag "long context", Codex 20 %. Reading: the build session is the whole bill. Give generation subagents Sonnet and `/clear` between weeks.

## Try it

<div class="visual"><iframe src="../visuals/b8-usage-reader.html" title="Enter a week of usage numbers and read what to change" loading="lazy"></iframe></div>

Predict first: enter last week's numbers from memory, then the real ones from `/usage`; which verdict changes?

**Phone:** claude.ai › Settings › Usage and the ChatGPT usage dashboard: write each weekly % and reset day into a note titled "usage report W39".
**Laptop:** `/usage`, press `w`, copy attribution and flags into the note; then `/insights` once and read only the friction section: you will see which request types Claude misread.

## Rules of thumb

- Read `/usage` on the 7-day view once a week and act on the top attribution item, not the total.
- Run `/insights` monthly on the laptop and take one suggestion into the playbook; it spends plan tokens.
- Count Codex work in tasks and `/usage weekly`, never in messages.

## Retrieval

??? question "Which parts of /usage are account-wide and which are this machine only?"
    The plan bars are the account. Attribution, behavior flags and Loops rows come from local session history, so other devices and claude.ai are missing.

??? question "What does /insights cost and where does the report go?"
    Its analysis runs through your plan and counts against it. The report lands in ~/.claude/usage-data/report.html, deleted after 30 days by default.

??? question "Worst window 95 %, weekly cap 40 %: what is the reading?"
    Sessions are bunched into one block. Spread them or move the heavy block to the other pool; the weekly cap is not the problem.

## Sources

- [Manage costs effectively](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }: `/usage`, `/insights`, 8 min.
- [Commands](https://code.claude.com/docs/en/commands){ .src data-checked="2026-09-28" }: 2 min.
- [Codex developer commands](https://learn.chatgpt.com/docs/developer-commands){ .src data-checked="2026-09-28" }: `/status`, `/usage`, 3 min.
- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan){ .src data-checked="2026-09-28" }: 4 min.

## Ledger prompt

> In **Weekly review**: your first usage report line ("W39: Claude 58 % / worst 92 % / subagents 31 % / long context; Codex 20 %; credits $0").

**Next:** budgets and escape hatches: credits, fast mode, resets and seat types, each with its own price.
