---
title: Lesson 5 · Fine-tuning failure modes
terms: [catastrophic forgetting, data leakage]
card: bridge-adaptation
---

# Lesson 5 · Fine-tuning failure modes

<p class="recall" markdown>**Previously:** PEFT's config chooses the target modules, alpha scales the update by alpha over r, dropout guards a tiny dataset, and the weight merge folds BA back into W.</p>

## Idea

A fine-tune that "works" can still be wrong in three ways a single number hides. The model can lose what it already knew (**catastrophic forgetting**). The score can be inflated because test data reached the training data (**data leakage**). Or the model can memorise a few hundred examples and generalise to nothing: overfitting at its most acute. Each has a signature in numbers you already log and a cheap check; an evaluation you trust has run all three.

## Mechanism

**Forgetting.** Training on task B changes weights that task A needed. The signature: task-B loss falls while a task-A score on unseen data drops. For a language model, task A is plain text: measure its loss on a fixed paragraph before and after. A rise of a few percent is normal; a doubling is forgetting. LoRA forgets less than full fine-tuning at the same task gain; Biderman and colleagues titled their 2024 study "LoRA learns less and forgets less". Lower rank forgets less still; the remedy is the rank ablation, the smallest \(r\) that reaches the task.

**Leakage.** If any test example, or a near copy, is in the training set, the score measures memory, not skill. Sources: duplicates, one document split across train and test, answers inside the prompts. The signature: a test loss far below the training loss, or a few test items with loss near zero while the rest look ordinary. The check is mechanical: split *by source* first, then hash the test texts and confirm none appear in training. Kapoor and Narayanan found leakage in hundreds of papers across seventeen fields.

**Memorising a tiny dataset.** With 300 examples and a million trainable numbers, the model can store the answers. The signature is week 3's curve: training loss keeps falling, loss on new data turns upward. Remedies, cheapest first: fewer steps, lower rank, dropout, more data.

The fixes conflict: more steps and higher rank fight memorising but worsen forgetting. You choose deliberately, which is why the checks come first.

**In practice.** The build session plants each failure; its leakage check is three lines:

```python
seen = {h(t) for t in train_texts}
leaked = [t for t in test_texts if h(t) in seen]
print(len(leaked), "test items also in train")   # must be 0
# forgetting: loss on a fixed paragraph, before vs after
# memorising: loss on train vs unseen prompts, per step
```

One test prompt is copied into the training set on purpose; after training its loss sits far below its neighbours. That gap, at the scale of a dataset, is a paper that will not replicate.

The `bridge-adaptation` card makes this personal. In a sensory-substitution study, a remapping that erases the earlier mapping is forgetting in a human; leakage is the participant who saw the test stimuli during training; overfitting is the mapping that works only for the ten stimuli it was tuned on. Where it breaks: a human's test set cannot be hashed, and human forgetting is gradual where a model's can be sudden.

## Try it

<div class="visual"><iframe src="../visuals/w08-failure-cards.html" title="Read a run's numbers, name the failure" loading="lazy"></iframe></div>

Before you tap a diagnosis, commit to it:

1. Card 1 shows training loss 0.4, loss on new prompts 0.35, base-text loss doubled. Name the failure before revealing.
2. Find the card where three test items have loss near zero. What single check would have caught it before training?
3. After all eight cards, which failure did you misdiagnose most? Write that check first.

## Retrieval

??? question "Task-B loss fell from 2.1 to 0.9; the base model's loss on a fixed plain paragraph went from 3.0 to 6.5. What happened, and what is the cheapest fix?"
    Catastrophic forgetting: the fine-tune overwrote general ability. Cheapest fix: lower the rank or stop earlier, then re-measure.

??? question "Loss on the test rows is 0.3 while training loss is 0.8. What do you suspect, and what is the mechanical check?"
    Data leakage: test items reached the training set. Hash the test texts and count how many appear in training; the count must be zero.

??? question "Why do the remedies for memorising and for forgetting pull in opposite directions?"
    Memorising is fought with fewer steps and lower rank; forgetting also wants lower rank but worsens with more steps. Both push toward the smallest rank that reaches the task.

## Sources

- [LoRA Learns Less and Forgets Less](https://arxiv.org/abs/2405.09673): abstract and figure 1, 8 min.
- [Kapoor and Narayanan: Leakage and the reproducibility crisis](https://arxiv.org/abs/2207.07048): abstract and the taxonomy table, 10 min.
- [Kirkpatrick et al.: Overcoming catastrophic forgetting](https://arxiv.org/abs/1612.00796): abstract and figure 1 only, 5 min.

## Ledger prompt

> Next to `bridge-adaptation`: the card proposes per-user calibration of a codec. Write the three checks as they would apply to that study, with the number each one reads.

**Next:** the build session: LoRA-tune a small language model, plant the three failures, ablate r in {1, 4, 16} with two seeds.
