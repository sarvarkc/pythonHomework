import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000)
y = x**2 - 4*x + 4

plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 4$", color='b', linestyle='-')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plot of $f(x) = x^2 - 4x + 4$")

plt.grid(True)
plt.legend()

plt.show()
