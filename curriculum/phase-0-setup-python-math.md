# Phase 0 - Setup, Python for Data, Math Refresh

**Duration:** ~3-4 weeks (focused evenings/weekends) | **Cost:** $0

## How this phase is structured

Same learning loop as every phase, grouped into **milestones**:

```
For each milestone:
  1. Run a WORKING EXAMPLE (starter code in projects/phase-0/...)
  2. MODIFY it to learn each concept (change one thing, observe the effect)
  3. Finish with a MILESTONE PROJECT that combines the whole group's concepts
```

Milestone 0.1 has no project - its deliverable *is* a working environment (the guide lives in `curriculum/environment-setup.md`). Milestones 0.2-0.4 end with the original Phase 0 projects, reorganized so each one applies its whole concept group.

## Goal

A working local + cloud environment for the whole course, Python fluency for data work (your weak point - this is the deliberate ramp), and a math refresh that turns "rusty" back into "usable" without a semester of lectures.

## Why this order matters

Everything after this runs on Python + NumPy + an intuition for gradients and probability. Skipping the ramp makes phases 1-5 fights with the language instead of the ideas. Two weeks here saves two months later.

---

# Milestone 0.1 - Environment setup: make every machine work (week 1)

**Concepts learned in this group:** the shared Python toolchain, per-machine extras (GPU driver, Ollama), and the habit of verifying your environment instead of assuming it.

## Working example (run this first)

`projects/phase-0/milestone-0.1/verify_environment.py`

Run it: `python3 projects/phase-0/milestone-0.1/verify_environment.py`

It prints the version of every package this course starts with (numpy, pandas, matplotlib, sklearn), and reports GPU + Ollama availability as *optional* checks - so the same script runs on all three machines and tells you what is missing.

## Learn the concepts by modifying the example

