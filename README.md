# AI Mastery Course

A customized, project-first curriculum to become an AI expert - from classical machine learning through to production-grade LLM systems.

## Who this is for

- **Background:** Experienced software developer; formal computer engineering education (calculus, linear algebra, statistics, diff eq - rusty but real)
- **Python:** Workable, not primary - this course ramps it deliberately, early
- **Goal:** Expert-level AI engineering - from classical ML to shipping reliable production LLM systems
- **Commitment:** As much time as it takes - realistically 9-15 months of focused evenings/weekends to expert-level competence

## Hardware reality (zero-dollar setup)

| Asset | What it's good for |
| --- | --- |
| Laptop | Coding, notebooks, editing, experiments that fit in RAM |
| Home server (Dell R610, 64GB+ RAM, ~12 CPU cores, Proxmox) | **CPU inference box** for quantized LLMs (Ollama / llama.cpp). Can run 7B-13B Q4 comfortably, even 30B slowly. This is your private inference server. |
| Older GPU (GTX 970, 4GB VRAM, 2TB NVMe, fresh OS) | Small PyTorch training/experiments (use CPU where the 4GB VRAM chokes). Fine for phase 2-3 scale. Maxwell (sm_52): pinned to NVIDIA legacy 470 driver + torch cu118 (see `curriculum/environment-setup.md`). |
| Kaggle free tier (30h/week GPU) | Training jobs too big for a 4GB-VRAM GPU. Also Colab/Paperspace free tiers. |

Key constraint: **4GB VRAM cannot fine-tune 7B models.** That's fine - the curriculum sequences around it (small models, LoRA on small bases, CPU quantized inference, cloud free tier for the rest). Full per-machine setup: `curriculum/environment-setup.md` (Python toolchain is `uv` everywhere).

## The course in one picture

```
PHASE 0  Setup + Python-for-data + math refresh      (~3-4 weeks)
PHASE 1  Classical ML with scikit-learn               (~4-6 weeks)
PHASE 2  Neural networks from first principles        (~5-7 weeks)
PHASE 3  Deep learning with a framework (fast.ai)     (~6-8 weeks)
PHASE 4  LLM engineering: RAG, evals, agents          (~8-12 weeks)
PHASE 5  Fine-tuning, inference, production           (~6-8 weeks)
PHASE 6  Capstone portfolio + specialization         (ongoing)
```

Each phase has: **goal, concepts, resources, hands-on projects with checkpoints, and a mastery rubric.** Do every project. The projects are the course.

## Design philosophy

1. **Build from scratch before using frameworks.** You'll implement backpropagation by hand (phase 2) before PyTorch hides it. This is what separates experts from API-pasters - and it makes every later failure legible.
2. **You learn by modifying running code.** Every milestone starts from a working example in `projects/` you run and modify one change at a time, then a milestone project applies the whole concept group together. The starter examples ARE the from-scratch builds - given to you already running, so the learning is in the modifications, not in staring at a blank page.
2. **Classical ML is not a relic.** Boosted trees still beat deep learning on tabular data (which is most real-world tabular data). Evaluation discipline transfers everywhere.
3. **The 2026 differentiator is evaluation, grounding, and reliability** - not training models from scratch. RAG is table stakes; good evals and reliable agents are what separate real systems from demos. We go deep there (phases 4-5).
4. **The portfolio IS the credential.** By phase 6 you'll have shipped a RAG system, a workflow automation, and a custom integration with documented results - the three capstone projects that prove you can ship.
5. **Real thinking, not courses-as-substitute.** Resources below are references to learn from, not to binge. Watch, then close the video and build it yourself.

## How to use this repo

- `curriculum/` - the phases, in order. Work top to bottom.
  - Each phase is divided into **milestones**: a concept group is learned by modifying a working example, then the group ends with one milestone project that applies all of it and requires recall of earlier material. You don't build a project after every single concept.
  - `curriculum/environment-setup.md` - per-machine environment setup (Arch laptop, GTX-970 box, Proxmox/R610), all on `uv`.
  - `curriculum/reference-library.md` - how this course relates to the eight major open-source AI course repos, and where to use each as a source, phase by phase.
- `projects/` - starter working examples live here as `projects/<phase>/milestone-<N>/`, and your own project work goes in the same tree (one subfolder per project). Phases 0 and 1 are the reference templates for this structure.
- `mentor-notes/` - a running log of what you learn and decide, session by session.
- Track your pace: estimate a phase, hit it or adjust, move on. Don't re-read materials to feel productive - build the next checkpoint.

## Key references used to build this (2026-verified)

- fast.ai Practical Deep Learning for Coders - course.fast.ai (free, code-first, PyTorch)
- Karpathy, Neural Networks: Zero to Hero - karpathy.ai/zero-to-hero.html
- 3Blue1Brown linear algebra + neural networks series - YouTube
- Chip Huyen, "AI Engineering" (book)
- Multiple 2026 roadmaps: RAG/agents/evals as the core AI-engineer stack; PyTorch as the dominant framework
- Eight open-source AI course repos assessed and mapped in `curriculum/reference-library.md` (Microsoft AI/ML/GenAI/Agents for Beginners, rohitg00's ai-engineering-from-scratch, Krishna Ik's Complete RoadMap, ashishps1's learn-ai-engineering, bishwaghimire's ai-learning-roadmaps)

Each phase doc links its specific sources.

## Your three-project portfolio (target, by end of Phase 6)

1. **Production RAG system** - chat-with-your-docs over a real corpus, with retrieval + faithfulness evals and citations
2. **Workflow automation** - an AI agent that does a real multi-step job with tools, state, and failure handling
3. **Custom integration** - an AI solution wired into a system (CRM/SaaS API/PDF pipeline), deployed as a service with telemetry

These demonstrate the full arc of AI engineering: from data and models to a reliable, measured, deployable system.
