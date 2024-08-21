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

# Vertices
A = np.array([-6, 0]).reshape(-1,1)
B = np.array([3, -8]).reshape(-1,1)
C = np.array([-4, 6]).reshape(-1,1)

# Generate lines
x_AC = line_gen(A, C)
x_BC = line_gen(B, C)

# Plot all lines
plt.plot(x_AC[0,:], x_AC[1,:],label="$AC$")
plt.plot(x_BC[0,:], x_BC[1,:],label="$BC$")


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

AC=LA.norm(A-C)
BC=LA.norm(B-C)
print(f"{AC = }")
print(f"{BC = }")
print(f"{AC/BC = }")

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

