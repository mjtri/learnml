---
title: B3 · Apply · A Stop hook for this repo, a compile oracle for Unity
playbook: verification
---

# B3 · Apply · A Stop hook for this repo, a compile oracle for Unity

<p class="recall" markdown>**This week in one sentence:** an oracle the agent can run closes the loop; a permission mode picks who stops a bad action; a hook makes a rule hold on every turn, in both tools.</p>

**Laptop · ~60 min · in the build session, before the Colab notebook.**

## Goal

Leave with (1) one script that blocks "done" in both tools while `check_lessons.py` fails, (2) the Unity batch-mode compile as an oracle, (3) two measured playbook lines.

## Steps

1. **The script (10 min).** Save as `.claude/hooks/stop_check.py`; plain Python, so both tools can run it:
   ```python
   import json, os, pathlib, subprocess, sys
   inp = json.load(sys.stdin)                     # what the tool tells the hook
   root = pathlib.Path(__file__).resolve().parents[2]
   r = subprocess.run([sys.executable, "check_lessons.py"], cwd=root, capture_output=True, text=True)
   if r.returncode == 0:
       sys.exit(0)                                # clean: the agent may stop
   if inp.get("stop_hook_active") and "CLAUDE_PROJECT_DIR" not in os.environ:
       sys.exit(0)                                # Codex: one forced retry, then let it stop
   errs = [l for l in r.stdout.splitlines() if l.startswith("ERROR")]
   print("check_lessons.py failed; fix these before reporting done:", *errs[:12], sep="\n", file=sys.stderr)
   sys.exit(2)                                    # 2 = do not stop; stderr becomes the next instruction
   ```
   Test: `'{}' | python .claude/hooks/stop_check.py`; `$LASTEXITCODE` is `0`. Delete a retrieval question from `docs/agentic-03/day-1.md`, run again: `2` plus the `ERROR` line. Restore with `git checkout -- docs/agentic-03/day-1.md`.
2. **Claude Code (10 min).** Add to `.claude/settings.json`:
   ```json
   {
     "hooks": {
       "Stop": [ { "hooks": [ {
         "type": "command",
         "command": "python \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/stop_check.py",
         "timeout": 120
       } ] } ]
     }
   }
   ```
   `/hooks` shows it under `Stop`. In accept-edits mode: `Delete the third retrieval question in docs/agentic-03/day-2.md, then report done.` You will see Claude try to stop, get the `ERROR` line as its next instruction, and restore the question. Record minutes, `/usage` before and after, a 1–5 quality score.
3. **Codex (10 min).** Add `.codex/hooks.json`:
   ```json
   {
     "hooks": {
       "Stop": [ { "hooks": [ {
         "type": "command",
         "command": "python \"$(git rev-parse --show-toplevel)\"/.claude/hooks/stop_check.py",
         "commandWindows": "python .claude/hooks/stop_check.py",
         "timeout": 120
       } ] } ]
     }
   }
   ```
   Trust the folder if asked; `/hooks`; same prompt; same three numbers (ChatGPT counter). If Codex stops after one forced retry, that is the script's guard: Codex documents no block cap.
4. **Unity (20 min).** Editor closed. Run the Lesson 1 command against your XR project; note exit code and minutes. In that project's `AGENTS.md`, put the command under a "Done when" line: exit 0, no `error CS` in the log. Ask the agent for a small change (rename a serialized field) and let it prove the compile passed.
5. **Deny rule (5 min).** Put `{"permissions": {"deny": ["Bash(git push *)"]}}` in `.claude/settings.local.json` (add that path to `.gitignore` if `git status` lists it). Local on purpose: week 5's scheduled cloud run clones the repo and pushes its own branch. `/permissions` shows the rule with its source file.

## Done when

- `/hooks` lists the `Stop` hook in both tools, pointing at the same `stop_check.py`.
- The bad-edit prompt cannot end with a broken lesson in either tool: you saw the block message.
- The Unity exit code and the minutes per compile are in the playbook.
- `python check_lessons.py` passes and `git status` shows only the files you meant to add.

## Log it

```bash
python track.py done agentic-03/apply --rating 3 --minutes 60 --note "which tool fixed the broken lesson faster, and the Unity compile time"
```

## Ledger prompt

> In **Verification**: the comparison line ("hook block: Claude 6 min / 4 % / 4; Codex 8 min / 5 msgs / 3") and the Unity compile time, the cost of one iteration.
