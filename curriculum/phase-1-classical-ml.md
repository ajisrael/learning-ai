# Phase 1 - Classical Machine Learning with scikit-learn

**Duration:** ~4-6 weeks | **Cost:** $0 (CPU only - this phase needs no GPU)

## How this phase is structured

This phase follows the course's core learning loop, organized into **milestones**:

```
For each milestone:
  1. Run a WORKING EXAMPLE (starter code in projects/phase-1/...)
  2. MODIFY it to learn each concept (change one thing, observe the effect)
  3. Finish with a MILESTONE PROJECT that combines the whole group's concepts
```

Projects are deliberately grouped into milestones - you don't build a project after every single concept. You learn a group of concepts via small modifications, then prove you can apply the whole group together in one project. Each milestone project also **requires recall of earlier milestones and phases** - that recall is the point.

## Goal

Master the classical ML stack on tabular data - the skill that (a) makes the rest of the field legible, and (b) is directly useful, because **boosted trees still beat deep learning on most real-world tabular data**. Learn evaluation discipline - the single skill that will carry through every later phase.

## Why this phase exists for you

In real engineering work you will repeatedly face "we have this messy CSV of transactions/customers/leads". The difference between an expert and a dabbler is: knowing the baseline, knowing the right metric, and knowing when a fancier model is a waste of time. That's this entire phase. Also: neural networks in phase 2 are *calibrated against* the intuition you build here (overfitting, train/val/test, metrics).

---

# Milestone 1.1 - Regression: from a working example to honest baselines (weeks 1-2)

**Concepts learned in this group:** linear regression, gradient descent intuition, regularization, evaluation for regression (RMSE/MAE), the "baseline" habit.

## Working example (run this first)

`projects/phase-1/milestone-1.1/example_linear_regression.py`

Run it: `python3 projects/phase-1/milestone-1.1/example_linear_regression.py`

