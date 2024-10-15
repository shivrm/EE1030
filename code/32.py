#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shivrm/Projects/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

#Given points
h1 = np.array([1, 1, 0]).reshape(-1, 1)
h2 = np.array([2, 1, -1]).reshape(-1, 1)
m1 = np.array([2, -1, 1]).reshape(-1, 1)
m2 = np.array([3, -5, 2]).reshape(-1, 1)

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

L1 = line_dir_pt(m1, h1, -10, 10)
L2 = line_dir_pt(m2, h2, -10, 10)

ax.plot(L1[0,:], L1[1,:], L1[2,:], label="L1")
ax.plot(L2[0,:], L2[1,:], L2[2,:], label="L2")

A = h1 + 25/59 * m1
B = h2 + 7/59 * m2

AB = line_gen(A, B)
ax.plot(AB[0,:], AB[1,:], AB[2,:], label="AB")

print(59 * A, 59 * B)
print(LA.norm(A-B))


# Scatter plot
colors = np.arange(1, 3)  # Example colors
tri_coords = np.block([A, B])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A', 'B']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.2f}, {tri_coords[1, i]:.2f}, {tri_coords[2, i]:.2f})',
             fontsize=12, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('fig.pdf')
#subprocess.run(shlex.split("termux-open chapters/12/11/3/6/figs/fig.pdf"))
#else
plt.show()

