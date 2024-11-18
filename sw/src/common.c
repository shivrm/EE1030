#define COMMON_C

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <omp.h>
#include <complex.h>

#define TOLERANCE 1e-9

typedef complex double entry;
typedef entry *matrix;

// Creates an m-by-n matrix
matrix mat_create(size_t m, size_t n) { 
    return malloc(m * n * sizeof(entry));
}

void mat_read(size_t n, matrix restrict a, FILE *f) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            double real, imag;
            fscanf(f, " (%lf+%lfj)", &real, &imag);
            a[i*n + j] = real + I*imag;
        }
    }
}

// Calculates res = a @ b
void mat_mul(size_t n, matrix restrict res, const matrix restrict a, const matrix restrict b) {
    memset(res, 0, n * n * sizeof(entry));

    size_t i, j, k;

    #pragma omp parallel for shared(res, a, b) private(i, j, k) schedule(static) num_threads(4)
    for (i = 0; i < n; i++) {
        for (k = 0; k < n; k++) {
            for (j = 0; j < n; j++) {
                res[i*n + j] += a[i*n + k] * b[k*n + j];
            }
        }
    }
}

// Computes the transpose of a matrix
void mat_trans(size_t n, entry *restrict a) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = i+1; j < n; j++) {
            entry temp = a[i*n + j];
            a[i*n + j] = a[j*n + i];
            a[j*n + i] = temp;
        }
    }
}

// Computes the conjugate transpose of an n-by-n matrix in place
void mat_conjt(size_t n, entry *restrict a) {
    for (size_t i = 0; i < n; i++) {
        for (size_t j = i+1; j < n; j++) {
            entry temp = a[i*n + j];
            a[i*n + j] = conj(a[j*n + i]);
            a[j*n + i] = conj(temp);
        }
    }
}

// Normalizes a vector
void normalize(size_t n, entry *restrict v) {
    entry norm = 0;
    for (size_t i = 0; i < n; i++) {
        norm += v[i] * v[i];
    } 
    norm = csqrt(norm);
    if (cabs(norm) == 0) norm = 1;
    for (size_t i = 0; i < n; i++) {
        v[i] /= norm;
    }
}


// Prints a matrix
void mat_print(size_t n, entry *restrict a) {
    printf("Matrix: \n");
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            printf("(%lf + %lfj) ", creal(a[i*n + j]), cimag(a[i*n + j]));
        }
        printf("\n");
    }
}

// Extracts the eigenvalues from a quasi-triangular matrix. Puts the eigenvalues in the
// diagonal eleements of the matrix.
void diagonalize(size_t n, const matrix restrict a) {
    size_t i = n - 1;
    while (i > 0) {
        if (cabs(a[i*n + (i-1)]) > TOLERANCE) {
            // Find the entries of the submatrix
            i = i - 1;
            entry p = a[i*n + i],
                  q = a[i*n + (i+1)],
                  r = a[(i+1)*n + i],
                  s = a[(i+1)*n + (i+1)];

            entry real = 0.5 * (p + s);
            entry imag_sqr = (p + s)*(p + s) - 4*(p*s - r*q);

            entry imag = 0.5 * csqrt(imag_sqr);
            a[i*n + i] = real + imag;
            a[(i+1)*n + (i+1)] = real - imag;
        } else {
            i = i - 1;
        }
    }
}