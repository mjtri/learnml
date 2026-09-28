---
title: "Lesson 3 · LoRA: freeze W, learn BA"
terms: [LoRA, adapter, PEFT]
card: lin-lora
---

# Lesson 3 · LoRA: freeze W, learn BA

<p class="recall" markdown>**Previously:** the SVD writes any matrix as a sum of stretches sorted by strength, and keeping the first k gives the best rank-k approximation.</p>

## Idea

Fine-tuning the old way touches every weight: optimizer state for billions of numbers and a full copy of the model per task. **LoRA** starts from an observation: the *change* fine-tuning makes to a weight matrix is nearly low rank. So leave the original matrix frozen and learn only the change, written as two thin matrices. Trainable numbers drop by a factor of hundreds, one base model serves many tasks, and the result runs as fast as before. This is the `lin-lora` card: the dropped assumption is that adaptation needs full-rank changes.

## Mechanism

A linear layer computes \(h = Wx\). Fine-tuning would replace \(W\) with \(W + \Delta W\). LoRA keeps \(W\) frozen and writes the change as a product of two thin matrices:

\[ h = Wx + BAx, \qquad B \in \mathbb{R}^{d \times r},\; A \in \mathbb{R}^{r \times d} \]

Frozen: \(W\), every original weight, no gradients, no optimizer state. Trains: \(A\) and \(B\), reached by the same chain rule as always, for one extra thin multiply. Two details make it work:

1. **Start at zero.** \(B\) is initialized to zeros and \(A\) to small random numbers, so \(BA = 0\) and the model begins exactly where the pretrained one was.
2. **Rank is the budget.** \(r\) fixes how many independent directions the change may use. The paper's table 6 shows \(r = 1\) already competitive when query and value are both adapted, and \(r = 64\) barely better.

Napkin arithmetic. A \(d \times d\) matrix with \(d = 4096\) holds 16.8 million weights. LoRA with \(r = 8\) trains \(r(d + d) = 65{,}536\), 0.4 percent. Apply that to two matrices in each of 32 layers and the whole change is 4.2 million numbers, 17 MB in 32-bit, against 32 GB for a full 32-bit copy of an 8-billion model. The paper's headline is the same sum at GPT-3 scale: 10,000 times fewer trainable parameters and a 35 MB checkpoint instead of 350 GB. That small file is the **adapter**: swap it and the same frozen model does a different job.

**In practice**, the method is a wrapper around one linear layer; the build session writes this class and checks it against the library:

```python
class LoRALinear(nn.Module):
    def __init__(self, base, r):
        super().__init__()
        self.base = base.requires_grad_(False)   # frozen W
        d_in, d_out = base.in_features, base.out_features
        self.A = nn.Parameter(torch.randn(r, d_in) * 0.01)
        self.B = nn.Parameter(torch.zeros(d_out, r))
    def forward(self, x):
        return self.base(x) + x @ self.A.T @ self.B.T
```

The library is **PEFT** from Hugging Face; the next lesson shows its knobs. Note the order in `forward`: \(x\) meets \(A\) first, so the intermediate is only \(r\) wide; `x @ (B @ A).T` would build the full \(d \times d\) change in memory.

The `bridge-adaptation` card's analogy is honest. In a sensory-substitution study the user is the frozen model: you do not retrain a cortex. What you tune per user is the device mapping, a small learned delta between the same sensor and the same skin: a thin adapter. Where it breaks: a brain keeps adapting on its own, while a LoRA base model cannot change at all.

## Try it

<div class="visual"><iframe src="../visuals/w08-lora-calculator.html" title="Trainable parameters of ΔW = BA against the full matrix" loading="lazy"></iframe></div>

Before you slide, guess:

1. Set a \(896 \times 896\) matrix (one Qwen2.5-0.5B query projection) and \(r = 8\). Predict the percentage of the matrix that trains.
2. Raise \(r\) until the adapter costs *more* than the matrix. Predict that crossover rank first.
3. Make the matrix \(960 \times 320\). Does the saving depend on the shape or only on \(r\)?

## Retrieval

??? question "A 2048×2048 weight matrix gets a LoRA adapter with r = 4. How many numbers train, and what fraction of the matrix is that?"
    4 × (2048 + 2048) = 16,384 numbers against 4,194,304: about 0.4 percent.

??? question "Why is B set to zero at the start rather than random, and what would go wrong otherwise?"
    So that BA is zero and the model starts as the pretrained one. Random B would perturb every chosen layer before training, wrecking the behaviour it is meant to keep.

??? question "Name one thing LoRA saves besides trainable parameters, and one thing it does not save at all."
    It saves optimizer memory and checkpoint size and keeps inference speed. It does not save memory for the frozen weights: the base model still has to fit.

## Sources

- [LoRA paper](https://arxiv.org/abs/2106.09685): sections 1 to 4 and table 6, 25 min.
- [PEFT: LoRA conceptual guide](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora): the first section and the figure, 8 min.
- [Raschka: practical tips for finetuning LLMs using LoRA](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms): takeaways 1 and 6, 6 min.

## Ledger prompt

> Next to `lin-lora`: write ΔW = BA in your own words, then state what is frozen, what trains, and why r = 1 can work at all.

**Next:** the library's knobs: which layers get an adapter, the alpha gain, dropout, and folding the adapter back into the weights.
