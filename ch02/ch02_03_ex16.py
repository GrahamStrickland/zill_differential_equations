#!/usr/bin/env python3
import sympy

y = sympy.Symbol('y')

LHS = sympy.exp(y) / y**2 

print(sympy.simplify(sympy.integrate(LHS)))
