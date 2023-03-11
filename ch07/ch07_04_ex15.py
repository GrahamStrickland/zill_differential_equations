#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems - 10e
# Section 7.4 - Question 15
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams


# Set parameters for latex encoding/packages.
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r"""
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{mathrsfs}
\newsavebox\foobox
\newlength{\foodim}
\newcommand{\slantbox}[2][0]{\mbox{%
        \sbox{\foobox}{#2}%
        \foodim=#1\wd\foobox
        \hskip \wd\foobox
        \hskip -0.5\foodim
        \llap{\usebox{\foobox}}%
        \hskip 0.5\foodim
}}
\def\Heaviside{\slantbox[-.45]{$\mathscr{U}$}}
"""


# Set domain of solution.
t = np.linspace(start=0, stop=2*np.pi, num=500)


# Define piecewise solution function.
funcs = []
funcs.append(lambda t: (1.0/4.0)*np.sin(4.0*t) + (1.0/8.0)*t*np.sin(4.0*t))
funcs.append(
    lambda t: (1.0/4.0)*np.sin(4.0*t) + (1.0/8.0)*t*np.sin(4.0*t) 
    - (1.0/8.0)*(t-np.pi)*np.sin(4.0*(t-np.pi))
    )

def y(t):
    return np.piecewise(t, [t < np.pi, t >= np.pi], funcs)


# Plot figure and axes.
fig, ax = plt.subplots()
eq = r"$y(t) = \frac{1}{4}\sin{4t} + \frac{1}{8}t\sin{4t} - \frac{1}{8}(t - \pi)\sin{4(t - \pi)} \Heaviside (t - \pi)$"
solution = ax.plot(t, y(t), label=eq)


# Add title and label.
ax.set_title("Zill - Section 7.4 - Exercise 15")
ax.set_xlabel("$t$")
ax.set_ylabel("$y$")
ax.legend(loc='upper left')


# Show plot and save figure.
plt.show()
fig.savefig("ch07_04_ex15.pdf")
