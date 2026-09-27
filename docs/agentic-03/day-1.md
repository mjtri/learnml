---
title: B3 · Lesson 1 · The agent needs an oracle
terms: [Unity batch-mode compile]
playbook: verification
---

# B3 · Lesson 1 · The agent needs an oracle

<p class="recall" markdown>**Previously:** keep one durable instruction file (`AGENTS.md`) that both tools read; keep it short and pruned.</p>

## Idea

An agent stops when the work *looks* done. Without a check it can run, that is its only signal, and you become the verification loop. An **oracle** is anything that returns pass or fail into the conversation: a test, a build exit code, a linter, `check_lessons.py`. With one, the loop closes by itself. Without one, keep the task small enough that you will actually read the output.

## How it works

Anthropic's rule: give Claude a check it can run, "tests, a build, a screenshot to compare"; it iterates until the check passes. Then choose how hard the check gates the stop: in the prompt, as a `/goal` condition re-checked every turn, as a Stop hook that blocks the turn from ending (Lesson 3), or as a review by a fresh subagent. Ask for evidence, the command and what it returned, not "done" ([best practices](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }). OpenAI's version: Codex "can do this loop for you, but only if it knows what 'good' looks like", from the prompt or `AGENTS.md` ([Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }).

Three oracles you already own:

1. **This repo:** `python check_lessons.py --only agentic-03` exits 1 on any error and prints each one.
2. **Unity/C#:** the Editor console only you can read. A **Unity batch-mode compile** turns it into an exit code: `Unity.exe -batchmode -nographics -quit -projectPath … -logFile …` compiles with no window; on failure Unity "immediately exits with return code 1" and the log holds every `error CS` line. Only one Editor may hold a project: close it first ([command-line arguments](https://docs.unity3d.com/Manual/EditorCommandLineArguments.html){ .src data-checked="2026-09-27" }).
3. **Experiments:** a script whose output you diff against a saved copy from a known-good run.

Not oracles: "make sure it works", the agent's own summary, a screenshot it describes but never compares: the model grading itself.

**In practice.** "Migrate `HapticController` to the new input API. Done when the batch-mode compile exits 0 and the log has no `error CS`." The agent compiles, reads `PulseScheduler.cs(42,17): error CS0103`, fixes the line, compiles again. You read one number.

## Try it

### Worked example

```powershell
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.18f1\Editor\Unity.exe"
& $unity -batchmode -nographics -quit -projectPath "D:\XR\HapticStudy" -logFile "$env:TEMP\unity.log"
"exit code: $LASTEXITCODE"
Select-String -Path "$env:TEMP\unity.log" -Pattern "error CS" | Select-Object -First 2
```

```text
exit code: 1
Assets\Haptics\PulseScheduler.cs(42,17): error CS0103: The name 'clock' does not exist in the current context
```

Two lines the agent can act on without you.

**Phone:** for your last three agent tasks (Claude app › Code tab; ChatGPT › Codex), name the oracle that would have caught each mistake, or "none"; three lines in the playbook under *Verification*.
**Laptop:** close the Editor, run the worked example against your XR project, and time it. You will see the exit code and the log path; the elapsed minutes are the price of one iteration of that oracle.

## Rules of thumb

- Name the oracle in the prompt before the agent starts; if there is none, write the check first or shrink the task.
- Ask for evidence, not assertions: the command it ran, the exit code, the failing line.
- Keep the oracle cheap (`--only agentic-03`, one test file, a compile, not a full build); a slow check gets skipped.

## Retrieval

??? question "What does an agent use as its stop signal when it has no oracle, and what does that make you?"
    "Looks done", its own judgement; you become the verification loop.

??? question "Name the four ways Anthropic lists for turning a check into a gate, weakest to strongest."
    In the prompt, as a `/goal` condition, as a Stop hook that blocks the turn, and as a review by a fresh subagent.

??? question "Why does a Unity batch-mode compile fail while the Editor is open, and what does that mean for the workflow?"
    Only one Editor instance can hold a project. Close it for hand-off runs; while editing, the console is your oracle.

## Sources

- [Give Claude a way to verify its work](https://code.claude.com/docs/en/best-practices){ .src data-checked="2026-09-27" }: 4 min.
- [Codex best practices](https://learn.chatgpt.com/guides/best-practices){ .src data-checked="2026-09-27" }: 5 min.
- [Unity Editor command-line arguments](https://docs.unity3d.com/Manual/EditorCommandLineArguments.html){ .src data-checked="2026-09-27" }: 3 min.

## Ledger prompt

> In **Verification**: your three tasks with their oracles, and the one kind of task that has none.

**Next:** permission modes and sandboxes: what each one lets the agent do without asking, and who stops a bad action.
