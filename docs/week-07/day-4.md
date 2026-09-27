---
title: Lesson 4 · Full fine-tuning in outline; memory arithmetic
terms: [memory footprint, fp16]
card: move-adapters
---

# Lesson 4 · Full fine-tuning in outline; memory arithmetic

<p class="recall" markdown>**Previously:** a linear probe reads a frozen model's hidden states through one trained layer; per-layer accuracy says where a distinction becomes readable, not whether the model uses it.</p>

## Idea

Fine-tuning is week 1's training loop pointed at a loaded checkpoint instead of random weights. The code is six lines. The cost is memory: training keeps several numbers per parameter where inference keeps one, and the free T4 has 15 GB. This lesson is the arithmetic that predicts an out-of-memory error before you launch.

## Mechanism

**The loop.** Every weight is trainable, the loss is the same next-token loss the model was pretrained with, and the learning rate is a hundred times smaller than from scratch:

```python
model = AutoModelForCausalLM.from_pretrained(ckpt)
opt = torch.optim.AdamW(model.parameters(), lr=2e-5)
for batch in loader:                  # your texts, tokenized
    out = model(**batch, labels=batch["input_ids"])
    out.loss.backward()               # next-token loss on your data
    opt.step(); opt.zero_grad()
```

`labels=` makes the model shift the ids by one internally and return the loss. The tiny learning rate is the whole philosophy: the weights already sit in a good place, so take small steps rather than leaps that throw the pretraining away.

**The bytes.** The **memory footprint** of a run is parameters × bytes per parameter, and the bytes depend on what you are doing. Per parameter, in 32-bit:

| State | Bytes | Kept during |
|---|---|---|
| the weight itself | 4 | everything |
| its gradient | 4 | training |
| Adam's two running averages | 8 | training |

Inference: 4 bytes per parameter, or 2 in 16-bit. Full fine-tuning with Adam: 16. So

\[ \text{training bytes} \approx N \times 16 \;+\; \text{activations} \]

SmolLM2-135M: \(135\text{M} \times 16 = 2.2\) GB, fine. SmolLM2-1.7B: 27 GB, not on a T4 even before activations. Llama-3 8B: 128 GB. Activations are the hidden states saved for the backward pass; they grow with batch × tokens × width × layers, and a smaller batch or shorter sequences shrink them for free.

**fp16** and bf16 are the 16-bit formats that halve the first row. fp16 can only count to 65 504, so a large activation overflows to infinity and the loss turns NaN; bf16 keeps 32-bit's range with coarser steps and is what recent checkpoints ship in, SmolLM2 included. The catch: the T4 has no bf16 hardware, so check `torch.cuda.is_bf16_supported()` before trusting a recipe written for newer cards.

**In practice**, the error reads:

> `torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.12 GiB. GPU 0 has a total capacity of 14.74 GiB of which 0.55 GiB is free.`

Note the 14.74: a "16 GB" T4 offers under 15. The SmolLM2-360M card prints `model.get_memory_footprint()` as 723.56 MB, 362M × 2 bytes: inference in bf16. Multiply by 8 for a full fine-tune: 5.8 GB plus activations. It fits; a 1.7B does not, the most common reason a first fine-tuning attempt dies.

The way out is to train less: freeze the model and train a probe (lesson 3), or freeze it and train a small piece beside it, which is LoRA, next week, so the 16 bytes are paid only on the piece. The canvas move "reuse a pretrained model cheaply" exists because of this arithmetic.

## Try it

<div class="visual"><iframe src="../visuals/w07-memory-calculator.html" title="Parameters × bytes × what you are doing: does it fit on a T4?" loading="lazy"></iframe></div>

Predict first, then tap:

1. Pick **SmolLM2-360M**, full fine-tune, 32-bit. Guess the GB before reading it, then switch to inference in 16-bit.
2. Slide the parameter count up until the full fine-tune stops fitting in 15 GB; that size is the ceiling next week attacks.
3. Set batch 8 × 2 048 tokens and watch the activations bar. At what batch do they overtake the weights?

## Retrieval

??? question "A 1.7B model: memory for inference in bf16, and for full fine-tuning with Adam in 32-bit, before activations?"
    3.4 GB for inference; 27 GB for training, at 16 bytes per parameter. The T4's 15 GB cannot hold the second.

??? question "The forward pass ran, then the first backward pass raised out-of-memory. Which memory appeared between the two, and name two knobs that shrink it."
    Gradients and Adam's state for every parameter, plus saved activations. Shrink with a smaller batch or shorter sequences, freezing most layers, or training only a small piece.

??? question "Why is a fine-tuning learning rate around 2e-5 when week 1's from-scratch loop used 0.1?"
    The weights already sit near a good minimum. Large steps would throw away the pretraining; small ones adjust it while keeping what it knows.

## Sources

- [Transformers docs: Model training anatomy](https://huggingface.co/docs/transformers/v4.46.0/model_memory_anatomy): "Anatomy of Model's Memory", 6 min.
- [HF LLM course, chapter 3: Fine-tuning a model](https://huggingface.co/learn/llm-course/chapter3/1): the introduction, 4 min.
- [EleutherAI: Transformer Math 101](https://blog.eleuther.ai/transformer-math/): the "Memory Requirements" section, 8 min.

## Ledger prompt

> Next to `move-adapters`: "freeze a big model; train a small module on top or beside it". Which model in your lab could be frozen with a small trainable piece added, and what would the piece be?

**Next:** the three pins that make a run repeatable, seed, config and git hash, and the one-row log that carries them.
