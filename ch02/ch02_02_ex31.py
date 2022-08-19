# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2. - Exercise 31
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = (-inf, inf)
x = np.linspace(-5, 5)

# function defined by explicit solution
def y(x):
    return np.sqrt(x**2 + x + 4)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(x, y(x), label=r"$y = \sqrt{x^2 + x + 4}$")

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 31")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex31.png")
