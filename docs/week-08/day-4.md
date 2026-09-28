---
title: "Lesson 4 · PEFT in practice: where, how hard, and folding it back"
terms: [target module, alpha, merge (weights)]
card: core-tooling
---

# Lesson 4 · PEFT in practice: where, how hard, and folding it back

<p class="recall" markdown>**Previously:** LoRA freezes W and learns the change as B times A, starting from B = 0, with the rank r as the budget of directions the change may use.</p>

## Idea

The library turns lesson 3 into four config decisions: *which* matrices get an adapter, *how hard* it pushes, *how much* of its input to drop while training, and whether to fold it back into the weights afterwards. Each has a sensible default and a failure mode, and the defaults are where most "LoRA did nothing" and "LoRA broke my model" stories start.

## Mechanism

**Where: target modules.** A **target module** is a layer chosen by name: `q_proj`, `v_proj`, `k_proj`, `o_proj` in attention, `up_proj`, `gate_proj`, `down_proj` in the MLP block. PEFT matches names as suffixes, so `"q_proj"` hits that projection in every layer. The paper's table 5 fixed the trainable budget and found query plus value best; later practice adapts every linear layer. The rule that survives: more modules at small rank beats one module at large rank.

**How hard: alpha.** The change is scaled before it is added:

\[ h = Wx + \frac{\alpha}{r}\, BAx \]

**Alpha** is a gain. Because it is divided by \(r\), changing the rank does not silently change how strongly the adapter acts. The paper fixed alpha once and never tuned it; the working rule is alpha equal to \(r\) or \(2r\). Doubling alpha is nearly the same as doubling the learning rate for \(A\) and \(B\).

**Dropout.** `lora_dropout` zeroes a random fraction of the adapter's input during training only. With a tiny dataset, 0.05 to 0.1 slows memorising; otherwise leave it at 0.

**Folding back: the weight merge.** After training, \(W + \frac{\alpha}{r} BA\) is itself one matrix. The **weight merge** computes it once and discards the thin matrices, so the model has no extra layers and runs at the base model's speed: the paper's "no inference latency" claim, unlike older adapters inserted in series.

**In practice**, the entire config is one call, and the printout checks your hand count:

```python
from peft import LoraConfig, get_peft_model
cfg = LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05,
                 target_modules=["q_proj"])
model = get_peft_model(base, cfg)
model.print_trainable_parameters()
# trainable params: 524,288 || all params: 1,236,338,688
# || trainable%: 0.0424
merged = model.merge_and_unload()   # plain model again
```

Those printed numbers are the PEFT quicktour's own: a 1-billion model, only `q_proj`, \(r = 8\). Compute the count from lesson 3's formula before reading the line. A misspelled name never prints zero: `get_peft_model` itself fails with `Target modules {'query'} not found in the base model`. `merge_and_unload()` changes layout, not numbers: outputs before and after must agree to floating-point noise, and the build session asserts that. Two things the library will not catch: a merged model can no longer swap adapters, so keep the adapter file; and an adapter is meaningless on a different base model, since \(BA\) was learned relative to one \(W\).

In your lab the target-module choice has an analogue: when a mapping needs recalibration per user, you pick the stage to adjust (sensor gain, encoding, actuator drive), and alpha is the gain on that adjustment. It stops there: a device's stages are engineered to be separable; a model's layers were not.

## Try it

<div class="visual"><iframe src="../visuals/w08-attach-point-picker.html" title="Tap modules in a transformer block, read trainable parameters" loading="lazy"></iframe></div>

Before you tap, guess:

1. Pick **SmolLM2-360M**, \(r = 8\), and tap only `q_proj` and `v_proj`. Predict the trainable count and percentage with lesson 3's formula.
2. Tap every linear module at \(r = 4\). More or fewer trainable numbers than `q_proj` plus `v_proj` at \(r = 64\)?
3. Slide alpha from 8 to 32 at fixed \(r = 8\). What changes in the readout, and what does not?

## Retrieval

??? question "You set target_modules=['query'] on a model whose layers are named q_proj. What happens, and why?"
    `get_peft_model` raises `Target modules {'query'} not found in the base model`: names match as suffixes, 'query' matches nothing, so PEFT refuses.

??? question "Alpha 16 at rank 8, versus alpha 16 at rank 16: which adapter pushes harder per unit of BA, and by how much?"
    The rank-8 one: its scale is 16/8 = 2 against 16/16 = 1, twice as hard. Dividing by r is what keeps the scale comparable across ranks.

??? question "After merge_and_unload, name one thing you gain and one thing you lose."
    Gain: base-model speed with no extra layers. Lose: the ability to detach or swap the adapter; the change is now baked into W.

## Sources

- [PEFT: LoRA developer guide](https://huggingface.co/docs/peft/main/en/developer_guides/lora): "Initialization" and "Post-Training" (merging), 10 min.
- [PEFT: LoraConfig reference](https://huggingface.co/docs/peft/main/en/package_reference/lora): the fields `r`, `lora_alpha`, `lora_dropout`, `target_modules`, 5 min.
- [LoRA paper](https://arxiv.org/abs/2106.09685): section 7.1 and table 5, which matrices to adapt, 8 min.

## Ledger prompt

> Next to `core-tooling`: write the four config decisions as a checklist you would run before any fine-tune, with the check that catches a misspelled module name.

**Next:** the three ways a fine-tune lies to you: forgetting, leakage, and memorising a tiny dataset.
