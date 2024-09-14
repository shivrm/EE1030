#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"

int main(void) {
    FILE *f = fopen("output.dat", "w");
    
    double **a = createMat(3, 1);
    a[0][0] = 1;
    a[1][0] = 1;
    a[2][0] = -2;
    
    double **b = createMat(3, 1);
    b[0][0] = 2;
    b[1][0] = -4;
    b[2][0] = 5;

    double **res = Matadd(Matscale(a, 3, 1, 3), Matscale(b, 3, 1, 2), 3, 1);
    double **dirn = Matscale(res, 3, 1, 1 / Matnorm(res, 3));

    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", dirn[i][0]);
    }

    return 0;
}
