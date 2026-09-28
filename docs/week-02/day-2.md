---
title: "Lesson 2 · Backward: local × upstream, in order"
terms: [topological order]
card: core-calc
---

# Lesson 2 · Backward: local × upstream, in order

<p class="recall" markdown>**Previously:** a Value is a number plus its history: the parents that made it and the operation that did.</p>

## Idea

The graph is built. Now the walk. Each node gets one small job: once it knows how sensitive the loss is to *itself*, it hands each parent their share, its own local derivative times that incoming number. The rule is week 1's chain rule; what is new is bookkeeping. Who starts, and in what order? A **topological order**: list the nodes so every node comes after everything it was made from, then walk that list backward from the loss.

## Mechanism

Each operation, when it creates its output node, also attaches a tiny function to it: `_backward`. It knows the local derivative because the operation that wrote it knows its inputs. For `out = a + b` both parents receive `out.grad`. For `out = a * b` each parent receives the *other's* value times `out.grad`. For `out = tanh(a)` the parent receives \((1 - \text{out}^2)\) times `out.grad`. Week 1's table of slopes, stored as code:

\[ \text{parent.grad} \mathrel{+}= \text{local derivative} \times \text{out.grad} \]

(The `+=` is the next lesson.) A node's `_backward` may only run once its own `grad` is final, so the order is forced. Same graph, \(d = a \times b,\ e = d + c,\ L = e \times e\). A topological order is `a, b, d, c, e, L`: every node after its parents. Reverse it and walk:

1. `L.grad = 1`. Every backward pass starts with this 1; forget it and every gradient stays 0.
2. `L._backward()`: `e` receives \(e \times 1\) twice, so `e.grad` = 8.
3. `e._backward()`: add copies, `d.grad` = 8 and `c.grad` = 8.
4. `d._backward()`: multiply swaps, `a.grad` = \(8 \times b = -24\), `b.grad` = \(8 \times a = 16\).

The same \((-24, 16, 8)\) as week 1, from closures that each knew only their own inputs. Now run `d._backward()` *before* `e._backward()`: `d.grad` is still 0, so `a` and `b` receive 0 and learn nothing this step. The failure mode is silence.

**In practice.** The entire `backward` method in micrograd's `engine.py`, unchanged. The order is built by a depth-first visit: add a node only after all its parents, so leaves come first and the loss last:

```python
def backward(self):
    topo, visited = [], set()
    def build_topo(v):
        if v not in visited:
            visited.add(v)
            for child in v._prev:
                build_topo(child)
            topo.append(v)
    build_topo(self)
    self.grad = 1
    for v in reversed(topo):
        v._backward()
```

The `visited` set matters: `e` is reached twice from `L` and must be listed once.

Week 1's pipeline picture holds, and it is the same mathematics: to blame the tracker for an error on the display, you first need how much the display blames the renderer, and the renderer the filter. Blame flows against the data, one complete stage at a time. Where the picture is thinner than the code: a pipeline is a chain, while a real graph branches and merges, and merging is where the order stops being obvious.

## Try it

<div class="visual"><iframe src="../visuals/w02-backward-order.html" title="Tap the nodes in the order the backward pass must visit them" loading="lazy"></iframe></div>

Predict first, then tap:

1. Write down an order for the six nodes before touching anything, then tap it in. A wrong tap tells you which gradient was not yet complete.
2. More than one order is valid. Find two. Which pairs of nodes can swap, and why does it not matter?
3. Set \(b = 0\) and walk again. Predict what `a` receives at the multiply node, then check.

## Retrieval

??? question "For out = a * b, what does each parent receive from out's _backward, in words?"
    `a` receives `b.data` times `out.grad`; `b` receives `a.data` times `out.grad`. Each gets the incoming gradient times the other input's value.

??? question "Give a topological order for d = a·b, e = d + c, L = e·e, and the order the backward pass runs."
    One valid order is `a, b, d, c, e, L` (`c` may sit anywhere before `e`). Backward runs the reverse, `L, e, c, d, b, a`, so every node's gradient is complete before its `_backward` runs.

??? question "What goes wrong if d._backward runs before e._backward, and how would you notice?"
    `d.grad` is still 0, so `a` and `b` receive 0 and do not learn. Nothing errors; you notice from parameters that never move, or by checking against a numerical gradient.

## Sources

- [Karpathy: micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0): about 1:09–1:22, "implementing the backward function for each operation" and "for a whole expression graph".
- [Olah: Calculus on computational graphs](https://colah.github.io/posts/2015-08-Backprop/): the "Factoring paths" section, 5 min.
- [3Blue1Brown: Backpropagation calculus](https://www.3blue1brown.com/lessons/backpropagation-calculus): 10 min.
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/), chapter 7, sections 7.1–7.4, in proper notation (verify).

## Ledger prompt

> Next to `core-calc`: write the topological order of your own three-stage pipeline from week 1, then the reverse. Which stage would you have to instrument first to get blame numbers out of it?

**Next:** why the closures say `+=`, and the bug that follows if you forget to reset.
