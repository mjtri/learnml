---
title: B6 · Lesson 1 · Literature review: search, dedupe, verify, summarise
terms: [literature review pipeline, MCP, DOI, arXiv ID]
playbook: research
---

# B6 · Lesson 1 · Literature review: search, dedupe, verify, summarise

<p class="recall" markdown>**Previously:** three clocks can fire an agent turn nobody watches, the phone only drives a process that runs elsewhere, and automation pays only for a boring manual workflow whose cost per run you can name.</p>

## Idea

A **literature review pipeline** is four fixed stages: search in both tools, dedupe the union, verify every reference, summarise only what survived. It prevents the fluent report whose references half-exist, pasted into a paper. Both research modes cite; neither promises a citation resolves. Research modes are expensive, so each question gets one run per tool.

## How it works

**ChatGPT Deep Research.** Start it with `/Deepresearch` or the tools menu. It proposes a plan you can edit before it runs. `Sites › Manage sites` restricts research to the domains you list, or prioritises them. The report cites its sources and downloads as Markdown, Word or PDF. Usage varies by plan; the in-product counter shows remaining tasks, and monthly allowances reset 30 days from first use ([deep research](https://help.openai.com/en/articles/10500283-deep-research-faq){ .src data-checked="2026-09-27" }). OpenAI publishes no number for Business seats.

**Claude Research.** Paid plans; web search must be on; start from `+ › Research`. It searches the web and connected sources, and is "subject to the same limits as standard Claude conversations" but spends them faster ([research](https://support.claude.com/en/articles/11088861-using-research-on-claude-ai){ .src data-checked="2026-09-27" }). Underneath, a lead agent spawns subagents and a citation agent attributes claims; agents use about 4× the tokens of chat, multi-agent runs about 15× ([multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system){ .src data-checked="2026-09-27" }). Attribution is not existence.

**Connectors.** Both apps accept a remote **MCP** server as a custom connector: Claude under Customize › Connectors ([custom connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp){ .src data-checked="2026-09-27" }), ChatGPT Business only through an admin's developer mode ([developer mode](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt){ .src data-checked="2026-09-27" }). In the terminal, `claude mcp add --transport http <name> <url>`; connector output is context, so Claude Code warns above 10,000 tokens and caps at 25,000 by default ([MCP](https://code.claude.com/docs/en/mcp){ .src data-checked="2026-09-27" }). Codex: `codex mcp add` ([Codex MCP](https://learn.chatgpt.com/codex/extend/mcp){ .src data-checked="2026-09-27" }).

**In practice.** "Which sensory-substitution encodings preserve spatial resolution best?" Deep Research restricted to arxiv.org, dl.acm.org and ieeexplore.ieee.org; Claude Research too; both reference lists into one file, a **DOI** or **arXiv ID** per line. The verify pass is Lesson 3; nothing enters a Projects workspace before it.

## Try it

<div class="visual"><iframe src="../visuals/b6-lit-review-pipeline.html" title="Step through a literature review pipeline and watch the counts" loading="lazy"></iframe></div>

Predict first: two tools find 18 and 14 references; how many reach the summary if a fifth fail verification?

**Phone:** in the ChatGPT app, start one Deep Research on your question with sites restricted to publishers, and edit the plan it proposes. In the Claude app, `+ › Research` with the same question.
**Laptop:** paste both reference lists into `research/<question>/refs.md`, one line each (`identifier · title · year · tool`), then in Claude Code: "Goal: dedupe refs.md by identifier. Done when: none appears twice and each line names every tool that found it." You will see a union larger than either list, with a small overlap.

## Rules of thumb

- Restrict Deep Research to publisher domains when you need references, not opinions.
- Run a research mode once per question; ask follow-ups in normal chat, which costs far less.
- Never paste a research report into a Projects workspace; paste only the verified reference list.

## Retrieval

??? question "What can you change about a Deep Research run before and during it?"
    Edit the plan first, restrict or prioritise sites, interrupt to refocus, change which sources it may use.

??? question "Why does Claude Research drain a usage window faster than chat, and by roughly how much?"
    A lead agent, subagents and a citation agent run; agents use about 4× chat's tokens, multi-agent runs about 15×.

??? question "A citation agent attached a source to every claim. What is still unproven?"
    That the paper exists and says that. Only a lookup by DOI or arXiv ID proves it: Lesson 3.

## Sources

- [Deep research in ChatGPT](https://help.openai.com/en/articles/10500283-deep-research-faq){ .src data-checked="2026-09-27" }: 5 min.
- [Use research on Claude](https://support.claude.com/en/articles/11088861-using-research-on-claude-ai){ .src data-checked="2026-09-27" }: 2 min.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system){ .src data-checked="2026-09-27" }: 12 min.
- [Claude Code MCP](https://code.claude.com/docs/en/mcp){ .src data-checked="2026-09-27" }: 4 min.

## Ledger prompt

> In **Research**: which tool found more references, how long each run took, and what each cost.

**Next:** the drafting side: Projects, standing instructions, TM reports, reviewer responses.
