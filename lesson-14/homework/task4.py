import numpy as np

A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

B = np.array([12, -5, 15])

res = np.linalg.solve(A, B)

rounded_res = np.round(res, 4)

print(rounded_res)