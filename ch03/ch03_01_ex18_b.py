#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 3.1: Exercise 18 (b)
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval t in I = (0, inf) where t = time
t = np.linspace(0.0, 60.0)

# define function T(t) where T = temperature
def T(t):
    return 38.0 - 2.2*t*np.exp(-0.1*t) - 11.0*np.exp(-0.1*t)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(t, T(t), label=r"$T(t) = 38 - 2.2te^{-0.1t} - 11e^{-0.1t}$")

# add title and label
ax.set_title("Zill - Section 3.1 - Exercise 18 (b)")
ax.set_xlabel("$t$")
ax.set_ylabel("$T$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch03_01_ex18_b.pdf")
