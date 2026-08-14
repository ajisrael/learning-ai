# Reference Library - External AI Course Repos

**How this course relates to the popular open-source AI curricula, and why it is built the way it is.**

This repo's curriculum is deliberately *not* "do these 8 courses". The plan was researched against the eight most-cited free AI course repos (cloned locally under `~/examples/` for fast reference). This doc records what each repo actually is, the decision to keep our own course instead of composing theirs, and how to use them as sources at the right moment in each phase.

## The eight repos, assessed (2026)

All were shallow-cloned on 2026-08-14 into `~/examples/<repo>`. Clones are for reference and quick copy of specific lessons, not to be pulled into this repo.

| Repo (local clone) | What it actually is | Strongest for us | Weakest for us |
| --- | --- | --- | --- |
| `microsoft/AI-For-Beginners` | 24-lesson classical AI intro: symbolic AI, perceptron-to-framework neural nets, CV, NLP, RL, ethics. BERT-era. | Alternate explanations + lab exercises for phases 2-3 (neural nets, CV). | Dated LLM coverage; ships TensorFlow as a first-class path (we chose PyTorch); notebook-sprawl. |
| `microsoft/ML-For-Beginners` | Gentle 26-lesson scikit-learn curriculum with quizzes and visuals. | Quiz/visual checkpoints if a Phase 1 concept needs a second angle. | Too beginner for an experienced dev; largely duplicates Phase 1; no value past it. |
| `krishnaik06/Complete-RoadMap-To-Learn-AI` | Hub README linking 3 sub-roadmaps (Data Science / GenAI / Agentic AI) - mostly YouTube playlists + week-by-week checklists. | The "pick a path, track a week" framing; nothing else survives contact with our plan. | Thin on projects, videos only, 2025-dated, career-course funneling. |
| `microsoft/generative-ai-for-beginners` | 21 current LLM-era lessons: prompt engineering, chat apps, embeddings/search, RAG, function calling, fine-tuning, security, lifecycle. Python + TS samples. | Best single repo for Phase 4 reading on RAG, function calling, fine-tune decisioning, security. | Azure/OpenAI-flavored; low-code lesson; it's an app-course, not an engineering course. |
| `ashishps1/learn-ai-engineering` | A curated index of free resources: books, papers, courses, tools, framework docs. No original content. | The reference shelf - best book/paper pointers (Chip Huyen, Karpathy, Illustrated Transformer, MCP docs). | Not a course; you must bring your own sequence. |
| `microsoft/ai-agents-for-beginners` | 18 current agentic-AI lessons: agentic frameworks, design patterns, tool use, agentic RAG, trustworthy agents, planning, multi-agent, metacognition, protocols (MCP/A2A), memory, security. | Best reading for Phase 4 project 4.4 (agents) and agentic RAG patterns. | Microsoft Agent Framework / Azure-centric; some lessons vendor-locked. |
| `rohitg00/ai-engineering-from-scratch` | **The outlier.** 20 phases, 503 lessons, ~1050h. From-scratch-first pedagogy, every lesson ships code + quiz + an output artifact. Includes a web site with a localStorage progress tracker, agent skills (`/learn`, `/start-learning`, `/course-guide`, `/find-your-level`), and compiled books. | Closest existing thing to this course's philosophy; per-lesson quizzes; the progress-tracker design is the seed for our future UI. | Scale is a trap (years to complete); much of it (multimodal research, autonomous systems, swarms) is beyond our app-engineering goal. |
| `bishwaghimire/ai-learning-roadmaps` | 12 leveled roadmaps (AI, DS, ML, DL, CV, NLP, LLM, GenAI, RAG, MLOps, research, safety) + the best leveled math-resource tables I've seen. | The math tables (Phase 0), and the LLM/RAG/MLOps roadmaps for mental maps of Phase 4-5. | No teaching content - maps and pointers only. |

## The decision: our own course as the spine, these repos as sources

Two ways to use these repos, and why we chose one.

### Option A - Compose the repos (submodules or "the course is the links")

Pull the repos in as git submodules, or define the course as "do this repo, then that repo".

**Why we rejected it:**

1. **Scale mismatch.** 503 lessons / ~1050h of aiefs alone is a multi-year path. The MS courses + roadmaps add another few hundred hours of overlap. Our goal is a focused, expert-level, 9-15 month path - curation *is* the product.
2. **Audience mismatch.** These repos teach a generic learner. None is tuned to this learner's real constraints: comp-eng math, 4GB-VRAM GPU, home-server CPU inference, Kaggle free tier, app-engineering goal. Composing them inherits their default assumptions (API spend, Azure, modern GPUs, "learn everything").
3. **Conflicting pedagogy.** Aiefs is build-from-scratch; the MS courses are follow-along notebooks; Krishna is watch-videos. Strung together they don't make a coherent path - they make a pile. Our plan's through-line (build first, then framework; evals as the differentiator; projects as the course) would be diluted, not strengthened.
4. **Maintenance and coherence.** Submodules pin versions; updating them mid-course changes content under you. The repos don't cross-reference each other, so overlap and gaps stay unresolved (e.g. MS has no from-scratch LLM; aiefs does, but 4x too deep for Phase 4).
5. **The projects are the differentiator.** The three-capstone portfolio (RAG system, agent, custom integration) exists in no repo. It's the credential, and it requires a custom course around it, not a link list.

