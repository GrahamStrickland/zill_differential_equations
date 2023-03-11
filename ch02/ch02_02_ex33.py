#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2. - Exercise 33
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = (-inf, ln(2))
x = np.linspace(-10, np.floor(np.log(2)))

# function defined by explicit solution
def y(x):
    return -np.log(2 - np.exp(x))

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(x, y(x), label=r"$y = -\ln(2 - e^{x})$")

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 33")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex33.pdf")
