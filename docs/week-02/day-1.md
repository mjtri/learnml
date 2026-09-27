---
title: Lesson 1 · A Value that remembers its history
terms: [Value object, micrograd]
card: core-calc
---

# Lesson 1 · A Value that remembers its history

<p class="recall" markdown>**Previously:** tensors in boxes, mixed by matrices, nudged downhill along the gradient.</p>

## Idea

Last week PyTorch recorded the computation graph for you and walked it backward when asked. This week you build that recorder from nothing. The trick fits in one small class: a **Value object** is a number that also remembers *which two numbers made it, and by which operation*. Do ordinary arithmetic with these objects and the graph builds itself as a side effect. That is **micrograd**, Karpathy's hundred-line engine; PyTorch's autograd is the same idea on whole tensors. Once you have built it, a wrong, zero or exploding gradient stops being magic and becomes a bug in an object you can picture.

## Mechanism

A Value holds four fields. `data` is the number. `grad` is the sensitivity of the final output to this number, zero until a backward pass fills it. `_prev` is the set of parent Values it was computed from. `_op` is the operation that did it.

Python lets a class define what `+` and `*` mean. `a * b` calls `a.__mul__(b)`, which returns a *new* Value whose `data` is the product and whose parents are `(a, b)`. Take week 1's graph, with \(a = 2,\ b = -3,\ c = 10\):

\[ d = a \times b \qquad e = d + c \qquad L = e \times e \]

Each line creates one node that knows its parents and its operation. Six objects, five arrows, and the forward pass is done: \(d = -6,\ e = 4,\ L = 16\). No gradient exists yet; the graph is there whether or not you ever ask for one.

```python
class Value:
    def __init__(self, data, prev=(), op=""):
        self.data, self.grad = data, 0.0
        self._prev, self._op = set(prev), op
    def __add__(self, o):
        return Value(self.data + o.data, (self, o), "+")
    def __mul__(self, o):
        return Value(self.data * o.data, (self, o), "*")

e = Value(2.0) * Value(-3.0) + Value(10.0)
L = e * e      # L._prev == {e}: one parent, used twice
```

Notice the last line: `L`'s parents are a *set*, so `e` appears once although it is used twice; lesson 3 is about what that does to gradients. Notice also the shape: leaves are inputs and weights, the root is the loss. Every graph you will train looks like that.

**In practice.** PyTorch stores the same fields under other names. Run `x = torch.tensor(2.0, requires_grad=True)`, `y = x * 3 + 1`, `print(y.grad_fn)`: it prints `<AddBackward0>`, the `_op` of the last operation, and `y.grad_fn.next_functions` lists the parents, a `MulBackward0` for `x * 3` and `None` for the constant. Without `requires_grad=True`, `y.grad_fn` is `None` and `.backward()` raises *element 0 of tensors does not require grad and does not have a grad_fn*: a backward walk on a Value with no parents.

If you have built a Unity scene, `_prev` has a familiar shape: a Transform keeps a pointer to its parent, and you follow the chain to see how moving the root moves a fingertip. The analogy breaks at lifetime: a hierarchy persists, while a Value graph is rebuilt on every forward pass by whatever code actually ran, then discarded. That is why PyTorch can record Python `if` statements and loops: it records what happened, not what you declared.

## Try it

<div class="visual"><iframe src="../visuals/w02-graph-builder.html" title="Tap operations to build a Value graph, then run backward" loading="lazy"></iframe></div>

Predict first, then tap:

1. Build \((a \times b + c) \times c\). Before tapping, predict how many nodes the graph will have and which node has two arrows leaving it.
2. Set \(a = 2,\ b = -3,\ c = 10\) and predict the root's `data` before the readout shows it.
3. Press **Backward**. You know \(\partial L/\partial a\) for week 1's graph; guess it for this one, then check. The walk itself is the next lesson.

## Retrieval

??? question "Name the four fields of a Value and say which of them ordinary arithmetic fills in."
    `data`, `grad`, `_prev` (parents) and `_op`. Arithmetic fills `data`, `_prev` and `_op` when it creates the new node; `grad` stays 0 until a backward pass.

??? question "For y = x * 3 + 1 with x requiring grad, what does y.grad_fn print, and what does next_functions point at?"
    `<AddBackward0>`, the last operation. `next_functions` holds the parents: a `MulBackward0` for `x * 3` and `None` for the constant 1.

??? question "Why does PyTorch rebuild the graph on every forward pass instead of storing it once like a scene hierarchy?"
    The graph is a record of one particular run. Python control flow can take a different path each time, so PyTorch records the operations that actually executed, then discards the record after backward.

## Sources

- [Karpathy: micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0): about 0:19–0:32, "starting the core Value object of micrograd and its visualization".
- [micrograd `engine.py`](https://github.com/karpathy/micrograd/blob/master/micrograd/engine.py): the first 30 lines only, `__init__`, `__add__` and `__mul__`. 5 min.
- [PyTorch: Autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd.html): the first section, "How autograd encodes the history". 5 min.

## Ledger prompt

> Next to `core-calc`: which computation in your own pipeline (a Unity script, a haptic renderer, an analysis notebook) would you have to rewrite so that every number remembers its parents? What in it is not arithmetic?

**Next:** the backward walk: each node does one small multiplication, in exactly the right order.
