---
title: "B9 · Lesson 3 · The radar, the A/B week and uninstall as a first-class move"
terms: [tool radar, marketplace scope, A/B week, superpowers, document skills, AgentShield, kordoc, ccusage]
playbook: tools
---

# B9 · Lesson 3 · The radar, the A/B week and uninstall as a first-class move

<p class="recall" markdown>**Previously:** star-history.com finds candidates; the six-line rubric decides, adopt at 8/12 with no trust zero; one method pack only.</p>

## Idea

A **tool radar** is a dated table, not a wishlist: score, install line, risk note, check date per row. A row earns its place through an **A/B week** and leaves by an uninstall as ordinary as the install.

## How it works

**The [radar](../agentic/radar.md), 2026-09-28.** Adopt: unity-mcp 11 (the Editor as tools), **superpowers** 11 (brainstorm, plan, TDD, subagent per task; one SessionStart hook), **kordoc** 10 (Korean HWP forms to Markdown, form filling; pin the version), **document skills** 10 (DOCX/PDF/PPTX/XLSX; demonstration quality: copies only), **ccusage** 10 (usage report from local logs), docling 9, zotero-mcp 9, playwright-mcp 8.

**Read, don't bundle-install.** ECC, 6: install one way, never stacked, never copy its `hooks/hooks.json` into `settings.json`; take single skills and **AgentShield** as a scanner. Pocock skills 8 versus superpowers 11: one method pack. codex-plugin-cc 7: no push since 2026-07-08; its review gate "may drain usage limits quickly" ([README](https://github.com/openai/codex-plugin-cc){ .src data-checked="2026-09-28" }).

**Scopes.** A **marketplace scope** is user (`~/.claude/settings.json`), project (committed `.claude/settings.json`) or local (`.claude/settings.local.json`); local beats project beats user ([install](https://code.claude.com/docs/en/plugins/install){ .src data-checked="2026-09-28" }). MCP servers default to local ([MCP](https://code.claude.com/docs/en/mcp){ .src data-checked="2026-09-28" }); Codex keeps them in `config.toml` with an `enabled` switch ([Codex MCP](https://learn.chatgpt.com/docs/extend/mcp.md){ .src data-checked="2026-09-28" }).

**The A/B week and the exit.** Same kind of task with and without; log minutes, usage delta (`/usage` attribution per plugin; Codex `/usage weekly`), quality 1–5. Keep at equal quality and less time or usage; otherwise `claude plugin uninstall <name> --scope user`; Codex skills off via `[[skills.config]]` ([security](https://code.claude.com/docs/en/plugins/security){ .src data-checked="2026-09-28" }, [Codex skills](https://learn.chatgpt.com/docs/build-skills.md){ .src data-checked="2026-09-28" }).

**Eight efficiency tips.** (1) `/context` shows what fills the window. (2) CLIs like `gh` before MCP servers. (3) `/mcp` off for idle servers; `/doctor` lists unused plugins. (4) Workflow text out of `CLAUDE.md` into skills; under 200 lines. (5) A hook pre-filters noisy output ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }). (6) `claude plugin details`: Always-on tokens, 2,000 or more highlighted ([measure](https://code.claude.com/docs/en/plugins/measure){ .src data-checked="2026-09-28" }). (7) Toggle plugins between tasks; it invalidates the prompt cache ([install](https://code.claude.com/docs/en/plugins/install){ .src data-checked="2026-09-28" }). (8) Codex: a tool only when it unlocks a real workflow ([Codex practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-28" }).

**In practice.** This repo: playwright-mcp at local scope; the XR project: unity-mcp at project scope; user scope: superpowers and document skills.

## Try it

<div class="visual"><iframe src="../visuals/b9-ab-calculator.html" title="Enter with and without numbers for one tool and read keep or uninstall" loading="lazy"></iframe></div>

Predict first: how many minutes must a method pack save to justify 5 usage points?

**Phone:** list your installed plugins; mark each used this month or not: the rest is the uninstall queue.
**Laptop:** `claude plugin list`, then `/plugin` and the *Not used recently* group: you will see which rows never had an A/B week.

## Rules of thumb

- Add a radar row only at 8 or more, dated; delete it when the monthly refresh finds a stale push.
- Run one A/B week per tool at a time, with the B8 numbers: minutes, usage delta, quality.
- Uninstall the day the A/B loses; a disabled plugin is a decision postponed.

## Retrieval

??? question "Where is a plugin enabled at each scope, and which wins when they disagree?"
    User in the home settings file, project in the committed one, local in settings.local.json; local beats project beats user.

??? question "What makes ECC a read case rather than an install case?"
    Twenty-four hook entries and hundreds of always-on descriptions score 6; single skills and its scanner transfer alone.

??? question "Which three numbers close an A/B week, and what decides keep?"
    Minutes, usage delta, quality 1–5, with and without; keep at equal quality and less time or usage.

## Sources

- [Install plugins](https://code.claude.com/docs/en/plugins/install){ .src data-checked="2026-09-28" }: scopes, uninstall, 8 min.
- [Measure plugins](https://code.claude.com/docs/en/plugins/measure){ .src data-checked="2026-09-28" }: 5 min.
- [Manage costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }: 6 min.
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-28" }: 5 min.

## Ledger prompt

> In **Tools**: one A/B line ("superpowers: 22 min / 6 % / 4 with; 31 / 5 / 3 without; keep") and the scope you gave it.

**Next:** the apply task: five scores, three files, two installs, two A/B lines.
