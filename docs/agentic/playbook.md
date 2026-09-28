---
title: Playbook
---

# Playbook

Your working rules for Claude Code (Max 20x) and ChatGPT Business (chat + Codex). This page is the **ledger for Track B**: each lesson ends with a prompt to add one line here. Keep it short: a rule earns its place by a source or a measurement, and gets deleted when it stops being true. Target ≤ 20 rules by week B8.

Format: `- rule — evidence (date)`. Evidence is a link, or a number you measured in an apply task.

## Seed rules (from official guidance, checked 2026-09-27)

These ten appear in several official sources at once. Keep, edit or delete them as your own evidence comes in.

1. Give the agent a check it can run: a test, a build, a checker, a "done when" it can evaluate itself. — [Claude Code best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }, [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }
2. Explore, then plan, then code. Skip the plan only for one-line diffs. — [Claude Code best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }, [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }
3. Keep one short, durable instruction file (AGENTS.md, imported by CLAUDE.md) and prune it. — [Memory docs](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }, [AGENTS.md docs](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md){ .src data-checked="2026-09-27" }
4. Context is the scarce resource: load it just in time; `/clear` or restart instead of piling on corrections. — [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents){ .src data-checked="2026-09-27" }
5. Hand research and noisy output to subagents that return summaries. — [Claude Code best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }
6. Keep a progress file and commit after each unit of work. — [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents){ .src data-checked="2026-09-27" }
7. Separate the doer from the grader: review with a different agent, ideally a different vendor. — [codex-plugin-cc](https://github.com/openai/codex-plugin-cc){ .src data-checked="2026-09-28" } (OpenAI-maintained plugin for Claude Code), [Code review](https://code.claude.com/docs/en/code-review){ .src data-checked="2026-09-27" }
8. Start with tight permissions or a sandbox; loosen only for trusted repos. — [Permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" }, [Codex sandboxing](https://learn.chatgpt.com/docs/sandboxing){ .src data-checked="2026-09-27" }
9. Few, well-described tools; prefer a CLI the agent can call over a heavy MCP server. — [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents){ .src data-checked="2026-09-27" } (few tools), [Manage costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" } (CLI over MCP)
10. Start with the simplest thing; automate a task only once the manual version runs reliably. — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents){ .src data-checked="2026-09-27" }, [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }

## Budget

_(B1 lines go here: how you read the meters, when you switch model or tool.)_

## Instructions

_(B2)_

## Verification

_(B3)_

## Delegation

_(B4)_

## Automation

_(B5)_

## Research

_(B6)_

## Experiments

_(B7)_

## Tools

_(B9: what you installed, its rubric score, and the A/B week that kept it; what you uninstalled and why.)_

## Automation recipes

_(B10: each recipe as data file + form template + skill + oracle + trigger, with minutes saved per run.)_

## Weekly review

_(B8: what you check every week, and what you deleted from this page.)_
