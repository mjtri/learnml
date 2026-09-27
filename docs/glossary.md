---
title: Glossary
---

# Glossary

Every dotted-underlined word in a lesson opens its definition when tapped. This page is the same list, A–Z, with the lesson that introduced each word.

## -

<div class="gl-entry" id="cloud" markdown>
**--cloud**

The Claude Code flag that starts a new cloud session for the current repository: claude --cloud "task" clones the GitHub remote at your branch, so push first.

<small>first met in [agentic-05/day-2](agentic-05/day-2.md)</small>
</div>

## /

<div class="gl-entry" id="loop" markdown>
**/loop**

A Claude Code command that re-runs a prompt on an interval inside the open session. Session-scoped: it stops with the session and expires after seven days.

<small>first met in [agentic-05/day-1](agentic-05/day-1.md)</small>
</div>

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

<div class="gl-entry" id="ablation" markdown>
**ablation** <small>(also: ablations, ablate, ablated, ablating)</small>

An experiment that removes or replaces one component of a model, keeps everything else fixed, and measures the change in loss, to learn what that component was doing.

<small>first met in [week-06/day-5](week-06/day-5.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="accept-edits-mode" markdown>
**accept-edits mode** <small>(also: acceptEdits, accept edits mode)</small>

Claude Code permission mode that runs file edits and simple file commands without asking; other shell commands, the network and paths outside the repo still prompt.

<small>first met in [agentic-03/day-2](agentic-03/day-2.md)</small>
</div>

<div class="gl-entry" id="accuracy" markdown>
**accuracy**

The fraction of examples the model labels correctly. What you report; the loss is what you train on, because accuracy has no useful gradient.

<small>first met in [week-03/day-1](week-03/day-1.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="activation-function" markdown>
**activation function** <small>(also: activation functions)</small>

The fixed bend applied to a neuron's weighted sum, such as tanh or ReLU. It has no parameters; it is what stops a stack of layers collapsing into one.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="adam" markdown>
**Adam** <small>(also: AdamW)</small>

The default optimizer for deep learning. Keeps running averages of each gradient and of its square, then steps each parameter by roughly the learning rate regardless of its gradient's size.

<small>first met in [week-03/day-3](week-03/day-3.md) · canvas card `core-optim`</small>
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

<div class="gl-entry" id="arxiv-id" markdown>
**arXiv ID** <small>(also: arXiv IDs, arXiv identifier)</small>

The label of an arXiv preprint: two digits of year, two of month, a dot, then a serial number, like 1706.03762. A month above 12 cannot exist.

<small>first met in [agentic-06/day-1](agentic-06/day-1.md)</small>
</div>

<div class="gl-entry" id="attention" markdown>
**attention** <small>(also: self-attention, attention head, attention heads)</small>

A soft lookup: each token asks for what it needs, every token advertises what it has, and the match decides how much of each token's content is mixed in.

<small>first met in [week-04/day-3](week-04/day-3.md) · canvas card `lin-attention`</small>
</div>

<div class="gl-entry" id="attention-weights" markdown>
**attention weights** <small>(also: attention weight, attention pattern)</small>

The numbers that say how much one token looks at each other token: one row per query, every entry at least zero, each row summing to 1.

<small>first met in [week-04/day-3](week-04/day-3.md) · canvas card `lin-attention`</small>
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

<div class="gl-entry" id="batchnorm" markdown>
**BatchNorm** <small>(also: batch normalization, batch norm, BatchNorm1d)</small>

A layer that normalizes each unit's output across the current batch, then lets the network re-scale it. Keeps activations well-sized in deep nets; behaves differently at evaluation time.

<small>first met in [week-03/day-5](week-03/day-5.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="bert" markdown>
**BERT**

Google's 2018 encoder, trained as a masked language model on raw text and then adapted per task. The template for train once, reuse everywhere.

<small>first met in [week-06/day-5](week-06/day-5.md) · canvas card `lin-bert`</small>
</div>

<div class="gl-entry" id="bigram" markdown>
**bigram** <small>(also: bigrams, bigram model)</small>

The smallest language model: predict the next token from the current token only. Learnable as a table of counts, one row per current token.

<small>first met in [week-04/day-2](week-04/day-2.md) · canvas card `core-prob`</small>
</div>

<div class="gl-entry" id="bpe" markdown>
**BPE** <small>(also: byte-pair encoding, byte pair encoding, Byte-Pair Encoding)</small>

Byte-pair encoding: build a tokenizer by starting from bytes and repeatedly gluing the most frequent adjacent pair of pieces into one new piece.

<small>first met in [week-06/day-1](week-06/day-1.md) · canvas card `core-transformer`</small>
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

<div class="gl-entry" id="byte" markdown>
**byte** <small>(also: bytes)</small>

A number from 0 to 255, the unit computers store text in. An English letter is one byte; a Korean syllable is three.

<small>first met in [week-06/day-1](week-06/day-1.md) · canvas card `core-transformer`</small>
</div>

## C

<div class="gl-entry" id="causal-mask" markdown>
**causal mask** <small>(also: causal masks, causal masking)</small>

Blanking every score that points to a later token before the softmax, so a token can only mix in its past. Without it, next-token training can read its own answer.

<small>first met in [week-04/day-4](week-04/day-4.md) · canvas card `core-transformer`</small>
</div>

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

<div class="gl-entry" id="chinchilla" markdown>
**Chinchilla**

DeepMind's 2022 result: for a fixed compute budget, grow parameters and training tokens together, roughly 20 tokens per parameter. Earlier large models were under-trained.

<small>first met in [week-06/day-4](week-06/day-4.md) · canvas card `lin-chinchilla`</small>
</div>

<div class="gl-entry" id="citation-verification" markdown>
**citation verification** <small>(also: citation check, citation checks, verify pass)</small>

A separate pass after drafting in which every reference is looked up by DOI or arXiv ID and dropped if no record exists or the record does not match.

<small>first met in [agentic-06/day-3](agentic-06/day-3.md)</small>
</div>

<div class="gl-entry" id="claude-md" markdown>
**CLAUDE.md**

Claude Code's project instruction file, loaded into every session. Keep it short; it can import other files with @path.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="cloud-routine" markdown>
**cloud routine** <small>(also: cloud routines)</small>

A saved Claude Code prompt plus repositories that runs as a cloud session whenever a trigger fires, laptop closed, without permission prompts. Research preview; spends your subscription usage.

<small>first met in [agentic-05/day-1](agentic-05/day-1.md)</small>
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

Codex running in an isolated cloud environment on a copy of your repo, started from the web, GitHub or a connected app, finishing in a pull request.

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

<div class="gl-entry" id="compute-optimal" markdown>
**compute-optimal** <small>(also: compute optimal)</small>

The model size and amount of training data that give the lowest loss for a fixed training compute budget, rather than the biggest model you can afford.

<small>first met in [week-06/day-4](week-06/day-4.md) · canvas card `lin-chinchilla`</small>
</div>

<div class="gl-entry" id="context-length" markdown>
**context length** <small>(also: context lengths, block size)</small>

How many previous tokens a model may look at when predicting the next one. A bigram has 1; a transformer has a fixed maximum set by its position table.

<small>first met in [week-04/day-2](week-04/day-2.md) · canvas card `core-prob`</small>
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

<div class="gl-entry" id="cosine-similarity" markdown>
**cosine similarity** <small>(also: cosine)</small>

The dot product of two vectors after dividing out their lengths: 1 means same direction, 0 unrelated, minus 1 opposite. Length no longer matters.

<small>first met in [week-04/day-1](week-04/day-1.md) · canvas card `lin-word2vec`</small>
</div>

<div class="gl-entry" id="cross-entropy" markdown>
**cross-entropy** <small>(also: cross entropy)</small>

The standard classification loss: how surprised the model is by the correct label, averaged over examples. Zero when it was certain and right; large when confident and wrong.

<small>first met in [week-03/day-2](week-03/day-2.md) · canvas card `core-optim`</small>
</div>

## D

<div class="gl-entry" id="dataloader" markdown>
**DataLoader** <small>(also: DataLoaders, data loader)</small>

The PyTorch helper that pulls examples from a Dataset, shuffles them and stacks them into batches, one batch per loop iteration.

<small>first met in [week-03/day-1](week-03/day-1.md) · canvas card `core-tooling`</small>
</div>

<div class="gl-entry" id="dataset" markdown>
**Dataset** <small>(also: dataset, datasets)</small>

A collection of examples. In PyTorch, a class that answers two questions: how many examples are there, and give me example number i.

<small>first met in [week-03/day-1](week-03/day-1.md) · canvas card `core-tooling`</small>
</div>

<div class="gl-entry" id="decoder" markdown>
**decoder** <small>(also: decoders)</small>

A transformer in which each position sees only earlier positions, so it can be trained to predict the next token and then generate text.

<small>first met in [week-06/day-5](week-06/day-5.md) · canvas card `lin-gpt3`</small>
</div>

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

<div class="gl-entry" id="desktop-scheduled-task" markdown>
**desktop scheduled task** <small>(also: desktop scheduled tasks, local scheduled task, local scheduled tasks)</small>

A prompt the Claude Desktop app starts on a schedule as a fresh session on your own machine. Runs only while the app is open and the computer awake.

<small>first met in [agentic-05/day-1](agentic-05/day-1.md)</small>
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

<div class="gl-entry" id="doi" markdown>
**DOI** <small>(also: DOIs)</small>

Digital Object Identifier: a permanent label for a publication, like 10.1038/221963a0. The prefix names the publisher; a lookup service returns the record or nothing at all.

<small>first met in [agentic-06/day-1](agentic-06/day-1.md)</small>
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

<div class="gl-entry" id="dropout" markdown>
**dropout**

During training, randomly zero a fraction of a layer's outputs on every step, so no unit can rely on another. Switched off for evaluation.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="dtype" markdown>
**dtype** <small>(also: dtypes)</small>

The number type stored in a tensor, such as 32-bit float or 64-bit integer. Model weights are almost always floats.

<small>first met in [week-01/day-1](week-01/day-1.md)</small>
</div>

## E

<div class="gl-entry" id="early-stopping" markdown>
**early stopping**

Watch the validation loss during training and keep the parameters from the step where it was lowest, stopping once it has clearly started to rise.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
</div>

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

<div class="gl-entry" id="embedding" markdown>
**embedding** <small>(also: embeddings, embedding vector, embedding vectors, embedding layer)</small>

A short list of learned numbers that stands in for a discrete thing such as a word. Things used alike end up pointing the same way.

<small>first met in [week-04/day-1](week-04/day-1.md) · canvas card `lin-word2vec`</small>
</div>

<div class="gl-entry" id="encoder" markdown>
**encoder** <small>(also: encoders)</small>

A transformer that reads the whole input at once, every position seeing every other, and outputs one vector per token for a later task.

<small>first met in [week-06/day-5](week-06/day-5.md) · canvas card `lin-bert`</small>
</div>

<div class="gl-entry" id="epoch" markdown>
**epoch** <small>(also: epochs)</small>

One full pass through the training data. With a tiny data set that fits in one step, one epoch is one step of the loop.

<small>first met in [week-02/day-5](week-02/day-5.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="exploding-gradient" markdown>
**exploding gradient** <small>(also: exploding gradients)</small>

Gradients that grow layer by layer on the way back, until updates are huge and the loss diverges. Caused by weights that are too large.

<small>first met in [week-03/day-5](week-03/day-5.md) · canvas card `core-dl`</small>
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

<div class="gl-entry" id="flops" markdown>
**FLOPs** <small>(also: FLOP, floating-point operations)</small>

Floating-point operations: the count of multiplies and adds a computation needs. Training compute is measured in FLOPs, about six per parameter per training token.

<small>first met in [week-06/day-4](week-06/day-4.md) · canvas card `lin-chinchilla`</small>
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

<div class="gl-entry" id="generalisation" markdown>
**generalisation** <small>(also: generalization, generalise, generalize, generalises, generalizes, generalising, generalizing)</small>

How well a model does on examples it never trained on. The only thing that matters; training loss is just a proxy for it.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="github-code-review-action" markdown>
**GitHub Code Review action** <small>(also: Code Review action)</small>

A review that runs on GitHub when a pull request opens: Anthropic's managed Code Review (Team and Enterprise, billed separately) or the claude-code-action review workflow, which can use your subscription.

<small>first met in [agentic-05/day-3](agentic-05/day-3.md)</small>
</div>

<div class="gl-entry" id="gpt" markdown>
**GPT**

OpenAI's family of language models that read text left to right and predict the next token. nanoGPT is a small copy of the design.

<small>first met in [week-06/day-1](week-06/day-1.md) · canvas card `lin-gpt3`</small>
</div>

<div class="gl-entry" id="gradient" markdown>
**gradient** <small>(also: gradients, grad, grads)</small>

The list of derivatives of one output (usually the loss) with respect to every input or parameter. It points in the direction of steepest increase.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="gradient-accumulation" markdown>
**gradient accumulation**

Gradients are added into a stored slot, never overwritten. Needed when a value feeds two places; a bug when last step's gradient is still in the slot.

<small>first met in [week-02/day-3](week-02/day-3.md) · canvas card `core-calc`</small>
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

<div class="gl-entry" id="hidden-layer" markdown>
**hidden layer** <small>(also: hidden layers, hidden units, hidden unit)</small>

Any layer between the input and the output of a network. Its values are not data and not answers, but learned in-between features.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="hook" markdown>
**hook**

A command Claude Code or Codex runs itself at a fixed moment, such as before a tool call or when the agent tries to stop. Deterministic, unlike an instruction.

<small>first met in [agentic-03/day-3](agentic-03/day-3.md)</small>
</div>

<div class="gl-entry" id="hyperparameter" markdown>
**hyperparameter** <small>(also: hyperparameters, hyper-parameter)</small>

A setting you choose rather than learn: learning rate, batch size, hidden width, how long to train. Training never changes it; you do.

<small>first met in [week-03/day-1](week-03/day-1.md)</small>
</div>

## I

<div class="gl-entry" id="inference" markdown>
**inference**

Using a trained model to produce outputs, with no learning happening. Only the forward pass runs.

<small>first met in [week-01/day-4](week-01/day-4.md)</small>
</div>

<div class="gl-entry" id="initialization" markdown>
**initialization** <small>(also: initialisation, init, Xavier, Kaiming, Xavier initialization, Kaiming initialization)</small>

The starting values of the weights. Their scale must shrink with the number of inputs per unit, or signals blow up or fade with depth. Xavier and Kaiming are recipes.

<small>first met in [week-03/day-5](week-03/day-5.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="instruction-file" markdown>
**instruction file** <small>(also: instruction files)</small>

A file the agent loads at the start of every session: AGENTS.md, CLAUDE.md and whatever they import. You write it; every line is paid for on every turn.

<small>first met in [agentic-02/day-1](agentic-02/day-1.md)</small>
</div>

## K

<div class="gl-entry" id="key-vector" markdown>
**key vector** <small>(also: key vectors)</small>

In attention, the vector a token advertises: what do I have? A query that matches it by dot product gets a large weight.

<small>first met in [week-04/day-3](week-04/day-3.md) · canvas card `lin-attention`</small>
</div>

<div class="gl-entry" id="kr-en-glossary" markdown>
**KR↔EN glossary** <small>(also: KR-EN glossary, bilingual glossary)</small>

A short table of your field's terms in Korean and English, kept in project knowledge so translations stay consistent across papers and reports.

<small>first met in [agentic-06/day-2](agentic-06/day-2.md)</small>
</div>

## L

<div class="gl-entry" id="language-model" markdown>
**language model** <small>(also: language models)</small>

A model that assigns probabilities to sequences of tokens, usually by predicting each next token from the ones before it. Generation is asking it repeatedly.

<small>first met in [week-04/day-2](week-04/day-2.md) · canvas card `core-prob`</small>
</div>

<div class="gl-entry" id="layer" markdown>
**layer** <small>(also: layers)</small>

One stage of a neural network: it takes a tensor in, applies a simple parameterised operation, and passes a tensor on.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="layernorm" markdown>
**LayerNorm** <small>(also: layer normalization, layer norm)</small>

A layer that normalizes across the features of each single example, independent of the batch. The normalization used inside transformers.

<small>first met in [week-03/day-5](week-03/day-5.md) · canvas card `core-dl`</small>
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

<div class="gl-entry" id="literature-review-pipeline" markdown>
**literature review pipeline** <small>(also: lit-review pipeline)</small>

A fixed sequence for a paper search: search in both tools, merge and dedupe the reference lists, verify every citation, then summarise only what survived. Nothing enters a document earlier.

<small>first met in [agentic-06/day-1](agentic-06/day-1.md)</small>
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

<div class="gl-entry" id="logits" markdown>
**logits** <small>(also: logit)</small>

The raw scores a classifier outputs, one per class, any real number. Softmax turns them into probabilities; the loss usually takes the logits directly.

<small>first met in [week-03/day-2](week-03/day-2.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="log-log-plot" markdown>
**log–log plot** <small>(also: log-log plot, log–log plots, log-log plots, log–log, log-log)</small>

A plot with both axes on log scales, so each tick is ten times the last. A power law appears as a straight line whose slope is the exponent.

<small>first met in [week-06/day-3](week-06/day-3.md) · canvas card `lin-kaplan`</small>
</div>

<div class="gl-entry" id="lookup-table" markdown>
**lookup table** <small>(also: lookup tables, embedding table)</small>

A matrix read by row number: token 17 comes back as row 17. In an embedding layer the rows are parameters, so training rewrites them.

<small>first met in [week-04/day-1](week-04/day-1.md) · canvas card `lin-word2vec`</small>
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

<div class="gl-entry" id="loss-curve" markdown>
**loss curve** <small>(also: loss curves)</small>

The loss plotted against training steps. The first thing anyone looks at: falling means learning, flat means stuck, rising means the step is too big.

<small>first met in [week-02/day-5](week-02/day-5.md) · canvas card `core-calc`</small>
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

<div class="gl-entry" id="masked-language-model" markdown>
**masked language model** <small>(also: masked language modelling, masked language modeling, MLM)</small>

Training by hiding some tokens of a text and predicting them from both sides. The objective BERT uses; it needs no labels.

<small>first met in [week-06/day-5](week-06/day-5.md) · canvas card `lin-bert`</small>
</div>

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
**MCP** <small>(also: Model Context Protocol, MCP server, MCP servers, connector, connectors, custom connector, custom connectors)</small>

Model Context Protocol: the open standard for plugging tools and data sources into an agent. A connector is an MCP server offered inside the Claude or ChatGPT app.

<small>first met in [agentic-06/day-1](agentic-06/day-1.md)</small>
</div>

<div class="gl-entry" id="merge-rule" markdown>
**merge rule** <small>(also: merge rules, BPE merge, BPE merges)</small>

One learned step of BPE: whenever these two pieces sit next to each other, glue them into one. Rules are applied in the order they were learned.

<small>first met in [week-06/day-1](week-06/day-1.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="micrograd" markdown>
**micrograd**

Karpathy's 100-line autograd engine that works on single numbers. Rebuilding it from memory is this week's goal, because PyTorch does the same thing on tensors.

<small>first met in [week-02/day-1](week-02/day-1.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="mini-batch" markdown>
**mini-batch** <small>(also: mini-batches, minibatch, minibatches)</small>

A small random handful of examples, typically 32 to 512, used for one gradient step. Its gradient is a noisy but cheap estimate of the full-data gradient.

<small>first met in [week-03/day-3](week-03/day-3.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="mlp" markdown>
**MLP** <small>(also: MLPs, multi-layer perceptron, multilayer perceptron)</small>

Multi-layer perceptron: linear layers stacked with an activation function between each pair. The plainest neural network, and a component inside far larger models.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="mlp-block" markdown>
**MLP block** <small>(also: MLP blocks)</small>

The second half of a transformer block: the same small two-layer network applied to every token on its own, widening to four times the stream width and back.

<small>first met in [week-05/day-2](week-05/day-2.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="mnist" markdown>
**MNIST** <small>(also: Fashion-MNIST)</small>

70,000 small grey images of handwritten digits, 28 by 28 pixels, ten classes. The standard first classification dataset. Fashion-MNIST swaps digits for clothing items.

<small>first met in [week-03/day-1](week-03/day-1.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="model" markdown>
**model** <small>(also: models)</small>

A function with adjustable parameters. Its architecture is the fixed form of the function; training picks the parameter values.

<small>first met in [week-01/day-5](week-01/day-5.md)</small>
</div>

<div class="gl-entry" id="momentum" markdown>
**momentum**

An optimizer trick: keep a running average of past gradients and step along that instead. Smooths mini-batch noise and speeds up travel along long shallow valleys.

<small>first met in [week-03/day-3](week-03/day-3.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="mse" markdown>
**MSE** <small>(also: mean squared error)</small>

Mean squared error: average of (prediction minus target) squared. The standard loss for predicting continuous numbers.

<small>first met in [week-01/build](week-01/build.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="multi-head-attention" markdown>
**multi-head attention** <small>(also: multi-head, multi-headed attention, multihead attention)</small>

Several small attention heads run side by side on slices of the vector, each with its own weights pattern, then their outputs are joined end to end.

<small>first met in [week-04/day-5](week-04/day-5.md) · canvas card `core-transformer`</small>
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

<small>first met in [week-04/day-4](week-04/day-4.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="negative-log-likelihood" markdown>
**negative log-likelihood** <small>(also: NLL, log-likelihood)</small>

Minus the log of the probability the model gave the right answer. Probability one gives zero; probability near zero gives a huge number. Cross-entropy is its average.

<small>first met in [week-03/day-2](week-03/day-2.md) · canvas card `core-optim`</small>
</div>

<div class="gl-entry" id="neural-network" markdown>
**neural network** <small>(also: neural networks, neural net, network)</small>

A function built by stacking simple layers, such as matrix multiplies with simple bends in between, whose parameters are learned from data.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="neuron" markdown>
**neuron** <small>(also: neurons)</small>

The smallest unit of a neural network: a weighted sum of its inputs plus an offset, pushed through a bend such as tanh.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="next-token-prediction" markdown>
**next-token prediction** <small>(also: next token prediction)</small>

The training job of a language model: given the tokens so far, give a probability to every possible next token. Every position in any text is a free labelled example.

<small>first met in [week-04/day-2](week-04/day-2.md) · canvas card `core-prob`</small>
</div>

<div class="gl-entry" id="nn-module" markdown>
**nn.Module**

PyTorch's building block: a Python class that owns parameters and defines a forward function. Modules nest, and model.parameters() walks the whole tree.

<small>first met in [week-03/day-1](week-03/day-1.md) · canvas card `core-tooling`</small>
</div>

<div class="gl-entry" id="nonlinearity" markdown>
**nonlinearity** <small>(also: nonlinearities, non-linearity)</small>

Any step whose output is not a weighted sum of its input, like a bend, a clip or a threshold. Without one, stacked layers are just one bigger linear layer.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="normalization" markdown>
**normalization** <small>(also: normalisation, normalized, normalised, normalizing)</small>

Rescaling a set of numbers so their mean is zero and their spread is one, so that every layer sees inputs of a predictable size.

<small>first met in [week-03/day-5](week-03/day-5.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="numerical-gradient" markdown>
**numerical gradient** <small>(also: numerical derivative, finite difference, finite differences)</small>

A derivative estimated by brute force: nudge the input a tiny bit, measure the output change, divide. Slow but a trustworthy check.

<small>first met in [week-01/day-3](week-01/day-3.md) · canvas card `core-calc`</small>
</div>

## O

<div class="gl-entry" id="one-hot" markdown>
**one-hot** <small>(also: one-hot vector, one-hot encoding)</small>

A label written as a vector of zeros with a single one at the true class. The gradient of cross-entropy at the logits is probabilities minus this vector.

<small>first met in [week-03/day-2](week-03/day-2.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="optimizer" markdown>
**optimizer** <small>(also: optimizers, optimiser)</small>

The object that applies the update rule to every parameter after a backward pass. SGD and Adam are optimizers; all of them read the .grad fields.

<small>first met in [week-03/day-1](week-03/day-1.md) · canvas card `core-optim`</small>
</div>

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

<div class="gl-entry" id="overfitting" markdown>
**overfitting** <small>(also: overfit, overfits, overfitted)</small>

The model memorises its training examples instead of learning the pattern: training loss keeps falling while validation loss rises. Like a study that only predicts its own participants.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
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

<div class="gl-entry" id="positional-encoding" markdown>
**positional encoding** <small>(also: positional encodings, position encoding, position encodings, position embedding, position embeddings, positional embedding, positional embeddings)</small>

A vector for each position, added to the token's embedding so attention can tell first from third. Without it the tokens before you are a bag with no order.

<small>first met in [week-04/day-5](week-04/day-5.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="power-law" markdown>
**power law** <small>(also: power laws, power-law)</small>

A relation where one quantity equals the other raised to a fixed power, so each tenfold increase buys the same percentage change. Straight on a log–log plot.

<small>first met in [week-06/day-3](week-06/day-3.md) · canvas card `lin-kaplan`</small>
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

<div class="gl-entry" id="project-instructions" markdown>
**project instructions**

The standing text a Projects workspace adds to every chat inside it: role, audience, format, language rules. Written once, applied to every draft.

<small>first met in [agentic-06/day-2](agentic-06/day-2.md)</small>
</div>

<div class="gl-entry" id="projects" markdown>
**Projects**

A workspace in ChatGPT or Claude that keeps its own chats, files, instructions and memory together, so every new chat starts with the same context.

<small>first met in [agentic-06/day-2](agentic-06/day-2.md)</small>
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

## Q

<div class="gl-entry" id="query-vector" markdown>
**query vector** <small>(also: query vectors)</small>

In attention, the vector a token uses to ask: what am I looking for? Compared by dot product against every key.

<small>first met in [week-04/day-3](week-04/day-3.md) · canvas card `lin-attention`</small>
</div>

## R

<div class="gl-entry" id="record-mode" markdown>
**record mode** <small>(also: ChatGPT record, ChatGPT Record)</small>

The ChatGPT macOS app feature that transcribes a meeting or voice note and writes notes into a canvas. The audio is deleted once transcribed.

<small>first met in [agentic-06/day-2](agentic-06/day-2.md)</small>
</div>

<div class="gl-entry" id="regularization" markdown>
**regularization** <small>(also: regularisation, regularizer, regularizers)</small>

Any change that trades a little training fit for better results on new data: penalising large weights, dropping units at random, stopping early, adding data.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="relu" markdown>
**ReLU**

The activation function max(0, x): negative inputs become zero, positive inputs pass unchanged. Cheap, and its slope is exactly 0 or 1.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="remote-control" markdown>
**Remote Control** <small>(also: remote control)</small>

Driving a Claude Code session that runs on your own machine from the Claude mobile app or browser. Execution stays local.

<small>first met in [agentic-01/day-3](agentic-01/day-3.md)</small>
</div>

<div class="gl-entry" id="residual-connection" markdown>
**residual connection** <small>(also: residual connections, skip connection, skip connections)</small>

Add a block's input to its output, so the block only learns a correction. Gives gradients a straight path back through any depth. The ResNet idea, used in every transformer.

<small>first met in [week-03/day-5](week-03/day-5.md) · canvas card `lin-resnet`</small>
</div>

<div class="gl-entry" id="residual-stream" markdown>
**residual stream** <small>(also: residual streams)</small>

The running sum that flows through a transformer: the token's embedding plus everything each block has added. Blocks read from it and add to it; nothing erases it.

<small>first met in [week-05/day-1](week-05/day-1.md) · canvas card `lin-resnet`</small>
</div>

<div class="gl-entry" id="reviewer-response" markdown>
**reviewer response** <small>(also: reviewer responses, response to reviewers)</small>

The point-by-point reply to a paper review: each comment quoted, then the change made or the reason it was not, with where it lives in the revision.

<small>first met in [agentic-06/day-2](agentic-06/day-2.md)</small>
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

<div class="gl-entry" id="scaled-dot-product" markdown>
**scaled dot-product** <small>(also: scaled dot-product attention)</small>

The standard attention recipe: dot every query with every key, divide by the square root of the vector size, softmax each row, then mix the values with those weights.

<small>first met in [week-04/day-4](week-04/day-4.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="scaling-law" markdown>
**scaling law** <small>(also: scaling laws)</small>

An empirical rule for how loss falls as you add parameters, data or compute: smoothly and predictably, as a power law, across many orders of magnitude.

<small>first met in [week-06/day-3](week-06/day-3.md) · canvas card `lin-kaplan`</small>
</div>

<div class="gl-entry" id="sequence" markdown>
**sequence** <small>(also: sequences)</small>

An ordered list of tokens, such as the characters of a line or the words of a sentence. Position in the list matters.

<small>first met in [week-04/day-2](week-04/day-2.md) · canvas card `core-prob`</small>
</div>

<div class="gl-entry" id="sgd" markdown>
**SGD** <small>(also: stochastic gradient descent)</small>

Stochastic gradient descent: gradient descent where each step uses the gradient of one mini-batch instead of all the data.

<small>first met in [week-03/day-3](week-03/day-3.md) · canvas card `core-optim`</small>
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

<div class="gl-entry" id="softmax" markdown>
**softmax**

Turns a list of scores into probabilities that add to one: exponentiate each score, then divide by the total. Bigger gaps between scores give sharper probabilities.

<small>first met in [week-03/day-2](week-03/day-2.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="subagent" markdown>
**subagent** <small>(also: subagents)</small>

A helper agent with its own fresh context that does a bounded job and returns a summary, so the main context stays small.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

## T

<div class="gl-entry" id="tanh" markdown>
**tanh**

The S-shaped activation function that squashes any number into the range minus one to one. Steep near zero, flat far out, so large inputs stop passing gradient.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="teleport" markdown>
**teleport** <small>(also: --teleport, /teleport)</small>

Pulling a cloud session, its branch and its conversation into your terminal with claude --teleport. Needs a clean tree, the same repository and the same account.

<small>first met in [agentic-05/day-2](agentic-05/day-2.md)</small>
</div>

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

<div class="gl-entry" id="tm-report-template" markdown>
**TM report template** <small>(also: TM template)</small>

Your fixed section list and rules for an ETRI Technical Memo, stored as project instructions so every TM draft starts in the right shape and language.

<small>first met in [agentic-06/day-2](agentic-06/day-2.md)</small>
</div>

<div class="gl-entry" id="token" markdown>
**token** <small>(also: tokens)</small>

The unit models read and write in; about three-quarters of an English word. Usage limits and costs are counted in tokens.

<small>first met in [agentic-01/day-1](agentic-01/day-1.md)</small>
</div>

<div class="gl-entry" id="tokenization" markdown>
**tokenization** <small>(also: tokenizer, tokenizers, tokenize, tokenized, tokenizing, tokenizes)</small>

Cutting text into tokens a model can number. A tokenizer is the program that does it; modern ones cut at learned sub-word chunks, not words or letters.

<small>first met in [week-06/day-1](week-06/day-1.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="tokenizer-artefact" markdown>
**tokenizer artefact** <small>(also: tokenizer artefacts, tokenizer artifact, tokenizer artifacts, tokenization artefact, tokenization artefacts)</small>

An odd model behaviour caused by how text was cut into tokens, not by the model: miscounted letters, arithmetic slips, spaces that change the answer, costly Korean.

<small>first met in [week-06/day-2](week-06/day-2.md) · canvas card `core-transformer`</small>
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

<div class="gl-entry" id="topological-order" markdown>
**topological order** <small>(also: topological sort, topo order)</small>

A listing of graph nodes where every value comes after everything it was made from. Walked in reverse, each gradient is complete before it is passed on.

<small>first met in [week-02/day-2](week-02/day-2.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="train-validation-test-split" markdown>
**train/validation/test split** <small>(also: train/val/test split, training set, validation set, validation data, test set)</small>

Divide the data three ways: train on the first part, tune choices on the second, report once on the third, which the model never sees during training.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="training" markdown>
**training**

Repeatedly adjusting a model's parameters to lower the loss on example data.

<small>first met in [week-01/day-5](week-01/day-5.md)</small>
</div>

<div class="gl-entry" id="training-loop" markdown>
**training loop** <small>(also: training loops)</small>

The five steps repeated to train any model: forward pass, loss, zero the gradients, backward pass, update the parameters.

<small>first met in [week-02/day-5](week-02/day-5.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="transformer-block" markdown>
**transformer block** <small>(also: transformer blocks)</small>

One repeated unit of a transformer: attention, then a small per-token network, each added back onto the residual stream. Stack many identical ones to make the model.

<small>first met in [week-05/day-1](week-05/day-1.md) · canvas card `core-transformer`</small>
</div>

<div class="gl-entry" id="trigger" markdown>
**trigger**

What starts a cloud routine's run: a schedule (hourly at most), an HTTP call to the routine's own endpoint, or a GitHub event such as a pull request opening.

<small>first met in [agentic-05/day-1](agentic-05/day-1.md)</small>
</div>

## U

<div class="gl-entry" id="ultrareview" markdown>
**ultrareview** <small>(also: ultra review)</small>

Claude Code's deep review in a cloud sandbox (/code-review ultra): many reviewer agents, every finding reproduced before it is reported. Three free runs on Max, then usage credits.

<small>first met in [agentic-04/day-3](agentic-04/day-3.md)</small>
</div>

<div class="gl-entry" id="underfitting" markdown>
**underfitting** <small>(also: underfit, underfits)</small>

The model is too weak or too briefly trained to capture the pattern: both training and validation loss stay high.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
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

<div class="gl-entry" id="value-object" markdown>
**Value object** <small>(also: Value objects)</small>

A single number wrapped in a tiny class that also remembers which numbers made it and how. The building block of micrograd; a one-number cousin of a tensor.

<small>first met in [week-02/day-1](week-02/day-1.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="value-vector" markdown>
**value vector** <small>(also: value vectors)</small>

In attention, the vector a token hands over once it is matched. The output is the weighted mix of the values, not of the keys.

<small>first met in [week-04/day-3](week-04/day-3.md) · canvas card `lin-attention`</small>
</div>

<div class="gl-entry" id="vanishing-gradient" markdown>
**vanishing gradient** <small>(also: vanishing gradients)</small>

Gradients that shrink layer by layer on the way back, until early layers get almost no learning signal. Caused by small weights or saturated units.

<small>first met in [week-03/day-5](week-03/day-5.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="vector" markdown>
**vector** <small>(also: vectors)</small>

A list of numbers; a tensor with one axis. Like one frame of readings from a row of sensors.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="vocabulary" markdown>
**vocabulary** <small>(also: vocabularies, vocab)</small>

The full list of pieces a tokenizer can output, each with an id number. GPT-2 has 50,257 of them; a character-level model has a few dozen.

<small>first met in [week-06/day-1](week-06/day-1.md) · canvas card `core-transformer`</small>
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

<div class="gl-entry" id="weight-decay" markdown>
**weight decay**

Shrink every weight slightly towards zero on each update, so only weights the data keeps pushing up stay large. A regularizer; AdamW applies it separately from the gradient.

<small>first met in [week-03/day-4](week-03/day-4.md) · canvas card `core-dl`</small>
</div>

<div class="gl-entry" id="word2vec" markdown>
**word2vec**

The 2013 method that learns word embeddings by predicting a word from its neighbours in raw text. The vectors are a by-product; nothing was labelled by hand.

<small>first met in [week-04/day-1](week-04/day-1.md) · canvas card `lin-word2vec`</small>
</div>

<div class="gl-entry" id="worktree" markdown>
**worktree** <small>(also: worktrees, git worktree)</small>

A separate checkout of the same git repository with its own files and branch, so parallel agents never write to each other's files. Claude Code keeps them under .claude/worktrees/.

<small>first met in [agentic-04/day-2](agentic-04/day-2.md)</small>
</div>

## X

<div class="gl-entry" id="xor" markdown>
**XOR**

Exclusive-or: true when exactly one of two inputs is on. Four points that no single straight line can split, so no single neuron can learn them.

<small>first met in [week-02/day-4](week-02/day-4.md) · canvas card `core-calc`</small>
</div>

## Z

<div class="gl-entry" id="zero-grad" markdown>
**zero_grad** <small>(also: zero the gradients, zeroing the gradients)</small>

Clearing every stored gradient before a backward pass, so the new gradient is not added on top of the old one. In PyTorch: w.grad.zero_() or the zero_grad() call.

<small>first met in [week-02/day-3](week-02/day-3.md) · canvas card `core-calc`</small>
</div>

## √

<div class="gl-entry" id="d-scaling" markdown>
**√d scaling**

Dividing attention scores by the square root of the vector size, so that scores stay moderate as vectors get longer and the softmax does not turn into a hard pick.

<small>first met in [week-04/day-4](week-04/day-4.md) · canvas card `core-transformer`</small>
</div>
