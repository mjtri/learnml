---
title: Lesson 1 · nn.Module and the canonical loop
terms: [nn.Module, Dataset, DataLoader, optimizer, hyperparameter, MNIST, accuracy]
card: core-tooling
---

# Lesson 1 · nn.Module and the canonical loop

<p class="recall" markdown>**Previously:** a Value remembers its history, the backward walk fills every gradient, and five repeated lines turn an MLP into a learner.</p>

## Idea

Your engine and PyTorch do the same job. The difference is scale and plumbing: PyTorch pushes thousands of examples through tensors at once, and it names the plumbing so that every training script in the world reads the same way. Learn four names and you can read most of them. A **nn.Module** owns parameters and defines a forward function. A **Dataset** hands out one example. A **DataLoader** stacks examples into batches. An **optimizer** applies the update. The loop itself is the five lines you wrote by hand.

## Mechanism

An `nn.Module` has two duties: own parameters and define `forward`. Modules nest, a `Linear` inside a `Sequential` inside your model, and `model.parameters()` walks the tree and yields every learnable tensor. That list is exactly what the optimizer needs.

```python
model = nn.Sequential(
    nn.Flatten(),                # (B,1,28,28) -> (B,784)
    nn.Linear(784, 256), nn.ReLU(),
    nn.Linear(256, 10))          # ten scores per image
opt = torch.optim.SGD(model.parameters(), lr=0.1)
for x, y in loader:              # one batch at a time
    loss = F.cross_entropy(model(x), y)
    opt.zero_grad()              # forget the last batch
    loss.backward()              # fill every .grad
    opt.step()                   # w <- w - lr * w.grad
```

Read it against your engine: `model(x)` is the forward pass, `loss.backward()` is your `backward()`, `opt.step()` is the update you wrote as `p.data -= lr * p.grad`, and `opt.zero_grad()` is the fix for the accumulation bug. Nothing new happens; it is faster and named.

The data side has the same shape. A `Dataset` answers two questions: *how many examples?* (`__len__`) and *give me example i* (`__getitem__`). The `DataLoader` turns that into an iterator over batches: shuffle the indices, fetch examples, stack them along a new first axis. **MNIST** has 60,000 training images of handwritten digits, 28×28 grey pixels each, so a batch size of 64 gives 938 batches per pass, the last one holding 32 images. One full pass is an epoch.

Batch size, learning rate, hidden width, number of passes: these are **hyperparameters**, settings you choose and training never touches.

Two numbers come out of every loop. The loss is what the gradient descends. **Accuracy**, the fraction of images whose highest score is the right digit, is what you report; you cannot train on it, because a small nudge to a weight almost never flips a decision, so its gradient is zero nearly everywhere.

If you write Unity, a module is close to a `MonoBehaviour`: serialised fields are the parameters and `forward` is the method the engine calls. Where the analogy breaks: nothing calls a module on its own. You call `model(x)` yourself, and nesting is plain Python attributes.

**In practice.** `print(model)` shows the tree, one line per module: `Linear(in_features=784, out_features=256, bias=True)` and so on. Summing `p.numel()` over `model.parameters()` gives 203,530 for the model above. Two silent bugs are worth memorising by symptom. Loss stuck near its starting value: you forgot `opt.step()`. Loss falls, then climbs and wanders: you forgot `opt.zero_grad()`, and last week's accumulation bug is back at scale.

## Try it

<div class="visual"><iframe src="../visuals/w03-dataloader-shapes.html" title="One epoch of the loop, step by step: batches, shapes and gradients" loading="lazy"></iframe></div>

Predict first, then press:

1. 60,000 images, batch size 64: how many batches per epoch, and how big is the last one?
2. Hidden width 256: guess the parameter count before reading it. Halve the width. Does the count halve?
3. Step through one iteration. At which line does `.grad` first hold numbers, and at which line do the weights actually change?

## Retrieval

??? question "Name the four PyTorch objects in a training script and the one job of each."
    `nn.Module` owns parameters and defines forward; `Dataset` returns one example by index; `DataLoader` shuffles and stacks examples into batches; the optimizer applies the update to every parameter.

??? question "Write the five lines inside the loop, in order, and say which one your engine did with p.data -= lr * p.grad."
    `logits = model(x)`; `loss = F.cross_entropy(logits, y)`; `opt.zero_grad()`; `loss.backward()`; `opt.step()`. The last one is the hand-written update.

??? question "Why is a model trained on cross-entropy but reported by accuracy?"
    Accuracy counts decisions, and a tiny weight change almost never flips one, so its gradient is zero nearly everywhere. The loss changes smoothly with every weight, so it gives a usable gradient.

## Sources

- [PyTorch: Build the neural network](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html): up to "Model parameters", 10 min.
- [PyTorch: Optimizing model parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html): the "Full implementation" section, 8 min.
- [d2l 5.2 Implementation of MLPs](https://d2l.ai/chapter_multilayer-perceptrons/mlp-implementation.html): section 5.2.2, the concise version, 5 min.

## Ledger prompt

> Next to `core-tooling`: which of the four objects maps onto something you already have in your Unity or experiment code? Which one has no counterpart, and what did you do by hand instead?

**Next:** what the ten output scores mean, and why the loss is a measure of surprise.
