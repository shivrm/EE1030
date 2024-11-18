#ifndef COMMON_C
#include "common.c"
#endif

#ifndef DEFLATE_C
#include "deflate.c"
#endif

// Computes v given x
void householder_vector(size_t n, entry *restrict v) {
    entry norm = 0;
    for (int i = 0; i < n; i++) {
        norm += v[i] * v[i];
    }
    norm = csqrt(norm);

    v[0] += (creal(v[0]) < 0)? -norm : norm;

    // Normalize v
    norm = 0;
    for (size_t i = 0; i < n; i++) {
        norm += v[i] * v[i];
    }
    norm = csqrt(norm);
    for (size_t i = 0; i < n; i++) {
        v[i] /= norm;
    }
}

complex double dot_product(complex double *v1, complex double *v2, int length) {
    complex double result = 0.0 + 0.0*I;
    for (int i = 0; i < length; i++) {
        result += conj(v1[i]) * v2[i];
    }
    return result;
}


// Function to perform the Householder QR decomposition for complex matrices
void householder_qr(size_t n, matrix q, matrix r, matrix a) {
    entry *v = malloc(n * sizeof(entry));
    entry *temp = malloc(n * sizeof(entry));

    // Initialize R to A and Q as identity matrix
    memcpy(r, a, n*n*sizeof(entry));
    memset(q, 0, n*n*sizeof(entry));
    for (int i =0; i < n; i++) {
        q[i*n + i] = 1;
    }

    for (size_t k = 0; k < n; k++) {
        // First get the subvector
        for (size_t i = k; i < n; i++) {
            v[i - k] = r[i * n + k];
        }
        // Then use that to compute the Householder vector
        householder_vector(n - k, v);

        // Update Q
        memset(temp, 0, n * sizeof(complex));
        for(int i = 0; i < n; ++i) {
            for(int j = k; j < n; ++j) {
                temp[i] += q[i*n + j] * v[j-k];
            }
        }

        for(int i = 0; i < n; ++i) {
            for(int j = k; j < n; ++j) {
                q[i*n + j] -= 2*temp[i] * v[j-k];
            }
        }
        
        // Update R
        memset(temp, 0, n * sizeof(complex));
        for(int j = k; j < n; ++j) {
            for(int i = 0; i < n; ++i) {
                temp[i] += r[j*n + i] * v[j-k];
            }
        }

        for(int j = k; j < n; ++j) {
            for(int i = 0; i < n; ++i) {
                r[j*n + i] -= 2*temp[i] * v[j-k];
            }
        }

        
    }

    free(v);
    free(temp);
}

// Checks if a matrix has converged
int converged(size_t n, matrix restrict a) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i - 1; j++) {
            if (cabs(a[i*n + j]) > TOLERANCE) {
                return 0;
            }
        }
    }
    return 1;
}

size_t qr_reduce(size_t n, matrix restrict a) { 
    // hessenberg_reduction(n, a);
    matrix q = mat_create(n, n);
    matrix r = mat_create(n, n);      

    while (!converged(n, a)) {
        // entry shift = 0*get_wilkinson_shift(n, a);

        // for (size_t i = 0; i < n; i++) {
        //     a[i*n + i] -= shift;
        // }

        householder_qr(n, q, r, a);
        mat_mul(n, a, r, q);    

        // for (size_t i = 0; i < n; i++) {
        //     a[i*n + i] += shift;
        // }

        n = deflate(n, a);
    }

    free(q);
    free(r);

    return n;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("usage: %s <size> <input file>\n", argv[0]);
        return 1;
    }

    int n;
    if (sscanf(argv[1], "%d", &n) != 1) {
        printf("%s: invalid size: '%s'\n", argv[0], argv[1]);
        return 1;
    }

    FILE *f = fopen(argv[2], "r");
    if (!f) {
        printf("%s: could not open '%s'", argv[0], argv[2]);
        return 1;
    }
    
    matrix a = mat_create(n, n);
    mat_read(n, a, f);
    fclose(f);

    n = qr_reduce(n, a);        
    diagonalize(n, a);
 
    for (size_t i = 0; i < n; i++) {
        entry eig = a[i*n + i];
        printf("%lf + %lfi\n", creal(eig), cimag(eig));
    }
 
    free(a);

    return 0;
}