#!/usr/bin/env python3
# Zill - Differential Equations with Boundary-Value Problems - 10e
# Section 4.3 - Question 25
from sympy import Symbol, div


m = Symbol('m')


# Auxilliary equation
f = 16*m**4 + 24*m*82 + 9


# p/q
potential_rational_roots = [1, -1, 3, -3, 9, -9, 1/2, -1/2, 3/2, -3/2,
                            9/2, -9/2, 1/4, -1/4, 3/4, -3/4, 9/4, -9/4,
                            1/8, -1/8, 3/8, -3/8, 9/8, -9/8, 1/16, -1/16,
                            3/16, -3/16, 9/16, -9/16]


# Print result of division 
for i in range(len(potential_rational_roots)):
    g = m - potential_rational_roots[i]
    q, r = div(f, g, domain='QQ')
    print("for root {}, q = {}, r = {}".format(potential_rational_roots[i], q, r))
