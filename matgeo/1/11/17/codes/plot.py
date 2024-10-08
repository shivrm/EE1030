import matplotlib.pyplot as plt
import numpy as np
from ctypes import *

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Vectors a and b
a = np.array([1, 1, -2]).reshape(-1, 1)
b = np.array([2, -4, 5]).reshape(-1, 1)

# Load 3a + 2b from file
V = np.loadtxt("output.dat").reshape(-1,1)

# Origin
O = np.array([0, 0, 0]).reshape(-1, 1)

# Plot the vectors
colors = np.arange(1, 4)
p = np.block([a, b, V])
ax.quiver(*O, p[0, :], p[1, :], p[2, :])

# Labels and their coordinates
points = {
    'a': a,
    'b': b,
    '3a + 2b': V,
}

# Label the points
for label, point in points.items():
    ax.text(
       point[0, 0], point[1, 0], point[2, 0],
       f"{label}\n({point[0,0]:.2f}, {point[1,0]:.2f}, {point[2,0]:.2f})",
       fontsize=12, ha="center", va="bottom"
    )

# Set axis limits
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([-4, 4])

# Enable grid
plt.grid()

# Save figure
plt.savefig('../figs/fig.pdf')


