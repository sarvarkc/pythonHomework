import numpy as np

matrix1 = np.random.randint(0, 100,(3,4))
matrix2 = np.random.randint(0, 100,(4,3)) 

print(matrix1@matrix2)