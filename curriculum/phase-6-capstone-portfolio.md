# Phase 6 - Capstone Portfolio and Specialization

**Duration:** ongoing - starts once Phase 5 is solid, never really "ends"

## Goal

Demonstrate mastery by shipping complete systems with documented, measured results, then go deep on one specialization. The capstone work proves you can take an idea from data to a reliable, evaluated, deployable system - the difference between knowing concepts and being able to ship them.

## Why this phase exists

Phases 0-5 taught you the skills. This phase makes them durable and public: three finished systems, each with an architecture diagram, measured results, and honest discussion of trade-offs. These are the artifacts that demonstrate real capability to anyone (teams, collaborators, or your future self), and the discipline of documenting decisions is the practice that makes all the earlier skill permanent.

## The three capstone projects

Each reuses and hardens work you already built - now finished to a professional standard.

### Capstone 1 - Production RAG system (hardens Project 4.1/4.2)

"Chat with your docs" over a real corpus you care about. Production standard means:

- Clean, reproducible ingestion pipeline (raw docs → chunks → index)
- Retrieval + faithfulness evals with a golden set, and the numbers in the README
- Citations in every answer
- A working service (API + a thin UI like Gradio)

**Mastery bar:** someone can clone your repo, run one command, and reproduce your documented results.

### Capstone 2 - Agent with tools (hardens Project 4.4)

An agent that does a real multi-step job with 2-4 narrow tools. Production standard means:

- Explicit failure handling (bad tool calls, retries, loops, hard stop)
- State management that survives long sessions
- Evaluation on trajectory and failure modes, not just the happy path
- A documented failure-mode table in the README

**Mastery bar:** you can describe a real failure you observed, how you detected it, and the guardrail you added.

### Capstone 3 - Custom integration (hardens the Phase 5 deployment work)

An AI solution wired into a real external system (a SaaS API, a CRM, an email or PDF pipeline), deployed as a service. Production standard means:

- Telemetry: token count, latency, and cost per call, logged for every request
- Guardrails (input validation, output schema checks, at least one injection test)
- Caching for repeated queries; routing cheap tasks to a small model
- A rollback story: revert a model or prompt change from config, not code

**Mastery bar:** you can state your p95 latency, per-request cost, and at least one measured failure mode.

## The README standard

Every capstone gets a README that a stranger could use to evaluate you as an engineer. Required sections: problem, architecture diagram, data sources, eval methodology + results, cost/latency numbers, known limitations, how to reproduce. Write the READMEs before the project is "done" - they force you to finish properly.

## Specialization track (pick one after the capstones)

At this depth, specialization is where expertise compounds. Options:

1. **Deep language systems** - advanced RAG (GraphRAG, agentic RAG), long-context, multilingual, reasoning models
2. **Computer vision** - object detection, segmentation, video, multimodal systems (fast.ai Part 2 is the natural next course here)
3. **Fine-tuning & model development** - dataset engineering at scale, alignment (RLHF/DPO), distillation to smaller models
4. **Inference & infrastructure** - serving engines (vLLM/SGLang), quantization, KV cache, GPU efficiency
5. **Reinforcement learning** - after you're confident in supervised work; RL is its own world
6. **Security & safety** - red-teaming, prompt injection defenses, guardrails, responsible AI

Pick based on what you found most interesting in phases 2-5. The rule: go deep on one, don't sample all shallowly.

## Continued learning habits

- Read one paper per week in your specialization; implement the small ones (this is how Karpathy built intuition, and it compounds)
- Re-run your capstone evals whenever a model or library you depend on changes - regression checking is a lifelong habit
- Build in public: publish your projects, write short notes on what failed and what you learned
- Contribute to an open-source project in your area once you're confident - the code review process is excellent feedback

## Mastery rubric - you've mastered the course when...

- Your three capstone projects are finished, documented, and reproducible
- You can explain - to yourself on paper - the full journey of an AI system: data → features → model → training → evaluation → serving → monitoring
- You have one specialization you can go deep on without tutorials
- You can read a research paper in your area and extract the idea, the method, and the limitations
- Your learning habits are self-sustaining: you no longer need a curriculum, you can self-direct new areas

## Notes

- Don't start this phase early - the capstones are built ON phases 1-5. Skipping foundations to "finish projects faster" produces portfolio pieces you can't defend at depth.
- The capstones don't need new technology - they need finish, measurement, and documentation. Polish beats novelty here.
- If a capstone takes far longer than expected, that's normal and useful: the friction IS the learning. Write down what took longest and why.
