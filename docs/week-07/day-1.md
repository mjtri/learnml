---
title: Lesson 1 · The Hub, model cards, and what a checkpoint contains
terms: [Hugging Face Hub, model card, checkpoint files, pretraining, fine-tuning, transfer learning]
card: lin-bert
---

# Lesson 1 · The Hub, model cards, and what a checkpoint contains

<p class="recall" markdown>**Previously:** text becomes tokens by learned merges, loss falls as a straight line on log–log axes, and a component removed on purpose tells you what it was for.</p>

## Idea

Until 2018 every language task trained its own model from scratch, so 300 labelled lab trials were never enough. The reframe behind BERT: somebody with a data centre runs **pretraining** once, on trillions of tokens, and everyone else starts from the saved result. The **Hugging Face Hub** is where those results live, one git repository per model, with a **model card** as its README. This lesson: what is inside one, and what you can do with it.

## Mechanism

Open the Hub page for SmolLM2-360M and tap *Files*. Every model repository has this skeleton:

| File | What it is | Size here |
|---|---|---|
| `config.json` | the architecture as numbers: 32 layers, width 960, vocabulary 49 152 | 689 B |
| `model.safetensors` | the weights, a dictionary of named tensors | 724 MB |
| `tokenizer.json`, `vocab.json`, `merges.txt` | the text → token rules, fixed at pretraining | 3.4 MB |
| `README.md` | the model card | 7 KB |

The first three rows are the **checkpoint files**: the config to build an empty model, the weights to fill it, the tokenizer to feed it. Lose any one and the other two are useless: weights without a config have no shapes to load into; the wrong tokenizer gives ids that index the wrong rows of the embedding table, gibberish without an error.

The size is arithmetic you already own: 362 million parameters × 2 bytes = 724 MB, so the weights are stored in 16-bit, not 32.

The model card answers three questions before you write code: the pretraining data (here 4 trillion tokens of web text, code and maths), the licence (Apache 2.0), and the scores, measured with no task-specific training.

Three things you can do with a checkpoint, the plan for the week:

1. **Prompt it.** No weight changes; GPT-3's move.
2. **Read its hidden states and train something tiny on top.** No weight changes, no GPU. Lessons 2 and 3.
3. **Fine-tuning.** Keep training the weights on your data with a small learning rate. Lesson 4 prices it.

**Transfer learning** is the umbrella name for routes 2 and 3: what the big task taught carries over to your small one.

**In practice**, the card's *How to use* block is six lines, and every Hub card has one:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
ckpt = "HuggingFaceTB/SmolLM2-360M"
tokenizer = AutoTokenizer.from_pretrained(ckpt)
model = AutoModelForCausalLM.from_pretrained(ckpt)
ids = tokenizer.encode("Gravity is", return_tensors="pt")
print(tokenizer.decode(model.generate(ids)[0]))
```

`from_pretrained` downloads the checkpoint files into `~/.cache/huggingface/hub` once, then reads them from there. Because the repository is git, `revision="<commit>"` pins the exact weights.

An honest analogy from your lab: the gaze model that ships in a headset was pretrained on thousands of eyes, then calibrated per wearer; routes 2 and 3 are that calibration. Where it breaks: a calibration adjusts a few numbers and tells you nothing about the pretraining; a checkpoint's card does.

## Try it

<div class="visual"><iframe src="../visuals/w07-checkpoint-routes.html" title="Three ways to use a checkpoint: which fits your labels and your GPU?" loading="lazy"></iframe></div>

Predict first, then tap:

1. Set 300 labelled examples, a 360M model, a free T4. Before reading the verdict, guess the route it recommends and how many weights that route trains.
2. Raise the labels to 50 000. At what count does full fine-tuning become the recommendation?
3. Move the model to 7B parameters. Which routes still fit in 15 GB?

## Retrieval

??? question "A repository's model.safetensors is 2.9 GB and its config says 1.4 billion parameters. Which storage format are the weights in, and how do you know?"
    2.9 GB ÷ 1.4 billion ≈ 2 bytes per parameter: 16-bit. A 32-bit copy would be 5.6 GB.

??? question "Name the three checkpoint files you need to run a model, and say what happens if the tokenizer is the wrong one."
    Config, weights, tokenizer. A wrong tokenizer produces ids that index the wrong embedding rows: the model reads and writes nonsense, and nothing raises an error.

??? question "300 labelled trials, a laptop, no GPU: which route fits, and what does fine-tuning need that the laptop lacks?"
    Route 2, a tiny model on the frozen hidden states: no weight changes, no GPU. Fine-tuning needs memory for gradients and optimizer state on every weight; the other routes run the model forward only.

## Sources

- [HF LLM course, chapter 1: How do Transformers work?](https://huggingface.co/learn/llm-course/chapter1/4): the "Transfer Learning" section, 6 min.
- [SmolLM2-360M model card](https://huggingface.co/HuggingFaceTB/SmolLM2-360M): Model Summary and the Files tab, 5 min.
- [Hub docs: Model Cards](https://huggingface.co/docs/hub/model-cards): the first section, 4 min.

## Ledger prompt

> Next to `lin-bert`: BERT dropped the assumption that labels are the main source of signal. For a lab task with few labels (sorting haptic patterns by felt roughness, say), what unlabelled data exists in quantity that a pretraining stage could learn from first?

**Next:** the two objects behind every Hub model, `AutoTokenizer` and `AutoModel`, and the shapes that flow between them.
