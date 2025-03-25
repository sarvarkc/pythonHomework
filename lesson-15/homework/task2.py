import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label=r"$sin(x)$", color='b', linestyle=':', marker='o', markevery=100, linewidth=2)
plt.plot(x, y2, label=r"$cos(x)$", color='g', linestyle='--', marker='s', markevery=100, linewidth=2)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plot of $sin(x)$ and $cos(x)$")

plt.grid(True)
plt.legend()

plt.show()