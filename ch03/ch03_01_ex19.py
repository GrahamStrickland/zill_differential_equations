#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems
# Section 3.1: Exercise 19
import sympy

k, t1 = sympy.symbols('k t1')

eq1 = 21 + 16*sympy.exp(k*t1) - 29
k1 = sympy.solve(eq1, k)
print("Equation 1: ")
print(eq1, " = 0 => k = ", k1[0])

eq2 = 21 + 16*sympy.exp(k*(t1+1)) - 27
k2 = sympy.solve(eq2, k)
print("Equation 2: ")
print(eq2, " = 0 => k = ", k2[0])

eq3 = k1[0] - k2[0]

print("Equation 3: ")
print(eq3, " = 0 ", end="")
print(" => ", end="")

answer = sympy.solve(eq3, t1)

if len(answer) > 0:
    print(answer[0])
else:
    print("No solution")
