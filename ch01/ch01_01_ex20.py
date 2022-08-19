# Zill - Differential Equations with Boundary-Value Problems
# Section 1.1: Exercise 20
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = ()
x = np.linspace(-4, 4)

# function defined by explicit solution
def f1(x):
    return x**2 - np.sqrt(x**4 + 1)

def f2(x):
    return x**2 + np.sqrt(x**4 + 1)

# explicit solution
y1 = f1(x)
y2 = f2(x)

# plot figure and axes
fig, ax = plt.subplots()
solutions = ax.plot(x, y1, x, y2)

# add title and label
ax.set_title("Zill - Section 1.1 - Exercise 20")
ax.set_xlabel("$x$", usetex=True)
ax.set_ylabel("$y$", usetex=True)
ax.legend((r"$y = \phi(x) = x^{2} - \sqrt{x^{4} + 1}$",
    r"$y = \phi(x) = x^{2} + \sqrt{x^{4} + 1}$"))

# show plot
plt.show()

# save plot
fig.savefig("ch01_ex20.png")
