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

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

a,b,c,d=5,3,6,8
Z = (-a*X - b*Y + d) / c
ax.plot_surface(X, Y, Z, alpha=0.5, color='g', label="Plane 1")

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

a,b,c,d=1,2,3,-4
Z = (-a*X - b*Y + d) / c
ax.plot_surface(X, Y, Z, alpha=0.5, color='r')

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

a,b,c,d=2,1,-1,5
Z = (-a*X - b*Y + d) / c
ax.plot_surface(X, Y, Z, alpha=0.5, color='r')

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

a,b,c,d=*(np.array([1,2,3])-29/7*np.array([2, 1, -1])), -(4 + 29/7 * 5)
print(a*7, b*7, c*7)
Z = (-a*X - b*Y + d) / c
ax.plot_surface(X, Y, Z, alpha=0.5, color='y')

plt.legend(loc="upper left")

ax.legend("A", 'g')

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

