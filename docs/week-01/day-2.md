---
title: Day 2 · Matmul as mixing
terms: [dot product, matmul, weight, parameter, linear layer, feature, neural network, layer]
card: core-linalg
---

# Day 2 · Matmul as mixing

<p class="recall" markdown>**Yesterday in one sentence:** everything is a tensor with a shape, and broadcasting lines shapes up from the right.</p>

## Idea

Open any **neural network** and you mostly find one operation repeated: multiply by a table of **weights**. Every output number is a weighted mix of all the input numbers. Different weights give a different mix; *learning* means finding good weights. Today is about reading that one operation three ways: as arithmetic, as similarity, and as a movement of space.

## Mechanism

Start with the **dot product** of a weight vector and an input vector:

\[ w \cdot x = w_1 x_1 + w_2 x_2 + \dots + w_n x_n \]

Reading one: a **weighted sum**. Reading two: a **similarity score**. It is largest when \(x\) points the same way as \(w\), zero when they are unrelated (perpendicular), negative when opposed. So \(w\) acts as a template and the dot product asks "how much of my pattern is in this input?" This is the textbook model of a receptive field: a cell that responds most when the stimulus matches its template. (Real neurons are not linear; more next week.)

Stack several templates as the rows of a matrix \(W\) and you get **matmul**:

\[ y = W x \qquad y_i = (\text{row } i \text{ of } W) \cdot x \]

The shape rule: `(m, n) @ (n, p) → (m, p)`. Inner sizes must match, and they vanish. A **linear layer** is exactly this, with \(W\) as its **parameters**: it turns \(n\) input **features** into \(m\) output features.

Here the analogy to your field is exact, not loose. The vOICe maps an image column to a sound: each pixel row owns a sine wave, brightness sets its loudness, and the ear gets the sum. For a column of 64 brightness values \(x\), the audio snippet is \(y = Wx\), where each *column* of \(W\) holds one row's sine wave. **A hand-designed sensory-substitution mapping is a fixed matrix.** The proposal of machine learning is small and radical: make \(W\) learnable, and let data and an objective choose it. You build this matrix on build day and learn one in week 12.

Reading three is geometric. A 2×2 matrix moves the whole plane, and its **columns are where the two unit arrows land**. That gives you rotation, stretch and shear for free. It also gives you the *squash*: when the two columns line up, the plane collapses onto a line. Different inputs now land on the same output, and no later **layer** can pull them apart. Keep that picture; in week 8 it becomes "low rank", the idea behind LoRA.

One caution. Two linear layers in a row are no more powerful than one: \(W_2(W_1x) = (W_2W_1)x\), just another matrix. Depth only pays once something non-linear sits between the layers (week 2).

PyTorch keeps examples as rows, so you will see the transposed form:

```python
import torch
x = torch.rand(32, 64)   # batch of 32 inputs, 64 features
W = torch.rand(10, 64)   # 10 outputs, each mixes 64 inputs
y = x @ W.T              # (32, 64) @ (64, 10) -> (32, 10)
```

## Try it

<div class="visual"><iframe src="../visuals/matmul-transform.html" title="Drag a 2x2 matrix and watch space move" loading="lazy"></iframe></div>

Predict first, then drag:

1. Before tapping **Rotate 90°**, predict where the input \(x = (1, 1)\) lands. Check the readout.
2. Drag the two column arrows until they line up. What happens to the grid and to the *area* readout? Find two different inputs that now land on the same output.
3. Pick any matrix and verify one output by hand: \(y_1\) = row 1 · \(x\).

## Retrieval

??? question "Inputs have shape (32, 64) and you want 10 outputs per example. What shape is W, and what shape is `x @ W.T`?"
    `W` is `(10, 64)`, one row (template) per output. `x @ W.T` is `(32, 64) @ (64, 10) → (32, 10)`: the inner 64s match and vanish.

??? question "Give the two non-geometric readings of a dot product."
    A weighted sum of the inputs; and a similarity score that is largest when the input points the same way as the weight vector, which makes the weight vector a template.

??? question "What do the columns of a 2×2 matrix tell you, and what happens when they are parallel?"
    They show where the two unit arrows land, which fixes what happens to every other point. If they are parallel the plane is squashed onto a line: area becomes 0, different inputs collide, and the information cannot be recovered.

## Sources

- [3Blue1Brown: Linear transformations and matrices](https://www.3blue1brown.com/lessons/linear-transformations): 11 min. The best single video for today.
- [3Blue1Brown: Dot products and duality](https://www.3blue1brown.com/lessons/dot-products): first 6 min.
- [d2l 2.3 Linear algebra](https://d2l.ai/chapter_preliminaries/linear-algebra.html): sections 2.3.8–2.3.10 (dot product, matrix–vector, matrix–matrix), 10 min.

## Ledger prompt

> Next to `core-linalg`: describe one hand-designed mapping from your own work (a sonification, a haptic rendering, a retargeting) as a matrix. What are its rows? What would it mean to *learn* it?

**Tomorrow:** how a model finds out which way to turn a weight: sensitivity.
