import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

plt.subplot(2, 2, 1)
y1 = x**3
plt.plot(x,y1, label=r"$f(x) = x^3$", color='b', linestyle=':', marker='o', markevery=100, linewidth=2)
plt.title("Cubic Function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
y2 = np.sin(x)
plt.plot(x,y2, label=r"$f(x) = sin(x)$", color='g', linestyle='-', marker='o', markevery=100, linewidth=2)
plt.title("Sine Function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
y3 = np.exp(x)
plt.plot(x,y3, label=r"$f(x) = e^x$", color='r', linestyle='--', marker='o', markevery=100, linewidth=2)
plt.title("Exponential Function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
y4 = np.where(x>=0, np.log(x+1), np.nan)
plt.plot(x,y4, label=r"$f(x) = log(x+1)$", color='k', linestyle='-.', marker='o', markevery=100, linewidth=2)
plt.title("Logarithmic Function")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.show()