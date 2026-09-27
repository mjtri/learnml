---
title: B5 · Lesson 3 · Automation that pays vs automation that burns usage
terms: [GitHub Code Review action]
playbook: automation
---

# B5 · Lesson 3 · Automation that pays vs automation that burns usage

<p class="recall" markdown>**Previously:** the phone is a client: Remote Control and Codex Remote drive your laptop, cloud sessions run elsewhere; `--cloud` sends work up, `--teleport` pulls it down.</p>

## Idea

Automation multiplies whatever it runs: a workflow that works nine times in ten becomes, weekly, a failure every ten weeks that nobody sees; hourly, 168 fresh sessions a week whether or not anything changed. Automate only what you have done by hand until it is boring, on a clock slower than the rate of change.

## How it works

**Three costs per fire.** Usage: a cloud routine or a desktop task starts a fresh session each run; a `/loop` re-sends the whole conversation. Verification: green means the session exited without an infrastructure error, not that the task succeeded; "open the run to read the transcript and confirm what Claude actually did" ([routines](https://code.claude.com/docs/en/routines){ .src data-checked="2026-09-27" }). Blast radius: a cloud routine asks no permissions; scope its repo and connected services.

**Review on GitHub, two prices.** A **GitHub Code Review action** reviews every pull request unasked; two products hide behind it. Anthropic's managed Code Review is Team and Enterprise only, about $15–25 per review billed to usage credits, multiplied by the pushes on "after every push" ([code review](https://code.claude.com/docs/en/code-review){ .src data-checked="2026-09-27" }). The other is the GitHub Action `/install-github-app` installs; with a subscription token from `claude setup-token` it spends your Max plan plus GitHub minutes; `--max-turns` caps a runaway run ([GitHub Actions](https://code.claude.com/docs/en/github-actions){ .src data-checked="2026-09-27" }). On Codex, "Automatic reviews" or `@codex review` does the same from the other pool, flagging only P0 and P1 ([Codex GitHub review](https://learn.chatgpt.com/docs/third-party/github.md){ .src data-checked="2026-09-27" }); no per-review figure is published. For a solo repo, `/code-review` before pushing beats both.

**When it pays.** The manual version worked first time on its last three runs; the "done" check is a script, not a reading; the clock is slower than the change (on-event for PRs, weekly for a site); and you can name the weekly cost: usage per run times runs per week.

**In practice.** This repo's deploy workflow is a script on a daily clock: right. A `/loop 10m` re-running `check_lessons.py` in a 120k-token session all evening is 18 fires re-sending 120k tokens each to learn nothing. A reviewer-response draft changes every time, so no clock fits it.

## Try it

<div class="visual"><iframe src="../visuals/b5-automation-payoff.html" title="Enter a manual workflow's numbers and see whether automating it pays or burns usage" loading="lazy"></iframe></div>

Predict first: the weekly refresh (25 minutes by hand, works 9 in 10, 6 % of the weekly cap per run): pays? Now the hourly CI babysitter.

**Phone:** list three things you do by hand every week for this repo or a Unity project; mark each "boring" or "still surprises me". Only boring ones qualify.
**Laptop:** do the weekly refresh by hand once, timed, with `/usage` before and after: you will see the two numbers a routine must beat.

## Rules of thumb

- Automate a workflow only after three manual runs that needed no correction.
- Match the clock to the rate of change, never faster than you would read the output.
- Name the weekly cost before turning it on, and who reads the transcript.

## Retrieval

??? question "A routine's run list shows green. What do you know, and what do you not?"
    The session exited without an infrastructure error. Not whether the task succeeded: read the transcript.

??? question "Two ways to get a Claude review on every PR; who pays for each?"
    Managed Code Review: Team and Enterprise, about $15–25 in usage credits per review. The GitHub Action with a subscription token: your plan plus GitHub minutes.

??? question "Why is an hourly routine on a repo that changes weekly a bad trade?"
    Most fires find nothing changed but each costs a fresh session, and nobody reads 168 transcripts.

## Sources

- [Automate work with routines](https://code.claude.com/docs/en/routines){ .src data-checked="2026-09-27" }: 6 min.
- [Code Review](https://code.claude.com/docs/en/code-review){ .src data-checked="2026-09-27" }: 5 min.
- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions){ .src data-checked="2026-09-27" }: 5 min.
- [Codex: review GitHub pull requests](https://learn.chatgpt.com/docs/third-party/github.md){ .src data-checked="2026-09-27" }: 3 min.

## Ledger prompt

> In **Automation**: your rule for when a task may be automated, and the weekly cost formula.

**Next:** the apply task: a weekly cloud routine that checks and deploys, and one lesson logged from the phone.
