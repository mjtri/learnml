---
title: B3 · Lesson 3 · Hooks: deterministic guard rails
terms: [hook]
playbook: verification
---

# B3 · Lesson 3 · Hooks: deterministic guard rails

<p class="recall" markdown>**Previously:** a mode picks who stops a bad action (you, a classifier, an allowlist, the OS, nobody); deny rules beat instructions.</p>

## Idea

An instruction file is advice; a crowded context skips lines. A Claude Code **hook** is a command the tool itself runs at a fixed moment (before a tool call, when the agent tries to stop), every time, no judgement involved. Anything that must hold with zero exceptions is a hook or a deny rule, not a sentence in `AGENTS.md`: "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic" ([best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }).

## How it works

**Claude Code.** A `hooks` block in `.claude/settings.json` or `~/.claude/settings.json`. Events: `PreToolUse` (can block the call), `PostToolUse`, `Stop` (whenever Claude finishes responding), `SessionStart`, and more. Shape: event → optional matcher (a tool name such as `Edit|Write`; `Stop` takes none) → commands, each with a `timeout` in seconds, default 600. The exit code is the decision: 0 proceeds; 2 blocks and stderr is the message: a `PreToolUse` call is refused and Claude reads why; on `Stop`, Claude keeps working with your text as its next instruction. `Stop` input includes `stop_hook_active`; after eight consecutive blocks without progress Claude Code overrides the hook ([hooks reference](https://code.claude.com/docs/en/hooks){ .src data-checked="2026-09-27" }, [hooks guide](https://code.claude.com/docs/en/hooks-guide){ .src data-checked="2026-09-27" }). On Windows shell-form commands run in Git Bash: put the logic in a Python script. `/hooks` lists them.

**Codex.** Same names (`PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`) in `.codex/hooks.json`, on by default; exit 2 plus stderr blocks, or on `Stop` gives the continuation reason; `stop_hook_active` exists too; `commandWindows` is the Windows override; `/hooks` inspects and trusts them ([Codex hooks](https://learn.chatgpt.com/docs/hooks){ .src data-checked="2026-09-27" }). An untrusted project skips its `.codex/` files ([config reference](https://learn.chatgpt.com/docs/config-file/config-reference.md){ .src data-checked="2026-09-27" }). One script serves both tools.

**In practice.** This repo: a `Stop` hook runs `check_lessons.py` and exits 2 with the `ERROR` lines, so the agent cannot say "done" with a broken lesson (the apply task). Unity: a `PreToolUse` hook on `Edit|Write` exiting 2 for paths under `Library/`. Paperwork: a `Stop` hook that greps a draft reply to reviewers for `TODO` placeholders.

## Try it

<div class="visual"><iframe src="../visuals/b3-hook-builder.html" title="Pick an event, a matcher and a command; read the JSON and what exit 2 does" loading="lazy"></iframe></div>

Predict first: for "never edit `docs/index.md`", which event, matcher and exit code? Then build it.

**Phone:** list three `AGENTS.md` rules you have watched an agent break; each is a hook candidate for the playbook's *Verification* section.
**Laptop:** the builder's block calls `.claude/hooks/protect_generated.py`, which does not exist yet: `New-Item -ItemType Directory -Force .claude\hooks`, then save this there:

```python
import json, sys
inp = json.load(sys.stdin)
path = inp.get("tool_input", {}).get("file_path", "")
if path.replace("\\", "/").endswith("docs/index.md"):
    print("docs/index.md is generated", file=sys.stderr)
    sys.exit(2)
```

Paste the block into `.claude/settings.json`, run `/hooks`, then ask Claude to "add a line to docs/index.md". You will see the tool call refused, with your reason in the transcript.

## Rules of thumb

- Convert any instruction the agent has ignored twice into a hook or a deny rule, then delete the sentence.
- Keep hooks narrow and fast: match one tool, exit 0 early; a slow `Stop` hook taxes every turn.
- Never install a hook you have not read; it runs with your permissions every time it fires.

## Retrieval

??? question "What do exit 0 and exit 2 mean for a PreToolUse hook, and for a Stop hook?"
    0: proceed. 2 on PreToolUse: the call is refused and Claude reads stderr. 2 on Stop: Claude keeps working, with stderr as its next instruction.

??? question "Why is 'always run the checker' a hook rather than an instruction?"
    The tool runs a hook every time; an instruction is advisory and can be skipped.

??? question "What stops a failing Stop hook looping forever in Claude Code, and which input field matters?"
    The override after eight consecutive blocks without progress; the script reads `stop_hook_active`.

## Sources

- [Hooks guide](https://code.claude.com/docs/en/hooks-guide){ .src data-checked="2026-09-27" }: 10 min; then the [hooks reference](https://code.claude.com/docs/en/hooks){ .src data-checked="2026-09-27" } for `Stop` and exit codes.
- [Codex hooks](https://learn.chatgpt.com/docs/hooks){ .src data-checked="2026-09-27" }: 6 min.
- [Best practices: set up hooks](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }: 1 min.

## Ledger prompt

> In **Verification**: the first `AGENTS.md` rule you turned into a hook, and the sentence you deleted.

**Next:** the apply task: one Stop hook that runs the checker in both tools, plus the Unity compile oracle.
