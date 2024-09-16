import matplotlib.pyplot as plt
import numpy as np
from ctypes import *

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# The two unit vectors a and b
# a and b are at and angle of 120 degrees
a = np.array([1, 0, 0]).reshape(-1, 1)
b = np.array([-1/2, pow(3, 0.5)/2, 0]).reshape(-1, 1)

# Loads a+b and a-b from the file
V_sum = np.loadtxt("output.dat", max_rows=3).reshape(-1,1)
V_diff = np.loadtxt("output.dat", skiprows=3).reshape(-1,1)

# Origin
O = np.array([0, 0, 0]).reshape(-1, 1)

# Plot the points
colors = np.arange(1, 5)
p = np.block([a, b, V_sum, V_diff])
ax.quiver(*O, p[0, :], p[1, :], p[2, :])

# Labels of points and the label coordinates
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


# Set axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
# Enabke grid
plt.grid()

# Save the figure
plt.savefig('../figs/fig.pdf')


