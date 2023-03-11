#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2. - Exercise 39
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# plot over interval (0,1)
x = np.linspace(0.01, 1)

# function defined by explicit solution
def y(x):
    return 1 - 1/x

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(x, y(x), label=r"$y = 1 - \frac{1}{x}$")

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 39")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex39.pdf")
