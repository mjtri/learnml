---
title: "Lesson 3 · ViT in one page: patches as tokens"
terms: [ViT, patch embedding, inductive bias]
card: lin-vit
---

# Lesson 3 · ViT in one page: patches as tokens

<p class="recall" markdown>**Previously:** CLIP's two encoders share one space, so a stack of embedded sentences is a classifier and a sorted column of similarities is a search engine.</p>

## Idea

A convolutional network arrives with beliefs about images: nearby pixels belong together, and a thing is the same thing wherever it appears. Those beliefs are its **inductive bias**, what the architecture assumes before seeing an example. The **ViT** (Vision Transformer, 2020) throws most of that away: cut the image into squares, call each square a token, and feed the sequence to the transformer you built in week 5, unchanged. With little data the convolution's beliefs win; with enough, the transformer learns them and keeps going.

## Mechanism

A \(224 \times 224\) RGB image cut into \(16 \times 16\) patches gives \((224/16)^2 = 196\) patches, each a block of \(16 \cdot 16 \cdot 3 = 768\) pixel values. Flatten each block into a row and push it through one linear layer, the **patch embedding**, to the model width \(d\): the image is now a \((196, d)\) matrix, indistinguishable from a 196-token sentence. Add a learned position vector per patch and one learned "class" token whose output is the answer, and \((197, d)\) enters block 1.

Attention compares every token with every other, so 196 tokens cost about \(196^2 \approx 38{,}000\) pairs per head. Halve the patch to 8 pixels: 784 tokens, 615,000 pairs, sixteen times more. That is why CLIP's cheapest model is *ViT-B/32*: 32-pixel patches, \(7 \times 7 = 49\) tokens.

**In practice**, a convolution with stride equal to its kernel does the flatten-and-multiply in one call. From `model.py` in openai/CLIP:

```python
self.conv1 = nn.Conv2d(3, width, kernel_size=patch_size,
                       stride=patch_size, bias=False)
# in forward:
x = self.conv1(x)                      # (B, 768, 7, 7)
x = x.reshape(x.shape[0], x.shape[1], -1)
x = x.permute(0, 2, 1)                 # (B, 49, 768)
```

A convolution that never overlaps *is* a patch embedding; the shapes are ViT-B/32 at 224 pixels.

Convolution assumes *locality* (a filter sees a small window) and *translation equivariance* (the same filter everywhere). ViT keeps only "a patch is the unit"; whether patch 5 and patch 6 are neighbours, the position vectors must learn. They do: figure 7 of the paper shows each learned position vector most similar to its grid neighbours. Trained on ImageNet alone, ViT trails a ResNet of the same size; on 300 million images it overtakes it.

For the week's "done when", name the assumption:

| Architecture | Assumes |
|---|---|
| Convolution | nearby pixels interact; same detector everywhere |
| Transformer | almost nothing; order only via position vectors |
| ViT | the patch is the unit; everything else learned |
| vOICe mapping | column is time, row is pitch; fixed by design |

The last row is the honest analogy: a vOICe scan also turns an image into a sequence by a fixed cutting rule. Where it breaks: in vOICe the order *is* the message; in a ViT it is a learned tag, and shuffling patches changes nothing unless the position vectors say so.

## Try it

<div class="visual"><iframe src="../visuals/w09-patch-splitter.html" title="Cut a 64×64 image into patches and count the tokens" loading="lazy"></iframe></div>

Predict first, then tap:

1. Start: 64-pixel image, 16-pixel patches. Before tapping **8**, predict the token count and how many times the attention pairs grow.
2. Tap a patch near the centre. Predict its index in the sequence and how many numbers it flattens to.
3. Tap **shuffle**. Which readouts change? Say what a model without position vectors would see.

## Retrieval

??? question "A 224×224 RGB image with 32-pixel patches enters a width-768 ViT. Give the token count, the numbers per patch before embedding, and the shape entering block 1."
    \(7 \times 7 = 49\) tokens; \(32 \cdot 32 \cdot 3 = 3072\) numbers each; with the class token the stream is \((50, 768)\).

??? question "Name the two assumptions a convolution makes that ViT drops, and say what dataset size did to the comparison."
    Locality and translation equivariance. ViT trailed a comparable ResNet at ImageNet scale and overtook it at 300 million images.

??? question "Your vOICe mapping and a ViT both turn an image into a sequence. Name the inductive bias each cutting rule imposes."
    vOICe: column is time and row is pitch, fixed by design. ViT: the patch is the unit and order lives only in learned position vectors.

## Sources

- [ViT paper (Dosovitskiy et al. 2020)](https://arxiv.org/abs/2010.11929): figure 1 and section 3.1, then figure 7, 12 min.
- [openai/CLIP model.py](https://github.com/openai/CLIP/blob/main/clip/model.py): the `VisionTransformer` class, 6 min.
- [d2l 11.8 Transformers for Vision](https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html): the patch-embedding section, 8 min.

## Ledger prompt

> Next to `lin-vit`: the card's move is "inductive bias". Write, in one sentence each, the assumption baked into one model you use (a gesture recogniser, an IMU filter) and one dataset where that assumption would hurt.

**Next:** a number is not a result: which metric, which split, and the leak that makes a good number a lie.
