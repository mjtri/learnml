---
title: "B9 · Lesson 1 · The extension map and the three files you read first"
terms: [extension layer, plugin marketplace, allowed-tools]
playbook: tools
---

# B9 · Lesson 1 · The extension map and the three files you read first

<p class="recall" markdown>**Previously:** a usage report is six numbers read weekly from `/usage`, `/insights` and Codex `/usage weekly`; every escape hatch (credits, fast mode, a reset, a Premium seat) becomes a budget rule with a threshold and a price; and the weekly review prunes the playbook to at most 20 evidenced rules installed as `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`.</p>

## Idea

Every add-on lands in one of seven **extension layers**; each differs in what it can do, where it runs and what it costs per turn. It prevents two wastes: a 300-skill bundle installed for one skill, and a catalog name trusted instead of the files that run as you.

## How it works

**Seven layers.** *Skills*: a folder with a `SKILL.md`; only the description sits in context until invoked, and both tools read the same Agent Skills format ([skills](https://code.claude.com/docs/en/skills){ .src data-checked="2026-09-28" }, [Codex skills](https://learn.chatgpt.com/docs/build-skills.md){ .src data-checked="2026-09-28" }). *Plugins*: skills, agents, hooks and MCP servers as one install; every invocable component's name and description is in context "on every turn", even when nothing from it runs ([plugins](https://code.claude.com/docs/en/plugins){ .src data-checked="2026-09-28" }). A **plugin marketplace** is a catalog: `claude-plugins-official` is added for you, nothing else is; its name says who publishes the list, not what a plugin does. *Hooks* (shell commands at 28 events) and *MCP servers* (processes on your machine) run outside the sandbox, as you ([security](https://code.claude.com/docs/en/plugins/security){ .src data-checked="2026-09-28" }). *Subagents* cost a separate context window. *Rules* (`.claude/rules/*.md` with `paths:`) load only when matching files are touched; Codex has only the AGENTS.md chain ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-28" }).

**The checklist.** The details pane says a hook exists, not what it runs, so open the repository and read `hooks/hooks.json` (each hook's command), `.mcp.json` (server commands or URLs) and every file in `bin/` (on the Bash tool's `PATH`). Then two settings: **allowed-tools** in each `SKILL.md`, because "a skill can grant itself broad tool access", and auto-update, on by default for official-name marketplaces, which rewrites reviewed files silently ([security](https://code.claude.com/docs/en/plugins/security){ .src data-checked="2026-09-28" }, [install](https://code.claude.com/docs/en/plugins/install){ .src data-checked="2026-09-28" }). Codex's version: review and trust plugin hooks before they run ([Codex plugins](https://learn.chatgpt.com/docs/plugins.md){ .src data-checked="2026-09-28" }).

**In practice.** `mattpocock-skills` installs as `…@claude-plugins-official` ([listing](https://claude.com/marketplace/plugins/mattpocock-skills){ .src data-checked="2026-09-28" }), so it auto-updates although a third party wrote it. Its repository has no `hooks/`, `.mcp.json` or `bin/`: two minutes, and the finding is the absence. The same walk through ECC finds 21 hook entries and a `chrome-devtools` server.

## Try it

<div class="visual"><iframe src="../visuals/b9-extension-map.html" title="Tap a layer to see its powers, where it runs and its cost per turn" loading="lazy"></iframe></div>

Predict first: which two layers add no model tokens yet run code as you?

**Phone:** open the GitHub page of one plugin you have; note "absent" or the first command in each of the three files.
**Laptop:** `claude plugin list`, then `claude plugin details <name>`: you will see an `Always-on` token figure per plugin.

## Rules of thumb

- Read `hooks/hooks.json`, `.mcp.json` and `bin/` before installing from any marketplace, official or not.
- Copy one skill folder instead of a plugin when one skill is all you want; the rest is per-turn cost.
- Turn auto-update off for a marketplace you reviewed by hand; update on purpose, after re-reading.

## Retrieval

??? question "Which layers run code with your privileges, and which only add instructions?"
    Hooks, MCP servers and `bin/` executables run as you, outside the sandbox. Skills, agents and rules are instructions using tools you already allow.

??? question "What does an enabled plugin cost in a session where you never use it?"
    Every invocable skill, agent and command's name and description, on every turn; bodies load only on use.

??? question "A marketplace is named claude-plugins-official. What does that prove about a plugin in it?"
    Only that Anthropic publishes the catalog and auto-update is on. Who wrote it and what its hooks run still need the three files.

## Sources

- [Plugin security and trust](https://code.claude.com/docs/en/plugins/security){ .src data-checked="2026-09-28" }: the three files, 6 min.
- [Plugins overview](https://code.claude.com/docs/en/plugins){ .src data-checked="2026-09-28" }: per-turn cost, 5 min.
- [Skills](https://code.claude.com/docs/en/skills){ .src data-checked="2026-09-28" }: allowed-tools, 4 min.
- [Codex plugins](https://learn.chatgpt.com/docs/plugins.md){ .src data-checked="2026-09-28" }: 3 min.

## Ledger prompt

> In **Tools**: the three files you read before any install, and which marketplaces on your machine auto-update.

**Next:** finding candidates by traction on star-history.com and deciding with six lines instead of hype.
