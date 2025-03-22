import numpy as np

matrix1 = np.random.randint(0, 100,(5,3))
matrix2 = np.random.randint(0, 100,(3,2)) 

print(matrix1@matrix2)