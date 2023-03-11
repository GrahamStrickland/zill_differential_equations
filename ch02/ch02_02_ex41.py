#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2. - Exercise 41
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# plot over interval (0,1)
x = np.linspace(0, 1)

# function defined by explicit solution
def y(x):
    return 1 + (1/10)*np.tan(x/10)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(x, y(x), label=r"$y = 1 + \frac{1}{10}\tan(\frac{x}{10})$")

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 41")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex41.pdf")
