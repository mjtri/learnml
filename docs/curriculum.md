<!-- Generated from /curriculum.md by build_today.py. Edit the root file, not this one. -->

# Curriculum: just enough ML to use and modify models

**12 weeks · 5 phone days (~20 min) + 1 build day (~3 h, free Colab) per week.**
Goal: read a modern paper, fine-tune or modify a small model, run a small controlled experiment. Not: become a theorist.

How it is organised
- **Just-in-time math.** A math idea appears only in the week a lesson needs it, with the smallest example that works.
- **Canvas-aligned.** Each week names cards from the Obsidian canvas *AI Research Roadmap*: ② Technical Core (`core-*`), ① Lineage (`lin-*`), ③ Build pipeline (`build-step*`), ⑤ Bridges (`bridge-*`). Each lesson's ledger prompt says which card the entry belongs next to.
- **Predict, then run.** Every build notebook makes you write the expected result first (canvas steps 7–8). The surprise is the output.
- **One week at a time.** Only week 1 exists at the start. `python gen_week.py N` prints the prompt that generates week N, using your ratings from week N−1. Day topics below are the plan, not a promise; they bend to what you found hard.

| Phase | Weeks | You can, by the end |
|---|---|---|
| A · Mechanics | 1–3 | explain and code the training loop: tensors → gradients → a small MLP that learns |
| B · Transformers | 4–6 | build a tiny GPT, change one part, and explain the loss change |
| C · Pretrained models | 7–9 | load, probe, LoRA-fine-tune and evaluate a pretrained model; use CLIP embeddings |
| D · Your experiment | 10–12 | design, run and write up a small controlled experiment tied to sensory substitution |

