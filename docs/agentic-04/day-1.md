---
title: B4 · Lesson 1 · Subagents and skills: summaries in, context saved
terms: [skill, plugin]
playbook: delegation
---

# B4 · Lesson 1 · Subagents and skills: summaries in, context saved

<p class="recall" markdown>**Previously:** week 3 gave the agent an oracle it can run, a permission mode chosen on purpose, and hooks for the rules that must always hold.</p>

## Idea

Delegation is a trade. A subagent spends *more* tokens in total (its own instructions, reads, reasoning) so that your main context window gets a 30-line summary instead of a 3,000-line log. A **skill** is the other half: instructions that stay on disk until needed instead of sitting in `CLAUDE.md` every turn. Every hand-off asks: does the window you keep small save more than the window you spawn costs?

## How it works

**Subagents.** A subagent is a Markdown file in `.claude/agents/<name>.md`, or `~/.claude/agents/` for every project: `name` and `description` required; `tools`, `model`, `permissionMode`, `isolation` optional ([subagents](https://code.claude.com/docs/en/sub-agents){ .src data-checked="2026-09-27" }). It starts with its own system prompt, your `CLAUDE.md` and the task message; it never sees your conversation, the files you already read, or your corrections. By default it runs in the background with fewer tools, up to 20 at once, on the same usage limits as the main session; the built-in `Explore` agent is read-only and skips `CLAUDE.md`.

**Skills.** A skill is a folder `.claude/skills/<name>/SKILL.md`. Only its `description` is in context; the body loads when you type `/<name>` or Claude decides it fits ([skills](https://code.claude.com/docs/en/skills){ .src data-checked="2026-09-27" }). `disable-model-invocation: true` keeps a costly skill manual. After compaction only the first 5,000 tokens of a loaded skill return, so keep the body short. Anthropic's cost advice: `CLAUDE.md` under about 200 lines, workflow detail in skills ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }).

**Plugins.** A **plugin** bundles skills, agents, hooks and MCP servers into one installable unit. The price: every invocable component's name and description sits in context on every turn, used or not; the marketplace shows a "Context cost" estimate ([plugins](https://code.claude.com/docs/en/plugins){ .src data-checked="2026-09-27" }).

**Codex** has both shapes: skills in `.agents/skills/<name>/SKILL.md`, description first, body when chosen ([Codex skills](https://learn.chatgpt.com/docs/build-skills.md){ .src data-checked="2026-09-27" }); subagents that "consume more tokens than comparable single-agent runs" ([Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents.md){ .src data-checked="2026-09-27" }). The same file format serves both tools; only the folder differs.

**In practice.** The ETRI TM report format is 60 lines you need twice a year. In `CLAUDE.md` it costs 60 lines on every turn of every Unity session; as `/tm-report` it costs one description line until the day you type it.

## Try it

<div class="visual"><iframe src="../visuals/b4-delegation-cost.html" title="Compare tokens spent with and without a subagent" loading="lazy"></iframe></div>

Predict first: a 6k-token log, then eight more turns. Does a subagent save tokens, and where is break-even?

**Phone:** which paragraph of your `CLAUDE.md` serves only one workflow? That is your first skill.
**Laptop:** move it to `.claude/skills/<name>/SKILL.md` with a one-line description, `/reload-skills`, then `/context` before and after: you will see the instructions share of the window drop.

## Rules of thumb

- Delegate a read whose output you will not edit; keep in the main window what you will.
- Put instructions used by one workflow in a skill; only rules for every session stay in `CLAUDE.md`.
- Read a plugin's context cost before installing it; disable the ones `/usage` shows as unused.

## Retrieval

??? question "What does a subagent see at start, and what does it never see?"
    Its own system prompt, your CLAUDE.md and the task message. Never your conversation, files or corrections.

??? question "What is in context before a skill is invoked, and what survives a compaction?"
    Only the description line. After compaction only the first 5,000 tokens of the loaded body come back.

??? question "Why can an installed plugin cost usage in a session that never uses it?"
    Every invocable component's name and description is in context on every turn; each turn pays for the listing.

## Sources

- [Subagents](https://code.claude.com/docs/en/sub-agents){ .src data-checked="2026-09-27" }: 8 min.
- [Skills](https://code.claude.com/docs/en/skills){ .src data-checked="2026-09-27" }: 8 min.
- [Plugins overview](https://code.claude.com/docs/en/plugins){ .src data-checked="2026-09-27" }: context cost, 4 min.
- [Codex: build skills](https://learn.chatgpt.com/docs/build-skills.md){ .src data-checked="2026-09-27" }: 4 min.

## Ledger prompt

> In **Delegation**: the paragraph you moved out of `CLAUDE.md`, and the `/context` numbers before and after.

**Next:** two agents at once without overwriting each other: worktrees and background sessions.
