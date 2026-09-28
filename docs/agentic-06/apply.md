---
title: B6 · Apply · One question, two tools, one verified reference list
playbook: research
---

# B6 · Apply · One question, two tools, one verified reference list

<p class="recall" markdown>**This week in one sentence:** a literature review is search in both tools, dedupe, a scripted citation verification and only then a summary; Projects hold the standing instructions (TM template, reviewer-response table, KR↔EN glossary); and the plan's training policy decides where an unpublished draft may live.</p>

**Laptop · ~60 min · in the build session; start both research runs first.**

## Goal

Leave with (1) a repeatable pipeline in `research/<question>/`, (2) a verified fraction per tool in the playbook, (3) a TM Project with its instructions block and `glossary.md`.

## Steps

1. **Meters (3 min).** `/usage`, the ChatGPT counter and its Deep Research tasks remaining.
2. **Two reports (5 min).** Export the two Lesson 1 runs as Markdown (`dr.md`, `cr.md`). If you skipped that task, start both now, same wording: "For vision-to-touch substitution, what spatial resolution do electrotactile and vibrotactile displays reach, and how was it measured? Peer-reviewed sources 2010–2026." Deep Research with sites restricted to `arxiv.org, dl.acm.org, ieeexplore.ieee.org`; Claude `+ › Research`. Note both start times.
3. **The script (10 min).** The Lesson 3 laptop prompt, or paste this as `verify_refs.py`:
   ```python
   import json, re, sys, urllib.request
   for line in open(sys.argv[1], encoding="utf-8"):
       ident = line.split("|")[0].strip(); doi = ident.startswith("10.")
       if not ident: continue
       url = "https://api.crossref.org/works/" + ident if doi else "https://export.arxiv.org/api/query?id_list=" + ident
       try:
           body = urllib.request.urlopen(url, timeout=20).read().decode()
           t = json.loads(body)["message"]["title"][0] if doi else re.findall(r"<title>(.*?)</title>", body, re.S)[1]
           t = " ".join(t.split())
           print("ok     " if t.lower()[:25] in line.lower() else "differs", ident, "|", t[:70])
       except Exception: print("missing", ident)
   ```
   Oracle: `10.1038/221963a0 | Vision substitution by tactile image projection | 1969 | test` prints `ok`; `10.1145/9999999.9999999 | x | 2024 | test` prints `missing`.
4. **Union (10 min).** Claude Code: "Goal: build `refs.md` from `dr.md` and `cr.md`, one `identifier | title | year | tools` line per reference. Done when: no identifier appears twice and each line names every tool that found it." Note each run's minutes.
5. **Verify (15 min).** `python verify_refs.py refs.md > verdicts.txt`. Hand `differs` lines to Codex (the other vendor): one title search each, corrected identifier or `drop`; re-run. Count per tool: offered, `ok`, `missing`.
6. **Project (10 min).** Create the "TM reports" Project (Lesson 2 block, `glossary.md`, one past TM) and add `refs-verified.md`, the `ok` lines only. Ask for the 참고문헌 section.
7. **Meters (2 min).** `/usage` and the ChatGPT counter again.

## Done when

- `refs-verified.md` contains only `ok` lines, and `verdicts.txt` shows the per-tool counts.
- The playbook's **Research** section has both verified fractions, run times and usage deltas.
- The TM Project exists with its block and `glossary.md`.

## Log it

```bash
python track.py done agentic-06/apply --rating 3 --minutes 60 --note "verified fraction per tool and which run cost more"
```

## Ledger prompt

> In **Research**: the comparison line ("resolution question: Deep Research 18 offered / 15 ok / 12 min / 1 task; Claude 14 / 11 / 6 min / 9 %") and the rule it suggests.
