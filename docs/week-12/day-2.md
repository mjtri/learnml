---
title: Lesson 2 · Shape the bottleneck like the display
terms: [autoencoder, reconstruction loss, bottleneck, quantization, straight-through estimator, VAE, ELBO]
card: bridge-codec
---

# Lesson 2 · Shape the bottleneck like the display

<p class="recall" markdown>**Previously:** two encoders and one InfoNCE loss give a space where distance should track what a listener confuses; the ablation drops the sound side.</p>

## Idea

The alternative is the codec: learn the rule instead of matching against a fixed one. A haptic display is a hard constraint: 16 tactors, 8 intensity levels each. The neat move is to build the constraint into the network as its narrowest layer, so training discovers a code for *this* display. The obstacle: rounding to 8 levels has no slope, and gradient descent needs one.

## Mechanism

An **autoencoder** is two networks in a row: an encoder squeezes the input to a few numbers, a decoder rebuilds it from them. The training signal is the **reconstruction loss**, the mean squared difference between input and output; no labels. The numbers in the middle are the **bottleneck**, and everything interesting is a decision about its shape. With 32 free numbers it is a latent like lesson 1's. With 16 numbers that must each be one of 8 levels it is a haptic frame: \(16 \times \log_2 8 = 48\) bits, exactly what the display carries.

The rounding is **quantization**: \(q = \mathrm{round}(7z)/7\) for \(z\) in \([0, 1]\). Its derivative is zero everywhere except at the steps, so the decoder's gradient dies at the bottleneck and the encoder never learns. The **straight-through estimator** fixes this in one line: forward with \(q\), backward as if \(q = z\).

\[ q = z + \mathrm{stopgrad}\big(\mathrm{round}(7z)/7 - z\big) \]

The gradient sees only \(z\). A useful lie: the decoder says "a bit brighter here would help", and the encoder moves \(z\) until it crosses into the next level. VQ-VAE, behind most discrete image and audio codes, uses the same trick.

**In practice**, in PyTorch the whole trick is the `.detach()`:

```python
def quantize(z, levels=8):
    q = torch.round(z * (levels - 1)) / (levels - 1)
    return z + (q - z).detach()   # forward: q, backward: z
```

The other way to shape a bottleneck is noise rather than steps: a **VAE**'s encoder outputs a mean and a spread per latent number, a sample from that bell shape is decoded, and a penalty pulls every code toward a standard bell. Its objective, the **ELBO**, is reconstruction minus that penalty; the noise makes nearby codes decode alike, so VAE latents are smooth (`lin-vae`: discrete for a display, noisy for a space to walk through).

The comparison is fair at equal bandwidth: week 10's hand downsampler (block average, round to 8 levels) also sends 48 bits per frame. The claim: a learned 48 bits keeps more shape identity, measured by a probe on the codes.

The analogy is honest: the bottleneck *is* the display, tactor for tactor. Where it breaks: 8 nominal levels may be 4 perceptual ones on skin; the network optimises for the decoder, not the finger.

## Try it

<div class="visual"><iframe src="../visuals/w12-bottleneck-shaper.html" title="Actuator grid and levels: bits, reconstruction error, distinct codes" loading="lazy"></iframe></div>

1. At 4×4, 8 levels, guess which of the six shapes share a code before moving anything.
2. Equal bits: 4×4 at 16 levels and 8×8 at 2 levels both send 64. Guess first which reconstructs better and which keeps all six shapes distinct.
3. Find the cheapest setting that keeps all six shapes distinct; read its bits per frame.

## Retrieval

??? question "An autoencoder with a 4×4, 8-level bottleneck trains, but the encoder's weights never change. Which line is missing and what does it do?"
    The straight-through estimator: `z + (q - z).detach()` keeps the rounded forward value but lets the gradient reach the encoder as if rounding were the identity.

??? question "Compute the bits per frame for a 4×4 grid at 8 levels and for a 2×2 grid at 64 levels. Which matches the display, and which would you trust on skin?"
    48 and 24 bits (16 × 3 and 4 × 6): only the first is equal bandwidth with the display. Trust the 4×4 grid: 64 intensity levels are far beyond a fingertip's JNDs, so most of the 2×2 grid's bits never reach the person.

??? question "Reconstruction loss is 0.01 but a probe on the codes scores at chance. What has the bottleneck kept and what has it lost?"
    It kept the smooth average brightness that gives a low pixel error and lost the thin strokes that tell shapes apart. Reconstruction loss does not measure identity.

## Sources

- [VQ-VAE paper](https://arxiv.org/abs/1711.00937): sections 3.1–3.2, the straight-through line, 10 min.
- [Bengio et al., gradients through stochastic neurons](https://arxiv.org/abs/1308.3432): the straight-through section, 6 min.
- [VAE paper](https://arxiv.org/abs/1312.6114): sections 1–2.3, 20 min, only if you pivot.
- [UDL book, chapter 17](https://udlbook.github.io/udlbook/): 17.1–17.3, 15 min.

## Ledger prompt

> Next to `bridge-codec`: which display constraints (tactor count, levels, frame rate, skin JNDs) go inside the bottleneck, and which stay outside as an evaluation? One line each.

**Next:** the first curves from the real run: learning, memorising, or broken, and the three numbers that tell them apart.
