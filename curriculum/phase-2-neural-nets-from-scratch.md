# Phase 2 - Neural Networks from First Principles

**Duration:** ~5-7 weeks | **Cost:** $0 | **Compute:** CPU is fine (small models)

## Goal

Build neural networks with your own hands, from zero, before any framework hides them from you. After this phase, "the model learns by backpropagation" will be something you've literally coded, not something you've heard.

## Why this phase exists for you

Your stated goal is **expert**, not "person who can call an API". The people who win at this are the ones who, when a training run misbehaves, can reason about *why* instead of reshuffling prompts. Karpathy's own framing: language models are the best place to learn deep learning, and almost everything transfers to vision and beyond. This is also the phase where your comp-eng math actually pays - the chain rule you brushed up in Phase 0 becomes the whole ballgame here.

## Concepts (in the order you'll actually build them)

1. The neuron, forward pass, and loss
2. Backpropagation = the chain rule applied mechanically - build a tiny autograd engine
3. Training loops, gradient descent, learning rates, overfitting
4. Building up: from bigram model to MLP language models
5. BatchNorm, and how real training tricks emerge from debugging real runs
6. Attention, then a complete GPT from scratch - the architecture behind every LLM
7. Tokenization (byte-pair encoding) - because "tokens" underpin all of phase 4
8. (Optional, expert-track) GPT-2-scale training on a small GPU - this is where your Kaggle/local-GPU time goes

## Resources

- **Karpathy - Neural Networks: Zero to Hero** (karpathy.ai/zero-to-hero.html, GitHub karpathy/nn-zero-to-hero) - THE course for this phase. Sequence:
  - Lecture 1: micrograd - backprop from scratch (~2h video + exercises)
  - Lectures 2-6: makemore parts 1-5 - bigram → MLP → BatchNorm → backprop ninja → WaveNet (~6h total)
  - Lecture 7: build GPT from scratch
  - minBPE / tokenizer lectures
- 3Blue1Brown neural network chapters (re-watch the backprop chapter at the exact moment you're writing yours - it will click differently)
- Each lecture has **exercises in the video description** - do them. They're the real work.

## Hands-on projects

### Project 2.1 - micrograd (Week 1-2)

Build your own tiny autograd engine in pure Python (a `Value` class that tracks a computation graph and supports backprop). Then train a small MLP to fit a function.

**Checkpoints to verify yourself:**
- [ ] You can explain, from your own code, exactly where the chain rule lives in backprop
- [ ] You can compute a gradient by hand on paper and verify your engine produces the same number

### Project 2.2 - Make it make text (Weeks 3-5)

Build a character-level language model that generates plausible text (names, baby names, etc.) from a real corpus. Iterate the way the lectures do: bigram first, then an MLP, add BatchNorm, debug the loss curves as you go.

**Checkpoints to verify yourself:**
- [ ] Each iteration's loss is recorded and you can explain what each change did
- [ ] You have fixed at least one real bug where the model misbehaved (learning too slow, plateauing, NaNs) - and you can explain the fix in terms of the math

### Project 2.3 - GPT from scratch (Weeks 5-7)

Build a minimal GPT - attention, multi-head, positional encoding, training loop - and train it on a small corpus (e.g. Shakespeare or a corpus of your choice). Make it *generate text you can actually read*.

**Checkpoints to verify yourself:**
- [ ] You can draw the attention mechanism from memory and explain what a query/key/value IS in plain words
- [ ] You can articulate what "training a language model" means at the token level (next-token prediction), because this exact mental model powers everything in Phase 4

## Mastery rubric - you're done with Phase 2 when...

- You have written backpropagation, a training loop, and an attention block yourself
- Given a training curve, you can diagnose at least: too-high LR, too-low LR, underfitting, overfitting
- You understand what tokens are and why next-token prediction produces language
- You can explain to a smart non-expert how a neural net learns, using your own code as the example

## Hardware note

Everything here runs on CPU. If you want the optional GPT-2 run, use Kaggle's free GPU (30h/week). An older 4GB-VRAM GPU can run the small GPTs in this phase fine.

## A word on difficulty

This is the hardest phase in the whole course, and it's where most people quit. If a lecture's code breaks, that's the lesson - the debugging IS the learning. Don't move to Phase 3 until the rubric is genuinely met; Phase 3 is enormously more pleasant with this underneath it.
