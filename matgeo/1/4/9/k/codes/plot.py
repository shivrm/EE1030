import matplotlib.pyplot as plt
import numpy as np
from ctypes import *

# Generates a line from point A to point B
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

####################################################
# First plot

# Points P and Q
P = np.array([1, 2, -1]).reshape(-1, 1)
Q = np.array([-1, 1, 1]).reshape(-1, 1)

# Point which divides PQ in the ratio 1/2 internally
R = np.loadtxt("output.dat", max_rows=3).reshape(-1, 1)

# Plot PQ
x_PQ = line_gen(P, Q)
ax.plot(x_PQ[0,:], x_PQ[1,:], x_PQ[2,:], label="PQ")

# Plot the points
colors = np.arange(1, 4)
p = np.block([P, Q, R])
ax.scatter(p[0, :], p[1, :], p[2, :], c=colors)

# Labels and their coordinates
points = {
    'P': P,
    'Q': Q,
    'R': R,
}

# Label the points
for label, point in points.items():
    ax.text(
       point[0, 0], point[1, 0], point[2, 0],
       f"{label}\n({point[0,0]:.2f}, {point[1,0]:.2f}, {point[2,0]:.2f})",
       fontsize=12, ha="center", va="bottom"
    )

# Enable grid
plt.grid()

# Save the figure
plt.savefig('../figs/fig1.pdf')


####################################################
# Second plot

# Clear figure
plt.clf()
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Point which divides PQ in the ratio 1/2 externally
R = np.loadtxt("output.dat", skiprows=3, max_rows=3).reshape(-1, 1)

# Plot PR (since Q lies in between P and R)
x_PR = line_gen(P, R)
ax.plot(x_PR[0,:], x_PR[1,:], x_PR[2,:], label="PR")

# Plot the points
colors = np.arange(1, 4)
p = np.block([P, Q, R])
ax.scatter(p[0, :], p[1, :], p[2, :], c=colors)

# Labels and their coordinates
points = {
    'P': P,
    'Q': Q,
    'R': R,
}

# Label the points
for label, point in points.items():
    ax.text(
       point[0, 0], point[1, 0], point[2, 0],
       f"{label}\n({point[0,0]:.2f}, {point[1,0]:.2f}, {point[2,0]:.2f})",
       fontsize=12, ha="center", va="bottom"
    )

# Enable grid
plt.grid()

# Save figure
plt.savefig('../figs/fig2.pdf')
