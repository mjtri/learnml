---
title: Changelog
---

# What changed since the lessons were written

Track B lessons cite features, limits and prices that change monthly. Each claim carries a `checked` date. `python gen_refresh.py` prints a monthly prompt that re-verifies them; whatever changed is logged here, newest first, so a lesson you read in the past can be corrected in one glance.

## 2026-09-27

- Found while writing B3 (verification & permissions): Claude Code's built-in starting permission mode for terminal/VS Code sessions is now **auto** (v2.1.283+); B1 Lesson 3's "plan mode first" remains the recommended habit, not the default. Codex's "untrusted" approval policy is no longer selectable and "on-failure" is deprecated (on-request / never remain). Codex now ships lifecycle hooks (`.codex/hooks.json`) and a native Windows sandbox. Claude Code's Bash sandbox is WSL2-only on Windows.
- Found while writing B4 (delegation): `/code-review` runs as a background subagent (v2.1.218+, `/review` is an alias); Code Review on GitHub is Team/Enterprise only; ultrareview on Max = 3 one-time free runs, then usage credits; agent teams cost ~7× tokens in plan mode; Codex has `.agents/skills` SKILL.md and `.codex/agents` TOML subagents.

- Track B created. All claims in B1 were checked against official pages on this date; a second link pass corrected four overstatements (Claude pool wording, ChatGPT shared-pool wording, the CLI-over-MCP source, a moved Anthropic URL).
- Seen while checking, for later weeks: Claude Code reads `AGENTS.md` directly only from v2.1.277; Codex caps `AGENTS.md` at 32 KiB by default (`project_doc_max_bytes`); the ChatGPT pricing page lists a "Business ($100)" tier using Pro 5x estimates and says weekly limits may apply; it also notes GPT-5.5 retires on 2026-10-14.
- Known at writing time, not yet reflected in lessons: OpenAI's "Codex-only" Business seats closed to new workspaces on 2026-06-24 (unverified, third-party report). GPT-6 Sol/Luna were released for Work and Codex on 2026-09-22 (official announcement page not fetchable at the time; unverified).
