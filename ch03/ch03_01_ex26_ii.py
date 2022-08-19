# Zill - Differential Equations with Boundary-Value Problems
# Section 3.1: Exercise 26 - Part II
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

# sample of interval t in I = (0, inf) where t = time
t = np.linspace(0, 600)

# define function A(t) where A = amount of salt in kg in tank
def A(t):
    return 250 + (1250/313)*(np.sin(t/4)/25 - np.cos(t/4)) - (57925/313)*np.exp(-t/100)

# plot figure and axes
fig, ax = plt.subplots()
solution = ax.plot(t, A(t), 
        label=r"$A(t) = 250 + \frac{1250}{313}\bigl(\frac{\sin(\frac{t}{4})}{25} - \cos(\frac{t}{4})\bigr) - \frac{57925}{313}e^{-\frac{t}{100}}$")

# add title and label
ax.set_title("Zill - Section 3.1 - Exercise 26 - Part II")
ax.set_xlabel("$t$")
ax.set_ylabel("$A(t)$")
ax.legend()

# show plot
plt.show()

# save plot
fig.savefig("ch03_01_26_ii.pdf")
