---
title: "B2 · Lesson 3 · Memory, instructions, context: what goes where"
terms: [auto memory]
playbook: instructions
---

# B2 · Lesson 3 · Memory, instructions, context: what goes where

<p class="recall" markdown>**Previously:** plan mode lets the agent read and propose before it edits; a Goal / Context / Constraints / Done-when prompt leaves it nothing to guess.</p>

## Idea

Three places hold what the agent knows: the conversation (this session only), the instruction file (every session, written by you) and memory (every session, written by the agent). A fact in the wrong place is lost at `/clear`, paid for on every turn, or applied when unwanted. Sort by two questions: who writes it, and must it always apply?

## How it works

**Auto memory, Claude Code.** On by default. Claude saves four kinds of note into `~/.claude/projects/<project>/memory/`: your role and preferences, corrections, project decisions not derivable from the code, and where to find things. The first 200 lines or 25 KB of the `MEMORY.md` index load every session. It skips what `CLAUDE.md` already says or the code shows. **Auto memory** is machine-local and shared across every checkout of the project, so a cloud session starts without it. `/memory` browses and toggles it; "remember X" lands in memory, "add this to CLAUDE.md" lands in instructions ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }).

**Memories, Codex.** Local memories live under `~/.codex/memories/`, generated once a chat has been idle. Enable them in Settings › Personalization or `config.toml`; `/memories` sets per-chat use. OpenAI's own framing: a "helpful recall layer", not "the only source for rules that must always apply" ([Codex memories](https://learn.chatgpt.com/docs/customization/memories.md){ .src data-checked="2026-09-27" }).

**Instructions versus memory.** Both load every session; both are context, not enforced configuration ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }). A rule that must always hold goes in the instruction file, where you can read and prune it; what the agent learned about you stays in memory. Anything that must happen every time needs an automatic mechanism (week B3).

**Context.** What was said in the session lives only there. The project-root `CLAUDE.md` survives `/compact`, re-read from disk; an instruction given only in conversation may not ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }). A correction typed twice is a candidate for the instruction file; a fact for this task only stays in the prompt.

**In practice.** ETRI TM report: "Korean headings, English abstract, the ETRI template" is a rule for every session, so it goes in the papers repo's `AGENTS.md`. "Prefers terse diffs, no emoji" is something Claude writes into auto memory by itself. "Reviewer 2 wants Fig. 3 on a log axis" belongs in this session's prompt and nowhere else.

## Try it

<div class="visual"><iframe src="../visuals/b2-memory-sorter.html" title="Sort eight facts into conversation, instruction file or memory and see what each tool does with them" loading="lazy"></iframe></div>

Predict first: which of the eight cards belong in memory? The readout says what each tool does with a misplaced fact.

**Phone:** in the Claude app, ask a Code session "what does auto memory say about me?"; anything stale is a laptop fix.
**Laptop:** run `/memory`, open the auto memory folder, delete one stale line, move one durable rule into `AGENTS.md`. You will see `MEMORY.md` is plain markdown, one line per memory.

## Rules of thumb

- Put a rule in the instruction file the second time you type it; leave preferences to auto memory and audit `/memory` monthly.
- Never rely on memory for a must-always-apply rule; both vendors call it recall, not enforcement.
- After `/compact`, re-state task-only constraints; only the root instruction file is re-read.

## Retrieval

??? question "Who writes each of the three stores, and which survive /clear?"
    Conversation: you and the agent, lost at /clear. Instruction file: you, persists. Auto memory: the agent, persists on that machine.

??? question "What loads from auto memory at session start, and where does it live?"
    The first 200 lines or 25 KB of MEMORY.md, under `~/.claude/projects/<project>/memory/`: machine-local, shared across every checkout of the project.

??? question "Where must a must-always-apply rule go, and why not memory?"
    In the instruction file. Both vendors say memory is a recall layer; neither tool enforces what it remembers.

## Sources

- [How Claude remembers your project](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-27" }: 6 min.
- [Codex memories](https://learn.chatgpt.com/docs/customization/memories.md){ .src data-checked="2026-09-27" }: 3 min.
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }: 2 min.

## Ledger prompt

> In **Instructions**: one line moved from memory into `AGENTS.md`, and one deleted from either.

**Next:** the apply task: an AGENTS.md the Unity project can build from, and one prompt rewritten and measured.
