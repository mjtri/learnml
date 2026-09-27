---
title: Lesson 4 · Train, validate, overfit
terms: [train/validation/test split, overfitting, underfitting, generalisation, regularization, dropout, early stopping, weight decay]
card: core-dl
---

# Lesson 4 · Train, validate, overfit

<p class="recall" markdown>**Previously:** a mini-batch gradient is a cheap, noisy estimate; momentum averages it over recent steps, and Adam also scales each parameter's step by its own gradient size.</p>

## Idea

A training loss of 0.01 proves nothing. A model with 200,000 parameters can memorise 60,000 images. What you want is **generalisation**: performance on images it never saw. So you hide some data and measure there. The gap between the two curves, training and held-back, is the whole diagnosis, and closing it is the job of **regularization**.

## Mechanism

The **train/validation/test split** has three parts and three rules. Train on the first. Use the second to choose hyperparameters and decide when to stop; look at it as often as you like. Look at the third once, at the end. Tune against the test set and it quietly becomes a second validation set, and its number is optimistic.

The split must respect the structure of the data, a rule you know from user studies: if participant 3's trials sit on both sides, the model learns participant 3's hand, not the gesture, and fails on participant 13. Split by participant, or leave one out and rotate. Where the analogy breaks: a study has twelve named people; a tensor has no idea who produced row 4,017. You encode the split yourself.

Read the two curves:

| Training loss | Validation loss | Name | First fix |
|---|---|---|---|
| high | high | **underfitting** | bigger model, higher learning rate, train longer |
| falling | falling | fine | keep going |
| falling | rising after a dip | **overfitting** | more data, then regularize |

A two-point gap on MNIST is normal; 100 % training against 87 % validation after training on 500 images is memorisation.

Regularization in one page, in the order to try it:

1. **More data.** The best regularizer and the only one that raises the ceiling. Label more, or transform what you have (shifts, small rotations).
2. **Weight decay.** Shrink every weight towards zero each step, so only weights the data keeps pushing up stay large: \[ w \leftarrow w - \eta\,(g + \lambda w) \] AdamW applies the shrink separately from the adaptive step; use \(\lambda\) around 0.01 to 0.1.
3. **Dropout.** During training, zero a random fraction of a layer's outputs on every step, so no unit can lean on a neighbour. At evaluation it is switched off, which is what `model.eval()` does.
4. **Early stopping.** Track the validation loss and keep a copy of the parameters from the step where it was lowest.

**In practice.** Karpathy's recipe puts a check *before* any of this: overfit a single batch. Train on two images until the loss is essentially zero. If the model cannot memorise two examples it has a bug; if it can, the pipeline works. The bug you will actually meet is `model.eval()`: dropout left on during evaluation makes the reported accuracy jump by a percent between identical runs. The fix is one line before you measure and `model.train()` after.

## Try it

<div class="visual"><iframe src="../visuals/w03-overfit-curves.html" title="Fit a curve: model size, train error and validation error" loading="lazy"></iframe></div>

Predict first, then drag:

1. Degree 1: both errors high. Predict the degree where validation error is lowest, then sweep and find it.
2. Degree 12: predict the training error, then the validation error. Which of the two is a lie about the model?
3. Stay at 12 and raise weight decay. Which error improves first?

## Retrieval

??? question "Training accuracy 99.8 %, validation 91 %. Name the condition and give two fixes in the order you would try them."
    Overfitting. First more data (collect or augment), then a regularizer such as weight decay, dropout or early stopping.

??? question "Why must a gesture dataset be split by participant rather than by trial?"
    Trials from one person share their hand, speed and device fit. With the same person on both sides, the validation score measures memorisation, not recognition on a new person.

??? question "What does dropout do during training, at evaluation, and what bug follows from forgetting model.eval()?"
    Training: zero a random fraction of a layer's outputs each step. Evaluation: nothing. Forgetting `model.eval()` keeps dropout active while measuring, so accuracy is lower and changes from run to run.

## Sources

- [Karpathy: A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/): sections 3 "Overfit" and 4 "Regularize", 8 min.
- [d2l 3.6 Generalization](https://d2l.ai/chapter_linear-regression/generalization.html): sections 3.6.1 to 3.6.3, 12 min.
- [d2l 5.6 Dropout](https://d2l.ai/chapter_multilayer-perceptrons/dropout.html): section 5.6.1 only, 6 min.

## Ledger prompt

> Next to `core-dl`: take one classifier from your own work. How was its data split, and could the same person, session or device appear on both sides? What number would you have to re-run to know?

**Next:** the three ways a network refuses to train, and the fingerprint of each.
