#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 2.1: Exercise 17
import matplotlib.pyplot as plt
import numpy as np

# create grid of x, y coordinates
X, Y = np.meshgrid(np.arange(-5, 5, 0.5), np.arange(-5, 12.5, 1))

# calculate U = dx/dt and V = dy/dt
U = np.ones_like(X)
V = X**2 - 2*Y

# normalize vectors U, V to unit length
magnitude = np.sqrt(U**2 + V**2)
U = U/magnitude
V = V/magnitude

# define function to superimpose on direction field
x = np.arange(-5, 5, 0.5)
def f(x):
    return 0.5*x**2
y = f(x)

# plot figure and axes
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V, color='blue')
f = ax.plot(x, y, color='red', label=r"$y = \frac{1}{2} x^{2}$")

# add title and label
plt.xlabel(r"$x$", usetex=True)
plt.ylabel(r"$y$", usetex=True)
plt.title("Zill - Section 2.1 -  Exercise 17")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_01_ex17.pdf")
