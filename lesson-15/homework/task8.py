import numpy as np
import matplotlib.pyplot as plt

time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [5, 7, 6, 8]
category_B = [3, 5, 2, 6]
category_C = [4, 6, 5, 7]

plt.bar(time_periods, category_A, label='Category A', color='red')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='blue')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='green')

plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart of Categories Over Time")
plt.legend()

plt.show()
