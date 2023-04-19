from sympy import Symbol, nsolve
import sympy
import mpmath
mpmath.mp.dps = 3
x = Symbol('x')
y = Symbol('y')
i = complex(0, 1)
f1 = (2+i)*x+y*(2-i)-6
f2 = (2-i)*x+(3-2*i)*y-8
print(nsolve((f1, f2), (x, y), (-1, 1)))

