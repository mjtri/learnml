---
title: B8 · Apply · Playbook v1 installed, first weekly review logged
playbook: weekly review
---

# B8 · Apply · Playbook v1 installed, first weekly review logged

<p class="recall" markdown>**This week in one sentence:** a usage report is six numbers read weekly from `/usage`, `/insights` and Codex `/usage weekly`; every escape hatch (credits, fast mode, a reset, a Premium seat) becomes a budget rule with a threshold and a price; and the weekly review prunes the playbook to at most 20 evidenced rules installed as `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`.</p>

**Laptop · ~60 min · in the build session.**

## Goal

Leave with (1) `playbook.md` at 20 rules or fewer, each with a link or a number, (2) both global files installed and proven to load, (3) the first weekly review line.

## Steps

1. **Meters (5 min).** `/usage` (press `w`), Codex `/usage weekly`, both Settings pages. Write the usage report line.
2. **Prune (20 min).** In plan mode, in this repo:
   ```
   Goal: rewrite docs/agentic/playbook.md to at most 20 rules.
   Context: read the page; every rule becomes "- rule — evidence (date)".
   Constraints: keep a rule only if its evidence is a link or a number;
   merge duplicates; list every deleted rule under "## Deleted" with the
   reason. Never invent evidence.
   Done when: `grep -c "^- " docs/agentic/playbook.md` prints 20 or less
   and every kept line contains "http" or a measured unit (min, %, /5).
   ```
   Approve, then read the Deleted list yourself: restore any rule you can measure next week, tagged "(measure by W40)".
3. **Install (10 min).** Ask: "Write the kept rules as imperatives only, no links or dates, to `rules.txt`." Then in PowerShell, one line each:
   ```
   New-Item -ItemType Directory -Force $HOME\.claude
   New-Item -ItemType Directory -Force $HOME\.codex
   Copy-Item $HOME\.claude\CLAUDE.md $HOME\.claude\CLAUDE.md.bak -ErrorAction SilentlyContinue
   Copy-Item $HOME\.codex\AGENTS.md $HOME\.codex\AGENTS.md.bak -ErrorAction SilentlyContinue
   Copy-Item rules.txt $HOME\.claude\CLAUDE.md
   Copy-Item rules.txt $HOME\.codex\AGENTS.md
   ```
   Existing files survive as `.bak`; delete `rules.txt` afterwards.
4. **Prove it loads (10 min).** New session in each tool from `$HOME`, outside any repo: "Quote the first rule in your instructions, verbatim." In Claude Code `/memory` also lists the user file. Record per tool: quoted yes/no, seconds to answer.
5. **One measured task (15 min).** The same small task in both tools, for example "make `check_lessons.py --only` accept `b8` as well as `agentic-08`": minutes, usage delta (`/usage` before and after; Codex `/usage weekly` before and after), 1–5 quality after reading the diff. Keep the better diff.

## Done when

- `grep -c "^- " docs/agentic/playbook.md` prints 20 or less, and every kept rule has a link or a number.
- Both global files exist and are identical (`Compare-Object (Get-Content $HOME\.claude\CLAUDE.md) (Get-Content $HOME\.codex\AGENTS.md)` prints nothing), and both tools quoted the first rule.
- The **Weekly review** section holds the usage report line and "kept / deleted / to measure".

## Log it

```bash
python track.py done agentic-08/apply --rating 3 --minutes 60 --note "rules kept/deleted; which tool quoted the global rule and how fast"
```

## Ledger prompt

> In **Weekly review**: "W39 review: 16 kept / 6 deleted / 2 to measure; global loaded: Claude yes 4 s, Codex yes 6 s; task X: Claude 9 min / 4 % / 4; Codex 12 min / 3 tasks / 3" and the one rule the comparison changed.
