#Code by GVV Sharma
#July 25, 2024
#released under GNU GPL
#Line intersection


import sys                                          #for path to external scripts
sys.path.insert(0, '/root/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if


#Given Points
#A = np.array(([3, 2])).reshape(-1,1) 
#Line parameters
r = 2

n1 = np.array(([3, -1])).reshape(-1,1) 
c1 = -8
n2 = np.array(([6, -r])).reshape(-1,1) 
c2 = -16

k1 = -1
k2 = 1
#Generating Lines
x_A = line_norm(n1,c1,k1,k2)
k1 = -1
k2 = 1
x_B = line_norm(n2,c2,k1,k2)

#Plotting all lines
plt.plot(x_A[0,:],x_A[1,:],label='$(3 \quad -1)\mathbf{x}=-8$')
plt.plot(x_B[0,:],x_B[1,:],label='$(6 \quad -r)\mathbf{x}=-16$', linestyle="--")

ax = plt.gca()
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
'''
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('fig.pdf')
#else
#plt.show()
