#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Secion Formula


import sys                                          #for path to external scripts
sys.path.insert(0, '/root/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
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

k = 2

# Vertices
A = np.array([k + 1, 2*k]).reshape(-1,1)
B = np.array([3*k, 2*k+3]).reshape(-1,1)
C = np.array([5*k-1, 5*k]).reshape(-1,1)

# Generate lines
x_AC = line_gen(A, C)
x_BC = line_gen(B, C)

# Plot all lines
plt.plot(x_AC[0,:], x_AC[1,:],label="$AC$")

# Helper function for annotating a point
def annot(p, lbl):
    # Sorry for the bad code :P
    # Basically p.tolist gives a list of the form [[float_x], [float_y]]
    # I map each list to the integer value of the coordinate
    # e.g. `[float_x]` is mapped to `int_x`
    #   ~shivrm
    coords = tuple(map(lambda x: x[0], p.tolist()))
    plt.annotate(f"{lbl}\n{coords}",
                 coords,
                  textcoords="offset points",
                  xytext=(20, -10),
                 ha="center")
annot(A, 'A')
annot(B, 'B')
annot(C, 'C')


coords = tuple(map(lambda x: x[0], B.tolist()))
plt.annotate("k = 2", coords, textcoords="offset points", xytext=(-20, 10), ha="center")



print("Rank:", LA.matrix_rank(np.block([A-C, B-C])))

k = 1/2

# Vertices
A2 = np.array([k + 1, 2*k]).reshape(-1,1)
B2 = np.array([3*k, 2*k+3]).reshape(-1,1)
C2 = np.array([5*k-1, 5*k]).reshape(-1,1)

# Generate lines
x_AC2 = line_gen(A2, C2)
x_AB2 = line_gen(A2, B2)
x_BC2 = line_gen(B2, C2)

# Plot all lines
plt.plot(x_AB2[0,:], x_AB2[1,:],label="$A'B'$")
# plt.plot(x_BC2[0,:], x_BC2[1,:],label="$B'C'$")


# Helper function for annotating a point
def annot(p, lbl):
    # Sorry for the bad code :P
    # Basically p.tolist gives a list of the form [[float_x], [float_y]]
    # I map each list to the integer value of the coordinate
    # e.g. `[float_x]` is mapped to `int_x`
    #   ~shivrm
    coords = tuple(map(lambda x: x[0], p.tolist()))
    plt.annotate(f"{lbl}\n{coords}",
                 coords,
                  textcoords="offset points",
                  xytext=(20, -10),
                 ha="center")
annot(A2, 'A\'')
annot(B2, 'B\'')

coords = tuple(map(lambda x: x[0], C2.tolist()))
plt.annotate("k = 1/2", coords, textcoords="offset points", xytext=(-20, 10), ha="center")

annot(C2, 'C\'')


print("Rank:", LA.matrix_rank(np.block([A-C, B-C])))

ax = plt.gca()

ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('fig.pdf')
#else
#plt.show()

