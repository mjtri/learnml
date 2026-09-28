---
title: "Lesson 2 · AutoTokenizer / AutoModel: shapes in, shapes out"
terms: [AutoTokenizer, AutoModel, config, hidden state]
card: core-tooling
---

# Lesson 2 · AutoTokenizer / AutoModel: shapes in, shapes out

<p class="recall" markdown>**Previously:** a Hub checkpoint is three files, config plus weights plus tokenizer, and a model card that says what it was trained on; you can prompt it, read its insides, or fine-tune it.</p>

## Idea

The Hub holds hundreds of architectures; you never need to know which class implements which. **AutoTokenizer** and **AutoModel** read the repository's files and hand back the right objects. Every model is then the same two-object pipeline, and the lesson is three shapes: batch × tokens in, batch × tokens × width inside, batch × tokens × vocabulary out.

## Mechanism

The **config** is `config.json` loaded as an object. For SmolLM2-135M, `model.config` says `hidden_size` 576, `num_hidden_layers` 30, `vocab_size` 49 152. Those three numbers fix every shape below.

```python
tok = AutoTokenizer.from_pretrained(ckpt)
model = AutoModel.from_pretrained(ckpt)
enc = tok(["Gravity is", "The glove buzzed twice"],
          return_tensors="pt", padding=True)
enc["input_ids"].shape           # (2, 5)        B × T
out = model(**enc, output_hidden_states=True)
out.last_hidden_state.shape      # (2, 5, 576)   B × T × d
len(out.hidden_states)           # 31: embedding + 30 layers
```

Read it top down. The tokenizer returns a batch \(B\) of \(T\) ids, the shorter text padded to the same length, plus an `attention_mask` of the same shape: 1 on real tokens, 0 on padding. The model returns a **hidden state** per token per layer, the residual stream of week 5 caught after every block, each shaped \((B, T, d)\). Index 0 is the embedding before any block; index 30 is the last.

**AutoModel is the bare transformer; the *ForCausalLM* variant adds the output layer.** `AutoModelForCausalLM` returns everything above plus `.logits` of shape \((B, T, V)\), a score for every vocabulary entry at every position. Notice the size: one sequence of 8 192 tokens gives \(8192 \times 49152\) scores, 1.6 GB in 32-bit, bigger than the model. When you only want features, load `AutoModel` and skip it.

**In practice**, the first thing that breaks is padding. For SmolLM2 and most decoder models, `padding=True` raises:

> `ValueError: Asking to pad but the tokenizer does not have a padding token.`

The fix is one line, `tok.pad_token = tok.eos_token`. The second break is quieter: with `padding_side` at `right`, position \(-1\) of a shorter row is a pad token, so `hidden_states[-1][:, -1]` reads padding, not the last word. Use the `attention_mask` to find each row's real last token, or average over the real ones. Nothing errors.

The parameter count is in the config too, with a twist. Week 5's rule gives \(12 \times 576^2 \times 30 = 119\)M plus a 28M embedding table: 148M. The model reports 134.5M, because `intermediate_size` 1536 makes the MLP narrower than the usual 4× and `num_key_value_heads` 3 lets 9 attention heads share 3 sets of keys and values. The rule gets you within 10 %; the config gets you exact.

## Try it

<div class="visual"><iframe src="../visuals/w07-shapes-explorer.html" title="Pick a Hub model and a batch; read every shape from input ids to output scores" loading="lazy"></iframe></div>

Predict first, then tap:

1. Before tapping **SmolLM2-360M**, guess how many hidden states come back, and their shape, for 4 sentences padded to 12 tokens.
2. Set \(T\) to 8 192 and \(B\) to 1. Guess the size of `logits` in MB before you read it; then compare it with the weights.
3. Switch to **GPT-2 small** and predict whether the parameter readout lands above or below the 12 per block rule, and why.

## Retrieval

??? question "A batch of 4 sentences padded to 12 tokens goes through SmolLM2-360M (32 layers, width 960). Give the shape of input_ids, the shape of one hidden state, and how many hidden states come back."
    (4, 12); (4, 12, 960); 33, the embedding plus one per layer.

??? question "What does AutoModelForCausalLM return that AutoModel does not, what shape is it, and when should you avoid asking for it?"
    `.logits`, shaped batch × tokens × vocabulary. Skip it when you only need hidden states; it is often the largest tensor in the run.

??? question "The padding error appears and you fix it with the eos token. What new silent problem does right-side padding create, and how do you avoid it?"
    Position −1 of shorter rows is now a pad token, so reading the last position reads padding. Use the attention mask to find each row's real last token, or average over real tokens only.

## Sources

- [HF LLM course, chapter 2: Behind the pipeline](https://huggingface.co/learn/llm-course/chapter2/2): from "Preprocessing with a tokenizer" to "A high-dimensional vector?", 10 min.
- [Transformers docs: Auto Classes](https://huggingface.co/docs/transformers/model_doc/auto): the first section only, 4 min.
- [Transformers docs: Model outputs](https://huggingface.co/docs/transformers/main_classes/output): the opening example, 4 min.

## Ledger prompt

> Next to `core-tooling`: write the input and output of one model in your own pipeline (a gesture classifier, a gaze predictor) in the same B × T × d form. Which axis is the batch there, and what plays the role of the tokenizer?

**Next:** those hidden states are features; one linear layer on top of a frozen model is the cheapest experiment in machine learning.
