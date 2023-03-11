#!/usr/bin/env python3
# Zill - Chapter 1 Section 1 - Exercise 63
# Verifying solutions to a differential equation using SymPy
import sympy

# Define x as symbol
x = sympy.symbols('x')

# Define solution y
y = x*sympy.exp(5*x) * sympy.cos(2*x)
print("Verification that y = ", end="")
print(y)
print("is a solution of the differential equation: ")
print("y^4 - 20y^3 + 158y\'\' - 580y\' + 841y = 0")

# Differentiate y and simplify until y^4
y1 = sympy.simplify(sympy.diff(y))
print("y\' = ", end="")
print(y1)

y2 = sympy.simplify(sympy.diff(y1))
print("y\'\' = ", end="")
print(y2)

y3 = sympy.simplify(sympy.diff(y2))
print("y^3 = ", end="")
print(y3)

y4 = sympy.simplify(sympy.diff(y3))
print("y^4 = ", end="")
print(y4)

# Verify that y is a solution of the DE
print("y^4 - 20y^3 + 158y\'\' - 580y\' + 841y = ", end="")
print(sympy.simplify(y4 - 20*y3 + 158*y2 - 580*y1 + 841*y))
