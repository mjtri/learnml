---
title: B8 · Lesson 2 · Budgets and escape hatches: credits, fast mode, resets, seats
terms: [budget rule, seat type, spend limit]
playbook: budget
---

# B8 · Lesson 2 · Budgets and escape hatches: credits, fast mode, resets, seats

<p class="recall" markdown>**Previously:** a usage report is six numbers written down once a week; `/usage` and `/insights` read Claude, `/status` and `/usage weekly` read Codex.</p>

## Idea

A meter alone changes nothing. A **budget rule** is a written trigger and action, "when this meter passes this number, do that", with the source that says the action works. Each hatch has its own price; the waste is grabbing the nearest one at the wall.

## How it works

**Claude, four hatches.** Usage credits bill "at standard API rates" once the plan is spent, under a monthly cap you set; prepaid bundles cut that rate up to 30 % ([usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans){ .src data-checked="2026-09-28" }, [usage bundles](https://support.claude.com/en/articles/14246112-buy-usage-bundles){ .src data-checked="2026-09-28" }). That cap is your **spend limit**, shown as a credits row in `/usage`; at a limit `/rate-limit-options` can wait and continue after the reset ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }). Fast mode is Opus "up to 2.5x faster" at $8/$40 per MTok on Opus 5.5, credits only; the first fast turn re-bills the whole conversation: a session-start decision ([fast mode](https://code.claude.com/docs/en/fast-mode){ .src data-checked="2026-09-28" }). A limit reset is free and occasional; its "Reset for free" button "isn't currently available" in Claude Code, only in Settings › Usage ([limit reset](https://support.claude.com/en/articles/17007452-what-is-a-limit-reset){ .src data-checked="2026-09-28" }).

**ChatGPT Business, three.** The **seat type** decides the allowance. Premium has 5x the usage of Standard, no 5-hour limit and a weekly reset, at $125 a month or $100 billed annually; only a workspace owner switches a member's seat ([Premium seats](https://openai.com/index/premium-seats-chatgpt-business/){ .src data-checked="2026-09-28" }, [seat types](https://help.openai.com/en/articles/8542216-managing-members-seat-types-and-roles-in-chatgpt-business){ .src data-checked="2026-09-28" }). Workspace credits take over once the seat's allowance is spent; owners or admins set a monthly credit limit per seat type or per user, none by default ([credits and spend controls](https://help.openai.com/en/articles/20001155-managing-credits-and-spend-controls-in-chatgpt-business){ .src data-checked="2026-09-28" }). The paid instant weekly reset is Plus and Pro only, "not available on ... Business" ([paid resets](https://help.openai.com/en/articles/20001507-paid-weekly-work-and-codex-rate-limit-resets){ .src data-checked="2026-09-28" }).

**The rule shape.** Meter, threshold, action, evidence: "When the Claude weekly bar passes 70 %, mechanical edits go to Sonnet; costs page." Then check the action can work: switching model does nothing against the weekly limit.

**In practice.** TM deadline, Claude weekly at 90 % on Wednesday: draft in ChatGPT, a separate pool, credits off. If the code fix must ship tonight, credits on under a $20 spend limit; never fast mode for an unattended run.

## Try it

<div class="visual"><iframe src="../visuals/b8-budget-rule.html" title="Build a budget rule and check whether its action can work" loading="lazy"></iframe></div>

Predict first: which actions fail against the Claude weekly cap?

**Phone:** claude.ai › Settings › Usage: is a limit reset offered, are credits on, is a spend limit set? ChatGPT app: your seat type.
**Laptop:** `/usage-credits`, set a spend limit you can afford, then `/usage`: you will see the credits row appear at 0 % under that limit.

## Rules of thumb

- Write each hatch as a budget rule with a threshold before you need it, never at the wall.
- Turn on usage credits only under a monthly spend limit; decide fast mode at session start or not at all.
- Ask for a Premium seat when the 5-hour window, not the weekly cap, is what stops Codex work.

## Retrieval

??? question "Name three things about fast mode that decide when to turn it on."
    Credits only, never the plan; Opus only, up to 2.5x faster at a higher price; the first fast turn re-bills the whole conversation.

??? question "What can a free limit reset do, and from where?"
    Restore a 5-hour or weekly limit once, from Settings › Usage on web or desktop; not from Claude Code, and not undone.

??? question "Your Codex weekly allowance is spent on a Business seat. List the options in order of cost."
    Wait for the weekly reset; workspace credits under the seat-type limit; a Premium seat. No paid instant reset exists on Business.

## Sources

- [Fast mode](https://code.claude.com/docs/en/fast-mode){ .src data-checked="2026-09-28" }: 5 min.
- [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans){ .src data-checked="2026-09-28" }: 3 min.
- [ChatGPT Business models and limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits){ .src data-checked="2026-09-28" }: 4 min.
- [Managing credits and spend controls in ChatGPT Business](https://help.openai.com/en/articles/20001155-managing-credits-and-spend-controls-in-chatgpt-business){ .src data-checked="2026-09-28" }: 3 min.

## Ledger prompt

> In **Budget**: two budget rules, one per tool, as meter · threshold · action · source, and the spend limit you set.

**Next:** the weekly review: fifteen minutes that turn the meters into a pruned playbook.
