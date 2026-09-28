---
title: Lesson 5 · The five-line training loop
terms: [training loop, epoch, loss curve]
card: core-calc
---

# Lesson 5 · The five-line training loop

<p class="recall" markdown>**Previously:** a neuron is a weighted sum with a bend; stack them into an MLP and XOR becomes learnable.</p>

## Idea

On the table: a model made of Values, the MSE loss from week 1, a backward pass, and the rule that you zero before you walk. The **training loop** is those pieces in a fixed order, five lines, the same five from a 17-parameter XOR net to a billion-parameter model. The skill to take from this lesson is reading the **loss curve** it draws: the plot that says which line is wrong.

## Mechanism

\[ \text{forward} \to \text{loss} \to \text{zero grads} \to \text{backward} \to \text{update} \]

```python
for step in range(400):
    preds = [model(x) for x in xs]              # 1 forward
    loss = sum((p - y) * (p - y)
               for p, y in zip(preds, ys))      # 2 loss
    for p in model.parameters(): p.grad = 0.0   # 3 zero
    loss.backward()                             # 4 backward
    for p in model.parameters():
        p.data -= 0.05 * p.grad                 # 5 update
```

Zero *before* backward, or lesson 3's stale gradient joins in. Update *after* backward, or you step along last step's gradient. The update touches `p.data` directly so it is not recorded into the graph. Line 2 adds the squared errors over the four XOR points; divide by four and it is MSE. Each pass through the whole data set is an **epoch**. Four points fit in one step, so here one step *is* one epoch; from week 3 an epoch becomes many steps over pieces of the data.

Reading the curve, loss against step on a log scale. Four shapes cover most of what you will see:

- **Falls, then flattens at a floor.** Learning, then done; the floor is noise.
- **Flat from step 0.** Gradients are zero or tiny: learning rate too small, every tanh saturated, or every ReLU at 0.
- **Falls, climbs, then NaN.** Steps too large, or the zeroing line is missing.
- **Flat at a plateau, then a sudden drop.** A symmetric half-solution. On XOR with MSE the plateau sits near 0.25, the score of "predict 0.5 for everything" *and* of "three of four right". The drop is the hidden units finally taking different jobs.

**In practice.** Your Colab log this week (loss divided by four) reads `step 0 loss 0.80`, `step 50 loss 0.14`, `step 150 loss 0.013`, `step 350 loss 0.002`: a fast fall, then a long slow tail. In PyTorch lines 3–5 shrink to three calls, `opt.zero_grad()`, `loss.backward()`, `opt.step()`; in any training script, find those three first.

One thing the loop quietly requires is this week's canvas move: every piece must be smooth. The loss measures *how far* each prediction is from its target, not *how many* are wrong, because "number wrong" has a derivative of zero almost everywhere and jumps at the rest: no slope to descend. The bend is tanh, not a hard threshold, for the same reason. Replacing hard, discrete things with soft, differentiable ones is the move that makes all of this work. A closed-loop calibration on a haptic rig is an honest analogy for the loop itself, with one break: there the plant is fixed and one gain is tuned; here the plant *is* what is being tuned.

## Try it

<div class="visual"><iframe src="../visuals/w02-training-loop.html" title="Press the five stages in order and watch the loss curve" loading="lazy"></iframe></div>

Predict first, then press:

1. Press the five stage buttons in order once. Then press **5 update** before **4 backward**: predict what the readout says, then see.
2. Set the learning rate to 0.5 and run 60 steps. Predict the shape of the curve before pressing Run.
3. Turn **zero grads** off and run 60 steps at 0.05. Predict the step at which the curve turns upward.

## Retrieval

??? question "Write the five lines of the training loop in order and name the two orderings you must never swap."
    Forward, loss, zero grads, backward, update. Never backward before zeroing (stale gradients add in), never update before backward (you would step along the previous gradient).

??? question "An XOR loss curve sits flat near 0.25 for 80 steps, then drops to 0.01. What was happening during the plateau?"
    The model was parked at a symmetric half-solution, where the gradient is small. The drop is the hidden units taking different jobs.

??? question "Why can you not use the number of wrong answers as the loss?"
    Its derivative is zero almost everywhere and undefined at the jumps, so gradient descent has no slope to follow. A smooth stand-in such as MSE is the discrete-to-continuous move.

## Sources

- [Karpathy: micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0): about 1:51–2:14, "creating a tiny dataset, writing the loss function" through "doing gradient descent optimization manually": the five lines typed live.
- [PyTorch tutorial: Optimizing model parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html): the "Full implementation" section only. 8 min.
- [3Blue1Brown: Gradient descent, how neural networks learn](https://www.3blue1brown.com/lessons/gradient-descent): 21 min; rewatch after building the loop.

## Ledger prompt

> Next to `move-discrete-continuous`: name one hard threshold or count in your own evaluation pipeline and write its soft, differentiable stand-in. What does the stand-in measure that the count did not?

**Next:** build session: rebuild micrograd from memory, train it on XOR and on moons, and check every gradient against PyTorch.
