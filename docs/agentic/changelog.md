---
title: Changelog
---

# What changed since the lessons were written

Track B lessons cite features, limits and prices that change monthly. Each claim carries a `checked` date. `python gen_refresh.py` prints a monthly prompt that re-verifies them; whatever changed is logged here, newest first, so a lesson you read in the past can be corrected in one glance.

## 2026-09-28

- Review pass over B1–B6 and B8: seven apply-task fixes (PowerShell `'{}'` piping, the `{"permissions": {"deny": …}}` settings shape in `settings.local.json`, the B3 hook script shipped in the lesson, B6 refs format `id | title | year | tools`, `Select-String` instead of `grep`, non-destructive global CLAUDE.md install, Unity path + close-Editor note). Rewordings from re-fetched pages: the ChatGPT pricing page now calls per-model message ranges "estimates, not fixed limits"; Deep Research allowances are read from the in-product counter (a fixed allowance, where a plan has one, resets 30 days from first use); the Codex MCP page is `learn.chatgpt.com/docs/extend/mcp`; `/goal`, `/reload-skills` and `claude remote-control --name` verified on the commands / remote-control pages.

- Found while writing B8 (your operating system): the Premium seat is now documented officially (5× usage, no 5-hour limit, weekly reset, $100/$125 per user per month; live since 2026-08-25) and B1 Lesson 2 has been updated and its "(unverified)" removed. The Standard-seat table is now per model (GPT-6 Astra 5–45 … Luna 250–2,000 local messages per 5 h) and OpenAI says message counts are "not a reliable measure"; B1 Lesson 2 reworded. The "Reset for free" button is not available inside Claude Code or the mobile app (web/desktop Settings › Usage only). `/usage` attribution and behaviour flags are computed from this machine only. Prepaid "usage bundles" (discounted credits) exist as a fourth escape hatch.

## 2026-09-27

- Found while writing B5 (automation & phone): the Codex cloud page now lists web, GitHub/GitLab, Linear and Slack as task sources and no longer mentions the phone; B1 Lesson 3's "started from … your phone" is softened to "or the ChatGPT app via Codex Remote". Since a July 2026 update a bare "@claude review" no longer subscribes a PR to push-triggered reviews (use "@claude review always"). `--remote` is a deprecated alias of `--cloud`.
- Found while writing B6 (research paperwork): the ChatGPT pricing page now lists GPT-6 Luna per-5-hour ranges and GPT-5.6 Sol promo pricing to 2026-11-21, so B1 Lesson 2's "15–150 messages per 5 hours" needs re-checking against the current Business column at the next refresh. ChatGPT connectors are presented as "connected apps" under Settings › Plugins; full MCP write support is beta for Business/Enterprise/Edu and only admins can enable developer mode. Claude's "using research" help article moved to a new slug (11088861) and still states the usage-limit sentence the lesson quotes. OpenAI's Deep Research page no longer publishes a monthly task count (in-product counter only).
- Found while writing B3 (verification & permissions): Claude Code's built-in starting permission mode for terminal/VS Code sessions is now **auto** (v2.1.283+); B1 Lesson 3's "plan mode first" remains the recommended habit, not the default. Codex's "untrusted" approval policy is no longer selectable and "on-failure" is deprecated (on-request / never remain). Codex now ships lifecycle hooks (`.codex/hooks.json`) and a native Windows sandbox. Claude Code's Bash sandbox is WSL2-only on Windows.
- Found while writing B4 (delegation): `/code-review` runs as a background subagent (v2.1.218+, `/review` is an alias); Code Review on GitHub is Team/Enterprise only; ultrareview on Max = 3 one-time free runs, then usage credits; agent teams cost ~7× tokens in plan mode; Codex has `.agents/skills` SKILL.md and `.codex/agents` TOML subagents.

- Track B created. All claims in B1 were checked against official pages on this date; a second link pass corrected four overstatements (Claude pool wording, ChatGPT shared-pool wording, the CLI-over-MCP source, a moved Anthropic URL).
- Seen while checking, for later weeks: Claude Code reads `AGENTS.md` directly only from v2.1.277; Codex caps `AGENTS.md` at 32 KiB by default (`project_doc_max_bytes`); the ChatGPT pricing page lists a "Business ($100)" tier using Pro 5x estimates and says weekly limits may apply; it also notes GPT-5.5 retires on 2026-10-14.
- Known at writing time, not yet reflected in lessons: OpenAI's "Codex-only" Business seats closed to new workspaces on 2026-06-24 (unverified, third-party report). GPT-6 Sol/Luna were released for Work and Codex on 2026-09-22 (official announcement page not fetchable at the time; unverified).
