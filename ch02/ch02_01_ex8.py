# Zill - Differential Equations with Boundary-Value Problems
# Section 2.1: Exercise 8
import matplotlib.pyplot as plt
import numpy as np

# create grid of x, y coordinates
X, Y = np.meshgrid(np.arange(-5, 5, 0.5), np.arange(-5, 5, 0.5))

# calculate U = dx/dt and V = dy/dt
U = np.ones_like(X)
V = 1/Y

# normalize vectors U, V to unit length
magnitude = np.sqrt(U**2 + V**2)
U = U/magnitude
V = V/magnitude

# plot figure and axes
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V, color='blue')

# add title and label
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.title("Zill - Section 2.1 -  Exercise 8")

# show plot
plt.show()

# save plot
fig.savefig("ch02_01_ex8.png")
