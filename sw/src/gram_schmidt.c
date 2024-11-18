#ifndef COMMON_C
#include "common.c"
#endif

#ifndef DEFLATE_C
#include "deflate.c"
#endif

// Computes an orthogonal basis es from a collection of vectors vs
void gram_schmidt(size_t n, matrix restrict es, const matrix restrict vs) {
    memcpy(es, vs, n * n * sizeof(entry));

    // Convert columnv vectors to row vectors
    mat_trans(n, es);

    for (int i = 0; i < n; i++) {        
        entry *v = &es[i*n];
        normalize(n, v);

        // For each succeeing vectpr u, subtract the projection of u on v from u.
        // v is already normalized, so proj_v(u) =  (u.v) v
        for (int j = i+1; j < n; j++) {
            entry *u = &es[j*n];

            entry dot = 0.0;
            for (int k = 0; k < n; k++) {
                dot += v[k] * u[k];
            }

            for (int k = 0; k < n; k++) {
                u[k] -= dot * v[k];
            }
        }
    }
}

// Checks if a matrix has converged
int converged(size_t n, matrix restrict a) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i-1; j++) {
            if (cabs(a[i*n + j]) > TOLERANCE) {
                return 0;
            }
        }
    }
    
    return 1;
}


// Decomposes a matrix a as a = qr, where q is orthogonal and r is upper-triangular
void gram_schmidt_qr(size_t n, matrix restrict q, matrix restrict r, const matrix restrict a) {
    gram_schmidt(n, q, a); 
    mat_mul(n, r, q, a);
    mat_trans(n, q);
}

// Reduces a matrix to quasi-triangular form, applying shifts and deflation
size_t qr_reduce(size_t n, matrix restrict a) { 
    matrix q = mat_create(n, n);
    matrix r = mat_create(n, n);      

    while (!converged(n, a)) {
        // Shift by last element
        // entry shift = a[(n-1)*n + (n-1)];

        // Shift
        // for (int i = 0; i < n; i++) {
        //     a[i*n + i] -= shift;
        // }

        // Decompose a as a = qr, then assign a = rq
        gram_schmidt_qr(n, q, r, a);
        mat_mul(n, a, r, q);    

        // Unshift
        // for (int i = 0; i < n; i++) {
        //     a[i*n + i] += shift;
        // }

        // Deflate
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