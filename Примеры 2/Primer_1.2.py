import math
import cmath
z = 2+2*math.sqrt(3)*1j
fi = round(math.degrees(cmath.phase(z)))
print(fi)
r = abs(z)
print(r)
