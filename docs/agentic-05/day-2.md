---
title: B5 · Lesson 2 · From the phone: Remote Control, Codex Remote, cloud sessions
terms: [teleport, --cloud]
playbook: automation
---

# B5 · Lesson 2 · From the phone: Remote Control, Codex Remote, cloud sessions

<p class="recall" markdown>**Previously:** three clocks fire a prompt nobody watches: `/loop` in a session, a desktop task on your machine, a cloud routine with the laptop closed; every fire is a full turn.</p>

## Idea

The phone is a client, not a computer. Every "code from the couch" feature answers one question: does the process run on your laptop (Remote Control, Codex Remote) or a vendor's machine (cloud sessions, Codex cloud)? That decides what it can see, what it does without you, and which pool it spends.

## How it works

**Remote Control (Claude, your machine).** `claude remote-control` in the repo folder starts a server with a QR code; the Claude app's Code tab lists it. Execution stays local: the app is "a client for Claude Code sessions rather than a place where code runs" ([mobile](https://code.claude.com/docs/en/mobile){ .src data-checked="2026-09-27" }). Close the terminal and the session goes offline; a sleeping laptop reconnects on wake; a stopped server returns within about four hours with `--continue`. From the phone: photos, permission approvals, text commands such as `/usage`; never `/plugin`, `/resume`, Auto or Bypass ([remote control](https://code.claude.com/docs/en/remote-control){ .src data-checked="2026-09-28" }). Turn on **Push when actions required** in `/config`, or a prompt stalls the run.

**Cloud sessions, two flags.** A cloud session runs on Anthropic's machines from a fresh clone of the GitHub repo, keeps going with the phone in your pocket, and shares your Claude rate limits. **`--cloud`** starts one: `claude --cloud "fix the failing check"` clones the remote at your branch, so push first. **Teleport** is the reverse: `claude --teleport` pulls a cloud session, its branch and history into your terminal, given a clean tree and the same repo and account; the CLI hand-off is one-way ([cloud](https://code.claude.com/docs/en/claude-code-on-the-web){ .src data-checked="2026-09-27" }).

**Codex Remote (OpenAI, your machine).** ChatGPT desktop app › Settings › Connections › Control this Mac or PC, then scan with the phone. It picks a computer and a project, describes the task, approves commands and inspects diffs; the computer must stay awake and online, and availability "depends on rollout and your workspace settings" ([Codex Remote](https://learn.chatgpt.com/docs/remote.md){ .src data-checked="2026-09-27" }). Codex cloud is the vendor-machine counterpart, ending in a diff and a PR ([Codex cloud](https://learn.chatgpt.com/docs/cloud.md){ .src data-checked="2026-09-27" }).

**In practice.** A 20-minute Unity batch-mode compile: start it under `claude remote-control`, walk to lunch; the phone shows "compile clean, run the play-mode tests?" and you tap approve. Nothing ran on the phone, nothing was cloned, the Library folder never rebuilt.

## Try it

<div class="visual"><iframe src="../visuals/b5-phone-matrix.html" title="Pick the tasks for tonight and see which phone surface can do them, laptop open or closed" loading="lazy"></iframe></div>

Predict first: of your five commonest evening tasks, how many need local files? Those need Remote Control or Codex Remote.

**Phone:** open the Claude app › Code and the ChatGPT app's Codex list; an empty one was never set up.
**Laptop:** `claude remote-control --name learnml`, scan, send `/usage` from the phone, then Ctrl+C: you will see the session go offline and return after `--continue`.

## Rules of thumb

- Start Remote Control before any run over ten minutes, with push for actions required on.
- Send a task to a cloud session when it needs no local file and the laptop will be closed; push first.
- Use Codex Remote for tasks on the other pool; keep the desktop app open and the machine awake.

## Retrieval

??? question "Where does the code run under Remote Control, and what happens when the terminal closes?"
    On your machine. It goes offline; a stopped server returns within about four hours with --continue.

??? question "Which direction is `--teleport`, and what must be true before it works?"
    Cloud to terminal. A clean tree, the same repository checked out, the branch pushed, the same account.

??? question "Name two things the Claude app cannot do to a Remote Control session."
    Start its server on the laptop, pick Auto or Bypass, run /plugin or /resume, or keep it alive after the laptop's process stops.

## Sources

- [Remote Control](https://code.claude.com/docs/en/remote-control){ .src data-checked="2026-09-28" }: 10 min.
- [Claude Code on mobile](https://code.claude.com/docs/en/mobile){ .src data-checked="2026-09-27" }: 4 min.
- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web){ .src data-checked="2026-09-27" }: 6 min.
- [Codex Remote](https://learn.chatgpt.com/docs/remote.md){ .src data-checked="2026-09-27" }: 2 min.

## Ledger prompt

> In **Automation**: the phone surfaces you have set up, and the one task you will hand each.

**Next:** when automation pays: measure the manual version first, then decide.
