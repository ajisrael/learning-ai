"""Working example - Milestone 1.1: Linear regression vs the constant baseline.

Run:  python3 projects/phase-1/milestone-1.1/example_linear_regression.py

This is the starter you build on for Milestone 1.1. It fits a linear model to
the sklearn diabetes dataset and reports RMSE for:
  1. a constant baseline (predict the mean every time)
  2. a linear regression model

The point of the baseline is NOT to be a good model. It is the bar your model
must clear. If your fancy model can't beat "predict the mean", it isn't
learning anything.

Modifications to try (from phase-1-classical-ml.md, M1.1.1 - M1.1.4):
  M1.1.1  change the baseline prediction (e.g. constant 0) and watch RMSE
  M1.1.2  add a loop that prints RMSE as training progresses (gradient descent made visible)
  M1.1.3  swap LinearRegression -> Ridge, sweep alpha, watch the trade-off
  M1.1.4  split train/test before scoring (never score on training data)
"""

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def rmse(y_true, y_pred):
    """Root mean squared error, computed directly so this example never
    depends on sklearn's API for the metric changing between versions."""
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


# Load the bundled diabetes dataset (442 rows, 10 features, regression target).
data = load_diabetes()
X = data.data
y = data.target

# --- Baseline: always predict the mean. -------------------------------------
baseline_prediction = y.mean()
baseline_rmse = rmse(y, [baseline_prediction] * len(y))
print(f"Baseline (predict mean = {baseline_prediction:.1f}): RMSE = {baseline_rmse:.1f}")

# --- Linear model on the SAME data ------------------------------------------
model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)
model_rmse = rmse(y, pred)
print(f"Linear model:                              RMSE = {model_rmse:.1f}")

# --- Interpretation ----------------------------------------------------------
print()
print(f"Improvement over baseline: {(1 - model_rmse / baseline_rmse) * 100:.1f}%")
print("The model is NOT allowed to score this well forever -")
print("both numbers above are on the TRAINING data. See M1.1.4.")
