# Learning-ai course design

Started 2026-08-13. Mentoring session - course design for an AI self-teaching path; guidance from here on (projects are the user's work, not solved-for-them).

## Session 1 - Course built

### The learner
- Software developer with comp eng education; math real but ~6 yrs rusty
- Python workable, not primary -> deliberate ramp in Phase 0
- Goal: become an AI expert, from classical ML to production-grade LLM systems
- "All of the above" area focus; will commit whatever time it takes

### Hardware reality (zero-dollar setup decided)
- Older 4GB-VRAM GPU (Maxwell-era): cannot fine-tune 7B models. Use for small runs; CPU as default; don't burn hours fighting CUDA wheel support on old arch - install older PyTorch or just use CPU
- Home server (64GB+ RAM, ~12 CPU cores, virtualized): CPU inference box via Ollama for quantized LLMs (7B-13B comfortable, up to 30B slow). This is the local inference server for phases 4-5
- Kaggle free tier (30h/wk GPU) is the training farm; Colab/Paperspace as backup
- User may add dedicated AI hardware (GPU or a higher-spec machine) later

### Course decisions (grounded in 2026 research)
- Sequence: Phase 0 (setup+Python+math refresh) -> 1 (classical ML, sklearn) -> 2 (neural nets from scratch, Karpathy) -> 3 (deep learning w/ framework, fast.ai Part 1) -> 4 (LLM engineering: RAG, evals, agents) -> 5 (fine-tune, inference, production) -> 6 (capstone portfolio + specialization)
- PyTorch chosen over TensorFlow (2026 consensus: research + new industry adoption)
- "Evaluation is the new system design" - evals treated as first-class skill, woven through phases 1-5, Phase 4 project 4.3 dedicated to it
- The 3-system capstone portfolio: RAG app, workflow automation/agent, custom integration - mapped to phases 4, 4, 5
- Balanced depth vs applied value: from-scratch builds (Karpathy, numpy NN) for depth, then deep applied LLM engineering (RAG/agents/evals). Skipping training-from-scratch as a career focus per research, but not as a learning phase
- Applied-AI insight recorded: most practitioners are no-code-only; the user's edge is custom engineering depth + integration background

### Key sources verified
- course.fast.ai (Practical DL for Coders, free, Part 1 + optional Part 2 Stable Diffusion from scratch)
- karpathy.ai/zero-to-hero (micrograd -> makemore -> GPT -> GPT-2)
- Chip Huyen "AI Engineering" (phase 4/5 spine)
- Andrew Ng ML Specialization: time-box/skim for someone with the math

### Next session ideas
- Review Phase 0 setup with the user once they start (env, Ollama on the home server, older-GPU decision)
- Pick first real dataset for Project 0.1
