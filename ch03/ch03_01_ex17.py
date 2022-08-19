# Zill - Differential Equations with Boundary-Value Problems
# Section 3.1: Exercise 17
import sympy

k, T_m = sympy.symbols('k T_m')

eq1 = T_m + (21 - T_m)*sympy.exp(0.5*k) - 43
k1 = sympy.solve(eq1, k)
print("Equation 1: ")
print(eq1, " = 0 => k = ", k1[0])

eq2 = T_m + (21 - T_m)*sympy.exp(k) - 63
k2 = sympy.solve(eq2, k)
print("Equation 2: ")
print(eq2, " = 0 => k = ", k2[0])

eq3 = ((T_m - 43)/(T_m - 21))**2 - (T_m - 63)/(T_m - 21)

print("Equation 3: ")
print(eq3, " = 0 ", end="")
print(" => ", end="")

answer = sympy.solve(eq3, T_m)

if len(answer) > 0:
    print(answer[0])
else:
    print("No solution")
