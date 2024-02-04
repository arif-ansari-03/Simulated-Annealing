import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = R + [np.random.normal(0,1,40)/5 for x in range(40)]

# [np.random.normal(0,1,n)/5 for x in range(m)] adds noise to a m by n matrix
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()




### SIMULATED ANNEALING ON Y = SINX

import numpy as np
import random

T = 10000
n = 100
j = random.randint(0, len(R))
e = 0

print(X)
print(Y)
print(Z)

# if de > 0 : accept
# if de < 0 : P(accept) = exp(de/T) 

# while T:
#     for i in range(n):
#         delx = random.uniform(-10, 10)
#         e2 = np.sin(x+delx)

#         de = e2 - e

#         if de > 0:
#             x = x + delx
#             e = e2
#         elif np.exp(-de/T) <= 1:
#             x = x + delx
#             e = e2
#     T -= 1

# print(np.sin(x))



