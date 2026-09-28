---
title: "B9 · Apply · Five scores, three files, two installs, two radar rows"
playbook: tools
---

# B9 · Apply · Five scores, three files, two installs, two radar rows

<p class="recall" markdown>**This week in one sentence:** add-ons come in seven layers, each with a place to run and a price per turn; star-history finds candidates, the six-line rubric decides, the three security files are read before any install, and a measured A/B week decides keep or drop.</p>

**Laptop · ~60 min · in the build session.**

## Goal

Leave with five scores, the three files of two repositories read, two tools installed at user scope with one measured task each, a **Tools** section in the playbook and two rows in the [radar](../agentic/radar.md).

## Steps

1. **Charts (10 min).** star-history.com: the *Weekly* tab, then `/compare/ai-coding-tool` and `/compare/document-to-markdown`. Pick five (start: superpowers, mattpocock/skills, ECC, kordoc, document-skills); score each with the lesson 2 visual, six numbers and a total.
2. **Three files (10 min).** Worked examples, one line each:
   ```
   Invoke-WebRequest https://raw.githubusercontent.com/affaan-m/ECC/main/hooks/hooks.json -OutFile ecc-hooks.json
   Invoke-WebRequest https://raw.githubusercontent.com/affaan-m/ECC/main/.mcp.json -OutFile ecc-mcp.json
   Select-String -Path ecc-hooks.json -Pattern '"command"' | Measure-Object
   git clone --depth 1 https://github.com/mattpocock/skills.git mp-skills
   Get-ChildItem mp-skills -Force -Name
   Select-String -Path mp-skills\skills\*\SKILL.md -Pattern 'allowed-tools'
   ```
   Note the hook count, the `.mcp.json` server, and whether the three files exist in the second repository.
3. **Install two (10 min).** Your two highest: one method pack (never both) and one document tool. Shell installs default to user scope.
   ```
   claude plugin install superpowers@claude-plugins-official
   claude plugin marketplace add anthropics/skills
   claude plugin install document-skills@anthropic-agent-skills
   claude plugin list
   ```
   Alternatives:
   ```
   claude plugin install mattpocock-skills@claude-plugins-official
   npx -y kordoc setup
   npx skills@latest add mattpocock/skills
   ```
   The last is Codex; superpowers uses its Plugins sidebar.
4. **One real task each (20 min).** `/usage` first. Unity project: `/superpowers:brainstorm` (or `/grill-with-docs`) for the next haptic-cue feature until a spec file exists. A copy of an ETRI form: "Fill `form-copy.docx` from `trip.md`; list every field you could not fill." `/usage` again; per task: minutes, usage delta, quality 1–5. Time left: the same task in Codex with `$skill-name`, `/usage weekly` before and after.
5. **Playbook and radar (10 min).** Add a **Tools** section with the three-file rule and both A/B lines; add two radar rows in its table format.

## Done when

- Scratch note: five totals; for two repositories, hook count, `.mcp.json` server, `allowed-tools` findings.
- `claude plugin list` shows exactly two new plugins at `Scope: user`.
- Playbook **Tools** section: two lines with minutes, usage delta, quality; radar: two new dated rows.

## Log it

```bash
python track.py done agentic-09/apply --rating 3 --minutes 60 --note "which two you installed, their scores, and the first A/B numbers"
```

**Next:** B10 turns these tools into automation recipes for monthly paperwork.

## Ledger prompt

> In **Tools**: "read three files before install" as the rule, then "superpowers: with 22 min / 6 % / 4; without 31 min / 5 % / 3" and the same line for the document tool.
