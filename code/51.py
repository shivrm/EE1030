#Program to plot  the tangent of a parabola
#Code by GVV Sharma
#Released under GNU GPL
#August 10, 2020
#Revised July 31, 2024

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shivrm/Projects/matgeo/codes/CoordGeo')        #path to my scripts


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-8,8,len)

#conic parameters
V = np.array(([0,0],[0,1]))
u = 4*e1
f = 0

n,c,F,p = conic_param(V,u,f)
print(n,c,F,p)

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)

#Standard parabola parameters
eta = 2*u.T@p
flen = -eta/D_vec[1]

#Standard parabola generation
x = parab_gen(y,flen)

#Affine Parabola parameters
cA = np.block([u+eta*p*0.5,V]).T
cb = np.block([[-f],[0.5*eta*p-u]])
O = LA.lstsq(cA,cb,rcond=None)[0]#vertex

#Directrix
k1 = -8
k2 = 8

#Latus rectum
cl = n.T@F
cl = cl[0][0]

#Generating lines
x_A = line_norm(n,c,k1,k2)#directrix
x_B = line_norm(n,cl,k1,k2)#latus rectum
#print(n,c)

#Affine parabola generation
xStandardparab =np.block([[x],[y]])
Of = O.flatten()
xActualparab = P@xStandardparab + Of[:,np.newaxis]

print("e = 1")

#plotting
plt.plot(xActualparab[0,:],xActualparab[1,:],label='Parabola',color='r')
plt.plot(x_A[0,:],x_A[1,:],label='Directrix')
plt.plot(x_B[0,:],x_B[1,:],label='Latus Rectum')
#
colors = np.arange(1,3)
#Labeling the coordinates
tri_coords = np.block([O,F])
plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
vert_labels = ['$\mathbf{O}$','$\mathbf{F}$']
for i, txt in enumerate(vert_labels):
#    plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-20,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
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
#else
plt.show()
