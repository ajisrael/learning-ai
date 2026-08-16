"""Working example - Milestone 0.2: NumPy and vectorized thinking.

Run:  python3 projects/phase-0/milestone-0.2/example_numpy.py

Builds a small array, does element-wise ops, a broadcasted row/column op, and a
matrix multiply - printing every result so you can see what vectorization does.

Modifications to try (from phase-0-setup-python-math.md, M0.2.1 - M0.2.4):
  [x]  M0.2.1  rewrite arr.sum(axis=1) as an explicit Python loop, compare results
  [x]  M0.2.2  make a broadcast fail on purpose and read the error message
  [x]  M0.2.3  verify one matrix-multiply cell against a manual dot product
  [x]  M0.2.4  extend into a tiny linear model: predictions + MSE loss, vectorized
"""

import numpy as np

# -----------------------------------------------------------------------------
# M0.2.1: Rewrite arr.sum(axis=1) as an explicit Python loop, compare.
#   Your loop goes here. Mark [x] when it's done, and make sure its output
#   matches the vectorized arr.sum(axis=1) printed below.
# -----------------------------------------------------------------------------

def sum_matrix(matrix):
    sums = []
    for row in matrix:
        current_sum = 0
        for elem in row:
            current_sum += elem
        sums.append(float(current_sum))
    return sums


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
print("row sums [loop](axis=1):", sum_matrix(arr))

print("col means (axis=0):", arr.mean(axis=0))

# -----------------------------------------------------------------------------
# M0.2.2: Make a broadcast fail on purpose and read the error message.
#   Temporary experiment: break a shape, read the ValueError, then restore.
#   The code below is back to the working state.
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# M0.2.3: Verify one matrix-multiply cell against a manual dot product.
#   Your manual check goes here and must equal the matching A @ B cell.
# -----------------------------------------------------------------------------

# Manual dot product of a cell for M0.2.3
def dot_prod_cell(cell_A, cell_B):
    if len(cell_A) != len(cell_B):
        return "cannot compute"

    product = 0

    for i in range(len(cell_A)):
        product += cell_A[i] * cell_B[i]

    return product

print("manual A[0][k] @ B[k][0]: ", dot_prod_cell(A[0], [row[0] for row in B]))
manual = sum(A[1][k] * B[k][0] for k in range(B.shape[0]))
print("manual A[1][k] @ B[k][0]: ", manual)

# Broadcasting trick: (3,1) * (1,4) -> outer product, no loops.
col = np.array([[1.0], [2.0], [3.0]])
print("\nouter product col * row =\n", col * row)

# -----------------------------------------------------------------------------
# M0.2.4: Extend into a tiny linear model: predictions + MSE loss, vectorized.
#   Data is provided below. Write it VECTORIZED (no loop over samples).
#
#   Hint:
#   - predictions are the dot product of input data (X) and the weights of
#     the network (w)
#   - MSE = the mean of the squared differences between predictions and the
#     real answers (y)
#
#   Print both.
# -----------------------------------------------------------------------------

w = np.array([0.5, -1.0])                           # one weight per feature
X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])  # 3 samples, 2 features
y = np.array([2.0, 5.0, 8.0])                       # the real answers

preds = X @ w
mse   = np.mean((preds - y) ** 2)

print("\nPredictions: ", preds)
print("MSE: ", mse)
