"""Working example - Milestone 1.2: Classification and the metric zoo.

Run:  python3 projects/phase-1/milestone-1.2/example_classification.py

Logistic regression on the breast-cancer dataset, printing the full metric
set: accuracy, precision, recall, F1, ROC-AUC. All of them are printed on
purpose - this milestone is about learning WHEN each is the right one.

Modifications to try (from phase-1-classical-ml.md, M1.2.1 - M1.2.5):
  M1.2.1  re-balance the data to ~5% positive -> watch accuracy lie
  M1.2.2  change the decision threshold -> precision/recall trade-off
  M1.2.3  add tree / random forest / gradient boosting, compare overfitting
  M1.2.4  wrap in cross_val_score (5-fold) -> distrust the single split
  M1.2.5  wrap in a Pipeline -> ship it the way real teams do
"""

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

# Load the bundled breast-cancer dataset (569 rows, 30 features, binary target).
data = load_breast_cancer()
X = data.data
y = data.target

# NOTE: this example deliberately trains AND scores on the same data so the
# metric behavior is clean to observe. Real work uses train/test - M1.2.4.
model = LogisticRegression(max_iter=5000)
model.fit(X, y)
pred = model.predict(X)
proba = model.predict_proba(X)[:, 1]

print("Positive-class share:", f"{y.mean():.2%}")
print()
print(f"Accuracy:  {accuracy_score(y, pred):.3f}")
print(f"Precision: {precision_score(y, pred):.3f}")
print(f"Recall:    {recall_score(y, pred):.3f}")
print(f"F1:        {f1_score(y, pred):.3f}")
print(f"ROC-AUC:   {roc_auc_score(y, proba):.3f}")
print()
print("Which metric is 'right' depends on the business cost of each error.")
print("Accuracy is the weakest - it hides what happens inside the minority class.")
