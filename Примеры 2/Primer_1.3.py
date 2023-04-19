import math
import cmath
z = -3+3*math.sqrt(3)*1j
fi = round(math.degrees(cmath.phase(z)))
print(fi)
r = abs(z)
print(r)
