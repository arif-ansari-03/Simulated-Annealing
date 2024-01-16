import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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

ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.9)
# plt.show()

T = 100
n = 100
x, y = randompoint(-10, 10, -10, 10)

ax.scatter(x, y, energyfunction(x, y)+0.1)

while(T):
    e1 = energyfunction(x, y)

    for i in range(n):
        nx, ny = randompoint(-10, 10, -10, 10)
        e2 = energyfunction(nx, ny)

        de = e2 - e1

        if de > 0 or np.exp(-de/T) <= 1:
            x, y = nx, ny

    T-=1

print(x, y, energyfunction(x,y))
ax.scatter(x, y, energyfunction(x, y)+0.1, marker = 'd')
plt.show()