Core resources used throughout
- Karpathy, *Neural Networks: Zero to Hero*: <https://karpathy.ai/zero-to-hero.html>
- 3Blue1Brown topics: [neural networks](https://www.3blue1brown.com/topics/neural-networks), [linear algebra](https://www.3blue1brown.com/topics/linear-algebra), [calculus](https://www.3blue1brown.com/topics/calculus)
- Prince, *Understanding Deep Learning* (UDL, free PDF): <https://udlbook.github.io/udlbook/>
- *Dive into Deep Learning* (d2l): <https://d2l.ai/>
- The Annotated Transformer: <https://nlp.seas.harvard.edu/annotated-transformer/>
- Hugging Face LLM course: <https://huggingface.co/learn/llm-course/chapter1/1>

---

# Phase A · Mechanics (weeks 1–3)

## Week 1 — Tensors → gradients

**Objectives**
- Read and predict tensor shapes, including broadcasting.
- See a matrix multiply as "every output is a weighted mix of the inputs" (a hand-designed image→sound mapping is exactly this).
- Explain a derivative as sensitivity, the chain rule as multiplying sensitivities along a path, and gradient descent as repeated small downhill steps.

**Just-in-time math:** shapes and indexing; dot product; matrix × vector; slope/derivative by nudging; chain rule on a graph. Nothing else yet.

**Days**
1. Tensors & shapes; broadcasting
2. Matmul as mixing; dot product as similarity
3. Derivative = sensitivity (nudge and measure)
4. Chain rule on a computation graph (what autograd automates)
5. Gradient descent and the learning rate
6. **Build:** gradients by hand, then by machine. Shapes drills → a vOICe-style image→sound matrix → numerical vs autograd gradients → fit a line with hand-written gradient descent → break it with a bad learning rate.

**Done when:** given a small expression graph you can compute every gradient by hand, confirm it with `torch.autograd`, and predict what doubling the learning rate does before you run it.

**Canvas cards:** `core-linalg` (first two bullets only), `core-calc`; lineage read `lin-bitter` (short essay, sets up why we learn mappings instead of designing them). *Suggestion: the canvas has no backprop-era card; consider adding Rumelhart, Hinton & Williams (1986).*

**Resources**
- 3Blue1Brown: [Linear transformations](https://www.3blue1brown.com/lessons/linear-transformations), [Dot products](https://www.3blue1brown.com/lessons/dot-products), [Derivatives](https://www.3blue1brown.com/lessons/derivatives), [Gradient descent](https://www.3blue1brown.com/lessons/gradient-descent)
- d2l: [2.1 Data manipulation](https://d2l.ai/chapter_preliminaries/ndarray.html), [2.4 Calculus](https://d2l.ai/chapter_preliminaries/calculus.html), [2.5 Automatic differentiation](https://d2l.ai/chapter_preliminaries/autograd.html)
- PyTorch: [Broadcasting semantics](https://pytorch.org/docs/stable/notes/broadcasting.html), [Tensors tutorial](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- Karpathy: [micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0), first 40 minutes only
- Sutton, [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
- Rumelhart, Hinton & Williams (1986), [Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0) (skim the abstract and figure 1)

## Week 2 — Autograd from scratch (micrograd)

**Objectives**
- Build a scalar autograd engine: a `Value` that remembers how it was made, and a backward pass that walks the graph in reverse.
- Define a neuron, a layer and an MLP on top of it; understand what a nonlinearity buys you.
- Write a loss, run the loop *forward → loss → zero grads → backward → update*, and watch it learn.

**Just-in-time math:** local derivatives of `+`, `×`, `tanh`/ReLU; topological order; why gradients **add** when a value is used twice; mean squared error.

**Days**
1. A `Value` object and the graph it builds
2. Backward pass: local derivative × upstream gradient
3. The accumulation bug (`+=`) and why you zero gradients
4. Neuron → layer → MLP; why a nonlinearity is needed (XOR)
5. Loss functions and the five-line training loop
6. **Build:** rebuild micrograd, train a 2-layer MLP on XOR and on a 2-D "moons" toy set; compare every gradient with PyTorch.

**Done when:** you have rebuilt micrograd from memory and trained a 2-layer MLP on XOR with it (the `core-calc` criterion).

**Canvas cards:** `core-calc`; move card `move-discrete-continuous` (soft, differentiable everything is what makes this work).

**Resources**
- Karpathy: [micrograd video](https://www.youtube.com/watch?v=VMj-3S1tku0) (whole), [micrograd repo](https://github.com/karpathy/micrograd)
- 3Blue1Brown: [What is backpropagation really doing?](https://www.3blue1brown.com/lessons/backpropagation), [Backpropagation calculus](https://www.3blue1brown.com/lessons/backpropagation-calculus)
- Olah, [Calculus on computational graphs](https://colah.github.io/posts/2015-08-Backprop/)
- UDL ch. 7 (Gradients and initialization), sections 7.1–7.4

## Week 3 — PyTorch training loop → a small MLP that generalises

**Objectives**
- Move from your engine to PyTorch: `nn.Module`, `Dataset`/`DataLoader`, optimizer, the standard loop.
- Classify with softmax + cross-entropy; read a loss curve; split train/validation and recognise overfitting.
- Make a net fail and fix it: learning rate, initialization, normalization.

**Just-in-time math:** softmax; cross-entropy as "surprise at the right answer" (negative log-likelihood); mini-batch noise; momentum and Adam as running averages; variance of activations (why init scale matters).

**Days**
1. `nn.Module`, parameters and the canonical loop
2. Softmax + cross-entropy; logits
3. Mini-batches, SGD → momentum → Adam
4. Train vs validation; overfitting; regularization in one page
5. When training breaks: learning rate, init, normalization, residual connections
6. **Build:** an MLP on MNIST or Fashion-MNIST (> 97 % / > 88 %), then make it diverge and fix it three ways, predicting which fix works first.

**Done when:** you can make a small net diverge and fix it three ways (LR, init, norm) and predict which fix works before trying (the `core-optim` criterion).

**Canvas cards:** `core-optim`, `core-dl` (first two bullets), `core-tooling` (first bullet); lineage `lin-resnet` (why deeper trained worse, and the residual fix you will meet again inside the transformer).

**Resources**
- Karpathy: [makemore 2: MLP](https://www.youtube.com/watch?v=TCH_1BHY58I), [makemore 3: activations, gradients, BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc)
- Karpathy, [A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/)
- PyTorch: [Learn the basics](https://pytorch.org/tutorials/beginner/basics/intro.html)
- UDL ch. 5 (Loss functions), 6 (Fitting models), 8 (Measuring performance); d2l [ch. 5 MLPs](https://d2l.ai/chapter_multilayer-perceptrons/index.html)
- Papers: [ResNet](https://arxiv.org/abs/1512.03385), [Adam](https://arxiv.org/abs/1412.6980) (abstract + algorithm 1)

---

# Phase B · Transformers (weeks 4–6)

## Week 4 — Embeddings and attention

**Objectives**
- Explain why words became vectors, and what "similar direction = similar meaning" buys you.
- Compute single-head attention by hand on three tokens: queries, keys, values, scaled dot products, softmax, weighted sum.
- Explain the causal mask, and why attention needs position information injected.

**Just-in-time math:** cosine similarity; softmax temperature; why divide by √d; probability distributions as rows that sum to 1.

**Days**
1. Embeddings: a lookup table that learns (word2vec in one page)
2. Next-token prediction: the bigram model and its loss
3. Attention as soft lookup: query, key, value
4. Scaled dot-product attention by hand; the causal mask
5. Multi-head attention and position encodings
6. **Build:** bigram language model → add one self-attention head (first half of "Let's build GPT"), with shape predictions at every step.

**Done when:** you can compute attention weights for a 3-token example on paper, and say what each of Q, K, V contributes in your own words.

**Canvas cards:** `core-transformer` (bullets 1–2), `core-prob` (cross-entropy bullet); lineage chain 1: `lin-word2vec` → `lin-seq2seq` → `lin-attention`; move `move-discrete-continuous`.

**Resources**
- 3Blue1Brown: [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), [Attention in transformers](https://www.3blue1brown.com/lessons/attention)
- Karpathy: [makemore 1: bigrams](https://www.youtube.com/watch?v=PaCmpygFfXo), [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) (to ~1:02:00)
- Alammar, [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- Papers: [word2vec](https://arxiv.org/abs/1301.3781), [Bahdanau attention](https://arxiv.org/abs/1409.0473) (sections 1–3)

## Week 5 — The transformer block and nanoGPT

**Objectives**
- Assemble a block: attention + MLP + residual stream + LayerNorm; say what each part is for.
- Train a character-level GPT on a tiny corpus in Colab; sample from it; read the loss curve.
- Read *Attention Is All You Need* and map every box in figure 1 to code you ran.

**Just-in-time math:** LayerNorm (mean/variance per token); the residual stream as a running sum; parameter counting.

**Days**
1. The residual stream: blocks read from and write to one running sum
2. The MLP block and LayerNorm placement (pre- vs post-norm)
3. Stacking blocks; counting parameters; where the compute goes
4. Sampling: temperature, top-k, and why outputs vary
5. Reading the Transformer paper with a map
6. **Build:** finish "Let's build GPT" / nanoGPT on tiny Shakespeare (T4, ~15 min runs); log val loss with config + seed.

**Done when:** you have trained nanoGPT on a tiny corpus and can point to the line of code for every box in the paper's figure 1.

**Canvas cards:** `core-transformer`; lineage `lin-resnet` → `lin-transformer`; move `move-inductive-bias`.

**Resources**
- Karpathy: [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) (rest), [nanoGPT](https://github.com/karpathy/nanoGPT)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
- Interactive: [Transformer Explainer](https://poloclub.github.io/transformer-explainer/), [LLM visualization](https://bbycroft.net/llm)
- UDL ch. 12 (Transformers); paper: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

## Week 6 — Tokenization, scaling intuition, first ablation

**Objectives**
- Explain BPE tokenization and name three odd model behaviours it causes.
- State the scaling-law picture in plain words: loss falls smoothly with parameters, data and compute; Chinchilla's correction.
- Run your first ablation: remove or change one component of nanoGPT and explain the loss difference.

**Just-in-time math:** log–log plots and power laws; tokens vs parameters vs FLOPs (the 6·N·D rule of thumb).

**Days**
1. Tokenization: bytes → BPE merges
2. Tokenizer artefacts (numbers, spaces, non-English text such as Korean)
3. Scaling laws: reading a log–log plot
4. Chinchilla, and what "compute-optimal" means for a small lab
5. Encoder vs decoder: BERT and GPT as two uses of the same block
6. **Build:** ablate one nanoGPT component (position encoding, LayerNorm, or number of heads), 2 seeds each; plus a three-size mini scaling run.

**Done when:** you have ablated one component and explained the loss change (the `core-transformer` criterion), with your prediction logged first.

**Canvas cards:** `core-transformer`, `core-dl` (inductive bias); lineage chain 2: `lin-bert` → `lin-gpt3` → `lin-kaplan` → `lin-chinchilla`; moves `move-scale`, `move-free-supervision`.

**Resources**
- Karpathy: [Let's build the GPT tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE); playground: [Tiktokenizer](https://tiktokenizer.vercel.app/)
- HF LLM course, [ch. 6 Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1)
- Papers: [BERT](https://arxiv.org/abs/1810.04805), [GPT-3](https://arxiv.org/abs/2005.14165) (sections 1–2), [Scaling laws](https://arxiv.org/abs/2001.08361) (figures 1–4), [Chinchilla](https://arxiv.org/abs/2203.15556) (abstract, figure 1)

---

# Phase C · Pretrained models (weeks 7–9)

## Week 7 — Using pretrained models with Hugging Face

**Objectives**
- Load a model and tokenizer from the Hub; inspect config, parameter count, layers; run generation and extract hidden states.
- Understand the pretrain → fine-tune pattern and when you need neither (prompting, embeddings + a linear probe).
- Reproduce a repo's setup: read its config, pin versions, set seeds, log a run.

**Just-in-time math:** none new; consolidation week.

**Days**
1. The Hub, model cards, and what a checkpoint contains
2. `AutoTokenizer` / `AutoModel`: shapes in, shapes out
3. Hidden states as features; the linear probe
4. Full fine-tuning in outline; memory arithmetic (why a T4 runs out)
5. Reproducibility basics: seeds, configs, run logs
6. **Build:** load a small LM (e.g. SmolLM2-135M/360M), probe its hidden states on a small classification task, log everything to a CSV with config + seed + git hash.

**Done when:** you can load any Hub model, state its input/output shapes and parameter count, and log a run someone else could repeat.

**Canvas cards:** `core-tooling`; lineage `lin-bert` (fine-tune pattern), `lin-gpt3` (in-context alternative); move `move-adapters`.

**Resources**
- HF LLM course [ch. 1–3](https://huggingface.co/learn/llm-course/chapter1/1); [Transformers docs](https://huggingface.co/docs/transformers/index)
- Model: [SmolLM2-360M](https://huggingface.co/HuggingFaceTB/SmolLM2-360M)
- PyTorch, [Reproducibility notes](https://pytorch.org/docs/stable/notes/randomness.html)

## Week 8 — LoRA fine-tuning

**Objectives**
- Explain LoRA's ΔW = BA: what is frozen, what trains, why rank r matters, where adapters attach.
- Fine-tune a small LM with PEFT on a free T4; compare against the base model on held-out data.
- Run a rank ablation and read it honestly.

**Just-in-time math:** rank and low-rank factorization; SVD in pictures (a matrix as a sum of a few simple stretches). This is where week 1's "squashing" matrix pays off.

**Days**
1. Rank: how many independent directions a matrix really uses
2. SVD in pictures; low-rank approximation of an image
3. LoRA: freeze W, learn BA; parameter arithmetic
4. PEFT in practice: target modules, alpha, dropout, merging
5. Fine-tuning failure modes: forgetting, leakage, overfitting tiny datasets
6. **Build:** LoRA-tune SmolLM2-360M (or Qwen2.5-0.5B) on a small instruction/style set; ablate r ∈ {1, 4, 16} with 2 seeds; predict the ordering first.

**Done when:** you can explain LoRA's ΔW = BA and why rank r matters (the `core-linalg` criterion), and show a before/after evaluation you trust.

**Canvas cards:** `core-linalg` (low-rank bullets), `core-tooling`; lineage `lin-lora`; bridge `bridge-adaptation` (learner = frozen model, device mapping = adapter).

**Resources**
- Paper: [LoRA](https://arxiv.org/abs/2106.09685) (sections 1–4, table 6 on rank)
- HF [PEFT docs](https://huggingface.co/docs/peft/index), [LoRA conceptual guide](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)
- 3Blue1Brown linear algebra: [Inverse matrices, column space and null space](https://www.3blue1brown.com/lessons/inverse-matrices) (covers rank)
- Model: [Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B)

## Week 9 — CLIP, multimodal embeddings, evaluation

**Objectives**
- Explain contrastive learning (InfoNCE) as "pick your partner out of the batch", and why it yields a shared image–text space.
- Use CLIP for zero-shot classification and retrieval; inspect the similarity matrix.
- Evaluate properly: metrics, held-out splits, confidence intervals from seeds or bootstrap, and the question "what baseline makes this go away?"

**Just-in-time math:** cosine similarity matrix; cross-entropy over a batch (InfoNCE); mean ± standard error; bootstrap in ten lines.

**Days**
1. Contrastive learning: positives, negatives, temperature
2. CLIP: two encoders, one space; text as the label set
3. ViT in one page: patches as tokens
4. Evaluation: metrics, splits, leakage
5. Uncertainty: seeds, standard error, bootstrap; how to read a results table sceptically
6. **Build:** zero-shot CIFAR-10 with OpenCLIP, prompt-template ablation, bootstrap CIs; then image↔text retrieval on a small custom set (your own XR/haptics images welcome).

**Done when:** given a new architecture you can name its inductive bias (the `core-dl` criterion), and you can report a result as "mean ± uncertainty vs a named baseline".

**Canvas cards:** `core-dl`, `core-prob` (entropy/KL bullets as needed); lineage chain 3: `lin-cpc` → `lin-simclr` → `lin-clip` → `lin-imagebind`, plus `lin-vit`; bridge `bridge-crossmodal`.

**Resources**
- Papers: [CLIP](https://arxiv.org/abs/2103.00020) (sections 1–3.1), [SimCLR](https://arxiv.org/abs/2002.05709) (figure 2, section 2), [ViT](https://arxiv.org/abs/2010.11929) (figure 1), [ImageBind](https://arxiv.org/abs/2305.05665) (abstract, figure 2)
- Code: [OpenCLIP](https://github.com/mlfoundations/open_clip), [openai/CLIP](https://github.com/openai/CLIP)
- UDL ch. 8 (Measuring performance)

---

# Phase D · Your experiment (weeks 10–12)

## Week 10 — Experiment design

**Objectives**
- Turn an intuition into a falsifiable prediction: "on task T, A beats B by ≥ X on metric M" (canvas steps 1–5).
- Choose baselines that could embarrass you; plan ablations that isolate one lever; decide seeds and compute budget up front.
- Know the common ways small ML experiments fool their authors.

**Just-in-time math:** variance across seeds; effect size vs noise; how many seeds for the difference you care about (rule-of-thumb level, reusing what you know from user studies).

**Days**
1. One lever at a time: data, architecture, objective, optimization, inference
2. Baselines: trivial, strong, and "same compute"
3. Ablations and controls: what an ML paper owes the reader
4. Seeds, variance and honest tables; tuning the baseline as hard as your method
5. Pre-registration for yourself: the one-page experiment plan
6. **Build:** run two candidate ideas through canvas steps 1–5; write the one-page plan for week 12; build the data pipeline (a vOICe-style sonifier or the haptic-grid downsampler) and sanity-check it.

**Done when:** your week-12 plan names task, metric, baseline B, prediction with a number, ablation, seeds and a compute budget ≤ a few T4-hours.

**Canvas cards:** ③ `build-step1` … `build-step6`; ④ Move Library (name the 1–2 moves your idea uses); `core-tooling`.

**Resources**
- Henderson et al., [Deep reinforcement learning that matters](https://arxiv.org/abs/1709.06560) (the seeds-and-variance lesson, applies beyond RL)
- Dodge et al., [Show your work](https://arxiv.org/abs/1909.03004) (reporting with compute budgets)
- Lipton & Steinhardt, [Troubling trends in machine learning scholarship](https://arxiv.org/abs/1807.03341)
- Karpathy, [A recipe for training neural networks](https://karpathy.github.io/2019/04/25/recipe/) (re-read)

## Week 11 — Reproduce one number from a paper

**Objectives**
- Read a paper in three passes; extract exactly what is needed to reproduce one table cell.
- Clone or reassemble the setup, reproduce the number within tolerance, and explain any gap.

**Default target (small, leads into week 12):** a zero-shot accuracy cell from the CLIP paper using OpenCLIP weights on a free T4. Alternatives: the rank row of the LoRA paper at small scale; nanoGPT's tiny-Shakespeare validation loss from its README.

**Days**
1. Three-pass paper reading; where the details hide (appendix, config, footnotes)
2. From paper to checklist: data, preprocessing, model, metric
3. Reading someone else's repo: entry point, config, data flow
4. When the number does not match: a debugging order
5. Writing the one-paragraph reproduction report
6. **Build:** reproduce the number; log prediction, result, gap and explanation.

**Done when:** you can clone a paper repo, reproduce one table row, and log your own run with config + seed (the `core-tooling` criterion).

**Canvas cards:** `core-tooling`; the `lin-*` card of the paper you reproduce (add a ledger entry next to it).

**Resources**
- Keshav, [How to read a paper](http://ccr.sigcomm.org/online/files/p83-keshavA.pdf)
- [HF Papers](https://huggingface.co/papers) and [HF trending papers](https://huggingface.co/papers/trending) (Papers with Code has shut down and now redirects here)
- The paper and repo you pick

## Week 12 — A small sensory-substitution experiment

**Objectives**
- Run the week-10 plan: A vs B, one ablation, ≥ 3 seeds, predictions logged first (canvas steps 6–9).
- Write the one-page result: claim, setup, plot, surprise, decision (kill / pivot / scale up), and ask an ML collaborator "what baseline would make this go away?" (step 10).

**Two ready-made options (choose in week 10)**
- **Cross-modal embedding** (`bridge-crossmodal`): sonify small images with a fixed vOICe-style mapping (column → time, row → pitch, brightness → loudness); train a tiny contrastive model between image patches and their sound spectrograms. Prediction example: "embedding distance predicts shape confusability better than pixel distance by ≥ X rank correlation." A later human study can test it.
- **Learned image→sound/touch codec** (`bridge-codec`): an autoencoder whose bottleneck is shaped like a real display (e.g. 4×4 actuators with 8 levels, or a band-limited 1-D signal); compare reconstruction and shape-classification-from-code against the fixed hand-designed mapping at equal bandwidth.

**Just-in-time math:** the autoencoder/VAE objective in one page (only if you choose the codec); rank correlation (only if you choose the embedding).

**Days**
1. Your chosen family in one page (contrastive recap *or* autoencoder → VAE)
2. Shaping a bottleneck like a display: quantization and the straight-through trick (*or* audio front-ends: spectrograms as images)
3. Reading your own curves: is it learning, memorising, or broken?
4. From model metric to human prediction: what a follow-up user study would test
5. The one-page write-up
6. **Build:** run, compare to prediction, decide, write up.

**Done when:** a one-page write-up exists with a plot, a baseline, an ablation, seeds, the logged prediction, the surprise, and a decision.

**Canvas cards:** ③ `build-step6` … `build-step10`; ⑤ `bridge-crossmodal` or `bridge-codec`; lineage `lin-vae`, `lin-clip`, `lin-perceiver`.

**Resources**
- Papers: [VAE](https://arxiv.org/abs/1312.6114) (sections 1–2.3), [CLIP](https://arxiv.org/abs/2103.00020), [Perceiver](https://arxiv.org/abs/2103.03206) (figure 1)
- UDL ch. 17 (Variational autoencoders); [The vOICe](https://www.seeingwithsound.com/) for the reference mapping
- Data: MNIST / Fashion-MNIST / simple rendered shapes (Unity or matplotlib); [ESC-50](https://github.com/karolpiczak/ESC-50) if real audio is needed

---

## After week 12
Pick the next canvas chain by need, not by order: generative (`lin-vae` → `lin-ddpm` → `lin-ldm`) if the codec worked; world models (`lin-worldmodels` → `lin-dreamer`) for `bridge-active`; post-training (`lin-instructgpt` → `lin-dpo`) if you start steering language models for assistive agents (`bridge-vr`).
