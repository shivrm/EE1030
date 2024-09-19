import matplotlib.pyplot as plt
import numpy as np

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


# Points A, B and C
A, B, C = np.loadtxt("output.dat").reshape(-1, 2, 1)

# Plot AB, BC, and CA
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)
plt.plot(x_AB[0,:], x_AB[1,:], label="AB")
plt.plot(x_BC[0,:], x_BC[1,:], label="BC")
plt.plot(x_CA[0,:], x_CA[1,:], label="CA")

# Plot the points
colors = np.arange(1, 4)
p = np.block([A, B, C])
plt.scatter(p[0, :], p[1, :], c=colors)

# Labels and their coordinates
points = {
    'A': A,
    'B': B,
    'C': C,
}

# Label the points
for label, point in points.items():
    plt.text(
       point[0, 0], point[1, 0],
       f"{label}\n({point[0,0]:.2f}, {point[1,0]:.2f})",
       fontsize=12, ha="center", va="bottom"
    )

# Enable grid
plt.grid()

# Save the figure
plt.savefig('../figs/fig.pdf')
