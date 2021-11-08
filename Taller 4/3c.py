import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

a = 8 / 3
b = 10
c = 28      

def taylor(x, y, z):
    u = b * (y - x)
    v = c*x - y - x*z
    w = x*y - a*z
    return u,v,w

h = 0.01
stepCnt = 10000

xs = np.empty((stepCnt + 1,))  #Necesitamos un valor mas para el contador
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

xs[0], ys[0], zs[0] = (0., 1., 1.05) #Fijamos valores iniciales de x,y,z

for i in range(stepCnt) :
    # Derivadas de x, y, z.
    x_dot, y_dot, z_dot = taylor(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * h)
    ys[i + 1] = ys[i] + (y_dot * h)
    zs[i + 1] = zs[i] + (z_dot * h)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Atractor de Lorentz simulado con Taylor")

plt.show()
