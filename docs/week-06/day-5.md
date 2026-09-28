---
title: "Lesson 5 · Encoder vs decoder: BERT and GPT"
terms: [encoder, decoder, masked language model, BERT, ablation]
card: lin-bert
---

# Lesson 5 · Encoder vs decoder: BERT and GPT

<p class="recall" markdown>**Previously:** for a fixed compute budget, grow parameters and training tokens together, about 20 per parameter; compute-optimal counts training cost only.</p>

## Idea

BERT and GPT are the week-5 block, stacked. Nearly the same size too: `bert-base-uncased` has 110 million parameters, `gpt2` 124 million. Two decisions made before training differ: what each position may *see*, and what it must *predict*. Those decisions make one an **encoder** and the other a **decoder**, and they decide what each is good for. The seeing decision is also the cleanest **ablation** you can run.

## Mechanism

A decoder keeps the causal mask: position \(t\) sees positions 1 to \(t\) and predicts token \(t+1\). Every position is a training example at once; generation appends the prediction and goes again. GPT-3's discovery (`lin-gpt3`): scaled far enough, a prompt with a few examples steers it to new tasks, no weight change.

An encoder drops the mask: every position sees the whole input. That buys richer per-token vectors but breaks next-token prediction, because the answer is now in the input. So BERT changes the objective: hide 15% of the tokens and predict them from the rest, a **masked language model**. Both are free supervision (`move-free-supervision`): raw text is its own label.

| | Encoder (BERT) | Decoder (GPT) |
|---|---|---|
| each position sees | everything | only the past |
| trained to predict | the hidden tokens | the next token |
| good for | classifying, tagging, retrieval | generating, prompting |
| cannot | write left to right | use the right-hand context |

Models that need both, translation classically, glue an encoder to a decoder: the original Transformer.

**In practice.** Appendix A.1 of the BERT paper gives the masking recipe. Of the 15% of positions chosen, 80% become the literal token `[MASK]`, 10% a random token, 10% are left alone: since `[MASK]` never appears at use time, the mix stops the model learning that only masked positions matter. And here is the ablation: in the week-5 model, delete the one line that applies the causal mask, keep next-token prediction, train. The loss falls toward zero within a few hundred steps and no language was learned: position \(t\) reads \(t+1\) and copies. That is an ablation: a component removed, the loss read. This one you can predict exactly, so it checks your setup.

Done properly it has four parts: one component removed, everything else fixed, two runs from different random starts (to see how much the untouched model wanders), and a prediction written first. The build does this for position encoding, LayerNorm, heads and the mask.

The XR analogy: a gesture recogniser run offline over a recorded session may use frames before and after each moment, encoder-like; inside the headset it acts on the past alone and must guess the future, decoder-like. Where it breaks: BERT's "both sides" is the rest of the sentence, not future time, and real-time systems can buy look-ahead with latency.

## Try it

<div class="visual"><iframe src="../visuals/w06-ablation-predictor.html" title="Ablation predictor: remove a component, guess the loss" loading="lazy"></iframe></div>

Reference numbers: this week's notebook, real config, on a CPU, two random starts each. Predict first:

1. Before revealing anything, order the four ablations from most to least damaging.
2. Drop the causal mask. Predict the validation loss to one decimal place, then reveal.
3. Which ablation will differ most between its two runs? Reveal all four and compare the spreads to the gaps.

## Retrieval

??? question "Remove the causal mask from a next-token model but keep the objective. What happens to the loss, and why is that not learning?"
    It falls toward zero within a few hundred steps: token t+1 is in the input, so position t copies it. No language is learned, and at generation time there is no future to copy.

??? question "BERT sees both sides of every token. Why can it not write a paragraph the way GPT does?"
    It was trained to fill a blank using both sides. Writing means predicting with nothing on the right, one token after another, which it was never trained to do.

??? question "Name the two decisions that make the same block an encoder or a decoder, and one task for each."
    What each position may see (everything, or only the past) and what it must predict (hidden tokens, or the next one). Encoder: classifying text. Decoder: generating it.

## Sources

- [Devlin et al., BERT](https://arxiv.org/abs/1810.04805): section 3.1 and appendix A.1, 15 min.
- [Brown et al., GPT-3](https://arxiv.org/abs/2005.14165): sections 1–2, 15 min.
- [HF LLM course, ch. 1: How do Transformers work?](https://huggingface.co/learn/llm-course/chapter1/4): the "General Transformer architecture" section, 10 min.

## Ledger prompt

> Next to `lin-bert`: for one data stream in your lab, encoder or decoder, and what would the free supervision be? Then next to `core-dl`: what assumption about the data does the causal mask build in?

**Next:** the build: train a BPE tokenizer, ablate one component twice, and draw your own scaling line.
