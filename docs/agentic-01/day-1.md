---
title: B1 · Lesson 1 · An agent is a loop; context is the budget
terms: [agent, context window, token, tool call, compaction, prompt cache, subagent, CLAUDE.md, AGENTS.md, playbook]
playbook: budget
---

# B1 · Lesson 1 · An agent is a loop; context is the budget

<p class="recall" markdown>**Previously:** nothing. **Why this track:** you already use Claude Code and Codex; the waste is in how the loop underneath them gets fed.</p>

## Idea

Every **agent** you use is the same machine: a model reads everything in its **context window**, makes one **tool call**, the result is pasted back into the window, and it goes round again. That window is the budget. Every file it reads, every command output, every "no, I meant…" stays there until the session ends, and each turn re-reads all of it. Waste is not "too many messages"; waste is a bloated window read over and over.

## How it works

The window fills from four sources:

1. **Instructions**: `CLAUDE.md` / `AGENTS.md`, loaded every turn. Keep it under about 200 lines; every line is paid for on every turn ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }).
2. **Your messages**: cheap in **tokens**; a vague one triggers a long exploration.
3. **Tool results**: the big one. A 2,000-line file, a full test log, a web page.
4. **The agent's own reasoning and edits.**

Near the limit, Claude Code runs **compaction**: it summarises the conversation and continues from the summary. Detail is lost, so *choose* when (`/compact <what to keep>`) rather than let it fire mid-task.

Two levers keep it small. A **subagent** does a bounded job in its own fresh window and returns only a summary ([best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }). And `/clear` starts a new window when a task is done; stacking a task on a finished one is the commonest silent waste.

One cost is invisible in the transcript: the **prompt cache**. The already-processed prefix of a conversation is reused cheaply, but it expires after idle time: one hour on a subscription, five minutes on usage credits. Come back after lunch and the whole history is reprocessed at full price ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }). Codex runs the same loop; OpenAI likewise says to keep durable rules in `AGENTS.md`, out of the chat ([Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }).

**In practice.** Unity: "migrate every `HapticController` call to the new API." Asked directly, the agent opens a dozen files in full; half the window is soon code it will never edit. Asked as "use a subagent to list call sites with line numbers, then edit only those", the window holds a 30-line list plus the edits. Same result, a fraction of the usage.

## Try it

<div class="visual"><iframe src="../visuals/b1-context-budget.html" title="Fill a context window and watch what each action costs" loading="lazy"></iframe></div>

Predict first: how many "read a big file" actions fit before compaction? Does a subagent hand-off change the bar? What does idling cost?

**Phone:** Claude app → Code tab → any past session; count the tool results you never needed. Put the number in your **playbook** under *Budget*.
**Laptop:** run `/context` ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }) at the start and end of one real task; note which of the four fillers was largest.

## Rules of thumb

- Start a new session (`/clear`) for each new task; never stack a task on a finished one.
- Send searches and long outputs to a subagent; keep only summaries in the main window.
- Compact on purpose (`/compact keep the failing test and the plan`) before the tool does it for you.

## Retrieval

??? question "Name the four things that fill an agent's context window, and which one you control least."
    Instructions, your messages, tool results, and the agent's own reasoning. Tool results are the least controlled and usually the largest.

??? question "What does compaction do, and why is triggering it yourself better than letting it fire?"
    It replaces the conversation with a summary. Doing it yourself lets you say what to keep; automatic compaction can drop the detail you needed.

??? question "You return to a large session after a 90-minute break. What happens to cost on the next turn, and why?"
    The prompt cache has expired (one hour on a subscription), so the whole history is reprocessed at full price.

## Sources

- [Manage costs effectively](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }: 6 min.
- [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents){ .src data-checked="2026-09-27" }: 12 min.
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }: 5 min.

## Ledger prompt

> In **Budget**: the one habit you will start tomorrow, and your phone count.

**Next:** what Max 20x and Business actually give you, side by side.
