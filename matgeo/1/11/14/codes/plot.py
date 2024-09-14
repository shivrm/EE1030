import matplotlib.pyplot as plt
import numpy as np
from ctypes import *

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

a = np.array([1, 0, 0]).reshape(-1, 1)
b = np.array([-1/2, pow(3, 0.5)/2, 0]).reshape(-1, 1)

V_sum = np.loadtxt("output.dat", max_rows=3).reshape(-1,1)
V_diff = np.loadtxt("output.dat", skiprows=3).reshape(-1,1)

O = np.array([0, 0, 0]).reshape(-1, 1)

# Plot the points
colors = np.arange(1, 5)
p = np.block([a, b, V_sum, V_diff])
ax.quiver(*O, p[0, :], p[1, :], p[2, :])

points = {
    'a': a,
    'b': b,
    'a + b': V_sum,
    'a - b': V_diff,
}

# Label the points
for label, point in points.items():
    ax.text(
       point[0, 0], point[1, 0], point[2, 0],
       f"{label}\n({point[0,0]:.2f}, {point[1,0]:.2f}, {point[2,0]:.2f})",
       fontsize=12, ha="center", va="bottom"
    )


ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])


plt.grid()
plt.savefig('../figs/fig.pdf')


