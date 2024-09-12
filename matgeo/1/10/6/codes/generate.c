#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"

int main(void) {
    FILE *f = fopen("output.dat", "w");
    
    double **P = createMat(3, 1);
    P[0][0] = 5;
    P[1][0] = 0;
    P[2][0] = 8;
    
    double **Q = createMat(3, 1);
    Q[0][0] = 3;
    Q[1][0] = 3;
    Q[2][0] = 2;

    double **dirn = Matsub(Q, P, 3, 1);
    double **result = Matscale(dirn, 3, 1, 1 / Matnorm(dirn, 3));

    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", result[i][0]);
    }

    return 0;
}
