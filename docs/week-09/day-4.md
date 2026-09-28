---
title: Lesson 4 · A number is not a result
terms: [evaluation metric, precision/recall, held-out set]
card: core-dl
---

# Lesson 4 · A number is not a result

<p class="recall" markdown>**Previously:** a ViT cuts the image into patches, embeds each as a token, and lets learned position vectors replace the assumptions a convolution was born with.</p>

## Idea

"94% accuracy" means nothing yet. You already refuse a hit rate until you know the chance level, the task, and whether the participants were the ones you piloted on. A model number needs the same three questions: *which* **evaluation metric**, on *which* data, and what a trivial method would score. Most exciting first-project numbers fail one of the three, invisibly.

## Mechanism

**Which metric.** Accuracy is the fraction right, and it lies when classes are unbalanced. One hundred screenshots, ten showing a hand near a virtual button. A detector flags twelve, eight correctly. Accuracy: \((8 + 86)/100 = 0.94\). The rule "always say no" scores 0.90 and detects nothing. **Precision/recall** separate the two failures: precision \(8/12 = 0.67\) (of what it flagged, how much was right), recall \(8/10 = 0.80\) (of what was there, how much it caught). Report both. For a contrastive model, report retrieval accuracy together with \(B\), because chance is \(1/B\).

**Which data.** Week 3's participant rule, now for any repeating unit. The **held-out set** is data nothing touched: not training, not the temperature, not the prompt template. Anything crossing from it into those decisions is a leak, and this week's leak is the quiet one: five templates tried, the best one's held-out score reported. Frames from one participant on both sides of a random split are near-duplicates: the model recognises the room, not the gesture. Split by participant, session, recording, whatever unit repeats.

**What would make it go away.** Before believing a number, name the dumbest comparison that would have to lose. Majority class. Labels shuffled (the number should fall to chance; if not, something leaks). Duplicates removed across the split. A one-line rule such as a brightness threshold. If it scores within a point of yours, you have shown nothing yet.

**In practice**, the leak you will actually write, and its fix:

```python
idx = torch.randperm(len(frames))         # leaks: same
train, test = idx[:800], idx[800:]        # participant
test_ids = {"P07", "P12"}                 # both sides
test = [i for i, p in enumerate(pid) if p in test_ids]
train = [i for i in range(len(pid)) if i not in test]
```

The CLIP authors faced the same question at scale: was CIFAR-10 hiding inside 400 million web images? Section 5 of the paper runs a duplicate detector over every evaluation set and reports how far accuracy moves without the overlaps, mostly a fraction of a point. Copy the check, not the reassuring answer.

The honest analogy is the user study itself: chance level, an unrehearsed task, results on people who were not in the pilot. Where it breaks: participants are expensive, so statistics make twenty of them count; examples here are cheap but *correlated*, so the split does the work statistics cannot.

## Try it

<div class="visual"><iframe src="../visuals/w09-go-away-checklist.html" title="A claimed 94%: tap each check and see what number it produces" loading="lazy"></iframe></div>

Predict first, then tap:

1. Before tapping **majority class**, write its accuracy for ten positives in a hundred. Then tap **shuffled labels** and explain why it is not 50%.
2. Guess the detector's precision and recall from the numbers on the card, then tap **the detector itself: precision and recall**.
3. Drag the imbalance slider to one positive in a hundred. Predict what happens to the accuracy of "always no" and the precision of "always yes".

## Retrieval

??? question "A hundred screenshots, ten positives. The detector flags twelve, eight correctly. Give precision, recall, accuracy, and the accuracy of always-no."
    Precision \(8/12 = 0.67\), recall \(8/10 = 0.80\), accuracy \(94/100 = 0.94\); always-no scores \(0.90\) with recall 0.

??? question "You try five prompt templates and a few temperatures, then report the best combination's accuracy on the held-out set. Name the leak, the fix, and the direction the honest number moves."
    The held-out set chose the template and temperature, so it tuned the method: best-of-many selection inflates the score. Choose them on a validation split, score the held-out set once; the honest number is lower.

??? question "A contrastive model reports 60% retrieval accuracy. Which two facts must travel with that number before it means anything?"
    The candidate-set size (chance is one over it) and that the pairs were held out, not training pairs. A shuffled-pairing run at chance is worth attaching too.

## Sources

- [Understanding Deep Learning, chapter 8: Measuring performance](https://udlbook.github.io/udlbook/): sections 8.1 to 8.3, 20 min.
- [scikit-learn: common pitfalls, data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage): the leakage section, 8 min.
- [Google ML crash course: accuracy, precision, recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall): 8 min.

## Ledger prompt

> Next to `core-dl`: take the last number you reported (a hit rate, an accuracy). Write its metric, the unit you split by (frame, trial, participant), and the dumbest comparison that would have to lose for it to mean anything.

**Next:** the number moves every time you run it: seeds as participants, the standard error, and a bootstrap in ten lines.
