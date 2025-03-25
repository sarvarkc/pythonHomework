import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, alpha=0.7, color="blue", edgecolor="black")

plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.6)
print(data)
plt.show()
