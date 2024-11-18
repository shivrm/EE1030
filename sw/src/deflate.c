#define DEFLATE_C

#ifndef COMMON_C
#include "common.c"
#endif

// Returns the index of the column which may be eliminated
size_t get_real_deflatable(size_t n, matrix a) {
    for (size_t i = n-1; i > 1; i--) {
        if (cabs(a[i*n + i - 1]) < TOLERANCE && cabs(a[(i+1)*n + i]) < TOLERANCE) {
            return i;            
        }
    }
    return -1;
}

// Returns the index of the top left corner of a 2x2 block which
// may be eliminated
size_t get_complex_deflatable(size_t n, matrix a) {
    for (size_t i = 1; i < n-2; i++) {
        double x = cabs(a[(i+2)*n + i]);
        double y = cabs(a[(i+2)*n + (i+1)]);
        double z = cabs(a[(i)*n + (i-1)]);
        if (x < TOLERANCE && y < TOLERANCE && z < TOLERANCE) {
            return i;
        }
    }
    return -1;
}

// Remoes the row and column with the given index
void remove_row_col(size_t n, matrix a, size_t d) {
    size_t yidx = 0;
    for (size_t i = 0; i < n; i++) {
        if (i == d) continue;
        size_t xidx = 0;
        for (size_t j = 0; j < n; j++) {
            if (j == d) continue;
            a[yidx*(n-1) + xidx++] = a[i*n + j];
        }
        yidx++;
    }
}

// Deflates the matrix if possible and prints the
// deflated eigenvalues
size_t deflate(size_t n, matrix a) {
    size_t d = get_real_deflatable(n, a);   
    if (d != -1) {
        entry eig = a[d*n + d];
        printf("%lf + %lfi\n", creal(eig), cimag(eig));
        remove_row_col(n, a, d);    
        return n - 1;
    }

    d = get_complex_deflatable(n, a);
    if (d != -1) {
        entry p = a[d*n + d],
                q = a[d*n + (d+1)],
                r = a[(d+1)*n + d],
                s = a[(d+1)*n + (d+1)];

        entry real = 0.5 * (p + s);
        entry imag_sqr = (p + s)*(p + s) - 4*(p*s - r*q);
        entry imag = 0.5 * csqrt(imag_sqr);

        entry eig1 = real + imag, eig2 = real - imag;
        printf("%lf + %lfi\n", creal(eig1), cimag(eig1));
        printf("%lf + %lfi\n", creal(eig2), cimag(eig2));
        remove_row_col(n, a, d);
        remove_row_col(n - 1, a, d);
        return n - 2;
    }

    return n;
}
