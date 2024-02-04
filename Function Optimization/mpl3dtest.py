import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

# function to get a random point in the rect lx <= x <= ux && ly <= y <= uy

def randompoint(lx, ux, ly, uy):

    x = np.arange(lx, ux, 0.1)
    x = x[np.random.randint(len(x))]
    y = np.arange(lx, ux, 0.1)
    y = y[np.random.randint(len(y))]

    return x, y

def energyfunction(X, Y):
    return np.sin(X) + np.sin(Y)  + 4 * np.exp(-(0.1*X*X + 0.1*Y*Y))

# single points

ax = plt.axes(projection="3d")

x_data = np.arange(-10, 10, 0.1)
y_data = np.arange(-10, 10, 0.1)

X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(X) + np.sin(Y)  + 4 * np.exp(-(0.1*X*X + 0.1*Y*Y))

ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.4)
# plt.show()

T = 10
n = 10
x, y = randompoint(-10, 10, -10, 10)
x, y = -10, -10
gx, gy = x, y

ax.scatter(x, y, energyfunction(x, y)+0.1)

while(T):
    e1 = energyfunction(x, y)

    for i in range(n):

        if energyfunction(gx, gy) < energyfunction(x, y):
            gx, gy = x, y
        step = 0.3
        nx = x + random.uniform(-1, 1) * step
        ny = y + random.uniform(-1, 1) * step

        if (nx > 10): nx -= step
        if (ny > 10): ny -= step
        if (nx < 0): nx += step
        if (ny < 0): ny += step
        e2 = energyfunction(nx, ny)
        de = e2 - e1

        if de > 0 or random.uniform(0, 1) <= np.exp(de/(T)):
            x, y = nx, ny

    T-=1

print(x, y, energyfunction(x,y))
ax.scatter(x, y, energyfunction(x, y)+0.1, marker = 'd')
ax.scatter(gx, gy, energyfunction(gx, gy)+0.1, marker='o')
plt.show()






