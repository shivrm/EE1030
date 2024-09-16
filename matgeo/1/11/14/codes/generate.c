#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"

int main(void) {
    FILE *f = fopen("output.dat", "w");

    // Defines the vector a
    double **a = createMat(3, 1);
    a[0][0] = 1;
    a[1][0] = 0;
    a[2][0] = 0;
    
    // Vector b is at an angle of 120 degrees to a
    double **b = createMat(3, 1);
    b[0][0] = cos(120 * M_PI / 180);
    b[1][0] = sin(120 * M_PI / 180);
    b[2][0] = 0;

    // Calculate their sum and difference
    double **sum = Matadd(a, b, 3, 1);
    double **diff = Matsub(a, b, 3, 1);

    // Write the sum to a file
    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", sum[i][0]);
    }
    
    // Write the difference to a file
    for (int i = 0; i < 3; i++) {
        fprintf(f, "%lf\n", diff[i][0]);
    }

    return 0;
}
