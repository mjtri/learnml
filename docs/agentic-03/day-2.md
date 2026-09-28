---
title: "B3 · Lesson 2 · Permission modes and sandboxes: what each one risks"
terms: [accept-edits mode, auto mode, bypass mode, dontAsk, allowlist, approval policy]
playbook: verification
---

# B3 · Lesson 2 · Permission modes and sandboxes: what each one risks

<p class="recall" markdown>**Previously:** an oracle is a check the agent can run itself; name it in the prompt, ask for evidence.</p>

## Idea

A permission mode is not a trust dial; it answers one question: *who stops a bad action?* You, a classifier, an allowlist, the OS, or nobody. Pick the stopper per repo; loosen only where an oracle plus git catch what it used to.

## How it works

**Claude Code**, what runs without asking: Manual (setting value `default`; no longer the starting mode): reads only. **Accept-edits mode**: reads, file edits, simple file commands (`mkdir`, `mv`, `cp`); other commands and the network prompt. Plan mode: reads, exploratory commands and a plan. **Auto mode**: everything; a separate classifier reviews each action instead of you, and after 3 blocks in a row or 20 in total prompting resumes. The starting mode on v2.1.283 or later. **dontAsk**: anything that would prompt is denied. **Bypass mode** (`--dangerously-skip-permissions`): everything, "no protection against prompt injection"; isolated containers and VMs only ([permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" }).

Rules sit on top: an **allowlist** entry such as `Bash(npm run *)` pre-approves a pattern; a `deny` rule such as `Bash(git push *)` blocks in every mode, bypass included; deny beats ask beats allow. Rules are enforced by Claude Code, not the model: a `CLAUDE.md` sentence grants nothing ([permissions](https://code.claude.com/docs/en/permissions){ .src data-checked="2026-09-27" }). The Bash sandbox (an OS fence around files and network) runs on macOS, Linux and WSL2 only ([sandboxing](https://code.claude.com/docs/en/sandboxing){ .src data-checked="2026-09-27" }): on native Windows the stoppers are mode, classifier and rules.

**Codex** splits the question in two. `sandbox_mode` says what a command can touch (`read-only`, `workspace-write`, `danger-full-access`), enforced by the OS ([Codex sandboxing](https://learn.chatgpt.com/docs/sandboxing){ .src data-checked="2026-09-27" }, [Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox.md){ .src data-checked="2026-09-27" }). The **approval policy** says when it asks: `on-request` asks only to step outside the sandbox; `never` asks nothing. The default "Auto" for a git folder, `workspace-write` plus `on-request`, runs edits inside the repo and routine commands; the network and writes outside ask ([approvals](https://learn.chatgpt.com/docs/agent-approvals-security.md){ .src data-checked="2026-09-27" }). Full access (`danger-full-access` plus `never`) is Codex's bypass; `/permissions` switches.

**In practice.** A task starts in plan mode (week 2); these modes are what it runs in once you approve. LearnML has an oracle and git: auto mode or Codex's Auto, plus deny rules for `git push` and generated files. The XR project, whose `Library/` takes twenty minutes to rebuild: accept-edits, never bypass; Codex's default would run `Remove-Item -Recurse Library` unasked; git is the only undo.

## Try it

<div class="visual"><iframe src="../visuals/b3-permission-risk-matrix.html" title="Tap a permission mode and see which actions run without asking" loading="lazy"></iframe></div>

Predict first: how many of six run unasked in accept-edits mode and in Codex's default?

**Phone:** the Claude app's Remote Control offers only Manual, Accept edits and Plan, never Auto or Bypass ([permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" }); note the laptop session's real mode.
**Laptop:** `/permissions` in both CLIs; note the settings. Put `{"permissions": {"deny": ["Bash(git push *)", "Edit(docs/index.md)"]}}` in `.claude/settings.local.json`, reopen `/permissions`: you will see each rule with the file it came from.

## Rules of thumb

- Pick the stopper per repo: oracle plus git → auto mode or Codex's Auto; no oracle → accept-edits or plan mode.
- Put every "never" in a deny rule, not in `AGENTS.md`: rules are enforced, instructions are advisory.
- Bypass mode or Codex full access only in a throwaway container or VM, never on the laptop with your headset drivers.

## Retrieval

??? question "Name the stopper in each Claude Code mode: Manual, auto, dontAsk, bypass."
    You; the classifier (you again after 3 blocks in a row or 20 total); the allowlist; nobody, only deny rules survive.

??? question "Codex's default for a git folder: which two settings, and what still asks?"
    `workspace-write` plus `on-request`; the network and writes outside the workspace.

??? question "Where does a rule you must never break go, and why?"
    A deny rule: enforced in every mode, bypass included; instructions are advisory.

## Sources

- [Permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" } and [permission rules](https://code.claude.com/docs/en/permissions){ .src data-checked="2026-09-27" }: 10 min.
- [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing){ .src data-checked="2026-09-27" }: skim.
- [Codex sandboxing](https://learn.chatgpt.com/docs/sandboxing){ .src data-checked="2026-09-27" }, [approvals](https://learn.chatgpt.com/docs/agent-approvals-security.md){ .src data-checked="2026-09-27" } and [Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox.md){ .src data-checked="2026-09-27" }: 8 min.

## Ledger prompt

> In **Verification**: mode and rules per repo (LearnML, XR, paperwork), and your deny rule.

**Next:** hooks: rules the tool itself enforces on every turn, in both tools.
