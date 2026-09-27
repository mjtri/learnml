---
title: Lesson 2 · SVD in pictures: a matrix as a few stretches
terms: [SVD, singular value, low-rank approximation]
card: core-linalg
---

# Lesson 2 · SVD in pictures: a matrix as a few stretches

<p class="recall" markdown>**Previously:** rank counts the independent directions a matrix's outputs can fill, and a rank-r matrix is two thin matrices multiplied, 2dr numbers instead of d².</p>

## Idea

Real matrices are rarely exactly low rank; they are *nearly* low rank. A few strong directions carry most of a photo or a weight matrix; the rest is small. The **SVD** makes this precise. It rewrites any matrix as a sum of simple stretches, each with a strength, sorted strongest first. Keep the first few and drop the rest: the best compression at that rank, and a way to *measure* low rank instead of guessing.

## Mechanism

A single stretch is the simplest matrix there is: take the input's component along a direction \(v\), scale it by \(\sigma\), send it out along a direction \(u\). Written out it is a column times a row, \(\sigma\, u\, v^{\top}\), rank 1. The SVD says every matrix is a sum of such stretches whose directions do not overlap:

\[ W = \sigma_1 u_1 v_1^{\top} + \sigma_2 u_2 v_2^{\top} + \cdots \]

Each \(\sigma_i\) is a **singular value**: the strength of that stretch, never negative, sorted so \(\sigma_1 \ge \sigma_2 \ge \cdots\). Counting the singular values that are not zero gives the rank, and the unit circle through \(W\) becomes an ellipse with axes \(\sigma_1, \sigma_2\): week 1's squash is a singular value near zero.

A 2×2 by hand, the `core-linalg` card's "done when". Take \(W = \begin{pmatrix}3 & 1\\ 1 & 3\end{pmatrix}\). It stretches the diagonal direction \((1, 1)\) by 4 and the anti-diagonal \((1, -1)\) by 2, so \(\sigma_1 = 4\), \(\sigma_2 = 2\), and \(u_1 = v_1\) is the unit diagonal. Keep only the first stretch: \(4 \cdot u_1 v_1^{\top} = \begin{pmatrix}2 & 2\\ 2 & 2\end{pmatrix}\). That is the **low-rank approximation** of \(W\) at rank 1; what it leaves out, \(\begin{pmatrix}1 & -1\\ -1 & 1\end{pmatrix}\), is the second stretch. No other rank-1 matrix gets closer; the error is always the first singular value you dropped.

For a \(64 \times 64\) image the sum has 64 terms. Keeping \(k\) stores \(k\) columns, \(k\) rows and \(k\) strengths: \(k(2 \cdot 64 + 1)\) numbers, 1032 instead of 4096 at \(k = 8\). Noise is the opposite case: all its singular values are about the same size, so nothing can be dropped. Sorted singular values are a fingerprint: steep means compressible, flat means not.

**In practice.** Three lines:

```python
U, S, Vh = torch.linalg.svd(W, full_matrices=False)
k = 8
W_k = U[:, :k] @ torch.diag(S[:k]) @ Vh[:k]
print(S[:10] / S[0])   # how fast do the strengths fall?
```

The LoRA paper does this to the *change* fine-tuning makes and finds a handful of stretches explain it: why rank 1 already works in its table 6. In your field the same move is a synergy: Santello and colleagues found two directions carry over 80 percent of the variance in fifteen grasp joint angles. Where it breaks: that analysis subtracts the mean posture first; a weight matrix has none.

## Try it

<div class="visual"><iframe src="../visuals/w08-svd-compressor.html" title="Keep k stretches of an image and read the error" loading="lazy"></iframe></div>

Before you slide, guess:

1. On **letters**, at which \(k\) can you first read the text, and what fraction of the numbers is stored?
2. Switch to **noise**. Predict the bar shape, then find the smallest \(k\) with error under 20 percent.
3. On **blob**, guess the \(k\) at which the error is under 5 percent.

## Retrieval

??? question "A matrix's singular values are 9, 3, 0.1, 0.02. What is its rank, and what rank would you use to store it approximately?"
    Rank 4: none is exactly zero. Rank 2 is the sensible approximation; dropping the last two costs at most 0.1.

??? question "For the 2×2 matrix with rows (2, 0) and (0, 5), write the singular values and the best rank-1 approximation."
    Singular values 5 and 2. The rank-1 approximation keeps the stronger stretch: rows (0, 0) and (0, 5); the error left is the stretch of size 2.

??? question "A 256×256 image: how many numbers does a rank-10 approximation store, and what does the singular-value plot look like for noise?"
    10 × (256 + 256 + 1) = 5130 instead of 65,536. For noise the plot is nearly flat: no small set of stretches dominates.

## Sources

- [3Blue1Brown: Eigenvectors and eigenvalues](https://www.3blue1brown.com/lessons/eigenvalues): the first half, special directions that only get stretched, 8 min.
- [Mathematics for Machine Learning](https://mml-book.github.io/): chapter 4, the SVD and matrix approximation sections, 20 min.
- [`torch.linalg.svd`](https://docs.pytorch.org/docs/2.14/generated/torch.linalg.svd.html): what `full_matrices=False` returns, 3 min.

## Ledger prompt

> Next to `core-linalg`: name one dataset of yours (postures, EEG, actuator patterns) whose singular values you expect to fall steeply, and one you expect flat. What changes in each case?

**Next:** fine-tuning changes a weight matrix by a nearly low-rank amount, so learn the change as B times A and leave the matrix alone.
