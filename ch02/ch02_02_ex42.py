# Zill - Differential Equations with Boundary-Value Problems
# Section 2.2. - Exercise 42
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# plot over interval (0,1)
x = np.linspace(0, 1)

# function defined by explicit solution
def y(x):
    return 1 + (1/10)*np.tanh(-x/10)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(x, y(x), label=r"$y = 1 + \frac{1}{10}\tanh(-\frac{x}{10})$")

# add title and label
ax.set_title("Zill - Section 2.2. - Exercise 42")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch02_02_ex42.png")
