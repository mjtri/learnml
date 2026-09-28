---
title: "B9 · Lesson 2 · Discover with traction, decide with a rubric"
terms: [star history, traction, worth-it rubric, ECC, Pocock skills]
playbook: tools
---

# B9 · Lesson 2 · Discover with traction, decide with a rubric

<p class="recall" markdown>**Previously:** seven extension layers, each with its own place to run and price per turn; before any install, read `hooks/hooks.json`, `.mcp.json` and `bin/`, then `allowed-tools` and the auto-update setting.</p>

## Idea

Hype arrives as a screenshot; **traction** arrives as a curve. Discovery is a ten-minute weekly habit on star-history.com; the decision is a **worth-it rubric** of six lines scored 0–2, adopt at 8/12 with no zero on trust. Stars get a repository onto the list; only the rubric gets it onto your machine.

## How it works

**The recipe.** (1) The home page's *Weekly* tab is a leaderboard of new stars in seven days, beside *All-time*; read it for the two or three rows in your lane. (2) The per-repo page `star-history.com/<owner>/<repo>` has *Overview*, *Trending* and *Badges* tabs: stars, rank, weekly new stars, pushes, forks, contributors. (3) `/compare/<category>` puts a lane side by side: `ai-coding-tool`, `document-to-markdown`, `browser-automation`, 42 in all. (4) Monthly posts (`/blog/skills`, `/blog/harness`) name each lane's contenders.

**Reading a star curve.** A **star history** with a steady slope is sustained use; a vertical step is a launch or a viral post, and what matters is the slope after the step. Stars against last push: 270k and a push this week is alive; 34k and no push since July needs a look at open issues first. 2026 caveat: GitHub cut off per-user stargazer data on June 30; the September endpoint returns weekly buckets with daily counts; large repositories now show the real curve to the end.

**The six lines.** Habit change (changes what you do weekly, or adds a feature?). Context and usage cost (always-on descriptions, hooks per turn, tool schemas). Trust (licence, who wrote the code that runs as you, the three files). Maintenance (last push, open issues, maintainer count). Both tools (Claude Code and Codex, or one?). Fit (Unity, paperwork, experiments, this repo). Tie-break: two candidates that change the same habit count as one; keep one method pack.

**In practice.** **ECC**: habit 1, cost 0 (24 hook entries, 292 skill descriptions), trust 1, maintenance 2, both 2, fit 0 = 6, a pattern library. **Pocock skills**: habit 2 (`grill-with-docs` changes how a Unity feature starts), cost 1, trust 1 (per-repo setup step), maintenance 1 (one maintainer, 533 open issues, unverified), both 2, fit 1 = 8, passes but shares superpowers' habit: keep one.

## Try it

<div class="visual"><iframe src="../visuals/b9-rubric-scorer.html" title="Score a repository on six lines and read the verdict" loading="lazy"></iframe></div>

Predict first: write your own six numbers for ECC before tapping its preset.

**Phone:** open star-history.com/affaan-m/ecc, *Trending* tab; note weekly stars and pushes: line 4, filled in.
**Laptop:** open `/compare/document-to-markdown`, score the top three in a scratch note: you will see one pass and two fail on fit.

## Rules of thumb

- Spend ten minutes weekly on the Weekly tab and one category page; never install from the leaderboard.
- Score the slope after a spike, and stars against the last push, before reading a README.
- Give trust a zero when the three files show anything you cannot explain; a zero ends the scoring.

## Retrieval

??? question "A repository gained 5,000 stars this week. What do you check before scoring it?"
    The slope after the spike on its per-repo page, the last push date, open issues and contributors; then the three files.

??? question "Why did star charts break in mid-2026, and what changed in the fixed ones?"
    GitHub cut per-user stargazer data on June 30; the September API returns weekly buckets with daily counts; big repositories show the full curve again.

??? question "Pocock skills scores 8. Why does the radar still list it under read, not adopt?"
    It changes the same habit as superpowers; two method packs count as one, so keep one and read the other for ideas.

## Sources

- [star-history.com](https://www.star-history.com/) (unverified): tabs and per-repo pages, 3 min.
- [The new GitHub star history API](https://www.star-history.com/blog/new-github-star-history-api){ .src data-checked="2026-09-28" }: 4 min.
- [Star History Monthly, Skills](https://www.star-history.com/blog/skills) (unverified): the method-pack lane, 6 min.
- [ECC README](https://github.com/affaan-m/ECC){ .src data-checked="2026-09-28" }: 8 min.

## Ledger prompt

> In **Tools**: your weekly discovery slot and the six-line scores of the first repository you rejected.

**Next:** the current radar, the "read, don't bundle-install" cases, scopes, and a one-week A/B with the B8 meters.
