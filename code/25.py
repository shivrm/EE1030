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
h = np.array(([-3, 0, 1])).reshape(-1,1) 
m = np.array([-2,1,2]).reshape(-1,1)

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#Generating all lines
x_AB = line_dir_pt(m,h,-10,10)
ax.plot(x_AB[0,:],x_AB[1,:], x_AB[2,:],label='$AB$')

# Scatter plot
colors = np.arange(1, 2)  # Example colors
tri_coords = np.block([h])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['A']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',
             fontsize=12, ha='center', va='bottom')

# Plots the plane
# Generate grid points for x and y
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

a,b,c,d=0,3,-1,0
Z = (-a*X - b*Y + d) / c
ax.plot_surface(X, Y, Z, alpha=0.5)

y = np.linspace(-10, 10, 50)
z = np.linspace(-10, 10, 50)
Y, Z = np.meshgrid(x, y)

a,b,c,d=1,2,0,0
X = (-d*Z - b*Y + d) / a
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

