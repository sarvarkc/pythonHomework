import numpy as np

matrix = np.random.randint(0, 999,(5,5))  


matrix_min = matrix.min()
matrix_max = matrix.max()
normalized_matrix = (matrix - matrix_min) / (matrix_max - matrix_min)

print("Original Matrix:\n", matrix)
print("\nNormalized Matrix:\n", normalized_matrix)
