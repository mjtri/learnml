---
title: Glossary
---

# Glossary

Every dotted-underlined word in a lesson opens its definition when tapped. This page is the same list, A–Z, with the lesson that introduced each word.

## /

<div class="gl-entry" id="plan" markdown>
**/plan**

The command that turns on plan mode for the next prompt (Claude Code) or toggles it (Codex): read and propose first, edit only after approval.

<small>first met in [agentic-02/day-2](agentic-02/day-2.md)</small>
</div>

## @

<div class="gl-entry" id="import" markdown>
**@import** <small>(also: @imports)</small>

A line in CLAUDE.md of the form @path that pulls another file into context at launch. Paths resolve relative to the importing file; at most four hops deep.

<small>first met in [agentic-02/day-1](agentic-02/day-1.md)</small>
</div>

## A

<div class="gl-entry" id="accept-edits-mode" markdown>
**accept-edits mode** <small>(also: acceptEdits, accept edits mode)</small>

Claude Code permission mode that runs file edits and simple file commands without asking; other shell commands, the network and paths outside the repo still prompt.

<small>first met in [agentic-03/day-2](agentic-03/day-2.md)</small>
</div>

<div class="gl-entry" id="adversarial-review" markdown>
**adversarial review** <small>(also: adversarial reviews)</small>

A read-only review told to argue against the chosen design and its assumptions, not only hunt bugs. In codex-plugin-cc: /codex:adversarial-review with focus text.

<small>first met in [agentic-04/day-3](agentic-04/day-3.md)</small>
</div>

<div class="gl-entry" id="agent" markdown>
**agent** <small>(also: agents)</small>

A model that runs in a loop: read the situation, pick a tool, act, read the result, repeat until a goal is met. Claude Code and Codex are agents.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="agent-teams" markdown>
**agent teams** <small>(also: agent team)</small>

An experimental Claude Code mode where a lead session spawns teammate sessions that message each other and share a task list. Each teammate is a full context window.

<small>first met in [agentic-04/day-2](agentic-04/day-2.md)</small>
</div>

<div class="gl-entry" id="agents-md" markdown>
**AGENTS.md**

The cross-tool instruction file convention read by Codex and, when no CLAUDE.md exists, by Claude Code. One source of truth for repo rules.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="allowlist" markdown>
**allowlist** <small>(also: allowlists, allowlisted, allow rule, allow rules)</small>

Tools or command patterns pre-approved in a settings file, like Bash(git commit *), so they run without a prompt. Deny rules override it in every mode.

<small>first met in [agentic-03/day-2](agentic-03/day-2.md)</small>
</div>

<div class="gl-entry" id="approval-policy" markdown>
**approval policy** <small>(also: approval policies)</small>

Codex's rule for when it must ask: on-request asks only to step outside the sandbox; never asks nothing. Paired with a sandbox mode that says what commands can touch.

<small>first met in [agentic-03/day-2](agentic-03/day-2.md)</small>
</div>

<div class="gl-entry" id="auto-memory" markdown>
**auto memory** <small>(also: auto memories, Codex memories)</small>

Notes the agent writes for itself across sessions: your preferences, corrections, project facts. Loaded every session but never enforced; Claude Code and Codex both keep them on your machine.

<small>first met in [agentic-02/day-3](agentic-02/day-3.md)</small>
</div>

<div class="gl-entry" id="auto-mode" markdown>
**auto mode**

Claude Code permission mode where a separate classifier reviews each action instead of you and blocks risky ones. The starting mode for terminal sessions on recent versions.

<small>first met in [agentic-03/day-2](agentic-03/day-2.md)</small>
</div>

<div class="gl-entry" id="autograd" markdown>
**autograd**

PyTorch's system that records the computation graph during the forward pass and applies the chain rule for you when you call backward().

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="axis" markdown>
**axis** <small>(also: axes)</small>

One direction you can index a tensor along, such as rows, columns, colour channels or time. Also called a dimension.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

## B

<div class="gl-entry" id="background-agent" markdown>
**background agent** <small>(also: background agents, background session, background sessions)</small>

