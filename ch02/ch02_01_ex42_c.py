# Zill - Differential Equations with Boundary-Value Problems
# Section 2.1: Exercise 42. (c)
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval I = (-infinity, infinity)
t = np.linspace(0, 10)

# functions defined by explicit solution
def X1(t, alpha):
    return alpha - 1/(t + 2/alpha)

def X2(t, alpha):
    return alpha - 1/(t - 1/alpha)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(t, X1(t, 1), 'red', t, X2(t, 1), 'blue')

# add title and label
ax.set_title("Zill - Section 2.1 - Exercise 42. (c)")
ax.set_xlabel("$t$")
ax.set_ylabel("$X$")
ax.legend((r"$X_1(t) = \alpha - \frac{1}{t + \frac{2}{\alpha}}$",
    r"$X_2(t) = \alpha - \frac{1}{t - \frac{1}{\alpha}}$"))
ax.grid()

# plot asymptotes
tlim = ax.get_xlim()
plt.hlines(1, tlim[0], tlim[1], 'gray', 'dashed', label=r"$t = /alpha$")
Xlim = ax.get_ylim()
plt.vlines(1, Xlim[0], Xlim[1], 'gray', 'dashed', label=r"$X = 1$")

# show plot
plt.show()

# save plot
fig.savefig("ch02_01_ex42_c.png")
