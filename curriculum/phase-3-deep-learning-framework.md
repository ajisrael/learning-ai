# Phase 3 - Deep Learning with a Framework (fast.ai + PyTorch)

**Duration:** ~6-8 weeks | **Cost:** $0 | **Compute:** Kaggle free GPU (30h/wk); older 4GB-VRAM GPU for small runs; CPU for tabular/classical

## Goal

Go from "I built a GPT from scratch" to "I can train and ship modern deep learning models for vision, text, and tabular data" using the industry framework (PyTorch) - the way real practitioners do. Phase 2 gave you the mechanics; this phase gives you the tools and the tricks of the trade.

## Why this phase exists for you

You chose PyTorch - verified 2026 consensus: it dominates research and new industry adoption (fast.ai, and every current roadmap agree). fast.ai is the best *code-first* course that exists: you build working state-of-the-art models in lesson 1 and progressively understand the machinery. Its structure (top-down, build-then-understand) deliberately complements Karpathy (bottom-up, understand-then-build) - that pairing is what makes you fast AND deep.

## Concepts

- PyTorch: `nn.Module`, tensors, autograd, `Dataset`/`DataLoader`, training loops, GPU movement
- Transfer learning + fine-tuning pretrained models (the single most useful practical skill - you rarely train from scratch in the real world)
- Computer vision: CNNs, image classification, augmentation, segmentation (overview)
- NLP: sentiment classification, and the beginnings of using pretrained transformers (Hugging Face)
- Tabular deep learning + collaborative filtering (recommendation systems)
- Deploying a model as a web app (Gradio) - first taste of shipping
- SGD and the complete training loop, implemented by hand - connecting Phase 2 to Phase 3
- (Optional, expert-track) Part 2: build Stable Diffusion from scratch (30+ hours, seriously deep - take it if time permits; it's the ultimate "I really understand this" proof)

## Resources

- **fast.ai - Practical Deep Learning for Coders Part 1** (course.fast.ai, free) - 9 lessons, ~90 min each, paired with the free book (Deep Learning for Coders with fastai & PyTorch, readable as Jupyter notebooks)
- Hugging Face course (huggingface.co/learn) - the transformers piece, in parallel with the last lessons
- Do NOT skip the lesson homework/own-project extensions - the lessons are built around you building your own model at the end of each one

## Hands-on projects

### Project 3.1 - Vision: your own classifier (Weeks 1-3)

Follow the fast.ai path: train an image classifier on a dataset you care about (pets, plants, product photos - whatever interests you). Use transfer learning from a pretrained model. Then push it: tune, augment, and get it measurably better.

**Checkpoints to verify yourself:**
- [ ] You trained a model with PyTorch/fastai and can explain what transfer learning did under the hood
- [ ] You improved accuracy from a naive baseline by a deliberate technique (augmentation, unfreezing, LR tuning) and can say which and by how much
- [ ] You built a Gradio app that serves your model

### Project 3.2 - NLP: sentiment + the transformers leap (Weeks 4-6)

Build a sentiment classifier on movie reviews. Then the key move: swap to a pretrained transformer (Hugging Face) and measure the difference.

**Checkpoints to verify yourself:**
- [ ] You can articulate why the pretrained transformer beats your from-scratch net (what does pretraining give it?)
- [ ] You fine-tuned a Hugging Face model and know where the weights went (what did you actually change?)

### Project 3.3 - Tabular + collab filtering (Weeks 6-8)

fast.ai's tabular lessons, applied to a dataset you bring. Build a recommendation system with collaborative filtering on a public dataset (e.g. MovieLens).

**Checkpoint to verify yourself:**
- [ ] You can explain the difference between a classical (Phase 1) tabular pipeline and a deep tabular model, and when each wins

## Mastery rubric - you're done with Phase 3 when...

- You can take a vision or text dataset and produce a fine-tuned, evaluated, deployed-as-a-demo model without a tutorial open
- You can build and debug a PyTorch training loop by hand (not just call `fitted()`)
- You understand where pretrained weights live in a fine-tune and what you actually changed
- You can articulate what makes deep learning beat classical ML in some domains and lose in others (e.g. tabular)

## Notes

- **Book + course pair:** the free book is the same content in prose/notebooks - read the chapter, do the lesson, then build your own variant. Don't do one without the other.
- **GPU budget:** Kaggle's 30h/week is enough for this phase if you train deliberately (small datasets, good checkpoints). An older GPU handles the small stuff on your own schedule.
