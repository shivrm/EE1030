import matplotlib.pyplot as plt
import numpy as np
from ctypes import *

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Vectors P and Q
P = np.array([5, 0, 8]).reshape(-1, 1)
Q = np.array([3, 3, 2]).reshape(-1, 1)

# Load unit vector along PQ from file
V = np.loadtxt("output.dat").reshape(-1,1)

# Plot the points
colors = np.arange(1, 3)
p = np.block([P, Q])
ax.scatter(p[0, :], p[1, :], p[2, :], c=colors)

# Label and their coordinates
points = {
    'P': P,
    'Q': Q,
}

# Label the points
for label, point in points.items():
    ax.text(
       point[0, 0], point[1, 0], point[2, 0],
       f"{label}\n({point[0,0]:.2f}, {point[1,0]:.2f}, {point[2,0]:.2f})",
       fontsize=12, ha="center", va="bottom"
    )

# Plot the unit vector along PQ
ax.quiver(*P, *V)

# Enable grid
plt.grid()

# Save the figure
plt.savefig('../figs/fig.pdf')


