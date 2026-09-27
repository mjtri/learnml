---
title: B1 · Lesson 3 · Which tool for which job, v1
terms: [Codex, Codex cloud, Deep Research, cloud session, Remote Control, Codex Remote, oracle, plan mode, permission mode, sandbox]
playbook: budget
---

# B1 · Lesson 3 · Which tool for which job, v1

<p class="recall" markdown>**Previously:** two rolling allowances on two clocks; `/usage` and the ChatGPT counter are the meters.</p>

## Idea

"Which is better, Claude Code or Codex?" is the wrong question; you have both, on separate pools. Ask three questions about the *task*: where does it run (your machine, a cloud copy of the repo, no repo), who verifies it (a test, or you reading), and how much context it needs (one file, a project, the open web). Answer those and the tool usually picks itself. Later weeks replace opinions with your measurements.

## How it works

**Where it runs.** Claude Code and the **Codex** CLI both run on your machine, next to your Unity install. Both have cloud forms: **Codex cloud** works on an isolated copy of the repo and ends in a pull request ([Codex cloud](https://learn.chatgpt.com/docs/cloud.md){ .src data-checked="2026-09-27" }); a Claude **cloud session** does the same from claude.ai/code or the mobile app ([overview](https://code.claude.com/docs/en/overview){ .src data-checked="2026-09-27" }). Editor, headset or local data → local; self-contained → cloud.

**Who verifies.** With an **oracle** (tests, a compile, `check_lessons.py`) either agent can be left alone. If the verifier is you, keep the task short enough that you will actually read the output.

**The phone.** **Remote Control** drives a Claude Code session on your laptop from the Claude app; execution stays local ([remote control](https://code.claude.com/docs/en/remote-control){ .src data-checked="2026-09-27" }). **Codex Remote** does the same from the ChatGPT app, you approving each action; the computer must stay awake ([Codex Remote](https://learn.chatgpt.com/docs/remote.md){ .src data-checked="2026-09-27" }). Claude's app cannot select bypass mode, nor auto mode over Remote Control ([mobile](https://code.claude.com/docs/en/mobile){ .src data-checked="2026-09-27" }).

**Safety defaults.** Claude Code sets a **permission mode** per session, including **plan mode** for approve-first work ([permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" }); Codex pairs an OS-level **sandbox** with an approval policy ([sandboxing](https://learn.chatgpt.com/docs/sandboxing){ .src data-checked="2026-09-27" }).

**No repo.** Literature search is **Deep Research** territory in ChatGPT, or Claude's research features; verify every citation before it enters a document (week B6).

**In practice.** "Haptic pulse stutters at 90 Hz" → local (editor, headset), Claude Code in plan mode. "Add unit tests to `SonifierUtils`" → self-contained with an oracle, Codex cloud, review the PR later. "Rewrite reviewer 2's response" → no repo, you verify, a ChatGPT Project.

## Try it

<div class="visual"><iframe src="../visuals/b1-tool-picker.html" title="Pick a task and see which tool the three questions point to" loading="lazy"></iframe></div>

Predict first, then tap through your real next three tasks: does the picker agree with your instinct? Each disagreement is a candidate for the apply task's comparison.

**Phone:** write your next three tasks in the playbook under *Budget*, tagged local / cloud / no-repo and oracle / me.
**Laptop:** start one self-contained task in Codex cloud and one in Claude Code locally; the one you forget about belonged in the cloud.

## Rules of thumb

- Editor, headset or local data → local agent; self-contained with a test → cloud task; no repo → chat.
- If you are the only verifier, keep the task small enough that you will actually read the output.
- Start non-trivial local tasks in plan mode (Claude) or sandboxed (Codex); loosen per repo, not per mood.

## Retrieval

??? question "What three questions about a task decide the tool, before any opinion about the tools?"
    Where it runs (local, cloud copy, no repo), who verifies it (test vs you), and how much context it needs (file, project, web).

??? question "A Unity build fix and a docs typo fix arrive together. Where does each go, and why?"
    The build fix stays local (needs the editor); the typo fix is a self-contained cloud task ending in a PR.

??? question "What is the same about Remote Control and Codex Remote, and what is one limit of each?"
    Both drive an agent on your own machine from the phone. Codex Remote needs the computer awake; Claude's app cannot select bypass mode.

## Sources

- [Claude Code on mobile](https://code.claude.com/docs/en/mobile){ .src data-checked="2026-09-27" }: 4 min.
- [Codex cloud](https://learn.chatgpt.com/docs/cloud.md){ .src data-checked="2026-09-27" } and [Codex Remote](https://learn.chatgpt.com/docs/remote.md){ .src data-checked="2026-09-27" }: 5 min.
- [Permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" } and [Codex sandboxing](https://learn.chatgpt.com/docs/sandboxing){ .src data-checked="2026-09-27" }: skim.
- Opinion: [Claude Code and Codex together](https://codex.danielvaughan.com/2026/03/27/using-claude-code-and-codex-together/) (unverified).

## Ledger prompt

> In **Budget**: your three tagged tasks, and one rule the picker did not have.

**Next:** the apply task in the build session: an instruction file for this repo, and the same task in both tools, measured.