### Option B - Our own course, each repo mapped in as a source (chosen)

The curriculum stays the curated 7-phase spine this repo already documents. Each external repo is used where it earns its keep: as **targeted reading and alternate explanations at the specific phase where a concept appears**, plus its best lesson *formats* (aiefs's per-lesson quiz pattern; the MS hands-on labs) borrowed as ideas.

This gives us: curation for our constraints, coherent sequencing, zero dependence on upstream churn, and the repos remain a deep reference library to dip into - locally, since they're cloned.

### When Option A *would* make sense

- A generic team learning track maintained by someone else, where "keep up with the repo" is a feature not a bug.
- A public curriculum project whose job is to aggregate others' work (a hub like Krishna's).
- None apply to a single-learner, project-first, hardware-constrained course. Note: if we ever want pinned, offline-safe copies of specific lessons, record their commit SHAs here rather than submoduling the whole repo.

## How to use each repo, phase by phase

| Our phase | Use these (local clone paths under `~/examples/`) |
| --- | --- |
| **0 - Setup, Python, math** | `bishwaghimire/ai-learning-roadmaps` math tables (README.md "The Math Behind It All" + `roadmaps/data-science-roadmap.md`). `rohitg00/ai-engineering-from-scratch` phases 00-01 for setup/math lesson alternatives. |
| **1 - Classical ML (sklearn)** | `microsoft/ML-For-Beginners` quizzes/visuals for any concept that needs a second angle. `rohitg00/ai-engineering-from-scratch` phase 02 for from-scratch implementations and evaluation lessons. |
| **2 - Neural nets from scratch** | `microsoft/AI-For-Beginners` lessons 03-05 (perceptron, own-framework) as alternate explanations. `rohitg00/ai-engineering-from-scratch` phase 03 (backprop, mini-framework) plus its quiz format. |
| **3 - Deep learning with PyTorch** | `microsoft/AI-For-Beginners` CV + NLP lessons (transfer learning, CNNs) for extra lab exercises. `rohitg00/ai-engineering-from-scratch` phases 04-05 for deeper CV/NLP lessons. |
| **4 - LLM engineering (RAG, evals, agents)** | `microsoft/generative-ai-for-beginners` lessons 04-08 (prompting, chat, search), 11 (function calling), 15 (RAG), 18 (fine-tuning decisioning). `microsoft/ai-agents-for-beginners` lessons 03-05 (design patterns, tool use, agentic RAG), 11-13 (protocols, context, memory). `rohitg00/ai-engineering-from-scratch` phase 11 (LLM engineering) + phase 13-14 (tools, agents) - the closest direct match to this phase's material. |
| **5 - Fine-tune, inference, production** | `rohitg00/ai-engineering-from-scratch` phase 10 lessons 06-12 (SFT, RLHF, DPO, quantization, inference) and phase 17 (infrastructure/production). `microsoft/generative-ai-for-beginners` lesson 14 (LLM lifecycle/LLMOps) and 13 (security). |
| **6 - Capstone + specialization** | `rohitg00/ai-engineering-from-scratch` phase 19 (87 capstone project briefs - use as idea bank, not workload). `ashishps1/learn-ai-engineering` + `bishwaghimire/ai-learning-roadmaps` as the reference shelf for specialization tracks. |

## The future progress-tracking UI (out of scope for now)

The gamified progress UI the course will eventually want already has a proven reference design: `rohitg00/ai-engineering-from-scratch/site/` ships a static site with `progress.js` (localStorage-only progress schema `aifs:progress:v1`, lesson-level completion + quiz answers), `roadmap.js` (phase prerequisite graph), and certification tracking. When we build our own tracker, reuse its data-model ideas (lesson path keys, completion + answers, versioned storage) rather than inventing a new one. It is deliberately out of scope until the course is being worked.

## Keeping this doc honest

- The clones in `~/examples/` are shallow (`--depth 1`); refresh them before deep-diving a lesson: `git -C ~/examples/<repo> pull`.
- When you copy an idea or a snippet from any of these repos into course material, they are all MIT/CC-licensed, but attribute the source in the notes file you keep.
- This mapping is a snapshot. If an upstream repo goes stale (or a better one appears), update this table, not the whole course.
