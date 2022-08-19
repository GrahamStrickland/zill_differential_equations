# Zill - Differential Equations with Boundary-Value Problems
# Section 3.1 - Exercise 28 (e)
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
t = np.linspace(0, 500)

# continuous function of solution A(t)
funcs = []
funcs.append(lambda t: 250 + 0.25*t - 2.25*10**14*(1000 + t)**-9)
funcs.append(lambda t: 3250/9 - 4.525*np.exp(-9*t/1300))

def A(t):
    return np.piecewise(t, [t < 300, t >= 300], funcs)

# plot figure and axes
fig, ax = plt.subplots()
eq = r'$A(t)=\left\{\begin{array}{lr} 250 + 0.25t - (2.25 \times 10^{14})(1000 + t)^{-9} & t \in [0,300) \\ \frac{3250}{9} - 4.525e^{-\frac{9t}{1300}} & t \in [300,500)\end{array} \right\}$'
solution = ax.plot(t, A(t), label=eq)

# add title and label
ax.set_title("Zill - Section 3.1 - Exercise 28 (e)")
ax.set_xlabel("$t$")
ax.set_ylabel("$A(t)$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch03_01_ex28_e.pdf")
