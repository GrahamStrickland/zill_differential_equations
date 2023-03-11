#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2. - Exercise 34
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = (-pi/3, pi/3)
x = np.linspace(-np.pi/3, np.pi/3)

# function defined by explicit solution
def y(x):
    return np.sqrt(2*np.cos(x) - 1)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(x, y(x), label=r"$y = \sqrt{2\cos x - 1}$")

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 34")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex34.pdf")
