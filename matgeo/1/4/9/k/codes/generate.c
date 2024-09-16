#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"

int main(void) {
    FILE *f = fopen("output.dat", "w");

    // Point P
    double **P = createMat(3, 1);
    P[0][0] = 1;
    P[1][0] = 2;
    P[2][0] = -1;
    
    // Point Q
    double **Q = createMat(3, 1);
    Q[0][0] = -1;
    Q[1][0] = 1;
    Q[2][0] = 1;

    // Find point which divides PQ in ratio 1/2 internally
    double k = 0.5;
    double **R = Matsec(Q, P, 3, k);

    // Write to a file
    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", R[i][0]);
    }
 
    // Find point which divides PQ in ratio 1/2 externally
    k = -0.5;
    R = Matsec(Q, P, 3, k);

    // Write to a file
    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", R[i][0]);
    }

    return 0;
}
