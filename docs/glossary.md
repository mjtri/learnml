---
title: Glossary
---

# Glossary

Every dotted-underlined word in a lesson opens its definition when tapped. This page is the same list, A–Z, with the lesson that introduced each word.

## A

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

## C

<div class="gl-entry" id="chain-rule" markdown>
**chain rule**

When one quantity affects another through a chain of steps, the overall sensitivity is the product of the step-by-step sensitivities.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="colab" markdown>
**Colab**

Google Colaboratory: free hosted Python notebooks in the browser, with an optional GPU. Where the weekly build sessions run.

<small>first met in [week-01/build](week-01/build.md) · canvas card `core-tooling`</small>
</div>

<div class="gl-entry" id="computation-graph" markdown>
**computation graph** <small>(also: computation graphs, computational graph)</small>

A drawing of a calculation as boxes (operations) joined by arrows (values). PyTorch records one as your code runs.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
</div>

<div class="gl-entry" id="converge" markdown>
**converge** <small>(also: converges, converged, convergence)</small>

To settle down: the loss stops improving meaningfully because the parameters have reached a low point.

<small>first met in [week-01/day-5](week-01/day-5.md) · canvas card `core-optim`</small>
</div>

## D

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

<div class="gl-entry" id="element-wise" markdown>
**element-wise** <small>(also: elementwise)</small>

An operation applied separately to each matching pair of numbers in two tensors, such as adding two images pixel by pixel.

<small>first met in [week-01/day-1](week-01/day-1.md)</small>
</div>

## F

<div class="gl-entry" id="feature" markdown>
**feature** <small>(also: features)</small>

One number that describes something about an input, such as a pixel's brightness or, deeper in a network, how strongly a learned pattern is present.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="forward-pass" markdown>
**forward pass**

Running the calculation from inputs to output, storing intermediate values along the way.

<small>first met in [week-01/day-4](week-01/day-4.md) · canvas card `core-calc`</small>
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

## I

<div class="gl-entry" id="inference" markdown>
**inference**

Using a trained model to produce outputs, with no learning happening. Only the forward pass runs.

<small>first met in [week-01/day-4](week-01/day-4.md)</small>
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

## P

<div class="gl-entry" id="parameter" markdown>
**parameter** <small>(also: parameters)</small>

Any number inside a model that training is allowed to change. Weights are parameters. A 7B model has seven billion of them.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>

<div class="gl-entry" id="pytorch" markdown>
**PyTorch**

The Python library this course uses for tensors, automatic gradients and neural networks. Imported as torch.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-tooling`</small>
</div>

## S

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

<div class="gl-entry" id="slope" markdown>
**slope** <small>(also: slopes)</small>

Rise over run: how steep a curve is at a point. The derivative is the slope of the curve at that point.

<small>first met in [week-01/day-3](week-01/day-3.md) · canvas card `core-calc`</small>
</div>

## T

<div class="gl-entry" id="tensor" markdown>
**tensor** <small>(also: tensors)</small>

A box of numbers arranged along zero or more axes. A single number, a list, a table and a stack of images are all tensors.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

<div class="gl-entry" id="training" markdown>
**training**

Repeatedly adjusting a model's parameters to lower the loss on example data.

<small>first met in [week-01/day-5](week-01/day-5.md)</small>
</div>

## V

<div class="gl-entry" id="vector" markdown>
**vector** <small>(also: vectors)</small>

A list of numbers; a tensor with one axis. Like one frame of readings from a row of sensors.

<small>first met in [week-01/day-1](week-01/day-1.md) · canvas card `core-linalg`</small>
</div>

## W

<div class="gl-entry" id="weight" markdown>
**weight** <small>(also: weights)</small>

A learnable number that says how strongly one input contributes to one output. A model's knowledge lives in its weights.

<small>first met in [week-01/day-2](week-01/day-2.md)</small>
</div>
