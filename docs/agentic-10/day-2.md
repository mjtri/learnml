---
title: "B10 · Lesson 2 · Documents you actually file: docx, xlsx, LaTeX, HWP and HWPX"
terms: [field map, HWPX, python-hwpx, pyhwpx, latexmk, pandoc]
playbook: automation
---

# B10 · Lesson 2 · Documents you actually file: docx, xlsx, LaTeX, HWP and HWPX

<p class="recall" markdown>**Previously:** a personal automation is five parts (data file, template, skill, oracle, trigger); it pays when the layout is fixed and only the facts change.</p>

## Idea

Each format you file has one honest route from the data file to a filled document and one way to check it. What survives across formats is the **field map**: a table from `trip.yaml` keys to the cell, placeholder or macro each format uses. Get the map right once; the rest is plumbing.

## How it works

Setup and oracle lines, one per line:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin marketplace add chrisryugj/kordoc
codex mcp add kordoc -- npx -y kordoc mcp
python -m pip install python-hwpx==6.6.0
winget install --source winget --exact --id JohnMacFarlane.Pandoc   # optional
latexmk -g -pdf -halt-on-error -interaction=nonstopmode report.tex
```

**docx and xlsx.** The docx, pdf, pptx and xlsx skills are source-available, "for demonstration and educational purposes only" ([anthropics/skills](https://github.com/anthropics/skills){ .src data-checked="2026-09-28" }), so run them on copies. The skill writes a filled copy; `check.py` reads it back with python-docx (label left, value right) or openpyxl.

**LaTeX.** The skill writes `fields.tex` as `\newcommand` lines; `report.tex` does `\input{fields.tex}` and never changes. **latexmk** reruns LaTeX until references settle ([latexmk](https://www.cantab.net/users/johncollins/latexmk/)) (unverified). Tested (4.88): stale PDF, `fields.tex` deleted: "Nothing to do", exit 0; `-g` forces a run and the missing file exits 12. **pandoc** (optional) converts Markdown to docx or LaTeX; not installed here.**pandoc** converts the same Markdown to docx or LaTeX (`--reference-doc` borrows office styles) ([manual](https://pandoc.org/MANUAL.html)) (unverified; not installed here).

**HWP and HWPX, three ways.** **HWPX** is Hancom's open zip-of-XML format; `.hwp` is the older closed binary.

1. **python-hwpx** 6.6.0, Apache-2.0, pure Python, no Hancom ([PyPI](https://pypi.org/project/python-hwpx/)) (unverified). Tested here: `fill_by_path` with `"Name > right"` paths filled 3 labels of 3 and read back (code below). Opens `.hwp`, says PyPI (untested). One maintainer: pin the version.
2. kordoc 4.15.7, MIT, Node ([README](https://github.com/chrisryugj/kordoc)) (unverified): reads HWP and HWPX to Markdown; `fill` with `-f 'Name=Kim'` fills by label-value patterns, after `--dry-run`. On the same template it found 1 label of 3 and still wrote a file after "매칭 실패". Plugin and MCP server: lines above.
3. **pyhwpx** 1.7.2 drives an installed Hancom Office through COM, Windows only, writes true `.hwp`, opens the Hancom window ([PyPI](https://pypi.org/project/pyhwpx/)) (unverified; untested here). Hancom 2024 was on the reference machine: the fallback when `.hwp` is demanded.

**Master and diff.** Convert master and output to Markdown with kordoc (`--keep-empty-cols`), then `git diff --no-index a.md b.md`. python-hwpx's `doc_diff` sees paragraphs only; kordoc's diff is an MCP tool, not a CLI command.

**In practice.** The ETRI trip request is a `.hwp`: open it once in Hancom, save as `.hwpx`, keep that as the master; pyhwpx waits until someone rejects an `.hwpx`.

## Try it

<div class="visual"><iframe src="../visuals/b10-field-mapper.html" title="Map trip.yaml keys onto the cells of three formats; unmapped cells light up and check.py reports the gaps" loading="lazy"></iframe></div>

Predict first: after the office renames one cell, how many outputs fail? Then press the rename button.

**Phone:** open your last filed trip request; write its cell labels in order. That is column one of your field map.
**Laptop:** run the lines below on any `.hwpx` with a labelled table: you will see `applied 2 failed []` and the value read back.

```python
from hwpx import HwpxDocument
doc = HwpxDocument.open("master.hwpx")
res = doc.tables.fill_by_path({"Name > right": "Hong Gildong",
                               "Destination > right": "Daejeon"})
print("applied", res["applied_count"], "failed", res["failed"])
assert not res["failed"]
doc.save_to_path("filled.hwpx")
back = HwpxDocument.open("filled.hwpx").tables.all[0]
print(back.cell(1, 1).text)
```

## Rules of thumb

- Fill HWPX by label with python-hwpx pinned; use kordoc to read and diff, only after `--dry-run`.
- Compile with `latexmk -g -halt-on-error` and test the exit code; a PDF on disk proves nothing.
- Keep one `.hwpx` master per form and diff master against output before anything leaves the folder.

## Retrieval

??? question "Why is `-g` part of the latexmk oracle command?"
    Without it latexmk can say "Nothing to do" and exit 0 on a stale PDF, even with an input file missing.

??? question "Which HWP route needs Hancom Office, and what do you get for it?"
    pyhwpx, through COM on Windows: true `.hwp` output.

??? question "kordoc fill wrote a file after 매칭 실패. What catches it?"
    check.py reads the output back by label and exits non-zero on the empty cell.

## Sources

- [anthropics/skills README](https://github.com/anthropics/skills){ .src data-checked="2026-09-28" }: licence, disclaimer, 3 min.
- [python-hwpx on PyPI](https://pypi.org/project/python-hwpx/) (unverified): `fill_by_path`, 5 min.
- [kordoc README](https://github.com/chrisryugj/kordoc) (unverified): `fill`, `--dry-run`, 6 min.
- [latexmk](https://www.cantab.net/users/johncollins/latexmk/) (unverified): 4.88, `-g`, 3 min.

## Ledger prompt

> In **Automation**: the field map of one real form (key → cell label) and which route fills it.

**Next:** unattended runs: which clock may touch your details, dry run and diff before overwrite, the never-silently list.
