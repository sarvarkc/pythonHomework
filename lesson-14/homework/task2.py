import numpy as np

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

@np.vectorize
def power(base, exponent):
    return base ** exponent

result = power(bases, exponents)

print(result)
