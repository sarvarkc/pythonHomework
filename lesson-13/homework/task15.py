import numpy as np

A = np.random.randint(1, 100, (5, 5))

row_sums = np.sum(A, axis=1)

col_sums = np.sum(A, axis=0)

print("Matrix A (5x5):\n", A)
print("\nRow-wise Sums:\n", row_sums)
print("\nColumn-wise Sums:\n", col_sums)