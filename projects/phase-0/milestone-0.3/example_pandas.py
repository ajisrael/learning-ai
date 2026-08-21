"""Working example - Milestone 0.3: pandas cleaning and plotting.

Run:  python3 projects/phase-0/milestone-0.3/example_pandas.py

Loads a small CSV (bundled here as sales_data.csv), inspects shape/types, finds
missing values, cleans them, and produces two plots saved to files. The plot
code is kept as a plain script so you can refactor it into a function (M0.3.4).

Modifications to try (from phase-0-setup-python-math.md, M0.3.1 - M0.3.4):
  [x]  M0.3.1  write a one-line justification next to each cleaning decision
  [x]  M0.3.2  derive a new column from existing ones
  [x]  M0.3.3  add a groupby and a merge on a key
  [x]  M0.3.4  refactor the plotting into a reusable function
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

# -----------------------------------------------------------------------------
# M0.3.1: Write a one-line justification next to each cleaning decision.
#   Each decision below already carries one as a model - keep the habit: every
#   decision you make gets a reason (why drop, why fill, why that value).
# -----------------------------------------------------------------------------

# decision: 'revenue' is the target - drop rows where it is missing, because
# a row without its target is useless for prediction.
df = df.dropna(subset=["revenue"])
# decision: fill missing 'units' with the column mean - units correlates with
# revenue, and the mean is the least-biased simple fill.
df["units"] = df["units"].fillna(df["units"].mean())
# decision: coerce 'category' to a categorical type (it has a small fixed set).
df["category"] = df["category"].astype("category")

print("\nafter cleaning, missing values:\n", df.isna().sum().sum())

# -----------------------------------------------------------------------------
# M0.3.2: Derive a new column from existing ones.
#   Hint: a ratio of two numeric columns, a category bucketing, or a datetime
#   parse are all fair game. Include it in the plots below.
df["revenue_per_unit"] = df["revenue"].divide(df["units"])
print("\nNew first 5 rows after adding revenue per unit:\n", df.head())
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# M0.3.3: Add a groupby and a merge on a key.
#   Hint: group by a categorical column and take the mean of a numeric one and
#   print it; then build a second tiny dataset and merge on a shared key.

# step 1: groupby + aggregate - bucket rows by region, average units per
# bucket. Result is a Series whose INDEX holds the region names, which is why
# assigning it straight to a column gave all-NaN (no "North" row label exists).
region_means = df.groupby("category", observed=True)["units"].mean()
print("\navg units per region (Series):\n", region_means)

# step 2: reset_index() promotes the region index back into a real column so
# it can act as a merge key; rename() gives the mean a distinct name so it
# cannot collide with the existing 'units' column during the merge.
region_stats = region_means.reset_index().rename(
    columns={"units": "avg_units_per_region"}
)
print("\nregion stats table:\n", region_stats)

# step 3: merge - for every salesperson row, look up its region in
# region_stats and attach that region's average as a new column.
df = df.merge(region_stats, on="category")
print("\nfirst 5 rows after merge:\n", df.head())
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# M0.3.4: Refactor the plotting into a reusable function.
#   Turn the plot code below into a function that takes a DataFrame and plot
#   settings, so it can be re-run on new data without edits. The two plots
#   below should end up calling it.
def save_plot(data, title, filename, **plot_kwargs):
    data.plot(**plot_kwargs)
    plt.title(title)
    plt.savefig(os.path.join(HERE, filename))
    plt.close()
# -----------------------------------------------------------------------------

# --- Plot 1: revenue by region ----------------------------------------------
save_plot(df.groupby("category", observed=True)["revenue"].sum(), "Revenue by category", "revenue_by_region.png", kind="bar")

# --- Plot 2: units vs revenue scatter ---------------------------------------
save_plot(df, "Units vs revenue", "units_vs_revenue.png", kind="scatter", x="units", y="revenue")

# --- Plot 3: revenue per unit by region ----------------------------------------------
save_plot(df.groupby("category", observed=True)["revenue_per_unit"].sum(), "Revenue Per Unit by category", "revenue_per_unit_by_region.png", kind="bar")

print("\nSaved plots:")
print("  projects/phase-0/milestone-0.3/revenue_by_category.png")
print("  projects/phase-0/milestone-0.3/units_vs_revenue.png")
print("  projects/phase-0/milestone-0.3/revenue_per_unit_by_region.png")
