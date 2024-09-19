#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "libs/matfun.h"

int main(void) {
    FILE *f = fopen("output.dat", "w");

    // Given values
    double a = 8;
    double B = 45 * M_PI / 180;
    double C = 30 * M_PI / 180;

    double ratio = sin(B) / sin(C); // b / c
    double c = a / (cos(B) + ratio * cos(C));

    // Vertex A
    double **vA = createMat(2, 1);
    vA[0][0] = c * sin(B);
    vA[1][0] = c * cos(B);
   
    // Vertex B
    double **vB = createMat(2, 1);
    vB[0][0] = 0;
    vB[1][0] = 0;

    // Vertex C
    double **vC = createMat(2, 1);
    vC[0][0] = a;
    vC[1][0] = 0;

    // Write the coordinates to a file
    for (int i = 0; i < 2; i++) {
        fprintf(f, "%lf\n", vA[i][0]);
    }
    for (int i = 0; i < 2; i++) {
        fprintf(f, "%lf\n", vB[i][0]);
    }
    for (int i = 0; i < 2; i++) {
        fprintf(f, "%lf\n", vC[i][0]);
    }
    

    return 0;
}
