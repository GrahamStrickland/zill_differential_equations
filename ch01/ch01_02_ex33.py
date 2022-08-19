import numpy as np
import matplotlib.pyplot as plt

def phi1(x):
    return np.sqrt(3*(x**2 - 1))

def phi2(x):
    return -np.sqrt(3*(x**2 - 1))

x = np.linspace(-10.0, 10.0) # 100 values between -10.0 and 10.0

fig = plt.figure()  # manually create a figure
lines = plt.plot(x, phi1(x), x, phi2(x))  # plot data

plt.show()
