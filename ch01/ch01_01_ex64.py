#!/usr/bin/env python3
# Zill - Chapter 1 Section 1 - Exercise 64

# Verifying solutions to a differential equation using SymPy
import sympy

# Define x as symbol
x = sympy.symbols('x')

# Define solution y
y = 20*((sympy.cos(5*sympy.log(x))) / x) - 3*((sympy.sin(5*sympy.log(x))) / x)
print("Verification that y = ", end="")
print(y)
print("is a solution of the differential equation: ")
print("x^3y\'\'\' + 2x^2y\'\' + 20xy\' - 78y = 0")

# Differentiate y and simplify until y^3
y1 = sympy.simplify(sympy.diff(y))
print("y\' = ", end="")
print(y1)

y2 = sympy.simplify(sympy.diff(y1))
print("y\'\' = ", end="")
print(y2)

y3 = sympy.simplify(sympy.diff(y2))
print("y^3 = ", end="")
print(y3)

# Verify that y is a solution of the DE
print("x^3y\'\'\' + 2x^2y\'\' + 20xy\' - 78y = ", end="")
print(sympy.simplify(x**3*y3 + 2*x**2*y2 + 20*x*y1 - 78*y))
