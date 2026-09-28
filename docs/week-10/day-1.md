---
title: Lesson 1 · One lever at a time
terms: [lever, falsifiable prediction]
card: build-step2
---

# Lesson 1 · One lever at a time

<p class="recall" markdown>**Previously:** pairs are free labels, so each item learns to pick its partner out of the batch, and a number becomes a result only with a metric, a held-out split and an interval against something dumb.</p>

## Idea

Most ML ideas fail at the moment they are written down, because they change three things at once. "A learned sonifier trained on more shapes with a contrastive loss" has three moving parts, so whatever happens, you will not know why. This week ports your user-study discipline to models: one manipulation, a comparison condition, a number written down first. Step one is naming the one thing your idea changes: its **lever**.

## Mechanism

Every training run is five decisions; an idea changes exactly one:

| Lever | The question it answers | Week 12 example |
|---|---|---|
| data | what does the model see? | more shapes; jittered positions |
| architecture | what structure is assumed? | a code shaped like a 4×4 actuator grid |
| objective | what is optimized? | contrastive image–sound loss instead of pixel loss |
| optimization | how is it trained? | learning-rate schedule, steps, batch size |
| inference | how is it used? | averaging several sound renderings at test time |

The canvas card is blunt: *pick one; if it is two, split the idea.* The lever also fixes what stays frozen: change the objective and you owe the reader the same data, architecture, steps and seeds.

Once the lever is named, the intuition becomes a **falsifiable prediction**, canvas step 5:

\[ \text{on task } T,\; A \text{ beats } B \text{ by} \ge X \text{ on metric } M \]

Four blanks, all mandatory. \(T\): a task you can run this month. \(M\): one number. \(B\): a method you would be embarrassed to lose to. \(X\): a size chosen before any run. A prediction with no \(X\) cannot fail, and what cannot fail cannot teach.

**In practice**, one of this week's two candidates through the blanks. Intuition: "a sonified shape should be confusable with the shapes it *sounds* like, not the ones it *looks* like." Lever: objective (the image encoder learns to match sound clips, not pixels). Prediction: on 20 rendered shapes, distance in the learned image–sound space predicts which pairs a listener confuses better than pixel distance does, by at least 0.2 on an agreement score between orderings. The other candidate, a learned image→touch code shaped like the display, has lever *architecture*; its blanks are yours in the build session.

The user-study analogy is close: lever = independent variable, frozen levers = what you counter-balance, \(M\) = dependent measure, \(B\) = comparison condition. Where it breaks: a participant cannot be copied, but a model can be re-run with a new random draw, so "how many participants" becomes "how many seeds" (lesson 4). One symptom of a double lever: the prediction contains "and".

## Try it

<div class="visual"><iframe src="../visuals/w10-lever-picker.html" title="Name the lever an idea changes" loading="lazy"></iframe></div>

Before tapping, guess how many levers each idea card touches. Then:

1. Tap the levers you think each idea moves; the readout says whether it is one experiment or several.
2. On the card that moves two levers, tap **split**. Which half would you run first?
3. Write your own idea and pick its lever. If you cannot, it is not yet an ML idea: back to canvas step 1.

## Retrieval

??? question "An idea reads: 'train the sonifier on depth-camera images instead of rendered shapes, with a bigger encoder.' How many levers, which ones, and how would you split it?"
    Two: data (depth images) and architecture (bigger encoder). Run the old encoder on the new data first; if that alone moves the metric, the second experiment is optional.

??? question "Fill the four blanks of a falsifiable prediction for a haptic-grid code that you believe beats a hand-designed mapping."
    T: shape identification from a 4×4 haptic code on 20 shapes. M: accuracy of a small probe. B: the hand-designed downsampler. X: at least 5 points.

??? question "Why must X be chosen before the first run, and what goes wrong if it is chosen after?"
    Chosen after, X becomes whatever the run produced, so the prediction can never fail. Chosen before, 2 points when you predicted 5 is a real disappointment you can learn from.

## Sources

- [Karpathy: A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/): sections 2 and 3, 10 min; re-read with the lever table beside you.
- [Lipton & Steinhardt: Troubling trends in ML scholarship](https://arxiv.org/abs/1807.03341): section 3.2, gains whose source is obscured, 8 min.
- [Henderson et al.: Deep RL that matters](https://arxiv.org/abs/1709.06560): section 2 only, what varies between "the same" experiments, 6 min.

## Ledger prompt

> Next to `build-step2`: take the intuition you wrote for `build-step1` and name its lever in one word. If you needed two, write both halves as separate ideas and mark which runs first.

**Next:** the comparison you must beat, and why the trivial one embarrasses the most people.
