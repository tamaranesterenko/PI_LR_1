from sympy import Symbol, solve
import sympy
import mpmath
mpmath.mp.dps = 3
x = Symbol('x')
i = complex(0,1)
print(solve(x**2-3+4*i))