**M0.1.1 - Make the script your own.**
Add a check for `jupyter --version` (you'll use Jupyter daily). If you prefer to track it differently, change the output format. The point: this file is now your machine's "doctor" - modify it whenever you install something new.

**M0.1.2 - Break it on purpose.**
Temporarily run it inside a bare shell (no venv activated). Watch it fail on `import numpy`. This is the failure mode you must never confuse with a real bug - "my code is fine, my env is wrong". Being able to tell the difference immediately is the skill of this milestone.

**M0.1.3 - Write the reachability test.**
If your R610/Ollama is up, extend the script to `curl`-check `http://<r610-ip>:11434/api/tags` and print "Ollama reachable: yes/no". If the GTX-970 box is up, add a `nvidia-smi` check.

## Milestone project 0.1 - the environment is done when...

- [ ] `verify_environment.py` runs clean on the laptop with every import present
- [ ] The GTX-970 box answers `torch.cuda.is_available()` `True` (or you've consciously chosen CPU and documented it)
- [ ] `curl http://<r610-ip>:11434/api/tags` from the laptop lists your pulled model
- [ ] This repo is a git repo with `.venv/` ignored, and you've committed your first change

**Full setup instructions, per machine:** `curriculum/environment-setup.md`.

---

# Milestone 0.2 - NumPy and vectorized thinking (weeks 1-2)

**Concepts learned in this group:** arrays, broadcasting, matrix ops, vectorized computation - why loops are the enemy, and the "represent data as arrays" habit that everything else sits on.

## Working example (run this first)

`projects/phase-0/milestone-0.2/example_numpy.py`

Run it: `python3 projects/phase-0/milestone-0.2/example_numpy.py`

It builds a small array, does element-wise ops, a broadcasted row/column op, and a matrix multiply - printing each result so you can see what vectorization produces.

## Learn the concepts by modifying the example

**M0.2.1 - Vectorize a loop.**
The example computes a row sum with `arr.sum(axis=1)`. Rewrite that one operation as an explicit Python loop first (to see the shape of the problem), then confirm the vectorized version produces the identical result. This loop-vs-vector pairing is the core mental exercise of the phase.

**M0.2.2 - Break broadcasting.**
Change the shapes in the broadcasted add so the shapes are incompatible (e.g. `(3,1)` + `(3,1)`... actually try `(3,)` + `(3,2)`). Read the error message. Then explain broadcasting in one sentence to yourself. (This exact trap reappears in deep learning, where shape mismatches are the #1 bug.)

**M0.2.3 - Verify a matrix multiply by hand.**
Multiply a `(2,3) @ (3,2)` pair and check a single output cell against a manual dot-product computation you write out. You did this in comp eng - this is the dust-off.

**M0.2.4 - Make the linear model real.**
Extend the example: given a weights vector `w` and inputs `X`, compute predictions and mean-squared-error loss, all vectorized. Verify the loss against a loop version. This is literally what Phase 1 and Phase 2 models do under the hood.

## Milestone project 0.2 - NumPy mechanics

Redo this by hand with pure NumPy - no ML libraries, no loops where a vector op exists:

- Matrix multiply `A @ B` for shapes you choose, and verify against a manual dot-product computation
- Compute the mean and standard deviation of a matrix along both axes
- Implement a tiny linear model: given weights `w` and inputs `X`, compute predictions and a mean-squared-error loss, all vectorized

**This project requires recall of:** Milestone 0.1's environment (numpy must import), and M0.2.1-0.2.4's vectorization skills.

**Checkpoint to verify yourself:**
- [ ] You can explain broadcasting to a colleague in one sentence, and you used it deliberately

---

# Milestone 0.3 - Pandas, plotting, and the data pipeline (weeks 2-3)

**Concepts learned in this group:** DataFrames, cleaning dirty data, groupby/joins, and matplotlib/Seaborn for EDA - the data-wrangling foundation for every real project in this course.

## Working example (run this first)

`projects/phase-0/milestone-0.3/example_pandas.py`

Run it: `python3 projects/phase-0/milestone-0.3/example_pandas.py`

It loads a small CSV (bundled in the example's folder), inspects shape/types, finds missing values, cleans them, and produces two plots saved to files.

## Learn the concepts by modifying the example

**M0.3.1 - Follow the cleaning logic.**
The example makes cleaning decisions (what to do with missing values). For each decision, write one line of justification next to it - why drop, why fill, why that value. This explicit-reasoning habit is exactly what Project 0.3.1 (the pipeline drill) will grade you on.

**M0.3.2 - Add a column.**
Derive a new column from existing ones (e.g. a ratio, a category bucketing, or a datetime parse) and include it in the plots. This is feature engineering, in miniature.

**M0.3.3 - Group and join.**
Add a `groupby` (e.g. mean of a numeric column by a categorical one) and print the result. Then, if you have a second tiny dataset, `merge` the two on a key and inspect the result.

**M0.3.4 - Make the plots reusable.**
Refactor the plotting code into a function that takes a DataFrame and plot settings, so it can be re-run on new data without edits. (This exact requirement appears as a checkpoint in the milestone project.)

## Milestone project 0.3 - The data pipeline drill

Grab a real messy dataset you care about (public options: a city's open-data portal, a Kaggle tabular set, or scrape something you use). Using pandas:

- Load it, inspect shape/types, and find the dirty spots (missing values, bad types, duplicates, inconsistent categories)
- Clean it with explicit reasoning for each decision, and write the cleaning as a reusable function
- Produce 3-4 plots that answer real questions about the data
- Save the cleaned result

**This project requires recall of:** Milestone 0.1's environment, Milestone 0.2's vectorized thinking (used inside pandas), and M0.3.1-0.3.4's cleaning + reusable-plot habits.

**Checkpoints to verify yourself:**
- [ ] Every cleaning decision has a one-line justification written next to it
- [ ] Your plotting function can be re-run on new data without edits
- [ ] You can load the result back into pandas and re-plot without errors

---

# Milestone 0.4 - Math refresh, checked by code (weeks 2-4, alongside the above)

**Concepts learned in this group:** linear algebra (vectors, dot products, transformations), calculus (chain rule as a tool), and probability/statistics (distributions, expectation, Bayes) - dusted off, not re-taught.

## Working example (run this first)

`projects/phase-0/milestone-0.4/example_math.py`

Run it: `python3 projects/phase-0/milestone-0.4/example_math.py`

It computes a dot product, applies a matrix as a transformation, and numerically checks a derivative via the limit definition - showing you the math *as code* so you can experiment with it.

## Learn the concepts by modifying the example

**M0.4.1 - The chain rule, by hand and by code.**
Watch the 3Blue1Brown neural networks chapters 1-4. Then extend `example_math.py` to numerically check `dy/dx` for `y = sigmoid(w*x + b)` using the central-difference limit, and compare to the analytic derivative you write by hand. This is the exact math Phase 2's backpropagation runs on.

**M0.4.2 - A matrix as a transformation.**
Plot (or print) what multiplying a few 2D vectors by a 2x2 matrix does to their direction/length - pick a rotation matrix and a shear matrix. Write a 3-line plain-English explanation of "matrix as transformation" in your notes file.

**M0.4.3 - Expectation and variance by simulation.**
Draw a large sample from a normal distribution with numpy, compute its mean/variance, and compare to the theoretical values as you increase the sample size. Watch the empirical values converge - that convergence *is* the intuition behind statistics.

**M0.4.4 - Bayes with a concrete example.**
Pick a real diagnostic example (e.g. a test with known sensitivity/specificity and a rare condition) and compute the posterior probability by hand and with a few lines of numpy. The number that surprises you is the one worth remembering.

## Milestone project 0.4 - Math dust-off

- Watch 3Blue1Brown linear algebra; for each of: dot product, matrix as transformation, inverse, eigenvectors - write a 3-line plain-English explanation in your own words (this becomes your notes file)
- Watch 3Blue1Brown neural networks chapters 1-4, then write out the chain rule for a 3-layer composition `f(g(h(x)))` by hand on paper
- Check the sigmoid derivative and Bayes example from M0.4.1/M0.4.4 in code

**This project requires recall of:** Milestone 0.2's NumPy (the code checks), Milestone 0.3's pandas habit (optional, if you verify on a real dataset).

**Checkpoint to verify yourself:**
- [ ] You can compute `dy/dx` for `y = sigmoid(w*x + b)` by hand without looking it up

---

## Mastery rubric - you're done with Phase 0 when...

- Your `verify_environment.py` runs clean everywhere (or you've consciously documented a CPU-only GTX-970 choice)
- You can load, clean, and explore an unfamiliar dataset in pandas without checking docs on every call
- You can express a data operation as a vectorized NumPy line instead of a loop
- You can explain dot products, the chain rule, and a normal distribution in plain words (your own words, not memorized)
- You have the two notes files started: `mentor-notes/` entries and your math plain-English notes

**Going faster:** if the math truly comes back in days, skip the lecture parts and just do the checkpoint exercises.

## Resources (reach for these when a concept won't click)

- 3Blue1Brown - Essence of Linear Algebra (YouTube, ~5h total) - https://www.3blue1brown.com/topics/linear-algebra
- 3Blue1Brown - Neural Networks series (the famous chapters 1-4 first: what a neuron is, gradient descent, backprop) - watch this week, it anchors phase 2
- khanacademy.org - statistics & probability (only the parts you don't recall)
- Python: numpy 100 exercises (github.com/rougier/numpy-100) and the pandas get-started guides (pandas.pydata.org)
- StatQuest (YouTube) for statistical intuition
- Reference library (curriculum/reference-library.md): `~/examples/bishwaghimire/ai-learning-roadmaps` math tables for leveled math resources; `~/examples/rohitg00/ai-engineering-from-scratch` phases 00-01 for alternate setup/math lessons.
