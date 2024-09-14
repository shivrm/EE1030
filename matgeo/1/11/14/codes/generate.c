#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"

int main(void) {
    FILE *f = fopen("output.dat", "w");
    
    double **a = createMat(3, 1);
    a[0][0] = 1;
    a[1][0] = 0;
    a[2][0] = 0;
    
    double **b = createMat(3, 1);
    b[0][0] = cos(120 * M_PI / 180);
    b[1][0] = sin(120 * M_PI / 180);
    b[2][0] = 0;

    double **sum = Matadd(a, b, 3, 1);
    double **diff = Matsub(a, b, 3, 1);

    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", sum[i][0]);
    }
    
    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", diff[i][0]);
    }

    return 0;
}
