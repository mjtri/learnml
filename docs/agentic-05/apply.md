---
title: B5 · Apply · One routine that checks and deploys, one lesson logged from the couch
playbook: automation
---

# B5 · Apply · One routine that checks and deploys, one lesson logged from the couch

<p class="recall" markdown>**This week in one sentence:** three clocks can fire an agent turn nobody watches, the phone only drives a process that runs elsewhere, and automation pays only for a boring manual workflow whose cost per run you can name.</p>

**Laptop · ~60 min · in the build session.**

## Goal

Leave with (1) a weekly cloud routine that runs the checker and strict build and opens a deployable PR, (2) its weekly usage cost, (3) one lesson logged from the phone through Remote Control.

## Steps

1. **Meters (2 min).** `/usage` and claude.ai/settings/usage; note the weekly bar and the remaining daily runs at claude.ai/code/routines.
2. **Manual run first (8 min).** In the repo, timing it:
   ```
   python check_lessons.py
   python build_today.py
   python -m mkdocs build --strict
   ```
   If a step needed a correction, stop here and fix the workflow, not the clock.
3. **The routine (20 min).** `git push` so `main` is on GitHub. Then `/schedule` and answer: weekly, Sunday 21:07, this repository, the Default environment with `pip install -r requirements.txt` as its setup script, nothing connected. Prompt:
   ```
   Run python check_lessons.py, python build_today.py and
   python -m mkdocs build --strict. If the checker fails, fix only what
   it names and rerun until clean. Commit changed files to the branch
   claude/weekly-refresh and open a PR titled "weekly refresh <date>"
   listing the checker's warnings and what you changed. Never push to
   main or gh-pages. If nothing changed, open no PR and say so.
   ```
   Click **Run now**; read the transcript, not the green dot. Merging the PR fires the deploy workflow, so merging from the phone is the deploy; the daily Action runs a script, the routine repairs what it flags. If `/schedule` is unavailable, create the same task as Desktop › Routines › New routine › Local, weekly, worktree on, ending "push to main": a desktop task has your git credentials.
4. **Cost (5 min).** claude.ai/settings/usage again: the delta is one run, once a week. Write it down.
5. **Phone (15 min).** In any `claude` session, `/config` → **Push when actions required** on; exit. Then `claude remote-control --name learnml`, space for the QR code, scan it. From the Claude app send:
   ```
   Run: python track.py done agentic-05/day-2 --rating 4 --minutes 15 --again --note "logged from the phone"
   Then show me the last line of progress/log.jsonl.
   ```
   Approve it from the phone. If Codex Remote is connected, ask it for `git status` on the same repo; note which felt faster.

## Done when

- claude.ai/code/routines lists the routine with a next run time; its first run produced a PR or an honest "nothing changed".
- The playbook's **Automation** section has the weekly cost line with a number.
- `progress/log.jsonl` has an `agentic-05/day-2` entry written from the phone.

## Log it

```
python track.py done agentic-05/apply --rating 3 --minutes 60 --note "usage per routine run; was the PR mergeable"
```

## Ledger prompt

> In **Automation**: "weekly refresh routine: <usage per run> per week, <minutes saved>, PR merged from phone yes/no" and the one rule it supports.
