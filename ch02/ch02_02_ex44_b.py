#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2: Exercise 44. (b)
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = (-1/2, inf)
x = np.linspace(-1/2, 3)

# define functions y_1(x) and y_3(x)
def y_1(x):
    return 3 + np.sqrt(2*x + 1)

def y_3(x):
    return 3 + np.sqrt(2*x - 1)

# plot figure and axes
fig, ax = plt.subplots()
solutions = ax.plot(x, y_1(x), y_3(x), x)

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 44. (b)")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend((r"$y_1(x) = y_2(x) = 3 + \sqrt{2x + 1}$",
           r"$y_3(x) = y_4(x) = 3 + \sqrt{2x - 1}$"))

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex44_b.pdf")
