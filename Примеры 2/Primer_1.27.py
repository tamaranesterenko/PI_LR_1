import math
import cmath
z = complex(-4, 0)
print(round(math.degrees(cmath.phase(z))))
r = abs(z)
print(r)
c = r*(math.cos(180)+1j*math.sin(180))
print(c)
