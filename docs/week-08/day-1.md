---
title: Lesson 1 · Rank: how many directions a matrix really uses
terms: [rank, low rank]
card: core-linalg
---

# Lesson 1 · Rank: how many directions a matrix really uses

<p class="recall" markdown>**Previously:** a checkpoint is config plus weights plus tokenizer; load it, read the shapes, probe its hidden states with the weights frozen, and log every run with config, seed and git hash.</p>

## Idea

Week 1 left you a picture: a matrix moves the plane, its columns are where the unit arrows land, and when the columns line up the plane is *squashed* onto a line. This lesson gives that squash a number. The **rank** of a matrix is how many independent directions its outputs can fill. A matrix has millions of entries; rank says how many do separate work, and that decides how cheaply a matrix, or a *change* to one, can be stored: the idea behind this week's fine-tuning method.

## Mechanism

Take the 2×2 matrix with columns \((1, 2)\) and \((2, 4)\). The second column is twice the first, so both unit arrows land on the same line, and every input comes out somewhere on that line. Four entries, one direction of output: rank 1. Nudge the second column to \((2, 4.1)\) and the columns stop lining up; the outputs fill the plane again: rank 2. Rank is a whole number and can never exceed the smaller side of the matrix.

Two readings agree: rank is the number of columns you cannot build from the others, and it is the dimension of the space the outputs fill, a point (0), a line (1), a plane (2). Squashing is losing rank, and week 1's warning holds: inputs that collide can never be told apart again.

The payoff is storage. A rank-1 matrix is a column times a row: \(\begin{pmatrix}1 & 2\\ 2 & 4\end{pmatrix} = \begin{pmatrix}1\\ 2\end{pmatrix}\begin{pmatrix}1 & 2\end{pmatrix}\). In general a matrix of rank \(r\) is a product of two thin ones:

\[ W_{d \times d} = B_{d \times r}\, A_{r \times d} \]

That is **low rank**: \(2dr\) numbers instead of \(d^2\). At \(d = 4096\) and \(r = 8\) that is 65 thousand instead of 16.8 million, a factor of 256. The factorization is exact only if the rank really is \(r\); the next lesson handles the case where it is only *nearly* so.

**In practice.** After the build's Part E, count directions in SmolLM2-360M's first `q_proj` and in the change its rank-8 adapter learned:

```python
q = tuned.base_model.model.model.layers[0].self_attn.q_proj
W = q.base_layer.weight.float()            # (960, 960)
print(torch.linalg.matrix_rank(W))         # close to 960
A = q.lora_A["default"].weight             # (8, 960)
B = q.lora_B["default"].weight             # (960, 8)
print(torch.linalg.matrix_rank(B @ A))     # tensor(8)
print(W.numel(), A.numel() + B.numel())    # 921600 vs 15360
```

The weight uses nearly every direction it has; the learned change fits in eight. That is the LoRA paper's finding, and lesson 3 exploits it.

An honest analogy from your bench: a haptic sleeve with sixteen actuators driven by two input channels through a fixed mixing matrix can only produce a two-dimensional family of patterns. The mixing matrix has rank two; no sensation outside that plane is reachable. Where it breaks: actuators saturate and skin responds nonlinearly, while rank describes a linear map alone.

## Try it

<div class="visual"><iframe src="../visuals/w08-rank-explorer.html" title="Drag column vectors, read the rank" loading="lazy"></iframe></div>

Before you drag, guess:

1. Drag the second column until it points the same way as the first. At what angle does the readout drop to rank 1, and what happens to the shaded area just before?
2. Press **random** five times. Predict how often you get rank 1, then say why a trained weight matrix is never exactly low rank either.
3. Put both columns on the origin. What is the rank, and what does every input become? Compare with `w01-matmul-transform.html` from week 1, where the same collapse appeared as a squash.

## Retrieval

??? question "A 3×3 matrix has columns (1, 0, 1), (2, 0, 2) and (0, 1, 0). What is its rank, and what shape do its outputs fill?"
    Rank 2. The second column is twice the first, so two independent directions remain; the outputs fill a plane inside 3-D space.

??? question "A 1024×1024 matrix is known to have rank 4. How many numbers store it exactly, and how did you get there?"
    Two thin matrices, 1024×4 and 4×1024: 8192 numbers instead of 1,048,576, because rank r means a tall d×r times a wide r×d.

??? question "Why does a rank-1 layer lose information, in week 1's language?"
    Its outputs all lie on one line, so different inputs land on the same output. No later layer can separate what has been merged onto a line.

## Sources

- [3Blue1Brown: Inverse matrices, column space and null space](https://www.3blue1brown.com/lessons/inverse-matrices): from "rank" to the end, about 5 min.
- [LoRA paper](https://arxiv.org/abs/2106.09685): section 1 only, the "low intrinsic rank" hypothesis, 5 min.
- [`torch.linalg.matrix_rank`](https://docs.pytorch.org/docs/2.14/generated/torch.linalg.matrix_rank.html): the `atol` and `rtol` arguments, 3 min.

## Ledger prompt

> Next to `core-linalg`: write the rank of one matrix from your own work (a sensor mixing matrix, a calibration, a projection) and what that rank means the mapping cannot express.

**Next:** every matrix is a sum of a few simple stretches, and keeping the biggest ones compresses an image.
