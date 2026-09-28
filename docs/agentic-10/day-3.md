---
title: "B10 · Lesson 3 · Run it unattended, safely: where, what it may touch, what it must never do silently"
terms: [personal data boundary, dry run]
playbook: automation recipes
---

# B10 · Lesson 3 · Run it unattended, safely: where, what it may touch, what it must never do silently

<p class="recall" markdown>**Previously:** docx and xlsx via the document skills, LaTeX via `latexmk -g`, HWPX by label with python-hwpx, the master diffed as Markdown.</p>

## Idea

Unattended means nobody answers a permission prompt or notices that a master was overwritten. The **personal data boundary** says what a run may read and where it may write. The **dry run** shows what it would write before it writes. Where it runs decides whether either boundary holds.

## How it works

**Four places it can run.** Desktop scheduled task: your machine and files, only while the app is open and the computer awake; "always allow" after a first Run now ([desktop tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks){ .src data-checked="2026-09-28" }). Cloud routine: a fresh clone of a GitHub repository, no permission prompts, every connected connector included by default ([routines](https://code.claude.com/docs/en/routines){ .src data-checked="2026-09-28" }). Cowork `/schedule`: also the cloud ([Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork){ .src data-checked="2026-09-28" }). Codex: desktop tasks need the computer on and the app running; web tasks "can't work directly in a folder on your computer" ([Codex tasks](https://learn.chatgpt.com/docs/automations.md){ .src data-checked="2026-09-28" }). So your details get a local task or you; cloud clocks see only repositories.

**The personal data boundary.** `trip.yaml` and the outputs live in `$HOME\forms\`, outside every repository; the skill folder holds no value. Proof, inside any repo: `git ls-files` never lists it. Secrets never go into `SKILL.md` or a routine's environment variables (readable by other users). Open Codex in `$HOME\forms`; edits outside the workspace need approval ([Codex sandbox](https://learn.chatgpt.com/docs/agent-approvals-security){ .src data-checked="2026-09-28" }).

**Dry run, diff, write.** `fill.py --dry-run` prints the map with tonight's values and touches nothing. The real run writes under `out\<date>\`, never over a master; then diff, `check.py`, upload. Unattended in Claude Code (line below), anything that would have prompted is denied and the run fails loudly (`claude update` to v2.1.259 or later) ([programmatic runs](https://code.claude.com/docs/en/headless){ .src data-checked="2026-09-28" }).

```
claude -p "/trip-forms" --allowedTools "Bash(python *),Read" --permission-prompts none
```

**Never silently.** Overwrite a master. Write outside `out\`. Submit, upload or email. Place a seal. Invent a missing value: `fill.py` exits 2 on a missing key, `check.py` 1 on an empty cell. Read another data file. Change the field map. Call the network. Skip the oracle. Each is a line in `SKILL.md`; those that have bitten you become a hook (week 7).

**In practice.** A weekly trip-report reminder is a fine cloud routine: calendar in, note out. The filling needs `trip.yaml`, so it is not. Let the clock nag; you run the recipe.

## Try it

<div class="visual"><iframe src="../visuals/b10-scheduler-safety-matrix.html" title="Pick where the recipe runs and what it handles; read its reach, cost and the actions that must stay forbidden" loading="lazy"></iframe></div>

Predict first: which runners can see `trip.yaml`? Then tap each and read the trip-forms verdict.

**Phone:** which of your Routines read a folder with personal data? Those move to a local task or to you.
**Laptop:** a Local routine running `/trip-forms --dry-run`, Run now, "always allow" for Python: you will see the map printed and no file written.

## Rules of thumb

- Run anything that reads your details locally or by hand; give cloud clocks only repositories.
- Dry-run and diff before any write; write to a dated output folder, never over a master.
- Put the never-silently list in `SKILL.md` and hook the items that have already bitten you.

## Retrieval

??? question "Why is a cloud routine the wrong runner for trip-forms?"
    It clones a repository fresh and sees nothing else; the data file is outside every repository.

??? question "What does `--permission-prompts none` change in an unattended run?"
    Anything that would have waited for you is denied and not retried; the run fails instead of hanging.

??? question "Name four things the recipe must never do silently."
    Any four of: overwrite a master, write outside out\, submit, seal, invent a value, read another data file, change the map, use the network, skip the oracle.

## Sources

- [Scheduled tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks){ .src data-checked="2026-09-28" }: 5 min.
- [Automate work with routines](https://code.claude.com/docs/en/routines){ .src data-checked="2026-09-28" }: 8 min.
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork){ .src data-checked="2026-09-28" }: 4 min.
- [Codex: scheduled tasks](https://learn.chatgpt.com/docs/automations.md){ .src data-checked="2026-09-28" }: 3 min.

## Ledger prompt

> In **Automation recipes**: where each recipe runs and its never-silently list, hooks marked.

**Next:** the apply task: build `trip-forms`, run it in both tools, watch the oracle reject a missing field, record the minutes saved.
