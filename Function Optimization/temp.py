import numpy as np
import random

T = 1000
n = 100
x = 0
e = 0

while T:
    for i in range(n):
        delx = random.uniform(-10, 10)
        e2 = np.sin(x+delx)

        de = e2 - e

        if de > 0:
            x = x + delx
            e = e2
        elif np.exp(-de/T) <= 1:
            x = x + delx
            e = e2
    T -= 1

print(np.sin(x))

"""
There are two cases where we expect that SA will lead to suboptimal solution:
1. When abs(de) is small and de < 0: In this case since abs(de) is small, even
if there are 10 jumps away from optimal, the difference btw the optimal and current solution is 
small. 100 jumps are unlikely as the product of 100 probabilities is expected to be small.
2. When abs(de) is large and de < 0: In this case even one jump is enough to go away from optimal
solution. But in this case the expression (np.exp(-de/de)<=1) is more likely to be false.

Both cases are more unlikely than a jump towards optimal solution. So SA is likely to work than not
"""
