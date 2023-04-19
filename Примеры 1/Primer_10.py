from sympy import Symbol, solve
import sympy
import mpmath
mpmath.mp.dps = 3
x = Symbol('x')
i = complex(0,1)
print(solve((2+i)*x**2-(5-i)*x+2-2*i))

