---
title: "B6 · Lesson 2 · Drafting in Projects: TM reports, reviewer responses, KR↔EN"
terms: [Projects, project instructions, record mode, TM report template, reviewer response, KR↔EN glossary]
playbook: research
---

# B6 · Lesson 2 · Drafting in Projects: TM reports, reviewer responses, KR↔EN

<p class="recall" markdown>**Previously:** a literature review is four fixed stages (search in both tools, dedupe, verify, summarise), and a research mode runs once per question.</p>

## Idea

Drafting waste is re-explaining: the TM format, the journal's tone, which Korean term is which English one, every new chat. **Projects** hold that once, as **project instructions** plus a few files, so each chat starts briefed. Worse: an unpublished result drafted in a chat that may train the model.

## How it works

**ChatGPT Projects.** Instructions "apply only within that project and override your global custom instructions". Business projects hold up to 40 files. Project-only memory keeps chats from referencing anything outside the project; shared projects are always project-only. Paid plans may include Deep Research inside ([Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt){ .src data-checked="2026-09-27" }).

**Claude Projects.** Instructions apply to every chat in the project; knowledge files expand "by up to 10x" with retrieval on paid plans ([what are projects](https://support.claude.com/en/articles/9517075-what-are-projects){ .src data-checked="2026-09-28" }); each project has "its own separate memory space" ([memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context){ .src data-checked="2026-09-27" }). Sharing is Team and Enterprise only ([projects](https://support.claude.com/en/articles/9517075-what-are-projects){ .src data-checked="2026-09-28" }).

**Which plan holds the draft.** Business: "No training on your business data by default" ([pricing](https://learn.chatgpt.com/docs/pricing){ .src data-checked="2026-09-27" }). Max: chats train Claude when Model Improvement is on in Privacy Settings; incognito chats never ([training policy](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training){ .src data-checked="2026-09-27" }).

**Record mode**, the ChatGPT macOS app transcribing a meeting into notes, is macOS-only, so on this Windows laptop it stays a test, not a given ([ChatGPT Record](https://help.openai.com/en/articles/11487532-chatgpt-record){ .src data-checked="2026-09-27" }).

**Three Projects, one template each.** The **TM report template** is an instructions block:

```
Role: ETRI researcher writing a Technical Memo (TM) for an internal review board.
Language: Korean body; English for figure labels, code and cited titles. Translate
terms only from glossary.md; flag any term missing from it with [용어?].
Sections, in this order: 개요, 배경 및 목적, 방법, 결과, 고찰, 향후 계획, 참고문헌.
Numbers: copy from the notes or tables I give you; never estimate a result.
References: only items from refs-verified.md; anything else is written as [verify].
Length: 2 pages; bullets over prose in 방법 and 결과.
Ask before writing if a section has no source material.
```

A **reviewer response** is a workflow: (1) the review goes in as a file; (2) ask for a table `comment · our change · where · status`; (3) draft each reply from the table, never from memory; (4) the other tool reads the letter against the review and lists unanswered comments (week 4's doer/grader rule). The **KR↔EN glossary** is a 30-row table (`한국어 · English · never as`) in project knowledge; the language line above points at it.

**In practice.** TM due Friday: Project "TM reports" holds the block above, last year's TM and `glossary.md`. One chat: "Draft the Q3 haptic-encoding TM from notes.md." Sections arrive in order, in Korean, with `[verify]` on every unchecked reference.

## Try it

<div class="visual"><iframe src="../visuals/b6-project-instructions.html" title="Assemble project instructions and read their size" loading="lazy"></iframe></div>

Predict first: instructions ride along on every turn; how many words before they outweigh the section you asked for?

**Phone:** in the ChatGPT app, New project › paste the TM block from the builder › Project settings › project-only memory.
**Laptop:** make a Claude Project with the same block, `glossary.md` and one past TM. Ask both tools for the 방법 section from the same `notes.md`; score each 1–5. You will see which tool keeps section order and glossary terms without a reminder.

## Rules of thumb

- Put format, audience and language rules in project instructions; put examples and glossaries in project files.
- Draft unpublished results only in a Business project or with Model Improvement off; never in a personal chat that trains.
- Answer reviewers from a comment table, then let the other tool check that every comment got a reply.

## Retrieval

??? question "How far do ChatGPT project instructions reach, and what does project-only memory add?"
    Only inside that project, overriding global custom instructions; project-only memory keeps chats inside and outside apart.

??? question "Where may an unpublished result be drafted on your two plans?"
    In a ChatGPT Business project (no training by default), or in Claude with Model Improvement off or an incognito chat.

??? question "Name the four steps of the reviewer-response workflow, and who does the last one?"
    Review in as a file; a comment table; replies drafted from the table; the other tool reads the letter against the review and lists unanswered comments.

## Sources

- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt){ .src data-checked="2026-09-27" }: 8 min.
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects){ .src data-checked="2026-09-28" }: 3 min.
- [ChatGPT Record](https://help.openai.com/en/articles/11487532-chatgpt-record){ .src data-checked="2026-09-27" }: 4 min.
- [Is my data used for model training?](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training){ .src data-checked="2026-09-27" }: 3 min.

## Ledger prompt

> In **Research**: the instructions block your TM Project uses, and which tool kept the format without reminders (1–5).

**Next:** the verify pass: every reference looked up by identifier before it enters a document.
