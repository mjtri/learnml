---
title: Lesson 1 · Tokenization: bytes → BPE merges
terms: [tokenization, byte, BPE, merge rule, vocabulary, GPT]
card: core-transformer
---

# Lesson 1 · Tokenization: bytes → BPE merges

<p class="recall" markdown>**Previously:** one running sum, read and written by identical blocks of attention and MLP, trained to guess the next character and then sampled with a temperature.</p>

## Idea

A model never sees text. It sees integers, one per position, and someone has to decide what an integer stands for. Week 5 chose characters, which is honest but expensive: this week's small model has a 64-position window, one sentence's worth, and attention cost grows with the square of the length. Whole words are the opposite failure: an unbounded **vocabulary**, every typo unseen, no plan for Korean. **Tokenization** is the compromise in between, and the modern recipe, **BPE**, is learned from data rather than designed. It also explains half of the "the model is oddly bad at X" stories, which is the next lesson.

## Mechanism

Start from **bytes**. Text is stored as UTF-8: an English letter is one byte, a Korean syllable three, every byte a number from 0 to 255. So 256 base tokens encode *any* string, and nothing is ever "unknown". Then run BPE on a large training text:

1. Count every adjacent pair of tokens.
2. Glue the most frequent pair into a new token, id 256.
3. Record that as a **merge rule**. Repeat with id 257, 258, … until the vocabulary is the size you asked for.

The smallest example that works: `aaabdaaabac`, 11 bytes. The pair `aa` appears most, so merge it into Z: `ZabdZabac` (9 tokens). Now `ab` wins: `ZYdZYac` (7). Now `ZY` wins: `XdXac` (5). Three rules, 11 bytes to 5 tokens. Encoding *new* text means applying the rules in the order they were learned. Nothing is understood; frequent chunks become units. The vocabulary size is a design choice: 256 bytes plus one token per merge. GPT-2's is 50,257 = 256 + 50,000 merges + one end-of-text marker.

**In practice.** In nanoGPT, `data/shakespeare_char/prepare.py` builds the week-5 vocabulary with a `stoi` dictionary over 65 characters; `data/openwebtext/prepare.py` instead calls `tiktoken.get_encoding("gpt2")` and `enc.encode_ordinary(text)`. `"Hello world"` comes out as `[15496, 995]`: two tokens, and the space belongs to `" world"`. And `train.py` sets `vocab_size = 50304`, not 50,257: padded to a multiple of 64 so the last matrix multiply runs faster on a GPU. Not a typo.

```python
from collections import Counter
def merge(ids, pair, new):
    out, i = [], 0
    while i < len(ids):
        if tuple(ids[i:i + 2]) == pair: out.append(new); i += 2
        else: out.append(ids[i]); i += 1
    return out
ids = list("aaabdaaabac".encode())
pair = Counter(zip(ids, ids[1:])).most_common(1)[0][0]
ids = merge(ids, pair, 256)   # (97, 97) -> 256; 11 -> 9 tokens
```

The perception analogy is chunking in skilled reading: a fluent reader sees word shapes, not letters, because frequent sequences became units. It holds this far: what gets chunked is what was *frequent in the training text*. Where it breaks: a reader's chunks follow morphology (`un-`, `-ing`), while BPE splits `strawberry` into `st`, `raw`, `berry` because those pieces were common elsewhere; the model must learn the spelling of its own tokens indirectly.

## Try it

<div class="visual"><iframe src="../visuals/w06-bpe-merges.html" title="BPE merge stepper: watch pairs become tokens" loading="lazy"></iframe></div>

Predict first, then step:

1. Preset `aaabdaaabac`: before tapping **merge**, write down the first merge and the token count after three merges.
2. Type a sentence in which one word repeats three times. Predict how many merges it takes before that word is a single token, then count.
3. Add a Korean word. Before any merge, how many tokens is each syllable? Guess what 50,000 mostly-English merges would do with it.

## Retrieval

??? question "GPT-2's vocabulary has 50,257 entries. Where do 256 of them come from, and what does that base guarantee?"
    They are the 256 possible byte values. Any string, in any script, can be encoded, so there is never an unknown-word token.

??? question "Run BPE by hand on `abababc` for two merges. Which pairs win, and what is the final token sequence?"
    Pairs: `ab` ×3, `ba` ×2, `bc` ×1, so merge `ab` → Z: `ZZZc`. Now `ZZ` ×2 wins: `YZc`. Seven bytes became three tokens.

??? question "Week 5 trained on characters. Give one cost of characters and one cost of whole words that BPE avoids."
    Characters make sequences four or five times longer, so a window holds less and attention pays for length squared. Words give an unbounded vocabulary, unseen words, and no way to encode other scripts.

## Sources

- [Karpathy: Let's build the GPT tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE): 0:00–0:25, the byte-level BPE idea and the `aaabdaaabac` example.
- [HF LLM course, ch. 6: Byte-Pair Encoding tokenization](https://huggingface.co/learn/llm-course/chapter6/5): the training algorithm section, 10 min.
- [nanoGPT `data/openwebtext/prepare.py`](https://github.com/karpathy/nanoGPT/blob/master/data/openwebtext/prepare.py): find the `tiktoken` lines, 3 min.

## Ledger prompt

> Next to `core-transformer`: your haptic or XR stream also has to be cut into units before a model sees it (frames? gestures? contact events?). Which cut would frequency-only BPE make, and where would that disagree with what you know matters?

**Next:** what tokens do to numbers, spaces and Korean, and the three odd behaviours that follow.