It fits a linear model to a real bundled dataset (sklearn's diabetes) and prints the RMSE of a **constant baseline** versus the **linear model**. That baseline-vs-model comparison is the single most important habit in this phase - never report a model score without a baseline to beat.

## Learn the concepts by modifying the example

Do each modification in order. After each one, re-run and *write one line about what changed and why* before moving on.

**M1.1.1 - What does the baseline actually capture?**
Change the baseline prediction (currently the mean of `y`). Try predicting a constant of `0` instead. What happens to baseline RMSE? What does that tell you about the scale of the target?

**M1.1.2 - See the loss, then shrink it.**
The example only prints RMSE. Add a loop that prints RMSE after each of the model's training iterations so you can *watch* the error fall - this is gradient descent made visible. (Hint: increase `max_iter` in `LinearRegression` and log `n_iter_` after fit.)

**M1.1.3 - Add regularization, see the trade-off.**
Replace `LinearRegression` with `Ridge` (same data). Sweep `alpha` from `0.001` to `1000` (use a loop) and print RMSE for each. Where does performance peak? What is happening to the coefficients? This is the bias-variance tradeoff in one number.

**M1.1.4 - Move the evaluation off the training data.**
Right now the model is scored on the same data it trained on. Split the data into train/test first, train on the train split, score on the test split. Does the model's RMSE get worse or better? Why? This is why "the test set exists".

## Milestone project 1.1 - Regression with honest baselines

House-price or similar regression dataset (Kaggle "House Prices - Advanced Regression" is the classic). Build in order - do NOT skip to the fanciest model:

1. Constant baseline (predict the mean) - record its metric
2. Linear regression
3. Ridge/Lasso with regularization
4. Random forest
5. Gradient boosting (XGBoost/LightGBM)

**This project requires recall of:** the baseline habit (example 1.1), train/test splitting (M1.1.4), and Phase 0's pandas cleaning and NumPy.

**Checkpoints to verify yourself:**
- [ ] Every model scored on the SAME held-out test set, same metric (RMSE/MAE)
- [ ] A one-line writeup per model: what you tried, what changed, why
- [ ] A "what would I do next" list with 3 ideas ranked by expected impact

---

# Milestone 1.2 - Classification, ensembles, and the RIGHT metric (weeks 3-5)

**Concepts learned in this group:** logistic regression and classification, decision trees, random forests, gradient boosting, the bias-variance mental model, and - the heart of the group - **metric selection** (precision, recall, F1, ROC-AUC, cross-validation) under class imbalance.

## Working example (run this first)

`projects/phase-1/milestone-1.2/example_classification.py`

Run it: `python3 projects/phase-1/milestone-1.2/example_classification.py`

It trains logistic regression on sklearn's breast-cancer dataset and prints accuracy, precision, recall, F1, and ROC-AUC. All those metrics are printed for a reason - this milestone is about learning *when each one is the right one to optimize*.

## Learn the concepts by modifying the example

**M1.2.1 - Make accuracy lie.**
The breast-cancer set is ~37% positive. Artificially re-balance the data to be 5% positive (drop most positive rows, keep negatives). Now re-check the metrics. Accuracy barely moves while recall collapses. Write down *why* accuracy is a terrible metric here - you'll need this explanation for the project.

**M1.2.2 - Trade precision against recall.**
Change the decision threshold (instead of predicting `proba > 0.5`, try `0.3`, `0.7`, `0.9`). Watch precision and recall move in opposite directions. Find the threshold that maximizes F1. This is the threshold-tuning skill you'll use in the project.

**M1.2.3 - Trees, forests, boosting, and overfitting.**
Add a decision tree with `max_depth=1` (tiny), then `max_depth=None` (full). Then add a `RandomForestClassifier(n_estimators=100)` and a `GradientBoostingClassifier`. Compare all on the same test set. Note which ones overfit the training set, and how the ensemble fixes it. (Optional: replace with XGBoost/LightGBM - the 2026 tabular kings.)

**M1.2.4 - Stop trusting a single split.**
Wrap the evaluation in `cross_val_score` (5-fold) and compare the mean and spread against your single-split number. If a model's 5-fold results vary wildly, a single split was lying to you.

**M1.2.5 - Make it a real pipeline.**
Wrap preprocessing (scaling) + model in a `sklearn.Pipeline` (or `ColumnTransformer` for mixed types). Verify the whole thing trains and scores with one `.fit()` / `.score()`. This is what real teams ship.

## Milestone project 1.2 - Classification with the RIGHT metric

Customer churn or fraud detection (fraud is great because the class imbalance forces the metric lesson). Build a pipeline with:

- Preprocessing (missing values, categorical encoding, scaling) as a real `Pipeline`/`ColumnTransformer`
- Cross-validation instead of a single split
- At least two of: logistic regression, random forest, XGBoost
- Metric selection: argue whether accuracy, precision, recall, F1, or ROC-AUC is right for the *business* cost of each error - and justify with the actual dollar/effort cost of a false positive vs false negative

**This project requires recall of:** the metric-lies lesson (M1.2.1), threshold tuning (M1.2.2), tree/ensemble behavior (M1.2.3), cross-validation (M1.2.4), pipelines (M1.2.5), and Milestone 1.1's baseline + train/test discipline.

**Checkpoints to verify yourself:**
- [ ] You can explain, from your own project, why accuracy is a bad metric when 1% of cases are positive
- [ ] Feature importance: which 5 features drive the model, and does that match domain sense?
- [ ] Your pipeline runs end-to-end from raw CSV to scored predictions with one command

---

# Milestone 1.3 - Unsupervised: embeddings intuition (weeks 5-6)

**Concepts learned in this group:** PCA (dimensionality reduction, "represent data as vectors"), k-means clustering, and why these skills matter - this is your first taste of the vector-space thinking that RAG and embeddings are built on in Phase 4.

## Working example (run this first)

`projects/phase-1/milestone-1.3/example_pca_kmeans.py`

Run it: `python3 projects/phase-1/milestone-1.3/example_pca_kmeans.py`

It takes the iris dataset, reduces it to 2 dimensions with PCA, clusters with k-means, and prints how much variance each principal component captures.

## Learn the concepts by modifying the example

**M1.3.1 - What does each PCA component capture?**
Change `n_components` from `2` to `4`, then to `None`. Print the explained-variance ratio each time. How many components do you need to keep ~95% of the variance? What are you throwing away by using 2?

**M1.3.2 - The elbow.**
Change `n_clusters` from `3` to `2` and `4`. Plot/print the inertia for each. Where does the "elbow" (biggest drop-off in improvement) land? How does that compare to what you *know* about this dataset?

**M1.3.3 - Scale before you reduce.**
PCA is sensitive to feature scale. Multiply one feature by 1000 and re-run - what happens to the principal components? Add `StandardScaler` before PCA and note the difference. (This is a classic interview trap, and it's real.)

**M1.3.4 - PCA on a non-image dataset you choose.**
Reuse your Milestone 1.1 or 1.2 preprocessing on a new dataset and run PCA + k-means on it. Do the clusters look meaningful? This is where you start trusting the method on your own data.

## Milestone project 1.3 - Embeddings intuition

Take a dataset with no labels (e.g. news article text or customer purchase data). Apply PCA to the features and inspect what the principal components capture. Then run k-means and look at what clusters emerge - are they meaningful? This is your first taste of the "represent things as vectors" idea that RAG and embeddings are built on in phase 4.

**This project requires recall of:** Milestone 1.1's evaluation discipline, Milestone 1.2's pipeline habit, Phase 0's pandas cleaning, and M1.3.3's scale lesson.

**Checkpoint to verify yourself:**
- [ ] You can explain, in plain words, what PCA is doing to the data (compression, finding directions of variance) - and what you lose

---

## Mastery rubric - you're done with Phase 1 when...

- You can take a raw CSV and produce a scored, cross-validated model pipeline without opening a tutorial
- You can justify a metric choice by business cost, not by default
- You can look at a model's test score and say whether it's overfitting, underfitting, or solid - and say why
- You can explain the bias-variance tradeoff and gradient boosting to a non-technical stakeholder

## Note: engineering discipline from day one

This is also where the *discipline* habits start: log every experiment (params + metric), write a README that lets a stranger reproduce it in 30 minutes, and keep one-line "decision log" entries. These are the habits that make phases 3-5 not-chaos - they're what separates good engineering from lucky experiments.

## Resources (reach for these when a concept won't click)

- Andrew Ng Machine Learning Specialization - **time-box this to 1-2 weeks and skim the math derivations** (you have the math). Its value is vocabulary and the mental model, not the derivations. (Coursera, audit-free)
- Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (Geron) - chapters 1-8 are the best classical-ML reference. Read a chapter, do the exercises, move on.
- scikit-learn docs - the "choosing the right estimator" chart is a cheat sheet you'll actually use
- StatQuest - decision trees, random forests, gradient boosting, ROC curves (intuition in 15 min each)
- Reference library (curriculum/reference-library.md): `~/examples/microsoft/ML-For-Beginners` quizzes/visuals for a second angle; `~/examples/rohitg00/ai-engineering-from-scratch` phase 02 for from-scratch implementations and evaluation lessons.
