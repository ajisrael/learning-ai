"""Working example - Milestone 0.3: pandas cleaning and plotting.

Run:  python3 projects/phase-0/milestone-0.3/example_pandas.py

Loads a small CSV (bundled here as sales_data.csv), inspects shape/types, finds
missing values, cleans them, and produces two plots saved to files. The plot
code is kept as a plain script so you can refactor it into a function (M0.3.4).

Modifications to try (from phase-0-setup-python-math.md, M0.3.1 - M0.3.4):
  M0.3.1  write a one-line justification next to each cleaning decision
  M0.3.2  derive a new column from existing ones
  M0.3.3  add a groupby and a merge on a key
  M0.3.4  refactor the plotting into a reusable function
"""

import os

import matplotlib
matplotlib.use("Agg")  # headless: save plots to files, never open a window
import matplotlib.pyplot as plt
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(HERE, "sales_data.csv"))
print("shape:", df.shape)
print("\ndtypes:\n", df.dtypes)
print("\nfirst 5 rows:\n", df.head())
print("\nmissing values per column:\n", df.isna().sum())

# --- Cleaning decisions ------------------------------------------------------
# decision: 'revenue' is the target - drop rows where it is missing, because
# a row without its target is useless for prediction.
df = df.dropna(subset=["revenue"])
# decision: fill missing 'units' with the column mean - units correlates with
# revenue, and the mean is the least-biased simple fill.
df["units"] = df["units"].fillna(df["units"].mean())
# decision: coerce 'region' to a categorical type (it has a small fixed set).
df["region"] = df["region"].astype("category")

print("\nafter cleaning, missing values:\n", df.isna().sum().sum())

# --- Plot 1: revenue by region ----------------------------------------------
df.groupby("region", observed=True)["revenue"].sum().plot(kind="bar")
plt.title("Revenue by region")
plt.savefig(os.path.join(HERE, "revenue_by_region.png"))
plt.close()

# --- Plot 2: units vs revenue scatter ---------------------------------------
df.plot.scatter(x="units", y="revenue")
plt.title("Units vs revenue")
plt.savefig(os.path.join(HERE, "units_vs_revenue.png"))
plt.close()

print("\nSaved plots:")
print("  projects/phase-0/milestone-0.3/revenue_by_region.png")
print("  projects/phase-0/milestone-0.3/units_vs_revenue.png")
