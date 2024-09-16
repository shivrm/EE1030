#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"

int main(void) {
    FILE *f = fopen("output.dat", "w");

    // Vector a
    double **a = createMat(3, 1);
    a[0][0] = 1;
    a[1][0] = 1;
    a[2][0] = -2;
    
    // Vector b
    double **b = createMat(3, 1);
    b[0][0] = 2;
    b[1][0] = -4;
    b[2][0] = 5;

    // Calculate 3a + 2b
    double **res = Matadd(Matscale(a, 3, 1, 3), Matscale(b, 3, 1, 2), 3, 1);

    // Write 3a + 2b to a file
    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", res[i][0]);
    }

    return 0;
}
