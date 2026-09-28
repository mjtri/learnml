---
title: Lesson 3 · Hidden states as features; the linear probe
terms: [linear probe, frozen weights]
card: lin-gpt3
---

# Lesson 3 · Hidden states as features; the linear probe

<p class="recall" markdown>**Previously:** the tokenizer gives batch × tokens ids, the model gives batch × tokens × width hidden states, one per layer, and right-side padding makes the last position lie.</p>

## Idea

Where is the knowledge in a pretrained model? Not in the words it emits but in the vectors between the layers. A **linear probe** is the cheapest experiment there is: fix the model's weights, take one layer's hidden state for each example, and fit a single linear layer to your labels. If a straight boundary separates the classes, that layer already holds the distinction in a readable form. No gradient reaches the model, so no fine-tuning memory, no GPU, and 300 labelled examples are often enough: lesson 1's route 2.

## Mechanism

Four steps:

1. **Pool.** Each example is \((T, d)\); reduce it to one vector by the mean over real tokens (using the attention mask) or the last real token's hidden state.
2. **Split.** Hold back 20 % of the examples that the probe never sees.
3. **Fit.** One linear layer from \(d\) to the number of classes, trained by gradient descent on the 80 %. Everything under it has **frozen weights**.
4. **Report** held-back accuracy against chance, for every layer.

The probe's prediction is

\[ \hat y = \arg\max_c \,(W h + b)_c \]

with \(h\) the pooled hidden state and \(W\) shaped classes × \(d\). For SmolLM2-135M and two classes that is \(576 \times 2 + 2 = 1154\) trained numbers on top of 135 million untouched ones. Small enough that a laptop fits it in a second, and too small to invent a distinction the features do not already contain: a probe measures the features, not itself.

Read the per-layer curve, not one number. The embedding probes poorly, because it knows single tokens and not their combination; accuracy climbs through the early blocks, and for sentiment on a small language model it often peaks in the middle and dips at the end, where the layers are shaped for guessing the next token.

**In practice**, the pooling line is where notebooks go wrong:

```python
H = out.hidden_states[layer]          # (B, T, d)
m = enc["attention_mask"][..., None]  # (B, T, 1), 1 = real
feat = (H * m).sum(1) / m.sum(1)      # masked mean: (B, d)
probe = torch.nn.Linear(d, 2)         # the only trained bit
```

Without the mask, padding pulls every short sentence's mean towards the same point, and the probe learns sentence length instead of sentiment.

A caveat from the papers: a working probe shows the information is *linearly readable* at that layer, not that the model *uses* it; a failing probe shows only that a straight boundary cannot read it. Two checks make a claim honest: shuffle the labels and confirm held-back accuracy falls to chance, and run the same probe on a randomly initialised copy of the model.

The honest analogy is neural decoding: a linear decoder from recorded activity to the stimulus shows the region carries the information. Same logic, same caveat. Where it breaks: a probe sees every unit without noise; an electrode array samples a few hundred cells.

## Try it

<div class="visual"><iframe src="../visuals/w07-probe-boundary.html" title="Hidden states projected to 2-D: drag a boundary, then let the probe fit one" loading="lazy"></iframe></div>

Predict first, then tap:

1. Before choosing a layer, guess whether the **embedding** or **layer 4** separates the two classes better, and by how many points.
2. Drag the boundary for the best accuracy you can, write the number down, then tap **fit probe** and compare.
3. Pick the **last layer**. Better or worse than the middle? Then tap **shuffle labels** and predict the fitted accuracy before it appears.

## Retrieval

??? question "SmolLM2-135M, width 576, three classes. How many parameters does the probe train, and how many stay frozen?"
    576 × 3 + 3 = 1731 trained; about 135 million frozen.

??? question "A probe reaches 90 % on layer 12 and 60 % on the embedding. What does this say about where the distinction is computed, and what does it not say?"
    The blocks between the embedding and layer 12 make it linearly readable, so they compute it. It does not say the model uses it, nor that layer 0 lacks it in a nonlinear form.

??? question "Why average over real tokens with the mask instead of reading position −1 of a right-padded batch?"
    Position −1 of a shorter row is padding. The masked mean builds each example's vector from its own tokens only, so the probe cannot learn sentence length by accident.

## Sources

- [Alain & Bengio 2016: Understanding intermediate layers using linear classifier probes](https://arxiv.org/abs/1610.01644): abstract and figure 1, 5 min.
- [Belinkov 2022: Probing Classifiers: Promises, Shortcomings, and Advances](https://arxiv.org/abs/2102.12452): sections 1 and 2, 10 min.
- [Tenney et al. 2019: BERT Rediscovers the Classical NLP Pipeline](https://arxiv.org/abs/1905.05950): figure 1 only, 3 min.

## Ledger prompt

> Next to `lin-gpt3`: GPT-3 dropped "new tasks need gradient updates"; the probe drops it too, by reading instead of prompting. For one classification task on your data, which would you try first, and what accuracy would make you switch?

**Next:** what full fine-tuning actually runs, and the byte arithmetic that says whether a free T4 can hold it.