A Claude Code session moved off your screen with /bg or claude --bg. It edits inside its own worktree and spends your quota on its own.

<small>first met in [agentic-04/day-2](agentic-04/day-2.md)</small>
</div>

<div class="gl-entry" id="backpropagation" markdown>
**backpropagation** <small>(also: backprop)</small>

The backward pass applied to a neural network: the chain rule run from the loss back to every weight, reusing shared work so it costs about one extra forward pass.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="backward-pass" markdown>
**backward pass**

Walking the computation graph from the output back to the inputs, computing how sensitive the output is to each value on the way.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="batch" markdown>
**batch** <small>(also: batches)</small>

A group of examples processed together, stacked along the first axis. 32 images of shape (3, 64, 64) form a batch of shape (32, 3, 64, 64).

<small>first met in [week-01/day-1](week-01/day-1.md)</small>
</div>

<div class="gl-entry" id="broadcasting" markdown>
**broadcasting** <small>(also: broadcast, broadcasts)</small>

The rule that lets tensors of different shapes combine: line shapes up from the right; a size-1 or missing axis is virtually copied to match the other.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="bypass-mode" markdown>
**bypass mode** <small>(also: bypassPermissions, bypass permissions mode, bypass permissions)</small>

Claude Code permission mode that skips prompts and safety checks entirely. For throwaway containers or VMs only; deny rules and a few critical paths still apply.

<small>first met in [agentic-03/day-2](agentic-03/day-2.md)</small>
</div>

## C

<div class="gl-entry" id="chain-rule" markdown>
**chain rule**

When one quantity affects another through a chain of steps, the overall sensitivity is the product of the step-by-step sensitivities.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="character-level-model" markdown>
**character-level model** <small>(also: character-level models, character-level)</small>

A language model whose tokens are single characters, so its alphabet is tiny (about 65 symbols) and it must learn spelling before words.

