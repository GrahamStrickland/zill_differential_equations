#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 1.1: Exercise 59.a
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)

x = np.linspace(-2.0, 2.0) # 100 values between -2.0 and 2.0

y = f(x) # evaluate f on the x points

fig = plt.figure()  # manually create a figure
lines = plt.plot(x, y)  # plot data

plt.show()

fig.savefig("ch01_01_ex59_a.pdf")
