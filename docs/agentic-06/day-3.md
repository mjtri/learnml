---
title: B6 · Lesson 3 · Citation verification is its own pass
terms: [citation verification]
playbook: research
---

# B6 · Lesson 3 · Citation verification is its own pass

<p class="recall" markdown>**Previously:** Projects hold the standing instructions (TM template, reviewer-response table, KR↔EN glossary), and the plan's training policy decides where an unpublished draft may live.</p>

## Idea

**Citation verification** is a separate pass, run by a script, after drafting, before anything reaches a document. Separate, because the session that wrote a reference is its worst judge (doer/grader). A script, because a DOI lookup is deterministic and free, while a model "checking" a reference by reading it is one more guess. It catches the reference with a real author, a real venue and an identifier that resolves elsewhere.

## How it works

**What a lookup is.** `api.crossref.org/works/<DOI>` returns the record or a 404; no sign-up, and `mailto=` puts you in the polite pool ([Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/){ .src data-checked="2026-09-27" }). `export.arxiv.org/api/query?id_list=<arXiv ID>` returns one entry, or none ([arXiv API](https://info.arxiv.org/help/api/basics.html){ .src data-checked="2026-09-27" }).

**Three verdicts.** Resolves and matches: keep. Resolves but differs: the model fused two papers; search the title once, fix the identifier, re-run. Nothing returned: invented; drop.

**Pattern tells** triage before the network: a DOI prefix that names one publisher (`10.1145` ACM, `10.1109` IEEE, `10.1038` Nature) on a venue from another; an arXiv month above 12; an arXiv year later than the paper's; suspiciously round serials. A passed pattern proves nothing; a failed one saves a lookup.

**Why the vendors agree.** OpenAI says Deep Research cites "so you can verify the information" ([deep research](https://help.openai.com/en/articles/10500283-deep-research-faq){ .src data-checked="2026-09-27" }). Anthropic graded its own Research system on "citation accuracy (do the cited sources match the claims?)", a criterion that exists because it fails ([multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system){ .src data-checked="2026-09-27" }).

**Who runs it.** Claude Code or Codex runs `verify_refs.py` and edits `refs.md` from its output, in a session that did not produce the list. The model helps only with `differs` cases, one title search each; the loop ends on the script's verdict, week 3's oracle habit.

**In practice.** 26 references from Lesson 1: the script prints 19 `ok`, 4 `differs`, 3 `missing`. Per tool, Deep Research 15 of 18 verified, Claude Research 11 of 14. Only `refs-verified.md` enters the TM Project; the counts go in the playbook.

## Try it

<div class="visual"><iframe src="../visuals/b6-citation-check.html" title="Sort reference cards by real or suspicious identifier patterns" loading="lazy"></iframe></div>

Predict first: which tells catch a fake without a lookup, and which card passes every pattern yet still needs one?

**Phone:** open your Deep Research report, pick three references, and search each title in the browser. Count how many resolve.
**Laptop:** in Claude Code: "Goal: write `verify_refs.py`: for each `identifier | title | year | tools` line of `refs.md`, look the DOI up on Crossref or the arXiv ID on the arXiv API and print `ok`, `differs` or `missing`. Done when `10.1038/221963a0` prints `ok` and `10.1145/9999999.9999999` prints `missing`." You will see the second fail with a 404, which is the point.

## Rules of thumb

- Verify with a lookup, never with a model reading the reference; a DOI resolves or it does not.
- Run the verify pass in a different session or tool from the one that produced the list.
- Give a `differs` reference one title search; drop it on the second failure.

## Retrieval

??? question "What are the three verdicts of a verify pass, and what happens to each?"
    Resolves and matches: keep. Resolves but differs: one title search, fix, re-run. Nothing returned: drop.

??? question "Why is the session that produced the reference list the wrong one to check it?"
    It grades its own work. A fresh session, ideally the other vendor, runs the script.

??? question "A reference passes every pattern tell. What do you know?"
    Only that a lookup is still needed; patterns reject fakes cheaply but never confirm one exists.

## Sources

- [Deep research in ChatGPT](https://help.openai.com/en/articles/10500283-deep-research-faq){ .src data-checked="2026-09-27" }: 5 min.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system){ .src data-checked="2026-09-27" }: 12 min.
- [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/){ .src data-checked="2026-09-27" }: 3 min.
- [arXiv API basics](https://info.arxiv.org/help/api/basics.html){ .src data-checked="2026-09-27" }: 4 min.

## Ledger prompt

> In **Research**: your verify counts per tool from the apply task, and the pattern tell that caught the most fakes.

**Next:** the apply task: one sensory-substitution question in both tools, one verified union, one number per tool.
