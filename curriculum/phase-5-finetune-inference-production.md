# Phase 5 - Fine-Tuning, Inference, Production

**Duration:** ~6-8 weeks | **Cost:** mostly $0; small API spend possible | **Compute:** Kaggle GPU for fine-tunes; home server for serving a quantized model

## Goal

Move from "LLM app that works on my laptop" to "a model and service that runs reliably, cheaply, and measurably in production" - including when (and whether) to fine-tune at all. This closes the gap between prototypes and real systems.

## Why this phase exists for you

Phase 4 made you an app-layer expert. Two things stop people there: they fine-tune when they shouldn't, and they ship systems with no idea of cost, latency, or quality drift. Real production systems are judged on the opposite: reliability, predictable cost, and evidence. This phase is where you learn the serving math (memory, quantization, latency), the when-to-fine-tune judgment, and the guardrails/observability that make a system trustworthy.

## Concepts (in order)

1. **When to fine-tune, and when not to:** the decision framework - prompting vs RAG vs fine-tuning. (Most of the time, better retrieval or prompts win; fine-tuning earns its keep for style/format/domain vocabulary and for cost-reduction via distillation.)
2. **The memory math:** trainable params, precision (fp16/bf16/int8/int4), what fits on what GPU. Understand WHY 4GB VRAM can't fine-tune 7B - and what the workarounds are (smaller models, LoRA, CPU, cloud).
3. **Parameter-efficient fine-tuning:** LoRA / QLoRA - train tiny adapters on a frozen base. Plus SFT basics and a taste of preference tuning (DPO).
4. **Dataset engineering:** the skill where most engineering time goes - building clean, representative training/preference examples.
5. **Serving & inference:** vLLM or llama.cpp/Ollama, quantization, batching, KV cache, latency budgets (TTFT, tokens/sec). The difference between prototype and service.
6. **Production discipline:** caching (semantic + prompt caching to slash cost), model routing (cheap model for easy tasks), guardrails (input/output validation, prompt-injection basics, PII protection), telemetry (token count, latency, cost per call), monitoring (drift at a high level), and rollback-by-config.
7. **MLOps for LLMs:** experiment tracking (MLflow/W&B), prompt versioning, CI smoke evals (your Phase 4 harness wired into a pipeline).

## Resources

- Chip Huyen "AI Engineering" - parts on fine-tuning and inference are the spine of this phase
- Hugging Face PEFT + TRL libraries (docs) - LoRA/QLoRA/DPO, free
- vLLM docs (free, local); Ollama on your home server for the quantized-serving path
- Kaggle free GPU for the actual fine-tune runs (30h/week)
- (Context) revisit your Phase 2 GPT-from-scratch: pretraining vs post-training will finally snap into place here

## Hands-on projects

### Project 5.1 - The when-to-fine-tune decision (Week 1)

Take a real task (e.g. reformatting messy free-text into a strict structured schema, or adopting a specific tone/style, or domain vocabulary). PROVE, with your Phase 4 harness, that prompting alone is not reliably achieving it. Document that evidence - this is the argument for fine-tuning.

**Checkpoint to verify yourself:**
- [ ] You have a numeric gap between "prompted best effort" and "acceptable" on a golden set. No vibes.

### Project 5.2 - A real LoRA fine-tune with evaluation (Weeks 2-5) ⭐ third portfolio piece

Fine-tune a small open-weights model (7B-class on Kaggle, or smaller on your own hardware) with LoRA/QLoRA on your own curated dataset for your own task. Then EVALUATE it against the base model with your harness - same golden set, same metric.

**Checkpoints to verify yourself:**
- [ ] You curated the dataset yourself (not a canned one) and can justify each example type in it
- [ ] Before/after scores on your golden set prove the fine-tune changed behavior in the intended direction
- [ ] You can articulate the memory math of your run: how many trainable params, what precision, why it fit on the GPU it ran on

### Project 5.3 - Serve it like a product (Weeks 5-7)

Take your best RAG or agent from Phase 4, or your fine-tuned model, and ship it properly:

- Serve via vLLM (GPU) or Ollama (home-server CPU) for the model; your app behind a small API (FastAPI)
- Add telemetry: token count, latency, and cost per call - log every call
- Add caching for repeated queries; route cheap queries to a small model
- Add at least two guardrails (input validation, output schema check, PII redaction, prompt-injection test)
- Write the production README: architecture, latency/cost measurements, failure modes, how to roll back a model or prompt change

**Checkpoints to verify yourself:**
- [ ] You can state your p95 latency and per-request cost, and what moves them
- [ ] You ran at least one "model or prompt rollback" drill and it worked from config, not code
- [ ] You can demonstrate one real failure mode (e.g. a prompt injection attempt) being caught

## Mastery rubric - you're done with Phase 5 when...

- You decide fine-tune-vs-RAG-vs-prompt with evidence, not fashion
- You can fine-tune with LoRA, prove it worked, and explain the memory math
- You can ship an LLM service with cost/latency numbers, guardrails, and a rollback story
- You know the difference between a prototype and a product - and you've built both

## Portfolio note

This completes your three portfolio pieces (RAG system, agent, fine-tuned/deployed system). Treat the READMEs as first-class artifacts: problem, architecture diagram, eval results, cost/latency, honest limitations. These three, with documented numbers, are your proof of real capability.
