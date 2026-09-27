---
title: B4 · Lesson 2 · Worktrees and background agents: parallel without collisions
terms: [worktree, background agent, agent teams]
playbook: delegation
---

# B4 · Lesson 2 · Worktrees and background agents: parallel without collisions

<p class="recall" markdown>**Previously:** a subagent trades more total tokens for a small main window; a skill keeps instructions on disk until invoked.</p>

## Idea

Two agents editing one checkout overwrite each other silently. A **worktree** gives each agent its own copy of the files on its own branch, sharing the history, so parallel work becomes one merge you do on purpose instead of collisions you never see. Every parallel session is still a full context window, paid separately.

## How it works

**Worktrees.** `claude --worktree <name>` creates `.claude/worktrees/<name>/` on branch `worktree-<name>` and starts a session there; a second name is a second isolated session ([worktrees](https://code.claude.com/docs/en/worktrees){ .src data-checked="2026-09-27" }). A subagent whose definition says `isolation: worktree` always gets its own. Two details that bite: new worktrees branch from the *remote* default branch unless `worktree.baseRef` is `"head"`, and approvals granted inside a worktree are saved to the main checkout, except on Windows, where they stay with the worktree.

**Background agents.** `/bg` (or `claude --bg "<prompt>"`) moves a whole session off your screen; `claude agents` lists every background session and its state ([agent view](https://code.claude.com/docs/en/agent-view){ .src data-checked="2026-09-27" }). Before its first edit a **background agent** moves itself into a worktree, so parallel sessions read one checkout and each write to their own. Each spends your quota on its own.

**Agent teams.** **Agent teams** are the expensive end: a lead session spawns teammates that message each other and share a task list. Experimental, off unless `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, no worktree isolation between teammates, about 7× the tokens of one session when teammates run in plan mode ([agent teams](https://code.claude.com/docs/en/agent-teams){ .src data-checked="2026-09-27" }, [costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }).

**Codex.** The Codex app's "Worktree" option makes one per chat under `$CODEX_HOME/worktrees`, pruned to the most recent 15 by default ([Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees.md){ .src data-checked="2026-09-27" }).

**In practice.** This lesson was written by a subagent in a worktree, and it started one commit behind: `main` held an unpushed commit, and the worktree branched from the remote's default branch. Push first, or set `baseRef` to `head`. Unity is the other caveat: a fresh checkout rebuilds the ignored `Library/` folder on first open, slowly for a big XR project. Worktrees suit C# and docs; give the scene files one session.

## Try it

<div class="visual"><iframe src="../visuals/b4-worktree-parallel.html" title="Assign files to parallel sessions and count collisions with and without worktrees" loading="lazy"></iframe></div>

Predict first: three sessions, six files, two shared. How many silent overwrites without worktrees, how many merge conflicts with them, how many windows either way?

**Phone:** write your next two independent tasks and mark whether they touch the same files; that decides worktree or one session.
**Laptop:** `claude --worktree docs-fix` and `claude --worktree lint-fix` in two terminals, a small task each; then merge both branches: you will see two clean merges, or one honest conflict instead of a silent overwrite.

## Rules of thumb

- Run agents in parallel only when their tasks touch different files; otherwise queue them in one session.
- Push `main` (or set `worktree.baseRef` to `head`) before spawning worktree agents, so they start from your real state.
- Reach for agent teams only for review or research that gains from agents arguing; for edits, subagents in worktrees.

## Retrieval

??? question "What does a worktree share with the main checkout, and what is its own?"
    Shared: repository history and project-scope plugins. Its own: files, branch, a fresh checkout without ignored files.

??? question "Where does a background session write its edits, and why?"
    Into its own worktree under .claude/worktrees/, entered before its first edit, so parallel sessions never share a checkout.

??? question "Name three reasons agent teams are rarely right for a solo researcher."
    Experimental and off by default; no worktree isolation between teammates; about seven times the tokens of one session when they plan.

## Sources

- [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees){ .src data-checked="2026-09-27" }: 10 min.
- [Manage agents with agent view](https://code.claude.com/docs/en/agent-view){ .src data-checked="2026-09-27" }: 5 min.
- [Orchestrate agent teams](https://code.claude.com/docs/en/agent-teams){ .src data-checked="2026-09-27" }: the comparison table only.
- [Codex: Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees.md){ .src data-checked="2026-09-27" }: 3 min.

## Ledger prompt

> In **Delegation**: your rule for when a task gets its own worktree, and the `baseRef` setting you chose.

**Next:** the agent that wrote the change must not grade it: `/code-review`, ultrareview and a Codex adversarial review.
