#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Secion Formula


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shivrm/matgeo/codes/CoordGeo')        #path to my scripts
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
A = np.array([5, -6]).reshape(-1,1)
B = np.array([6, 4]).reshape(-1,1)
C = np.array([0, 0]).reshape(-1,1)

# Midpoint
D = (B + C) / 2
coords = tuple(map(lambda x: int(x[0]), D.tolist()))
print(f"D: {coords}")

# Generate lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)
x_AD = line_gen(A, D)

# Plot all lines
plt.plot(x_AB[0,:], x_AB[1,:],label="$AB$")
plt.plot(x_BC[0,:], x_BC[1,:],label="$BC$")
plt.plot(x_CA[0,:], x_CA[1,:],label="$CA$")
plt.plot(x_AD[0,:], x_AD[1,:],label="$AD$")


# Helper function for annotating a point
def annot(p, lbl):
    # Sorry for the bad code :P
    # Basically p.tolist gives a list of the form [[float_x], [float_y]]
    # I map each list to the integer value of the coordinate
    # e.g. `[float_x]` is mapped to `int_x`
    #   ~shivrm
    coords = tuple(map(lambda x: int(x[0]), p.tolist()))
    plt.annotate(f"{lbl}\n{coords}",
                 coords,
                  textcoords="offset points",
                  xytext=(20, -10),
                 ha="center")

# Refer to the annotation in `annot`
# Finds the coordinates of the midpoint of AD
coords = tuple(map(lambda x: int(x[0]), ((A+D)/2).tolist()))

# Calculates the length of AD
length = LA.norm(D-A)
print(f"AD = {length}")

plt.annotate(f"AD = {length}", coords,
                  textcoords="offset points",
                  xytext=(20, -10),
                 ha="center")

annot(A, 'A')
annot(B, 'B')
annot(C, 'C')
annot(D, 'D')

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
#plt.savefig('chapters/10/7/2/1/figs/fig.pdf')
#subprocess.run(shlex.split("termux-open chapters/10/7/2/1/figs/fig.pdf"))
#else
plt.show()
