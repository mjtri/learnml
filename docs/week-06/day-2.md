---
title: Lesson 2 · Tokenizer artefacts: numbers, spaces, Korean
terms: [tokenizer artefact]
card: core-transformer
---

# Lesson 2 · Tokenizer artefacts: numbers, spaces, Korean

<p class="recall" markdown>**Previously:** BPE starts from 256 bytes and glues the most frequent adjacent pair, 50,000 times; the model then sees only the resulting token ids.</p>

## Idea

Some model failures are not failures of the model. They are consequences of the cut made before the model ran, and the tell is that they vanish when you change the tokenizer. Call them **tokenizer artefacts**. Three families cover most of them: the model cannot see letters, it sees digits in uneven chunks, and it pays a very different price per language. Each turns "the model is dumb" into a hypothesis you can check in a token viewer.

## Mechanism

The whole mechanism is one fact: a token is an opaque id. The model learns what `berry` tends to follow, never what letters it contains. Everything below is that fact meeting a particular text.

**In practice.** Real output of the GPT-2 encoder (the one nanoGPT uses), with GPT-4's newer encoder beside it:

| Text | GPT-2 | GPT-4 |
|---|---|---|
| `strawberry` | `st` `raw` `berry` | 3 |
| ` strawberry` (leading space) | 1 token | 1 |
| `20240928` | `20` `24` `09` `28` | `202` `409` `28` |
| `haptic feedback` → `촉각 피드백` | 3 → 16 | 3 → 11 |
| `Hello, welcome to Seoul.` → `안녕하세요, 서울에 오신 것을 환영합니다.` | 6 → 50 | 6 → 20 |

Read the rows as three artefacts.

1. **Letters are invisible.** "How many r's in strawberry?" asks the model to recall the spelling of three ids it has only seen as wholes; reversing or rhyming a word fails the same way. And ` strawberry` with a leading space is a *different, single* token, so the same word at the start of a prompt and mid-sentence are different inputs. A prompt that ends in a space forces an odd split right where prediction happens.
2. **Digits arrive in arbitrary chunks.** GPT-2 cuts `20240928` by frequency, so the year is `20` `24` and the day `09` `28`, with no tens-and-ones structure. Newer encoders cut digits in fixed groups of up to three: one reason arithmetic improved without smarter models.
3. **Korean costs three to eight times more.** A Hangul syllable is three bytes, and an English-heavy merge table learned few Korean merges, so `안녕하세요` is 14 GPT-2 tokens for five syllables. The context window holds fewer Korean characters, every call is slower and pricier, and the model spent less capacity per unit of Korean meaning. A syllable split across tokens can also end sampling mid-character: a broken glyph.

The sensory-substitution analogy holds well here: a fixed image-to-sound mapping decides what is cheap to perceive (a horizontal line is one steady pitch) and what is expensive (a diagonal is a sweep to track), so the *encoding* sets the difficulty before the brain does any work. Where it breaks: a tokenizer's cost is countable today; a device's perceptual cost needs a user study.

## Try it

<div class="visual"><iframe src="../visuals/w06-tokenizer-artefacts.html" title="Tokenizer artefact explorer: a toy BPE next to GPT-2's counts" loading="lazy"></iframe></div>

The visual trains a toy BPE on a few kilobytes of English, then tokenizes what you type, with GPT-2's real count beside the presets. Predict first:

1. `strawberry` and ` strawberry`: does the leading space change the count? Check both encoders.
2. `20240928`: write down the chunks you expect, then compare toy and GPT-2.
3. Korean welcome versus English: guess the token ratio in the toy encoder and in GPT-2. Why is the toy one worse?

## Retrieval

??? question "A model says strawberry has two r's. Explain the mistake from the tokenizer's side."
    It sees `st` `raw` `berry` as three ids and never their letters, so counting letters means recalling spellings it was never shown. Reversing a word fails the same way.

??? question "Roughly how many times more GPT-2 tokens does a Korean sentence cost than its English translation, and what two costs follow?"
    Around eight times in the example (50 versus 6); three to eight is typical. Fewer Korean characters fit in the context window, and every call is slower and pricier.

??? question "Why is `20` `24` `09` `28` a worse input for date arithmetic than `202` `409` `28`, and what is the deeper point?"
    Frequency-based chunks differ from number to number, so the model must learn a new alignment each time; fixed three-digit groups are consistent. Deeper point: the tokenizer, not the model, set the difficulty.

## Sources

- [Karpathy: Let's build the GPT tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE): 0:00–0:08, the list of odd behaviours that trace back to tokenization.
- [Tiktokenizer](https://tiktokenizer.vercel.app/): paste the table's rows, switch between `gpt2` and `cl100k_base`, 5 min.
- [HF LLM course, ch. 6: Tokenizers introduction](https://huggingface.co/learn/llm-course/chapter6/1): 5 min; then skim 6.2, why you retrain a tokenizer for a new language.

## Ledger prompt

> Next to `core-transformer`: one odd answer you have had from a model in Korean or about numbers, sorted into the three artefact families. If it fits none, that is a finding too.

**Next:** why loss falls as a straight line when both axes are logarithmic, and what the slope buys you.
