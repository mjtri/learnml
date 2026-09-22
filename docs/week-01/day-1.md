---
title: Day 1 · Tensors & shapes
terms: [tensor, scalar, vector, matrix, shape, axis, batch, broadcasting, element-wise, dtype, PyTorch]
card: core-linalg
---

# Day 1 · Tensors & shapes

<p class="recall" markdown>**Why this week:** every model you will ever touch is numbers in boxes, pushed through arithmetic, then nudged to be less wrong. This week builds those three pieces: boxes (today), arithmetic (day 2), nudging (days 3–5).</p>

## Idea

Deep learning code never handles "an image" or "a sentence". It handles **tensors**: boxes of numbers with a known **shape**. A model is a pipeline that reshapes and recombines those boxes. When you read someone's model code, most of understanding it is knowing the shape at each line, and most bugs in your first month will be shape mismatches. So the first skill is unglamorous and decisive: look at a shape, know what each axis means, and predict the shape an operation produces *before* you run it.

## Mechanism

A tensor has zero or more **axes**. Its shape lists the size of each one.

| Shape | Name | Example from your world |
|---|---|---|
| `()` | **scalar** | one error score |
| `(7,)` | **vector** | one head pose: xyz + quaternion |
| `(4, 4)` | **matrix** | one frame of a 4×4 actuator grid |
| `(3, 64, 64)` | 3 axes | an RGB image: channels, height, width |
| `(32, 3, 64, 64)` | 4 axes | a **batch** of 32 such images |

Two conventions carry a lot of weight. The batch axis comes **first**. And a shape tells you sizes, not meanings: `(90, 7)` could be 90 frames of head pose or 90 users with 7 questionnaire scores. The meaning of each axis lives in your head, which is why papers annotate tensors as B×T×C (batch, time, channels). Get in the habit now.

**Element-wise** operations (`+`, `*`, …) want identical shapes. When shapes differ, **broadcasting** decides whether the operation is still legal:

1. Line the two shapes up **from the right**.
2. Each pair of sizes must be equal, or one of them must be 1 (or missing).
3. The size-1 or missing axis is virtually copied to match.

An honest example from haptics: a stream of frames `(32, 4, 4)` times a per-actuator calibration gain `(4, 4)`. From the right: 4 vs 4 ✓, 4 vs 4 ✓, 32 vs *missing* ✓. Result `(32, 4, 4)`: one calibration table applied to every frame. That is literally what broadcasting is for.

Now a per-frame intensity `(32,)`. From the right: 4 vs 32 ✗. Error. You meant "one number per frame", so say so with shape `(32, 1, 1)`.

The dangerous case is when broadcasting *succeeds* and you did not mean it. `(100, 1) - (100,)` lines up as 1 vs 100 ✓ and 100 vs missing ✓, giving `(100, 100)`: every prediction minus every target. No error, a wrong number, and a model that quietly refuses to learn. This exact bug costs beginners days.

```python
import torch
frames = torch.rand(32, 4, 4)   # batch of haptic frames
gain = torch.rand(4, 4)         # per-actuator calibration
out = frames * gain             # broadcast over the batch
print(out.shape, out.dtype)     # (32, 4, 4) torch.float32
```

The **dtype** is the other half of a tensor's identity. The numbers flowing through a model are floats; labels and indices are integers. **PyTorch** complains when you mix them wrongly, and the message usually names both dtypes.

## Try it

<div class="visual"><iframe src="../visuals/tensor-shapes.html" title="Broadcasting shape checker" loading="lazy"></iframe></div>

Predict first, then tap:

1. Preset **(3,4) + (4,)**. What is the result shape? Which tensor got copied, and along which axis?
2. Change B to **(3,)**. Predict: legal or not? Now repair it without changing how many numbers B holds.
3. Make A **(3,1)** and B **(1,4)**. Both get stretched. How many numbers come out of 3 + 4 numbers in?

## Retrieval

??? question "A batch of 16 RGB images, 224×224, in PyTorch order. What is the shape, and what does each axis mean?"
    `(16, 3, 224, 224)`: batch, channels, height, width. Batch first; PyTorch puts channels before height and width.

??? question "State the broadcasting rule from memory. What is the result of combining (8, 1, 5) with (4, 5)?"
    Align shapes from the right; each pair must be equal, or one is 1 or missing; the size-1/missing axis is virtually copied. Result: `(8, 4, 5)`.

??? question "Why is `pred - target` with shapes (100, 1) and (100,) dangerous, and what is the fix?"
    It broadcasts to `(100, 100)`, every prediction minus every target, with no error message, so the loss is silently wrong. Fix: make the shapes identical first, e.g. `pred.squeeze(1)` or `target.unsqueeze(1)`.

## Sources

- [PyTorch: Broadcasting semantics](https://pytorch.org/docs/stable/notes/broadcasting.html): the whole page, 5 min.
- [d2l 2.1 Data manipulation](https://d2l.ai/chapter_preliminaries/ndarray.html): sections 2.1.1–2.1.4, 15 min. Pick the PyTorch tab.
- [PyTorch tensors tutorial](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html): skim, 10 min.

## Ledger prompt

> Next to `core-linalg`: write the shapes of three data streams from your own XR/haptics work (a head-pose trace, a depth frame, an actuator pattern…) and name every axis.

**Tomorrow:** the one operation that does almost all the work inside a neural network.
