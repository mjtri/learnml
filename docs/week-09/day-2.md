---
title: "Lesson 2 · CLIP: two encoders, one space"
terms: [CLIP, shared embedding space, zero-shot classification, prompt template, image–text retrieval, ImageBind]
card: lin-clip
---

# Lesson 2 · CLIP: two encoders, one space

<p class="recall" markdown>**Previously:** a batch of pairs is its own exam: InfoNCE makes each item pick its partner from the batch, and the temperature decides how much the hard negatives count.</p>

## Idea

A classifier trained on ImageNet knows a thousand nouns and nothing else. **CLIP** removes the layer that fixed them. It trains an image encoder and a text encoder together, with lesson 1's loss, on 400 million captioned pictures, until a picture and a sentence describing it land close. The "classes" are now whatever sentences you type: the label set became text, and text can be rewritten at test time.

## Mechanism

Two encoders, one output width. The image side is a ResNet or a ViT (next lesson); the text side is a small transformer; each ends in 512 numbers scaled to unit length. They live in one **shared embedding space**, where a picture and a sentence compare by cosine similarity. Training is the symmetric InfoNCE over batches of 32,768 pairs. Everything else is one matrix product on that space.

**Zero-shot classification.** For classes *cup, shoe, hat*, write three sentences, embed them, and stack the three vectors as rows. That stack *is* a linear classifier's weight matrix, written by the text encoder. Multiply by the image vector, scale by 100 (the learned \(1/\tau\)), softmax: three probabilities. *Zero-shot* means zero labelled examples of these classes.

**Prompt templates.** The sentence a class name is dropped into is a **prompt template**. On ImageNet, `a photo of a {label}.` beats the bare label by 1.3 points, and averaging the text vectors of 80 hand-written templates adds 3.5 more. The captions CLIP learned from were sentences, so a bare noun is out of distribution.

**Image–text retrieval** is the same product read the other way: embed 200 images once, embed one query sentence, sort the 200 similarities, look at the top ten.

**In practice**, the whole pipeline in OpenCLIP, the code you run in the build session:

```python
model, _, pre = open_clip.create_model_and_transforms(
    "ViT-B-32", pretrained="laion2b_s34b_b79k")
tok = open_clip.get_tokenizer("ViT-B-32")
img = pre(Image.open("hand.jpg")).unsqueeze(0)
txt = tok(["a photo of a hand", "a photo of a cup"])
with torch.no_grad():
    i = F.normalize(model.encode_image(img), dim=-1)
    t = F.normalize(model.encode_text(txt), dim=-1)
    print((100 * i @ t.T).softmax(-1))   # [[0.93, 0.07]]
```

The honest analogy is a sensory-substitution user: after enough hours, a vOICe soundscape and the shape it stands for mean the same thing, matched without step-by-step translation. Where it breaks: the user aligns by acting in the world; CLIP aligns through captions strangers wrote, so it learns what people *say* about pictures, gaps and prejudices included.

**ImageBind** (2023) goes one step further: audio, depth, thermal and motion are each trained against images only; anchored to one image space, audio and text line up although no audio–text pair was ever shown.

## Try it

<div class="visual"><iframe src="../visuals/w09-zero-shot-prompts.html" title="A toy zero-shot classifier: edit the prompts, watch the predictions" loading="lazy"></iframe></div>

Predict first, then type:

1. Prompts start as bare words: guess the accuracy over the six tiles, read it, then change each to `a photo of a …` and guess again.
2. Add the word *sketch* to the cat prompt only. Predict which tiles flip, and in which direction.
3. Replace the car prompt with `a bird`. Predict where the car tiles go, then say what a zero-shot classifier can never answer.

## Retrieval

??? question "CLIP has no class layer. Explain how it classifies an image into cup, shoe or hat, and say what plays the role of the weight matrix."
    Embed the three sentences; their unit vectors, stacked, are the weight matrix. Cosine with the image vector, times 100, softmax over the three.

??? question "Why does 'a photo of a dog' beat the bare word 'dog', and what does that reveal about the training data?"
    Training captions were sentences, so a lone noun is unlike anything the text encoder saw. The model learned caption *style*, not only object names.

??? question "You want the screenshots among 200 that show a hand near a virtual button. Give the procedure in three steps and say what you check at the end."
    Embed all 200 images once, embed the sentence, sort by cosine similarity. Then inspect the top ten by eye and count the hits: a sorted list has no built-in threshold.

## Sources

- [CLIP paper (Radford et al. 2021)](https://arxiv.org/abs/2103.00020): figure 1, then section 3.1.4 on prompt engineering, 15 min.
- [OpenCLIP README](https://github.com/mlfoundations/open_clip): the usage snippet and the pretrained-model table, 5 min.
- [ImageBind (Girdhar et al. 2023)](https://arxiv.org/abs/2305.05665): abstract and figure 2 only, 5 min.

## Ledger prompt

> Next to `lin-clip`: the card's reframe is "text becomes the label space". Name one label set in your work that was fixed at design time and write the prompts that would replace it. One line for `lin-imagebind`: which of your sensors could be anchored to images?

**Next:** the image encoder inside CLIP: cut the picture into patches, call them tokens, and reuse the transformer you built in week 5.
