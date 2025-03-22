import numpy as np

identity_matrix = np.eye(3, 3, dtype=int)
print(identity_matrix)

#solution 2
identity_matrix2 = np.identity(3, dtype = int)
print(identity_matrix2)