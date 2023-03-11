#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2: Exercise 43
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = (log(sqrt(3/4)), inf)
x = np.linspace(np.ceil(np.log(np.sqrt(4/3))), 3)

# define functions y_1(x), y_2(x), y_3(x), and y_4(x)
def y_1(x):
    return np.sqrt((-np.exp(2*x)) / ((3/4) - np.exp(2*x)))

def y_2(x):
    return np.sqrt((-np.exp(2*x)) / (-3 - np.exp(2*x)))

def y_3(x):
    return np.sqrt((-np.exp(2*x)) / (3 - np.exp(2*x)))

def y_4(x):
    return np.sqrt((-np.exp(2*x)) / (-(3/4) - np.exp(2*x)))

# plot figure and axes
fig, ax = plt.subplots()
solutions = ax.plot(x, y_1(x), x, y_2(x), y_3(x), x, y_4(x), x)

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 43")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend((r"$y_1(x) = \sqrt{\frac{-e^{2x}}{\frac{3}{4} - e^{2x}}}$",
           r"$y_2(x) = \sqrt{\frac{-e^{2x}}{-3 - e^{2x}}}$",
           r"$y_3(x) = -\sqrt{\frac{-e^{2x}}{3 - e^{2x}}}$",
           r"$y_4(x) = -\sqrt{\frac{-e^{2x}}{-\frac{3}{4} - e^{2x}}}$"))

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex43.pdf")
