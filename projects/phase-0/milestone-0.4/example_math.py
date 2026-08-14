"""Working example - Milestone 0.4: math as code.

Run:  python3 projects/phase-0/milestone-0.4/example_math.py

Computes a dot product, applies a matrix as a transformation, and numerically
checks a derivative via the central-difference limit - so you can experiment
with the math instead of just reading it.

Modifications to try (from phase-0-setup-python-math.md, M0.4.1 - M0.4.4):
  M0.4.1  numerically check d/dx sigmoid(w*x + b), compare to the analytic form
  M0.4.2  apply a rotation vs a shear matrix to 2D vectors, watch direction change
  M0.4.3  draw bigger normal samples; watch empirical mean/var converge
  M0.4.4  compute a posterior with Bayes (sensitivity/specificity example)
"""

import numpy as np

# --- Dot product -------------------------------------------------------------
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])
print("dot(a, b) =", a @ b, "  (manual:", 1 * 4 + 2 * 5 + 3 * 6, ")")

# --- Matrix as transformation ------------------------------------------------
# Identity-ish matrix times a couple of vectors, so you can see the mapping.
M = np.array([[2.0, 0.0],
              [0.0, 1.0]])   # stretches x by 2
v = np.array([[1.0, 1.0],
              [1.0, -1.0]])  # two test vectors, as rows
print("\nM * v (each row transformed):\n", v @ M.T)

# --- Numerical derivative via central difference -----------------------------
def f(x):
    return x ** 2

h = 1e-6
x0 = 3.0
num_deriv = (f(x0 + h) - f(x0 - h)) / (2 * h)
print(f"\nf(x) = x^2, d/dx at x=3: analytic 6.0, numeric {num_deriv:.6f}")

# --- Empirical convergence of mean/variance (M0.4.3) -------------------------
rng = np.random.default_rng(0)
for n in (100, 10_000, 1_000_000):
    s = rng.normal(loc=0.0, scale=1.0, size=n)
    print(f"n={n:>9}: mean {s.mean():+.4f}  var {s.var():.4f}")
