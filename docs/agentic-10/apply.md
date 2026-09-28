---
title: "B10 · Apply · trip-forms: one data file, three documents, one oracle, both tools"
playbook: automation
---

# B10 · Apply · trip-forms: one data file, three documents, one oracle, both tools

<p class="recall" markdown>**This week in one sentence:** a personal automation is a data file, templates, a skill, an oracle and a trigger; docx and xlsx go through the document skills, LaTeX through `latexmk -g`, HWPX by label with python-hwpx; anything that reads your details runs on your machine, dry-run and diff first, never silently past the forbidden list.</p>

**Laptop · ~60 min.**

## Goal

Leave with the `trip-forms` skill (Claude Code folder plus its `.agents/skills` copy) turning `trip.yaml` into a filled `.docx`, a filled `.hwpx` and a compiled LaTeX report, `check.py` refusing a missing field, timed in both tools against your Lesson 1 number.

## Steps

1. **Folders and pins (5 min).** One line each in PowerShell:
   ```
   New-Item -ItemType Directory -Force $HOME\forms\masters
   New-Item -ItemType Directory -Force $HOME\forms\out
   python -m venv $HOME\forms\.venv
   & "$HOME\forms\.venv\Scripts\python.exe" -m pip install python-hwpx==6.6.0 python-docx openpyxl pyyaml
   ```
   Copy the real trip request into `masters\request.hwpx` (open the `.hwp` in Hancom, save as HWPX) and the report `.docx` beside it. Write `$HOME\forms\trip.yaml` with tonight's facts.
2. **Build the skill (20 min).** In Claude Code, plan mode, from `$HOME\forms`:
   ```
   Goal: a skill trip-forms in ~/.claude/skills/trip-forms/ with SKILL.md,
   field-map.yaml, scripts/fill.py, scripts/check.py, scripts/report.tex.
   Context: trip.yaml here; masters in masters/; python-hwpx fill_by_path
   with "label > right" paths; docx by label via python-docx; fields.tex
   written from trip.yaml, compiled by latexmk -g -pdf -halt-on-error.
   Constraints: --dry-run prints the map and writes nothing; outputs go to
   out/<date>/; never touch masters/; a missing key exits 2; no network.
   Done when: check.py exits 0 on out/<date>/ and exits 1 after I delete
   one key from trip.yaml and re-run.
   ```
   Keep `SKILL.md` to name, description and the never-silently list; scripts by relative path, so the Codex copy works unchanged.
3. **Run in Claude Code (10 min).** `/usage`, then `/trip-forms --dry-run`, `/trip-forms`, `check.py`. Delete `budget_code` from `trip.yaml`, re-run: the oracle must fail. Restore it. Record minutes, usage delta, quality 1–5.
4. **Run in Codex (10 min).** `Copy-Item -Recurse $HOME\.claude\skills\trip-forms $HOME\.agents\skills\trip-forms`, open Codex in `$HOME\forms`, `$trip-forms`, same checks; ChatGPT counter before and after.
5. **Diff the HWPX (5 min).** `npx -y kordoc@4.15.7 masters\request.hwpx --keep-empty-cols -o a.md`, the same for the output, then `git diff --no-index a.md b.md`: every changed cell.
6. **Playbook (5 min).** Add an **Automation recipes** block under **Automation**: one line per recipe with minutes by hand, minutes per run in each tool, and the oracle command.

## Done when

- One real form fills from `trip.yaml` in both tools and `check.py` exits 0.
- `check.py` exits non-zero with one key removed, and `git ls-files` inside any repo never lists `trip.yaml`.
- The **Automation recipes** block records minutes saved per run.

## Log it

```bash
python track.py done agentic-10/apply --rating 3 --minutes 60 --note "manual vs recipe minutes per tool; which format needed rework"
```

## Ledger prompt

> In **Automation**, under **Automation recipes**: "trip-forms: by hand 25 min; Claude 4 min / 3 % / 4; Codex 6 min / 2 tasks / 3; oracle check.py + latexmk -g" and the one rule the timing suggests.
