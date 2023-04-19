from sympy import Symbol, solve
import sympy
import mpmath
mpmath.mp.dps = 3
x = Symbol('x')
i = complex(0,1)
print(-(3-5*i)**10-25*(3*i-9)/(2+8*i))

