"""Working example - Milestone 0.2: NumPy and vectorized thinking.

Run:  python3 projects/phase-0/milestone-0.2/example_numpy.py

Builds a small array, does element-wise ops, a broadcasted row/column op, and a
matrix multiply - printing every result so you can see what vectorization does.

Modifications to try (from phase-0-setup-python-math.md, M0.2.1 - M0.2.4):
  M0.2.1  rewrite arr.sum(axis=1) as an explicit Python loop, compare results
  M0.2.2  make a broadcast fail on purpose and read the error message
  M0.2.3  verify one matrix-multiply cell against a manual dot product
  M0.2.4  extend into a tiny linear model: predictions + MSE loss, vectorized
"""

import numpy as np

# A 3x4 matrix.
arr = np.array([[1.0, 2.0, 3.0, 4.0],
                [5.0, 6.0, 7.0, 8.0],
                [9.0, 10.0, 11.0, 12.0]])
print("arr =\n", arr)

# Element-wise ops.
print("\narr * 2 =\n", arr * 2)
print("\narr ** 2 (element-wise) =\n", arr ** 2)

# Vectorized reductions along an axis.
print("\nrow sums (axis=1):", arr.sum(axis=1))
print("col means (axis=0):", arr.mean(axis=0))

# Broadcasting: (3,4) + (1,4) stretches the row across all three rows.
row = np.array([10.0, 20.0, 30.0, 40.0])
print("\narr + row (broadcast) =\n", arr + row)

# Matrix multiply: (2,3) @ (3,2) -> (2,2).
A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
B = np.array([[1.0, 0.0],
              [0.0, 1.0],
              [1.0, 1.0]])
print("\nA =\n", A)
print("B =\n", B)
print("A @ B =\n", A @ B)

# Broadcasting trick: (3,1) * (1,4) -> outer product, no loops.
col = np.array([[1.0], [2.0], [3.0]])
print("\nouter product col * row =\n", col * row)
