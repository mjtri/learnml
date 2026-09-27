---
title: B2 · Lesson 2 · Plan first, then the four-part prompt
terms: [four-part prompt, /plan, opusplan]
playbook: instructions
---

# B2 · Lesson 2 · Plan first, then the four-part prompt

<p class="recall" markdown>**Previously:** one instruction file, read by both tools; files are joined and the nearest is read last; 32 KiB (Codex) and 200 lines (Claude) are the ceilings.</p>

## Idea

The most expensive turn in a session is the first one after a vague prompt: the agent guesses the goal, explores widely, edits the wrong thing, and every correction after that stays in the window. Two habits cut it: let the agent read and propose before it edits, and write the prompt in a shape that leaves nothing to guess.

## How it works

**Plan mode, Claude Code.** Claude reads files and runs exploratory commands but does not edit until you approve the plan. Enter with `Shift+Tab`, prefix one prompt with **`/plan`**, or start `claude --permission-mode plan`; `Ctrl+G` opens the plan in your editor; approving switches the session to the permission mode you pick ([permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" }). **`opusplan`** (`/model opusplan`) uses Opus while planning and Sonnet for execution ([model config](https://code.claude.com/docs/en/model-config){ .src data-checked="2026-09-27" }): the costly model thinks, the cheaper one types. The counterweight: planning has overhead, and "if you could describe the diff in one sentence, skip the plan" ([best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }).

**Plan mode, Codex.** `/plan` or `Shift+Tab` toggles it; Codex gathers context, asks clarifying questions and builds a plan before implementing ([Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }). OpenAI publishes no automatic model switch like opusplan; pick the model by hand.

**The four-part prompt.** OpenAI's recommended default ([Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }); it maps onto Anthropic's "be specific" table ([best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }). A **four-part prompt** states:

- **Goal**: what changes or gets built.
- **Context**: which files, docs and examples matter; `@`-mention them in either tool.
- **Constraints**: standards, safety, what must not change.
- **Done when**: what must be true before it stops; the oracle from week B1.

Each part you leave out is a guess the agent makes for you, and a wrong guess costs a round trip of context.

**In practice.** Before: "fix the haptic stutter". After: "Goal: stop `HapticController` dropping pulses at 90 Hz. Context: `Assets/Scripts/Haptics/`, the failing PlayMode test `Pulse90HzTest`. Constraints: public API unchanged, no new packages. Done when: that test passes and the 60 Hz test still does." In plan mode the first reply names the files it will touch; you correct one line of a plan, not ten of code.

## Try it

<div class="visual"><iframe src="../visuals/b2-prompt-shape.html" title="Add Goal, Context, Constraints and Done-when to a vague prompt and watch the guesses disappear" loading="lazy"></iframe></div>

Predict first: with only a Goal, how many things must the agent guess? Which part removes the most?

**Phone:** find your last vague prompt in either app and write its four-part version in a note.
**Laptop:** run that prompt in Claude Code with `/plan` and `/model opusplan`. You will see the files it intends to touch before any edit exists; note `/usage` before and after.

## Rules of thumb

- Default to plan mode for anything touching more than one file; skip it when you could describe the diff in one sentence.
- Never send a prompt without a Done-when; if you cannot write one, the task is not ready for an agent.
- Use opusplan when the plan is the hard part and the edits are mechanical.

## Retrieval

??? question "What can Claude Code do in plan mode, and what stays blocked?"
    Read files, run exploratory commands and write a plan. Edits stay blocked until you approve the plan or leave plan mode.

??? question "Name the four parts of the prompt shape and the one an agent can never invent for you."
    Goal, Context, Constraints, Done when. Done when: without your oracle it can only guess that it has finished.

??? question "What does opusplan change, and what does Codex offer instead?"
    Opus plans, then Sonnet executes. Codex has plan mode but no published automatic switch; you choose the model.

## Sources

- [Permission modes](https://code.claude.com/docs/en/permission-modes){ .src data-checked="2026-09-27" }: 3 min.
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }: 8 min.
- [Model configuration](https://code.claude.com/docs/en/model-config){ .src data-checked="2026-09-27" }: 2 min.
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" } and [Codex prompting](https://learn.chatgpt.com/docs/prompting.md){ .src data-checked="2026-09-27" }: 5 min.

## Ledger prompt

> In **Instructions**: your plan-mode rule (when on, when skipped) and your four-part template as one line.

**Next:** memory, instructions and context: what belongs where.
