---
title: "B10 · Apply · trip-forms: one data file, three documents, one oracle, both tools"
playbook: automation recipes
---

# B10 · Apply · trip-forms: one data file, three documents, one oracle, both tools

<p class="recall" markdown>**This week in one sentence:** a personal automation is a data file, templates, a skill, an oracle and a trigger; docx and xlsx go through the document skills, LaTeX through `latexmk -g`, HWPX by label with python-hwpx; anything that reads your details runs on your machine, dry-run and diff first, never silently past the forbidden list.</p>

**Laptop · ~60 min.**

## Goal

Leave with the `trip-forms` skill (Claude Code folder plus its `.agents/skills` copy) turning `trip.yaml` into a filled `.docx`, a filled `.hwpx` and a compiled LaTeX report, `check.py` refusing a missing field, timed in both tools against your Lesson 1 number.

## Steps

1. **Folders and pins (5 min).** Needs TeX Live with `latexmk` on PATH, Node 20+ (kordoc), and Hancom Office for the one-time `.hwp` to `.hwpx` save (no Hancom: docx + LaTeX only). `claude update` first: Lesson 3's `--permission-prompts none` needs v2.1.259 or later. One line each in PowerShell:
   ```
   claude update
   New-Item -ItemType Directory -Force $HOME\forms\masters
   New-Item -ItemType Directory -Force $HOME\forms\out
   python -m pip install --user python-hwpx==6.6.0 python-docx openpyxl pyyaml
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
   out/<date>/; never touch masters/; fill.py exits 2 on a missing key and
   writes nothing; no network. check.py walks field-map.yaml: every key
   must exist in trip.yaml and every mapped output cell must be non-empty,
   else exit 1.
   Done when: check.py exits 0 on out/<date>/ and exits 1 after I delete
   one key from trip.yaml and run check.py again.
   ```
   Keep `SKILL.md` to name, description and the never-silently list; scripts by relative path, so the Codex copy works unchanged.
3. **Run in Claude Code (10 min).** `/usage`, then `/trip-forms --dry-run`, `/trip-forms`, `check.py`. Delete `budget_code` from `trip.yaml`, re-run: `fill.py` stops with exit 2 and `check.py` exits 1 on the missing key. Restore it. Record minutes, usage delta, quality 1–5.
4. **Run in Codex (10 min).** Copy the skill:
   ```
   New-Item -ItemType Directory -Force $HOME\.agents\skills
   Copy-Item -Recurse $HOME\.claude\skills\trip-forms $HOME\.agents\skills\trip-forms
   ```
   Open Codex in `$HOME\forms`, `$trip-forms`, same checks; ChatGPT counter before and after.
5. **Diff the HWPX (5 min).** `npx -y kordoc@4.15.7 masters\request.hwpx --keep-empty-cols -o a.md`, the same for the output, then `git diff --no-index a.md b.md`: every changed cell.
6. **Playbook (5 min).** In **Automation recipes**: one line per recipe with minutes by hand, minutes per run in each tool, and the oracle command.

## Done when

- One real form fills from `trip.yaml` in both tools and `check.py` exits 0.
- `check.py` exits 1 with one key removed, and `git ls-files` inside any repo never lists `trip.yaml`.
- **Automation recipes** records minutes saved per run.

## Log it

```bash
python track.py done agentic-10/apply --rating 3 --minutes 60 --note "manual vs recipe minutes per tool; which format needed rework"
```

**Next:** the monthly refresh: `python gen_refresh.py` re-checks every stamped claim and every tool-radar row.

## Ledger prompt

> In **Automation recipes**: "trip-forms: by hand 25 min; Claude 4 min / 3 % / 4; Codex 6 min / 2 tasks / 3; oracle check.py + latexmk -g" and the one rule the timing suggests.
