---
title: Lesson 2 · Softmax and cross-entropy
terms: [logits, softmax, cross-entropy, negative log-likelihood, one-hot]
card: core-dl
---

# Lesson 2 · Softmax and cross-entropy

<p class="recall" markdown>**Previously:** a training script is four named objects (module, dataset, loader, optimizer) around the same five-line loop you wrote by hand.</p>

## Idea

A classifier ends in ten numbers, one per class, and they can be any size. Training needs two things those raw scores do not give: a way to read them as a belief, and one number saying how wrong that belief was. **Softmax** does the first, **cross-entropy** the second: turn the scores into probabilities, then charge the model for how surprised it was by the right answer. Every language model you will read about is trained with exactly this pair.

## Mechanism

The raw scores are **logits**, \(z\). Softmax exponentiates each and divides by the total:

\[ p_i = \frac{e^{z_i}}{\sum_j e^{z_j}} \]

Logits \((2, 1, 0)\) give \(e^z = (7.39, 2.72, 1)\), total 11.1, so \(p = (0.67, 0.24, 0.09)\). Every probability is positive, they add to one, and only *gaps* matter: add 5 to all three and nothing changes; widen the gaps and the belief sharpens.

Write the label as a **one-hot** vector, a one at the true class and zeros elsewhere. Cross-entropy is the **negative log-likelihood** of that class:

\[ L = -\log p_{\text{true}} \]

Probability 0.67 for the right class costs 0.40; 0.09 costs 2.41; 0.999 costs 0.001. Gentle when right, brutal when confidently wrong: one badly labelled example can dominate a batch.

The gradient is the part to memorise, because it says what the network feels:

\[ \frac{\partial L}{\partial z} = p - y \]

Probabilities minus one-hot. At \(p = (0.67, 0.24, 0.09)\) with the first class true, the push on the logits is \((-0.33, 0.24, 0.09)\): raise the right score by the remaining doubt, lower each wrong score by exactly the belief it wrongly received. When the model is certain and right, the gradient is zero and that example stops teaching.

Perception has the same rule. Luce's choice axiom says the probability of picking an option is its strength divided by the total strength of all options; softmax is that rule with strength \(e^{z}\). Where it breaks: logits are not measured evidence, and the probabilities are honest confidences only if training made them so.

**In practice.** Karpathy's recipe starts with a check you can do in your head: at random initialization the model knows nothing, every class gets about \(1/10\), and the first printed loss should be \(-\log(1/10) = 2.303\). If it reads 27, the logits are too large at the start (lesson 5). If it later settles near 1.46 and refuses to fall, you applied a softmax *before* `nn.CrossEntropyLoss`: that loss takes logits and does its own softmax, so your probabilities in \([0, 1]\) were squashed twice and the largest possible logit gap became 1.

## Try it

<div class="visual"><iframe src="../visuals/w03-softmax-surprise.html" title="Logits to probabilities to surprise" loading="lazy"></iframe></div>

Predict first, then drag:

1. Logits \((2, 1, 0)\), true class A. Predict the loss, then read it. Add 3 to every logit: what changes?
2. Make C the true class and drag its logit to −3. How high does the loss go, and what does the gradient on that logit read?
3. Set the scale to 4×. Predict the loss when the model is right, and when it is wrong.

## Retrieval

??? question "Logits (1, 1, 3) and the true class is the third. Compute the probabilities and the loss roughly."
    \(e^z \approx (2.7, 2.7, 20.1)\), total 25.5, so \(p \approx (0.11, 0.11, 0.79)\). Loss \(= -\log 0.79 \approx 0.24\).

??? question "What is the gradient of cross-entropy with respect to the logits, and what does its sign pattern do to the scores?"
    \(p - y\), probabilities minus one-hot. The true class is pushed up by its remaining doubt; each wrong class is pushed down by the probability it was wrongly given.

??? question "Ten classes, first printed loss 2.30. Later it plateaus at 1.46. Diagnose both numbers."
    2.30 is \(-\log(1/10)\): correct, the model starts knowing nothing. 1.46 is the floor when a softmax is applied before the loss function's own softmax. Remove the extra one.

## Sources

- [Karpathy: makemore 1](https://www.youtube.com/watch?v=PaCmpygFfXo): from about 0:50, negative log-likelihood; from about 1:20, logits and softmax.
- [Karpathy: A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/): section 2, "verify loss @ init", 3 min.
- [d2l 4.1 Softmax regression](https://d2l.ai/chapter_linear-classification/softmax-regression.html): sections 4.1.1 and 4.1.2, 12 min.

## Ledger prompt

> Next to `core-dl`: pick a discrimination task from your own studies (which of four haptic patterns did the participant feel?). Write its label as one-hot and say what a "surprise of 2.3" would mean for one trial.

**Next:** why one batch's gradient is noisy, and the two optimizers that smooth it out.