<small>first met in [week-05/day-1](week-05/day-1.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="chatgpt-business" markdown>
**ChatGPT Business** <small>(also: Business plan, ChatGPT Business plan)</small>

OpenAI's team subscription (formerly Team). Seats share one usage pool across ChatGPT and Codex; business data is not used for training by default.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="checkpoint" markdown>
**checkpoint** <small>(also: checkpoints)</small>

A saved copy of a model's weights (and often optimizer state) at one moment of training, so a run can be resumed, compared or shared.

<small>first met in [week-05/day-3](week-05/day-3.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="claude-md" markdown>
**CLAUDE.md**

Claude Code's project instruction file, loaded into every session. Keep it short; it can import other files with @path.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="cloud-session" markdown>
**cloud session** <small>(also: cloud sessions, Claude Code on the web)</small>

Claude Code running on Anthropic's servers against your GitHub repo, started from claude.ai/code or the mobile app.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="codex" markdown>
**Codex**

OpenAI's coding agent, available as a CLI, an IDE extension, a desktop app and a cloud service; included in ChatGPT Business.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="codex-cloud" markdown>
**Codex cloud** <small>(also: cloud task, cloud tasks)</small>

Codex running in an isolated cloud environment on a copy of your repo, started from the web, GitHub or the phone, finishing in a pull request.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="codex-remote" markdown>
**Codex Remote**

Starting, steering and approving Codex on your own computer from the ChatGPT mobile app. The computer must stay awake.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="codex-plugin-cc" markdown>
**codex-plugin-cc** <small>(also: Codex plugin, Codex plugin for Claude Code)</small>

OpenAI's plugin that runs Codex from inside Claude Code for reviews and delegated tasks. It spends your ChatGPT/Codex usage, not the Claude plan.

<small>first met in [agentic-04/day-3](agentic-04/day-3.md)</small>
</div>

<div class="gl-entry" id="colab" markdown>
**Colab**

Google Colaboratory: free hosted Python notebooks in the browser, with an optional GPU. Where the weekly build sessions run.

<small>first met in [week-01/build](week-01/build.md) · canvas card `core-tooling`</small>
</div>

<div class="gl-entry" id="compaction" markdown>
**compaction** <small>(also: auto-compaction)</small>

Summarising the conversation so far to free context. Claude Code does it automatically near the limit; /compact does it on demand.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="computation-graph" markdown>
**computation graph** <small>(also: computation graphs, computational graph)</small>

A drawing of a calculation as boxes (operations) joined by arrows (values). PyTorch records one as your code runs.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="context-window" markdown>
**context window** <small>(also: context windows)</small>

Everything the model can see at once: instructions, your messages, tool results, files it read. Finite, and the main thing you spend.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="converge" markdown>
**converge** <small>(also: converges, converged, convergence)</small>

To settle down: the loss stops improving meaningfully because the parameters have reached a low point.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

## D

<div class="gl-entry" id="deep-research" markdown>
**Deep Research** <small>(also: deep research)</small>

ChatGPT's long-running web research mode that reads many sources and returns a cited report. Verify its citations before reusing them.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="derivative" markdown>
**derivative** <small>(also: derivatives)</small>

How much a function's output changes per tiny change of one input, at one particular point. A sensitivity. Zero means nudging the input does nothing.

<small>first met in [week-01/day-3](week-01/day-3.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="diverge" markdown>
**diverge** <small>(also: diverges, diverged, divergence)</small>

To blow up: each step makes the loss larger, usually because the learning rate is too high. Often ends in NaN.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="doer-grader" markdown>
**doer/grader** <small>(also: doer and grader, doer vs grader)</small>

The rule that the agent which made a change never grades it. The grader starts from a fresh context and, at best, is a different vendor's model.

<small>first met in [agentic-04/day-3](agentic-04/day-3.md)</small>
</div>

<div class="gl-entry" id="dontask" markdown>
**dontAsk** <small>(also: dontAsk mode)</small>

Claude Code permission mode for scripts and CI: anything that would prompt is denied instead. Only reads and allowlisted tools run.

<small>first met in [agentic-03/day-2](agentic-03/day-2.md)</small>
</div>

<div class="gl-entry" id="dot-product" markdown>
**dot product** <small>(also: dot products)</small>

Multiply two equal-length vectors number by number and add up the results. Large when the vectors point the same way, so it works as a similarity score.

<small>first met in [week-01/day-2](week-01/day-2.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="dtype" markdown>
**dtype** <small>(also: dtypes)</small>

The number type stored in a tensor, such as 32-bit float or 64-bit integer. Model weights are almost always floats.

<small>first met in [week-01/day-1](week-01/day-1.md)</small>
</div>

## E

<div class="gl-entry" id="effort-level" markdown>
**effort level** <small>(also: effort levels)</small>

How much thinking a Claude model does per request (low to max). Higher effort costs more usage; lower is fine for routine edits.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="element-wise" markdown>
**element-wise** <small>(also: elementwise)</small>

An operation applied separately to each matching pair of numbers in two tensors, such as adding two images pixel by pixel.

<small>first met in [week-01/day-1](week-01/day-1.md)</small>
</div>

## F

<div class="gl-entry" id="fast-mode" markdown>
**fast mode**

A Claude Code option that runs Opus with much faster output. Billed only from usage credits, never from plan limits.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="feature" markdown>
**feature** <small>(also: features)</small>

One number that describes something about an input, such as a pixel's brightness or, deeper in a network, how strongly a learned pattern is present.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="feed-forward" markdown>
**feed-forward** <small>(also: feed-forward layer, feed-forward network, feedforward)</small>

The 2017 paper's name for the MLP block: information flows straight through it, one token at a time, with no mixing between positions.

<small>first met in [week-05/day-2](week-05/day-2.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="forward-pass" markdown>
**forward pass**

Running the calculation from inputs to output, storing intermediate values along the way.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="four-part-prompt" markdown>
**four-part prompt** <small>(also: four-part prompts, prompt shape, Goal/Context/Constraints/Done-when)</small>

A task prompt in four labelled parts: Goal, Context, Constraints, Done when. Each part you leave out is a guess the agent makes for you.

<small>first met in [agentic-02/day-2](agentic-02/day-2.md)</small>
</div>

<div class="gl-entry" id="function" markdown>
**function** <small>(also: functions)</small>

A rule that turns inputs into an output. A whole neural network is one big function from input numbers to output numbers.

<small>first met in [week-01/day-3](week-01/day-3.md)</small>
</div>

## G

<div class="gl-entry" id="gradient" markdown>
**gradient** <small>(also: gradients, grad, grads)</small>

The list of derivatives of one output (usually the loss) with respect to every input or parameter. It points in the direction of steepest increase.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="gradient-descent" markdown>
**gradient descent**

The learning algorithm: compute the gradient of the loss, move every parameter a small step in the opposite direction, repeat.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="greedy-decoding" markdown>
**greedy decoding**

Always pick the single most likely next token, no randomness. Deterministic, and prone to repeating itself in loops.

<small>first met in [week-05/day-4](week-05/day-4.md) · canvas card `core-transformer`</small>
</div>

## H

<div class="gl-entry" id="hook" markdown>
**hook**

A command Claude Code or Codex runs itself at a fixed moment, such as before a tool call or when the agent tries to stop. Deterministic, unlike an instruction.

<small>first met in [agentic-03/day-3](agentic-03/day-3.md)</small>
</div>

## I

<div class="gl-entry" id="inference" markdown>
**inference**

Using a trained model to produce outputs, with no learning happening. Only the forward pass runs.

<small>first met in [week-01/day-4](week-01/day-4.md)</small>
</div>

<div class="gl-entry" id="instruction-file" markdown>
**instruction file** <small>(also: instruction files)</small>

A file the agent loads at the start of every session: AGENTS.md, CLAUDE.md and whatever they import. You write it; every line is paid for on every turn.

<small>first met in [agentic-02/day-1](agentic-02/day-1.md)</small>
</div>

## L

<div class="gl-entry" id="layer" markdown>
**layer** <small>(also: layers)</small>

One stage of a neural network: it takes a tensor in, applies a simple parameterised operation, and passes a tensor on.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="learning-rate" markdown>
**learning rate** <small>(also: learning rates)</small>

The step-size knob of gradient descent. Too small: learning crawls. Too large: steps overshoot and the loss bounces or explodes.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="limit-reset" markdown>
**limit reset** <small>(also: limit resets)</small>

An occasional free reset of a spent usage window, applied from Settings > Usage on claude.ai.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="linear-layer" markdown>
**linear layer** <small>(also: linear layers, linear map, linear maps)</small>

A layer that computes each output as a weighted sum of its inputs: one matrix multiply (plus an optional constant offset).

<small>first met in [week-01/day-2](week-01/day-2.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="local-derivative" markdown>
**local derivative** <small>(also: local derivatives)</small>

The derivative of a single operation's output with respect to its own direct input, ignoring the rest of the graph.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="local-minimum" markdown>
**local minimum** <small>(also: local minima)</small>

A valley that is lower than its surroundings but not the lowest point overall. Gradient descent can settle there because every direction looks uphill.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="lora" markdown>
**LoRA**

Low-Rank Adaptation: fine-tune a big frozen model by learning only a small low-rank change to its weight matrices. Week 8.

<small>canvas card `lin-lora`</small>
</div>

<div class="gl-entry" id="loss" markdown>
**loss** <small>(also: losses, loss function)</small>

One number that scores how wrong the model currently is. Lower is better. Training means changing parameters to push this number down.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="loss-surface" markdown>
**loss surface** <small>(also: loss landscape)</small>

The loss pictured as a landscape: each position is one setting of the parameters, and height is how wrong the model is there.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="low-rank" markdown>
**low rank** <small>(also: low-rank)</small>

A matrix that uses fewer independent directions than its size suggests, so it squashes space. It can be stored as two thin matrices multiplied. Week 8.

<small>canvas card `core-linalg`</small>
</div>

## M

<div class="gl-entry" id="matmul" markdown>
**matmul** <small>(also: matrix multiplication, matrix multiply, matrix multiplies)</small>

Matrix multiplication. Each output number is the dot product of one row of the first matrix with one column of the second. Written A @ B in Python.

<small>first met in [week-01/day-2](week-01/day-2.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="matrix" markdown>
**matrix** <small>(also: matrices)</small>

A table of numbers with rows and columns; a tensor with two axes.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="max-plan" markdown>
**Max plan** <small>(also: Max 20x, Max plan 20x)</small>

Anthropic's top individual subscription. The 20x tier gives twenty times Pro's per-window allowance plus a weekly cap.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="mcp" markdown>
**MCP** <small>(also: MCP server, MCP servers, connector, connectors)</small>

Model Context Protocol: the open standard both Claude Code and Codex use to plug in external tools and data sources.

</div>

<div class="gl-entry" id="mlp-block" markdown>
**MLP block** <small>(also: MLP blocks)</small>

The second half of a transformer block: the same small two-layer network applied to every token on its own, widening to four times the stream width and back.

<small>first met in [week-05/day-2](week-05/day-2.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="model" markdown>
**model** <small>(also: models)</small>

A function with adjustable parameters. Its architecture is the fixed form of the function; training picks the parameter values.

<small>first met in [week-01/day-5](week-01/day-5.md)</small>
</div>

<div class="gl-entry" id="mse" markdown>
**MSE** <small>(also: mean squared error)</small>

Mean squared error: average of (prediction minus target) squared. The standard loss for predicting continuous numbers.

<small>first met in [week-01/build](week-01/build.md) · canvas card `core-optim`</small>
</div>

## N

<div class="gl-entry" id="nan" markdown>
**NaN**

Not a Number: what arithmetic returns after overflow or invalid operations. A loss of NaN almost always means training diverged.

<small>first met in [week-01/day-5](week-01/day-5.md)</small>
</div>

<div class="gl-entry" id="nanogpt" markdown>
**nanoGPT**

Karpathy's small, readable PyTorch repository that trains a GPT-style model. Its model.py is the reference code this week maps the paper onto.

<small>first met in [week-05/day-1](week-05/day-1.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="neural-network" markdown>
**neural network** <small>(also: neural networks, neural net, network)</small>

A function built by stacking simple layers, such as matrix multiplies with simple bends in between, whose parameters are learned from data.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="numerical-gradient" markdown>
**numerical gradient** <small>(also: numerical derivative, finite difference, finite differences)</small>

A derivative estimated by brute force: nudge the input a tiny bit, measure the output change, divide. Slow but a trustworthy check.

<small>first met in [week-01/day-3](week-01/day-3.md) · canvas card `core-calc`</small>
</div>

## O

<div class="gl-entry" id="opusplan" markdown>
**opusplan**

A Claude Code model setting that uses Opus while in plan mode and switches to Sonnet for the edits: the costly model thinks, the cheaper one types.

<small>first met in [agentic-02/day-2](agentic-02/day-2.md)</small>
</div>

<div class="gl-entry" id="oracle" markdown>
**oracle** <small>(also: oracles, test oracle)</small>

A check the agent can run to know whether it is done: a test suite, a build, a checker script. Without one it can only guess.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

## P

<div class="gl-entry" id="parameter" markdown>
**parameter** <small>(also: parameters)</small>

Any number inside a model that training is allowed to change. Weights are parameters. A 7B model has seven billion of them.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="parameter-count" markdown>
**parameter count** <small>(also: parameter counts, parameter counting)</small>

The total number of learned weights in a model. For a transformer it is about twelve times the stream width squared per block, plus the embedding tables.

<small>first met in [week-05/day-3](week-05/day-3.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="permission-mode" markdown>
**permission mode** <small>(also: permission modes)</small>

Claude Code's per-session setting for what the agent may do without asking: manual, accept edits, plan, auto, dontAsk or bypass.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="plan-mode" markdown>
**plan mode**

A Claude Code mode where the agent explores and proposes (read-only commands allowed) but every edit stays blocked until you approve its plan.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="playbook" markdown>
**playbook**

Your own page of workflow rules, each backed by a source or a measurement. The ledger for Track B.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="plugin" markdown>
**plugin** <small>(also: plugins)</small>

A directory of skills, agents, hooks and MCP servers installed as one unit from a marketplace. Its component descriptions sit in context on every turn.

<small>first met in [agentic-04/day-1](agentic-04/day-1.md)</small>
</div>

<div class="gl-entry" id="pre-norm" markdown>
**pre-norm** <small>(also: post-norm, pre-norm/post-norm)</small>

Where LayerNorm sits. Pre-norm normalises what a sub-block reads, so the residual stream stays a clean sum (GPT-2, nanoGPT). Post-norm normalises the sum itself after each add (the 2017 paper).

<small>first met in [week-05/day-2](week-05/day-2.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="precedence" markdown>
**precedence**

The order instruction files are read: broadest first, the nearest last. Files are joined, not replaced, so two conflicting lines leave the agent free to follow either.

<small>first met in [agentic-02/day-1](agentic-02/day-1.md)</small>
</div>

<div class="gl-entry" id="premium-seat" markdown>
**Premium seat** <small>(also: Premium seats)</small>

A higher-priced ChatGPT Business seat with much more usage and no 5-hour window. Seats can be mixed and reassigned.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="prompt-cache" markdown>
**prompt cache** <small>(also: prompt caching, cache miss, cache misses)</small>

Reuse of an already-processed conversation prefix so the next turn is cheaper. It expires after idle time; a cold restart reprocesses everything.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="pytorch" markdown>
**PyTorch**

The Python library this course uses for tensors, automatic gradients and neural networks. Imported as torch.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-tooling`</small>
</div>

## R

<div class="gl-entry" id="remote-control" markdown>
**Remote Control** <small>(also: remote control)</small>

Driving a Claude Code session that runs on your own machine from the Claude mobile app or browser. Execution stays local.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="residual-stream" markdown>
**residual stream** <small>(also: residual streams)</small>

The running sum that flows through a transformer: the token's embedding plus everything each block has added. Blocks read from it and add to it; nothing erases it.

<small>first met in [week-05/day-1](week-05/day-1.md) · canvas card `lin-resnet`</small>
</div>

<div class="gl-entry" id="rules-directory" markdown>
**rules directory** <small>(also: rules directories)</small>

Claude Code's .claude/rules/ folder of topic files loaded with the instruction file. A file with a paths: line loads only when matching files are opened.

<small>first met in [agentic-02/day-1](agentic-02/day-1.md)</small>
</div>

## S

<div class="gl-entry" id="sampling" markdown>
**sampling**

Turning the model's probabilities for the next token into one chosen token, by drawing at random in proportion to those probabilities. Repeated once per token.

<small>first met in [week-05/day-4](week-05/day-4.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="sandbox" markdown>
**sandbox** <small>(also: sandboxing, sandboxed)</small>

An enforced boundary around what an agent's commands can touch on disk and network. Codex uses an OS-level sandbox plus an approval policy.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="scalar" markdown>
**scalar** <small>(also: scalars)</small>

A single number; a tensor with no axes. Its shape is empty: ().

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="shape" markdown>
**shape** <small>(also: shapes)</small>

The size of a tensor along each axis, written like (32, 4, 4). Most beginner bugs in ML are shape bugs.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="size-cap" markdown>
**size cap** <small>(also: size caps)</small>

Codex's limit on combined instruction-file text, 32 KiB by default; files past it are not loaded. Claude Code has no byte cap but targets 200 lines per file.

<small>first met in [agentic-02/day-1](agentic-02/day-1.md)</small>
</div>

<div class="gl-entry" id="skill" markdown>
**skill** <small>(also: SKILL.md)</small>

A folder holding a SKILL.md: instructions loaded into context only when you type /name or the agent picks it. Until then only its description costs tokens.

<small>first met in [agentic-04/day-1](agentic-04/day-1.md)</small>
</div>

<div class="gl-entry" id="slope" markdown>
**slope** <small>(also: slopes)</small>

Rise over run: how steep a curve is at a point. The derivative is the slope of the curve at that point.

<small>first met in [week-01/day-3](week-01/day-3.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="subagent" markdown>
**subagent** <small>(also: subagents)</small>

A helper agent with its own fresh context that does a bounded job and returns a summary, so the main context stays small.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

## T

<div class="gl-entry" id="temperature" markdown>
**temperature** <small>(also: sampling temperature)</small>

A number the logits are divided by before softmax. Below 1 sharpens the choice towards the favourite; above 1 flattens it towards uniform. Same knob as in chat APIs.

<small>first met in [week-05/day-4](week-05/day-4.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="tensor" markdown>
**tensor** <small>(also: tensors)</small>

A box of numbers arranged along zero or more axes. A single number, a list, a table and a stack of images are all tensors.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="tiny-shakespeare" markdown>
**tiny Shakespeare**

A one-megabyte text file of Shakespeare's plays, about a million characters. The standard tiny corpus for training a first language model in minutes.

<small>first met in [week-05/day-1](week-05/day-1.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="token" markdown>
**token** <small>(also: tokens)</small>

The unit models read and write in; about three-quarters of an English word. Usage limits and costs are counted in tokens.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="tool-call" markdown>
**tool call** <small>(also: tool calls, tool use)</small>

The agent asking to run something outside itself: read a file, run a command, search the web. The result comes back into the context.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="top-k" markdown>
**top-k** <small>(also: top-k sampling)</small>

Before drawing, keep only the k most likely tokens and give the rest zero probability. Cuts off the long tail of unlikely characters that produce gibberish.

<small>first met in [week-05/day-4](week-05/day-4.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="training" markdown>
**training**

Repeatedly adjusting a model's parameters to lower the loss on example data.

<small>first met in [week-01/day-5](week-01/day-5.md)</small>
</div>

<div class="gl-entry" id="transformer-block" markdown>
**transformer block** <small>(also: transformer blocks)</small>

One repeated unit of a transformer: attention, then a small per-token network, each added back onto the residual stream. Stack many identical ones to make the model.

<small>first met in [week-05/day-1](week-05/day-1.md) · canvas card `core-transformer`</small>
</div>

## U

<div class="gl-entry" id="ultrareview" markdown>
**ultrareview** <small>(also: ultra review)</small>

Claude Code's deep review in a cloud sandbox (/code-review ultra): many reviewer agents, every finding reproduced before it is reported. Three free runs on Max, then usage credits.

<small>first met in [agentic-04/day-3](agentic-04/day-3.md)</small>
</div>

<div class="gl-entry" id="unity-batch-mode-compile" markdown>
**Unity batch-mode compile** <small>(also: batch-mode compile, batch-mode compile check)</small>

Running the Unity Editor from the command line with no window, so it imports and compiles a project, writes a log and quits with an exit code. A build oracle.

<small>first met in [agentic-03/day-1](agentic-03/day-1.md)</small>
</div>

<div class="gl-entry" id="usage-credits" markdown>
**usage credits** <small>(also: extra usage)</small>

Pay-as-you-go balance that Claude Code can draw on once plan limits are spent, managed with /usage-credits and an optional spend cap.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="usage-pool" markdown>
**usage pool** <small>(also: usage pools)</small>

One shared allowance drawn on by several surfaces. On Claude Max one pool covers claude.ai, Claude Code, desktop and mobile; Opus and Sonnet have separate limits.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="usage-window" markdown>
**usage window** <small>(also: usage windows, session window, 5-hour window)</small>

A rolling 5-hour period with a fixed allowance of usage; when it is spent you wait for the window to reset.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

## V

<div class="gl-entry" id="vector" markdown>
**vector** <small>(also: vectors)</small>

A list of numbers; a tensor with one axis. Like one frame of readings from a row of sensors.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

## W

<div class="gl-entry" id="weekly-cap" markdown>
**weekly cap** <small>(also: weekly limit, weekly caps)</small>

A second, larger allowance that spans seven days and applies across all models; it resets at a fixed time set per account.

<small>first met in [agentic-01/day-2](agentic-01/day-2.md)</small>
</div>

<div class="gl-entry" id="weight" markdown>
**weight** <small>(also: weights)</small>

A learnable number that says how strongly one input contributes to one output. A model's knowledge lives in its weights.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="worktree" markdown>
**worktree** <small>(also: worktrees, git worktree)</small>

A separate checkout of the same git repository with its own files and branch, so parallel agents never write to each other's files. Claude Code keeps them under .claude/worktrees/.

<small>first met in [agentic-04/day-2](agentic-04/day-2.md)</small>
</div>
