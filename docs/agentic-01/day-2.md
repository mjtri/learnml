---
title: B1 · Lesson 2 · What you actually pay for
terms: [usage window, weekly cap, usage pool, usage credits, fast mode, limit reset, Max plan, ChatGPT Business, Premium seat, effort level]
playbook: budget
---

# B1 · Lesson 2 · What you actually pay for

<p class="recall" markdown>**Previously:** an agent is a loop over a finite context window; tool results fill it fastest, subagents and `/clear` keep it small.</p>

## Idea

Both subscriptions sell the same thing: a rolling allowance that refills on a clock. Waste is spending it on the wrong model, at the wrong time, in the wrong tool, then hitting the wall mid-task. Today: the shape of each allowance and where the meters are.

## How it works

**Claude Max 20x.** One **usage pool** is shared across Claude chat and Claude Code ([Pro/Max with Claude Code](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan){ .src data-checked="2026-09-27" }). It refills in 5-hour **usage windows**, under a **weekly cap** across all models that resets at a fixed time per account ([Max plan](https://support.claude.com/en/articles/11049741-what-is-the-max-plan){ .src data-checked="2026-09-27" }). Opus and Sonnet also have model-specific limits: when "you've hit your Opus limit", `/model sonnet` keeps you working; when the shared window itself is spent, nothing does ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }). The meter is `/usage`: window and weekly bars, plus what spent them. Escape hatches: **usage credits** (pay-as-you-go via `/usage-credits`, with an optional cap) and an occasional free **limit reset** in Settings › Usage ([limit reset](https://support.claude.com/en/articles/17007452-what-is-a-limit-reset){ .src data-checked="2026-09-27" }). **Fast mode** is billed only from credits, never from the plan ([fast mode](https://code.claude.com/docs/en/fast-mode){ .src data-checked="2026-09-27" }). Spend also scales with the **effort level**; `low` suits mechanical edits ([model config](https://code.claude.com/docs/en/model-config){ .src data-checked="2026-09-27" }).

**ChatGPT Business.** A Standard seat also runs on 5-hour windows, and weekly limits may apply too. Codex and ChatGPT Work share one allowance; the published table is per model (roughly 5–45 messages per 5 hours on the top model, 250–2,000 on the lightest), and OpenAI calls those estimates, not fixed limits. Business data is not used for training by default ([pricing](https://learn.chatgpt.com/docs/pricing){ .src data-checked="2026-09-28" }). Deep Research and agent-mode allowances are not published; the in-product counter is the meter.

A **Premium seat** gives 5× the usage with no 5-hour window (weekly reset), at $100/user/month annually or $125 monthly; seats can be mixed and reassigned ([models and limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits){ .src data-checked="2026-09-28" }).

**In practice.** Reviewer response due tonight, Claude weekly cap at 85 %: draft the reply in ChatGPT (separate pool) and keep Claude Code for the code fix that needs the repo. Nothing waits for a reset.

## Try it

<div class="visual"><iframe src="../visuals/b1-usage-windows.html" title="Simulate a week of usage windows and caps" loading="lazy"></iframe></div>

Predict first: with your usual pattern (two evenings + a weekend build), do you hit the weekly cap before a window? Then move the build session to Sonnet.

**Phone:** open claude.ai → Settings › Usage, and the ChatGPT app's usage counter. Screenshot both: your baseline for the apply task.
**Laptop:** run `/usage` before and after a 10-minute task; note which attribution item moved the bar most.

## Rules of thumb

- Check `/usage` at the start of every laptop session; switch to Sonnet when the Opus bar passes about 70 %.
- Put separate-pool work (drafting, literature search) in ChatGPT so the Claude cap goes only to repo work.
- Never leave fast mode on by habit; it is a credits-only spend for the rare "I need it now" moment.

## Retrieval

??? question "What shares one usage pool on Claude Max, and when does switching model help?"
    Claude chat and Claude Code share it. Switching helps only against a model-specific (Opus or Sonnet) limit, not when the shared window or weekly cap is spent.

??? question "Fast mode is on and your plan window is empty. What happens to the bill?"
    Fast mode never draws on the plan; it is billed from usage credits only, so it keeps working and costs money.

??? question "Name two things about ChatGPT Business limits you can only learn from the product itself."
    The exact Deep Research and agent-mode allowances, and where you are in the 5-hour window: OpenAI publishes ranges, not counts.

## Sources

- [What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan){ .src data-checked="2026-09-27" }: 3 min.
- [Manage costs effectively](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-27" }: `/usage`, credits, model pools, 6 min.
- [Fast mode](https://code.claude.com/docs/en/fast-mode){ .src data-checked="2026-09-27" }: 2 min.
- [ChatGPT Business pricing](https://learn.chatgpt.com/docs/pricing){ .src data-checked="2026-09-28" }: seats, shared pool, training policy, 4 min.

## Ledger prompt

> In **Budget**: your two baseline numbers (Claude weekly %, ChatGPT counter) and the model you will default to for mechanical edits.

**Next:** which tool for which job, first cut.
