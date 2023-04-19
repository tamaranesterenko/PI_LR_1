from sympy import Symbol, solve
import sympy
import cmath
import math
import mpmath
from math import sqrt
mpmath.mp.dps = 3
z = complex(2, 2*sqrt(3))
cmath.phase(z)
print(round(math.degrees(cmath.phase(z))))
print(abs(z))

