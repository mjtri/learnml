---
title: Tool radar
---

# Tool radar

Repositories worth adopting for the long run, scored with the B9 **worth-it rubric** (six lines, 0–2 each: changes a weekly habit · context/usage cost · trust · maintenance · works in both tools · fit for your four workflows; adopt at ≥ 8/12 with no zero on trust). Stars and dates come from the GitHub API on the `checked` date. `python gen_refresh.py` re-checks every row monthly; changes are logged in the [changelog](changelog.md). Discovery source: [star-history.com](https://www.star-history.com/) (Weekly tab → per-repo Trending tab → `/compare/<category>`).

## Adopt (passes the rubric)

| Repo | What it changes | Score | Install | Risk note | Checked |
|---|---|---|---|---|---|
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | Your daily Unity loop: the agent reads scenes, assets and scripts through the Editor | 11 | Unity Package Manager → add from git URL `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main` (pin a tag) | MIT, pushed 2026-09-27, 97 issues; both tools; client config step not verified | 2026-09-28 |
| [obra/superpowers](https://github.com/obra/superpowers) | How you plan and test: brainstorm → plan → TDD → subagent, loaded on demand | 11 | `/plugin install superpowers@claude-plugins-official` (Codex: Plugins sidebar) | MIT, 292k stars, 270 issues; overlaps mattpocock/skills, pick one method pack | 2026-09-28 |
| [chrisryugj/kordoc](https://github.com/chrisryugj/kordoc) | Korean paperwork: HWP/HWPX/PDF → Markdown, form filling, old/new diff | 10 | `npx -y kordoc setup` (choose Claude Code and Codex) | MIT, single maintainer → pin the version | 2026-09-28 |
| [anthropics/skills](https://github.com/anthropics/skills) (document-skills) | DOCX/XLSX/PDF/PPTX in and out | 10 | `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills` | Anthropic-maintained; labelled demo-quality; test on copies | 2026-09-28 |
| [ccusage/ccusage](https://github.com/ccusage/ccusage) | The weekly usage report, for Claude Code and Codex, from local logs | 10 | `npx ccusage@latest daily` · `npx ccusage@latest codex daily` | No hooks, no context cost; licence "Other" | 2026-09-28 |
| [docling-project/docling](https://github.com/docling-project/docling) | Paper PDFs → Markdown with tables and formulas, for literature reviews | 9 | `pip install docling` | MIT, 68k stars, large contributor base; heavy models on first run | 2026-09-28 |
| [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) | Your reference library inside both agents | 9 | `uv tool install zotero-mcp-server` then `zotero-mcp setup`; add to CC/Codex with `claude mcp add` / `codex mcp add` | MIT; setup auto-configures Claude Desktop only | 2026-09-28 |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Browser tasks and web-form checks, per project | 8 | `claude mcp add playwright npx @playwright/mcp@latest` | Apache-2.0; enable per project to limit tool-schema cost | 2026-09-28 |

## Read, don't bundle-install

| Repo | Why it is here | Score | What to take | Checked |
|---|---|---|---|---|
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 292 skills, 68 agents, hooks on every turn: high context cost; install one way only, never stacked | 6 | The [shortform guide](https://github.com/affaan-m/ECC/blob/main/the-shortform-guide.md), single skills copied into `.claude/skills`, AgentShield as a scanner | 2026-09-28 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Good method pack (`grill-with-docs`, `to-spec`, `tdd`, `handoff`); overlaps superpowers | 8 | `claude plugins install mattpocock-skills` if you did not install superpowers; third-party, auto-updates | 2026-09-28 |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | Cross-vendor review inside Claude Code; no push since 2026-07-08 | 7 | `/plugin marketplace add openai/codex-plugin-cc` → `/plugin install codex@openai-codex`; re-check activity first | 2026-09-28 |
| cc-switch, ruflo, gstack, claude-code-router, github-mcp-server | Popular but a poor fit: writes your configs / heavy orchestration / startup roles / not needed on Max / `gh` is cheaper | ≤ 6 | Nothing for now | 2026-09-28 |

## Bookmarks (discover, never install from the list)

[star-history.com](https://www.star-history.com/) · [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) · [openai/skills](https://github.com/openai/skills)

_Add a row when a candidate scores ≥ 8; delete a row when a monthly refresh drops it. The B9 apply task adds your first two rows._
