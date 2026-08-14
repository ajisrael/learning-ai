# Phase 4 - LLM Engineering: RAG, Evaluation, Agents

**Duration:** ~8-12 weeks | **Cost:** mostly $0 (free tiers); some provider API spend possible (see below) | **Compute:** home-server Ollama for local inference; laptop for the rest

## Goal

Become dangerous with LLMs as an engineering material: call them reliably, ground them in private data, measure whether they're actually good, and wire them into tools that do real work. This is the phase where you go from "LLM demo" to "LLM product" - grounding models in your own data and building automation that holds up.

## Why this phase exists for you

The 2026 consensus (verified across multiple current roadmaps) is blunt: **prompting is commodity, RAG is table stakes, and the differentiators are evaluation, reliable agents, and production discipline.** This phase is also where your Phase 2 "GPT from scratch" pays off - you understand tokens, attention, and next-token prediction, so you debug LLM apps instead of guessing at them. You'll deliberately NOT use a framework for the first RAG build - you'll wire the pipeline yourself so you understand every joint, then adopt tooling where it earns its keep.

## Concepts (in dependency order)

1. **LLM APIs as an engineering surface:** context windows as the cost/limit model, sampling params (temperature/top-p), streaming, structured output (JSON/schemas), token budgets, rate limits. "The LLM is an API you engineer around."
2. **Prompt/context engineering:** system vs user, few-shot, context as a budget, chaining. (Not memorized tricks - engineering habits.)
3. **RAG (Retrieval-Augmented Generation):** the pipeline - chunk, embed, store, retrieve, ground. Why it exists (grounding in fresh/private data, cutting hallucination).
4. **Retrieval quality:** chunking strategies, embeddings + vector search, BM25/keyword, hybrid search, reranking, metadata filters, and **retrieval evals** (recall, precision, MRR).
5. **Evaluation (the underrated skill):** golden datasets, deterministic checks, LLM-as-judge, faithfulness/relevance metrics (RAGAS), regression suites. If quality isn't measured, it isn't engineered.
6. **Agents and tool use:** the agent loop (decide → act → observe), tool design as a contract (narrow tools, clear schemas, error-as-observation), state management, failure handling, retries, human-in-the-loop checkpoints.
7. **When NOT to build:** know when RAG, when fine-tuning (phase 5), when a canned tool beats custom - a senior engineer's judgment skill.

## Resources

- **Chip Huyen, "AI Engineering"** - the definitive book for this exact phase. Read it, keep it as reference.
- Hugging Face course (free) - transformers/LLM APIs/pipelines
- OpenAI and Anthropic API docs - the structured-output and function-calling pages are the real curriculum
- RAGAS docs for evaluation; one vector store to start (pgvector or Chroma - both free/local)
- (Context) revisit your Phase 2 GPT lecture 7: this is the practical face of what you built
- 2026 AI-engineer roadmaps (dataskew.io, vibeengines.com) for the mental map of what production LLM systems look like

## Hands-on projects

### Project 4.1 - RAG from first principles (Weeks 1-3) ⭐ your first portfolio piece

Build "chat with your docs" over a real corpus you care about (a set of public reports, your own notes, a manual, legal texts - pick something meaty). First build it WITHOUT a framework: chunk → embed → vector store → retrieve → prompt with citations. Then measure it.

**Checkpoints to verify yourself:**
- [ ] You can draw the full pipeline from document to cited answer, and identify where each of: chunking, embedding, retrieval, and generation happen
- [ ] Write 20 golden questions with expected answers/citations. Measure retrieval hit rate and answer faithfulness. You now have evidence, not vibes
- [ ] Break it on purpose: bad chunking, wrong embeddings, poisoned context - and diagnose each failure from the retrieval numbers, not the output

### Project 4.2 - Make RAG production-decent (Weeks 3-5)

Add, in order: hybrid search (BM25 + vectors), a reranker, metadata filters, and smarter chunking. Measure the delta on your golden set after each change.

**Checkpoint to verify yourself:**
- [ ] A change-log with numbers: "added reranker → retrieval precision 0.72 → 0.85" style entries. This is the artifact that proves each change actually improved the system.

### Project 4.3 - LLM evaluation pipeline (Weeks 5-7)

Build a reusable eval harness: golden dataset, LLM-as-judge with calibration (spot-check judges against human labels), deterministic checks (format, schema, citation presence), and a regression command you can run after any prompt or model change.

**Checkpoints to verify yourself:**
- [ ] You can point this harness at any prompt/model change and get a before/after score
- [ ] You caught at least one real regression with it (change a prompt that LOOKS fine, watch quality drop, catch it with the harness)

### Project 4.4 - Agent with tools (Weeks 7-10) ⭐ second portfolio piece

Build an agent that does a real multi-step job with tools - pick something with genuine workflow (e.g. "research X and produce a structured briefing with citations", or an internal-sales-qualification agent, or an ops troubleshooting agent). Give it 2-4 narrow tools with proper schemas. Make it handle failures: bad tool calls, retries, loops, and a hard stop.

**Checkpoints to verify yourself:**
- [ ] You can describe one failure mode you observed, how you detected it, and the guardrail you added - the exact narrative that separates reliable agents from demos
- [ ] You evaluate it on its trajectory (did it plan well?) and failure modes, not just the happy path

## Mastery rubric - you're done with Phase 4 when...

- You can build a RAG system from scratch, then harden it, and PROVE the improvements with numbers
- You can build and debug a tool-using agent and articulate why it's reliable (or not) without hand-waving
- You treat evaluation as a first-class engineering artifact, not an afterthought
- You can say, for a given real-world task, whether RAG / agent / canned tool / fine-tune is right and defend it

## Cost & hardware notes

- Do API experimentation on free/low tiers first; for steady local work run a quantized model on your home server via Ollama (your Phase 0 setup) - 7B-class models are enough for most exercises
- Some eval work (embedding models, small fine-tune previews) can run on your Kaggle free tier
- Budget note: real API spend is part of LLM engineering practice - keep it small while learning, and track it (token counts, cost per call) as a habit; that discipline pays off in every later project

## Portfolio note

Projects 4.1 and 4.4 are two of your three course portfolio pieces. When each passes its rubric, write its README properly (problem, architecture diagram, eval results, honest trade-offs) - that README is a portfolio asset.
