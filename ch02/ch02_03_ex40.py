#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.3. - Exercise 40
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
x = np.linspace(0, 4)

# continuous function of solution y(x)
funcs = []
funcs.append(lambda x: x**2 / 2*(1 + x**2))
funcs.append(lambda x: (x**2 / 2*(1 + x**2) + (1 / (1 + x**2))))

def y(x):
    return np.piecewise(x, [x < 1, x >= 1], funcs)

# plot figure and axes
fig, ax = plt.subplots()
eq = r'$y=\left\{\begin{array}{lr} \frac{x^{2}}{2(1 + x^{2})} & 0 \leq x < 1 \\ \frac{x^{2}}{2(1 + x^{2})} + \frac{1}{1 + x^{2}} & x \geq 1 \end{array} \right\}$'
solution = ax.plot(x, y(x), label=eq)

# add title and label
ax.set_title("Zill - Section 2.3. - Exercise 40")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_03_ex40.pdf")
