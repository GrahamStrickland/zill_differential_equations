# Zill - Differential Equations with Boundary-Value Problems
# Section 3.1 - Exercise 34
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
t = np.linspace(0, 20)

# continuous function of solution A(t)
funcs = []
funcs.append(lambda t: 80 - 80*(1-0.1*t)**2)
funcs.append(lambda t: 20)

def i(t):
    return np.piecewise(t, [t <= 10, t > 10], funcs)

# plot figure and axes
fig, ax = plt.subplots()
eq = r'$i(t)=\left\{\begin{array}{lr} 80 - 80(1-0.1t)^{2} & 0 \leq t \leq 10 \\ 20 & t > 10\end{array} \right\}$'
solution = ax.plot(t, i(t), label=eq)

# add title and label
ax.set_title("Zill - Section 3.1 - Exercise 34")
ax.set_xlabel("$t$")
ax.set_ylabel("$i(t)$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch03_01_ex34.pdf")
