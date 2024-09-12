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
h1 = np.array(([-3, 1, 5])).reshape(-1,1) 
h2 = np.array(([-1, 2, 5])).reshape(-1,1)  

m1 = h1
m2 = h2

n = np.array([1, -2, 1]).reshape(-1, 1)
c = np.array([[0]])

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#Generating all lines
x_AB = line_dir_pt(h1,m1,-1,1)
ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],label='$AB$')

x_AB = line_dir_pt(h2,m2,-1,1)
ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],label='$AB$')

X = np.array([0,0,0]).reshape(-1,1)

# Scatter plot
colors = np.arange(1, 4)  # Example colors
tri_coords = np.block([h1, h2, X])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A', 'B', 'X']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',
             fontsize=12, ha='center', va='bottom')

# Plots the plane

# Generate grid points for x and y
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z values for each (x, y) pair to satisfy the plane equation
a,b,c,d=1,-2,1,0
Z = (-a*X - b*Y + d) / 1

ax.plot_surface(X, Y, Z, alpha=0.5)

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

