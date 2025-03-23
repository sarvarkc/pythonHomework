import numpy as np

temeratures = np.array([32, 68, 100, 212, 77])

@np.vectorize
def convert(x):
    res = round((x-32)*5/9,1)
    return res

print(convert(temeratures))