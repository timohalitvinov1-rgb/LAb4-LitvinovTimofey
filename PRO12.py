def fk(k):
    r = 1
    for i in range(2, k+1):
        r *= i
    return r


import math
P = 0
for n in range (1,26,1):
    a = fk(n)
    b = (n/2) * fk((n-1))
    c = math.cos(n+1)
    P += (a/b)*c
print(P)