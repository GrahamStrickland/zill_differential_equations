#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2. - Exercise 32
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = (-inf, inf)
x = np.linspace(-2, 2)

# functions defined by explicit solution
def y1(x):
    return x**3 + 2*x**2 + 2*x + 3

def y2(x):
    return x**3 + 2*x**2 + 2*x + 5

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(x, y1(x), 'red', x, y2(x), 'blue')

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 32")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend([r"$y_1(x) = x^3 + 2x^2 + 2x + 3$",
        r"$y_2(x) = x^3 + 2x^2 + 2x + 5$"])

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex32.pdf")
