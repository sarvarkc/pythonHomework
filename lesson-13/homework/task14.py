import numpy as np

matrix = np.random.randint(0, 100,(3,3))
vector = np.random.randint(0, 100,(3,1)) 

print(np.linalg.solve(matrix,vector))