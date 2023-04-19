import math
import cmath
z = complex(6,6)
print(round(math.degrees(cmath.phase(z))))
r = abs(z)
print(r)
c = r*(math.cos(-45)+1j*math.sin(-45))
print(c)
