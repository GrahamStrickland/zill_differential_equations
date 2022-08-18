#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems - 10e
# Section 7.4 - Question 15


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams


# Set parameters for latex encoding/packages.
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


# Set domain of solution.
t = np.linspace(0, 2*np.pi)


# Define piecewise solution function.
funcs = []
funcs.append(lambda t: (1.0/4.0)*np.sin(4.0*t) + (1.0/8.0)*t*np.sin(4.0*t))
funcs.append(lambda t: (1.0/8.0)*np.sin(4.0*t) + (1.0/8.0)*t*np.sin(4.0*t))

def y(t):
    return np.piecewise(t, [t < np.pi, t >= np.pi], funcs)


# Plot figure and axes.
fig, ax = plt.subplots()
eq = r"""
\[
    y(t) = 
    \left \{
    \begin{array}{lr} 
        \frac{1}{4} \sin{4t} + \frac{1}{8}t \sin{4t} & 0 \leq t < \pi \\ 
        \frac{1}{8} \sin{4t} + \frac{1}{8}t \sin{4t} & t \geq \pi
    \end{array}
    \right \}
\]
"""
solution = ax.plot(t, y(t), label=eq)


# Add title and label.
ax.set_title("Zill - Section 7.4 - Exercise 15")
ax.set_xlabel("$t$")
ax.set_ylabel("$y$")
ax.legend()


# Show plot and save figure.
plt.show()
fig.savefig("ch07_4ex15.png")
