---
title: B2 · Lesson 1 · One instruction file, read by both tools
terms: [instruction file, "@import", rules directory, precedence, size cap]
playbook: instructions
---

# B2 · Lesson 1 · One instruction file, read by both tools

<p class="recall" markdown>**Previously:** an agent is a loop over a finite context; two subscriptions are two rolling allowances with meters; where a task runs and who verifies it picks the tool.</p>

## Idea

An **instruction file** is the part of the context you write once and pay for on every turn. Both tools load it at session start: the cheapest place to stop a repeated mistake, the most expensive place to be verbose. Waste has two shapes: two drifting files, or one long file whose rule was buried under forty others. This lesson: where each tool looks, and what "nearest wins" promises.

## How it works

**Claude Code** loads `CLAUDE.md` from the working directory and every directory above it, plus `~/.claude/CLAUDE.md`; subdirectory files load on first read there. With an `AGENTS.md` and no `CLAUDE.md` on that path, it reads `AGENTS.md` directly (v2.1.277 or later); with both, `CLAUDE.md` only. The shared setup: a `CLAUDE.md` whose first line is the **@import** `@AGENTS.md`; imports may nest four hops deep ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }).

**Codex** reads `~/.codex/AGENTS.md`, then one `AGENTS.md` per directory from the git root down to the working directory ([AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md){ .src data-checked="2026-09-27" }).

**Precedence.** Both tools join what they find; nothing is replaced. The nearest file is read last, and that is all **precedence** promises: between conflicting lines Claude "may pick one arbitrarily" ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }), and Codex's nearer file "overrides" only because it comes later ([AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md){ .src data-checked="2026-09-27" }). Delete the old line instead of adding a louder one.

**Size.** Codex stops adding files once the combined text reaches its **size cap**, 32 KiB by default ([AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md){ .src data-checked="2026-09-27" }). Claude has no byte cap: a 200-line target per file, a warning past it, files over 4 MiB skipped ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }).
**Rules directory.** Claude's `.claude/rules/*.md` is a **rules directory** of topic files; with a `paths:` line, one loads only when matching files open ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }). Codex's `.codex/rules/` governs shell commands, not instructions ([Codex rules](https://learn.chatgpt.com/docs/agent-configuration/rules.md){ .src data-checked="2026-09-27" }).

**In practice.** This repo: `CLAUDE.md` is `@AGENTS.md` plus three Claude-only lines; `AGENTS.md` holds commands, layout and rules, nothing about lesson format, which is read from `LESSON_FORMAT.md` only when needed.

## Try it

<div class="visual"><iframe src="../visuals/b2-instruction-precedence.html" title="Tap a folder to launch from it and see which instruction files load, in what order" loading="lazy"></iframe></div>

Predict first: launched from `Assets/`, how many files load, and which is read last? Then switch to Codex.

**Phone:** in the Claude app's Code tab, ask a repo session which instruction files it loaded and how long each is.
**Laptop:** `/context` in Claude Code lists *Memory files*; ask Codex to quote the first heading of the instructions it loaded. You will see whether `AGENTS.md` loaded once, twice, or not at all.

## Rules of thumb

- Keep one `AGENTS.md`; make `CLAUDE.md` an `@AGENTS.md` line plus Claude-only rules, never a copy.
- Add a line only when the agent makes the same mistake twice; cut any line it gets right from the code.
- When a rule concerns one folder, use `.claude/rules/` with `paths:` (Claude) or a subdirectory `AGENTS.md` (Codex).

## Retrieval

??? question "Your repo has both AGENTS.md and CLAUDE.md. Which does Claude Code read, and how do you get both?"
    CLAUDE.md only. Put `@AGENTS.md` on its first line; the import never loads the file twice.

??? question "What does 'nearest file wins' actually guarantee?"
    Only that the nearest file is read last. Files are joined, not replaced, so either tool may follow either conflicting line.

??? question "Codex stops loading instruction files at what size, and what is Claude Code's equivalent?"
    32 KiB combined by default. Claude has no byte cap: a 200-line target per file; files over 4 MiB are skipped.

## Sources

- [How Claude remembers your project](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }: 10 min.
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md){ .src data-checked="2026-09-27" }: 3 min.
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" } and [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }: 4 min.

## Ledger prompt

> In **Instructions**: one line to delete from this repo's `AGENTS.md`, one to add, and the mistake that earned it.

**Next:** plan first: plan mode, `/plan`, and the four-part prompt shape.
