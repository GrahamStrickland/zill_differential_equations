# Zill - Differential Equations with Boundary-Value Problems 9e
# Section 2.4 - Exercise 39. (c)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['text.usetex'] = True

# Determine sample of interval of definition I = (-inf, 3).
x = np.linspace(-5, 3)

# Define functions for explicit solutions y_1(x) and y_2(x).
def y_1(x):
    return -x**2/2 + np.sqrt(x**4 - x**3 + 4)

def y_2(x):
    return -x**2/2 - np.sqrt(x**4 - x**3 + 4)

# Plot functions on iterval.
fig, ax = plt.subplots()
solutions = ax.plot(x, y_1(x), 'r', x, y_2(x), 'b')

# Add title, labels, and gridlines.
plt.title("Zill - Section 2.4 - Exercise 39. (c)")
plt.xlabel("$x$")
plt.ylabel("$y$")
ax.legend([r"$y_1(x) = -\frac{x^{2}}{2} + \sqrt{x^{4} - x^{3} + 4}$",
    r"$y_2(x) =  -\frac{x^{2}}{2} - \sqrt{x^{4} - x^{3} + 4}$"])

# Show plot and save image
plt.show()
fig.savefig("ch02_04_ex39_c.pdf")
