---
title: B8 · Lesson 3 · The weekly review and the playbook v1
terms: [weekly review, playbook v1]
playbook: weekly review
---

# B8 · Lesson 3 · The weekly review and the playbook v1

<p class="recall" markdown>**Previously:** a budget rule is meter, threshold, action and source; credits, fast mode, resets and seat types are hatches with different prices.</p>

## Idea

The **weekly review** is fifteen minutes at the same slot each week, in which the usage report and the week's logs change the playbook: one rule added or edited, one rule without evidence deleted. **Playbook v1** is the first full pass: at most 20 rules, each with a source or a measurement, installed as global instructions in both tools. A rule that lives only on a web page does nothing on a Tuesday evening.

## How it works

**The ritual, in order.** (1) Usage report line into the **Weekly review** section. (2) The week's `track.py` notes and CHANGELOG failed-approach bullets: did a rule fail, did a missing rule cost a session? (3) Every rule needs a link or a number; one with neither gets a measurement scheduled for next week, or goes. (4) Monthly, `python gen_refresh.py` re-checks stamped claims; changes go to the changelog. (5) If a rule changed, re-install.

**Where the rules go.** Claude reads `~/.claude/CLAUDE.md` for "personal preferences for all projects", and user rules load before project rules, "neither set overrides the other". Target "under 200 lines" ([memory](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-28" }). Codex reads `~/.codex/AGENTS.md` first, "only the first non-empty file at this level", then project files from the Git root down, up to 32 KiB combined ([AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md){ .src data-checked="2026-09-28" }). Instruction tokens "are present even when you're doing unrelated work" ([costs](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }), so both global files hold the same imperatives only; evidence and dates stay in `playbook.md`.

**What survives pruning.** A rule an apply-task measurement backs, or one an official page states (the ten starter rules). Merge duplicates: "check `/usage` first" and "Sonnet past 70 %" are one budget rule.

**In practice.** After week 6 the playbook had 10 starter rules and 14 ledger lines. Pruned: starter rules 4 and 5 merged into one context rule; three research lines became "verify by identifier before a reference enters a document"; two lines with no number deleted. Sixteen rules, 31 lines, the same file in both homes.

## Try it

<div class="visual"><iframe src="../visuals/b8-playbook-pruner.html" title="Tag each rule with its evidence and see how many survive" loading="lazy"></iframe></div>

Predict first: of the fourteen rules, how many have evidence today? Tag them, then read what the installed file would weigh.

**Phone:** open the playbook page, read the Budget section, mark each line "link", "number" or "neither" in a note. The "neither" lines are the apply task's first deletions.
**Laptop:** `type $HOME\.claude\CLAUDE.md` and `type $HOME\.codex\AGENTS.md`: you will see whether anything global loads today.

## Rules of thumb

- Review at the same weekly slot; end with one rule changed and the usage report line written.
- Install imperatives only in the two global files; keep evidence and dates in the playbook.
- Delete a rule with neither a link nor a number after one review; re-add it when it earns one.

## Retrieval

??? question "In what order do user and project instruction files load in each tool, and who wins a conflict?"
    Claude: the user file before project files, neither overrides, so keep them consistent. Codex: the global file first, then Git root down; later files override because they appear later.

??? question "What makes a rule survive the prune?"
    A source link or a measured number. A rule with neither is scheduled for a measurement or deleted.

??? question "Why not install the whole playbook page as the global file?"
    Instruction tokens load at every session start even for unrelated work. Evidence and stamps belong in the ledger; the imperatives, under 200 lines, in the global files.

## Sources

- [How Claude remembers your project](https://code.claude.com/docs/en/memory){ .src data-checked="2026-09-28" }: user file, size target, 6 min.
- [AGENTS.md in Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md){ .src data-checked="2026-09-28" }: global file, 32 KiB, 3 min.
- [Manage costs effectively](https://code.claude.com/docs/en/costs){ .src data-checked="2026-09-28" }: 2 min.

## Ledger prompt

> In **Weekly review**: the date of your first review slot and the count "rules kept / deleted / scheduled for measurement".

**Next:** the apply task: prune to at most 20 evidenced rules, install both global files, log the first weekly review.
