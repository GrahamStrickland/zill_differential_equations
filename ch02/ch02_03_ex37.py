#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.3. - Exercise 37
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# set parameters for latex encoding/packages
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r"""
\usepackage{amsthm}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{mathtools}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
"""

# sample of interval [0,inf)
x = np.linspace(0, 6)

# continuous function of solution y(x)
funcs = []
funcs.append(lambda x: 0.5 * (1 - np.exp(-2 * x)))
funcs.append(lambda x: ((np.exp(6 - 2*x) / 2) * (1 - np.exp(-6))))

def y(x):
    return np.piecewise(x, [x <= 3, x > 3], funcs)

# plot figure and axes
fig, ax = plt.subplots()
eq = r'$y=\left\{\begin{array}{lr} \frac{1}{2}(1 - e^{-2x}) & 0 \leq x \leq 3 \\ \frac{e^{6-2x}}{2}(1 - e^{-6}) & x > 3 \end{array} \right\}$'
solution = ax.plot(x, y(x), label=eq)

# add title and label
ax.set_title("Zill - Section 2.3. - Exercise 37")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(loc='upper right')

# show plot
plt.show()

# save plot
fig.savefig("ch02_03_ex37.pdf")
