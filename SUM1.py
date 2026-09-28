def fk(k):
    r = 1
    for i in range(2, k+1):
        r *= i
    return r


import math
S = 0
for n in range (1,101,1):
    a = (math.cos(0.3*n))
    b = fk(n)
    S += a/b
print(S)