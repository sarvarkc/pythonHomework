import numpy as np

matrix1 = np.random.randint(0, 100,(3,3))
matrix2 = np.random.randint(0, 100,(3,3)) 

print(np.dot(matrix1,matrix2))