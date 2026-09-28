---
title: "B10 · Lesson 1 · Anatomy of a personal automation: five parts, one payoff"
terms: [automation recipe, data file, form template]
playbook: automation recipes
---

# B10 · Lesson 1 · Anatomy of a personal automation: five parts, one payoff

<p class="recall" markdown>**Previously:** add-ons come in seven layers, each with a place to run and a price per turn; star-history finds candidates, the six-line rubric decides, the three security files are read before any install, and a measured A/B week decides keep or drop.</p>

## Idea

A trip request, a trip report, a TM cover sheet: the same twelve facts typed into three layouts. An **automation recipe** separates facts from layouts: a data file you edit, templates you replace, a skill mapping between them, an oracle that refuses a half-filled form, a trigger. Remove one part and a familiar failure returns.

## How it works

**Data file.** The **data file** is the only thing you type per run: `trip.yaml`, one key per fact, kept outside every repository because it holds your details.

**Template.** A **form template** is the form as the office issued it, cells empty: `request-master.hwpx`. Never edited by hand; when the office changes it, replace it and re-run.

**Skill.** The mapping, in prose plus a script: which key lands in which cell, how a date is written in Korean, what to do when a key is missing (stop). Claude Code loads it from `~/.claude/skills/` on `/trip-forms` ([skills](https://code.claude.com/docs/en/skills){ .src data-checked="2026-09-28" }); Codex reads the copy in `~/.agents/skills/` as `$trip-forms` ([Codex skills](https://learn.chatgpt.com/docs/build-skills.md){ .src data-checked="2026-09-28" }).

**Oracle.** `check.py` walks the field map: every key must exist in `trip.yaml`, every mapped cell must be non-empty, else exit 1. Week 3: a check the agent runs beats a check it claims. Without one, an empty budget cell reaches the approver under your name.

**Trigger.** Usually you: `/trip-forms` the evening before travel. Week 5's clocks return in Lesson 3, mostly to be declined.

**Payoff maths.** B5's rule: three clean manual runs first, then name the cost per run. For forms the unit is minutes: 25 by hand times 8 trips a year is 200; the recipe costs one build session (60), a few minutes per run and about 10 per form change, so it pays in year one unless the form changes a dozen times. A form filed twice a year: by hand.

**What stays manual.** Your signature or seal (kordoc has a `seal` command; the skill never calls it), the approver's click, the upload under your login, and other people's details, typed at submission and never stored.

**In practice.** Reviewer responses look automatable and are not: no template, only a prompt. Trip forms are the opposite: someone else fixes the layout and only the facts change. Template stable, facts varying, oracle possible: that is the test.

## Try it

<div class="visual"><iframe src="../visuals/b10-recipe-builder.html" title="Build a recipe from five parts; switch one off and read the failure it causes; check the payoff" loading="lazy"></iframe></div>

Predict first: which missing part gives a form that looks right and is wrong? Then switch each off.

**Phone:** for the last three forms you filed: template stable? facts in your head? a check a script could run? Three yeses is a recipe.
**Laptop:** time one trip request by hand, opening to saving: you will see the minutes per run the apply task must beat.

## Rules of thumb

- Split facts from layout before automating anything: a data file you edit, templates you only replace.
- Write the oracle before the skill; if "filled correctly" cannot be said in code, fill by hand.
- Keep signature, approval and upload manual, and other people's details out of the data file.

## Retrieval

??? question "Name the five parts and the failure each one prevents."
    Data file (retyped facts), template (drifting layout), skill (mapping in your head), oracle (half-filled form goes out), trigger (wrong time or never).

??? question "Why not automate a form filed twice a year?"
    Forty minutes a year never repays a 60-minute build plus upkeep; fill it by hand with the document skill.

??? question "Which things never go into the recipe?"
    Your signature or seal, the approval, the upload under your login, other people's details.

## Sources

- [Extend Claude with skills](https://code.claude.com/docs/en/skills){ .src data-checked="2026-09-28" }: 8 min.
- [Codex: build skills](https://learn.chatgpt.com/docs/build-skills.md){ .src data-checked="2026-09-28" }: 4 min.
- [kordoc README](https://github.com/chrisryugj/kordoc){ .src data-checked="2026-09-28" }: 3 min.

## Ledger prompt

> In **Automation recipes**: the three forms you file most, tagged recipe or by hand, with minutes per run.

**Next:** docx, xlsx, LaTeX and HWPX: one honest route and one check per format.
