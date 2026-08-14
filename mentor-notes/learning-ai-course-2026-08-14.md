# Learning-ai course design

Started 2026-08-13. Mentoring session - course design for an AI self-teaching path; guidance from here on (projects are the user's work, not solved-for-them).

## Session 2 - External repo research and mapping

### What happened
- User gathered 8 popular open-source AI course repos and asked to clone, analyze, and decide: compose them (submodules) vs keep our own course.
- Cloned all 8 shallow into `~/examples/`: microsoft/AI-For-Beginners, microsoft/ML-For-Beginners, krishnaik06/Complete-RoadMap-To-Learn-AI, microsoft/generative-ai-for-beginners, ashishps1/learn-ai-engineering, microsoft/ai-agents-for-beginners, rohitg00/ai-engineering-from-scratch, bishwaghimire/ai-learning-roadmaps.

### Key findings
- `rohitg00/ai-engineering-from-scratch` is the outlier: 20 phases / 503 lessons / ~1050h, from-scratch-first pedagogy that matches our design philosophy, per-lesson quiz + code + outputs, and a static site with a localStorage progress tracker (`site/progress.js`, schema `aifs:progress:v1`) - the seed for our future gamified UI.
- Microsoft's GenAI-for-Beginners + Agents-for-Beginners are the best Phase 4 reading (RAG, function calling, agentic patterns, security).
- Krishna Ik and the two "roadmap/resource" repos add navigation value, not content; ML-for-Beginners is too gentle for this learner; AI-for-Beginners is dated but useful for phases 2-3 alternates.
- The decision: keep our own 7-phase course as the spine; map the repos in as targeted sources per phase (documented in `curriculum/reference-library.md`). Rejected submodules because of scale/audience/pedagogy mismatch and the fact that the 3-capstone portfolio exists in no repo.

### Decisions recorded
- No submodules. Repos stay as shallow clones in `~/examples/`; the course points at specific lessons, never becomes "do these repos".
- Gamification UI stays out of scope; when built, reuse aiefs's progress-tracker data-model design.
- Attribute copied ideas/snippets in notes; refresh clones with `git -C ~/examples/<repo> pull` before deep use.

### Next session ideas
- Phase 0 setup walkthrough once the user starts (env, Ollama on home server, older-GPU decision).
- Pick first real dataset for Project 0.1.
