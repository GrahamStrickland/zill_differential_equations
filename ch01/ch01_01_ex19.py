# Zill - Differential Equations with Boundary-Value Problems
# Section 1.1: Exercise 19
import numpy as np
import matplotlib.pyplot as plt

# sample of interval I = (ln(2), infinity)
t = np.linspace(1, 5)

# function defined by explicit solution
def X(t):
    return (1 - np.exp(t)) / (2 - np.exp(t))

# explicit solution
phi = X(t)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(t, phi, label=r"$X = \phi(t) = \frac{1 - e^{t}}{2 - e^{t}}$")

# add title and label
ax.set_title("Zill - Section 1.1 - Exercise 19")
ax.set_xlabel("$t$", usetex=True)
ax.set_ylabel("$X$", usetex=True)
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch01_01_ex19.png")
