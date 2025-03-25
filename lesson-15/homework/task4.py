import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

a = np.random.uniform(0,10,100)
b = np.random.uniform(0, 10, 100)
markers = ["o", "*", ".", ",", "x", "X", "+", "p", "s", "D", "d", "p", "H", "h", "v", "^", "<", ">", "1", "2", "3", "4", "|", "_"]
colors = ["r", "b", "g", "c", "m", "y", "k", "w"]

for x in range(len(a)):
    plt.scatter(a[x],b[x], c=np.random.choice(colors), marker=np.random.choice(markers), s=50)

plt.title("Dots")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)

plt.show()