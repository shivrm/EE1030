#ifndef COMMON_C
#include "common.c"
#endif

#include <stdio.h>
#include <time.h>

int main(int argc, char* argv[]) {
    srand(clock());

    if (argc != 3) {
        printf("usage: %s <size> <output file>\n", argv[0]);
        return 1;
    }

    int n;
    if (sscanf(argv[1], "%d", &n) != 1) {
        printf("%s: invalid size: '%s'\n", argv[0], argv[1]);
        return 1;
    }

    FILE *f = fopen(argv[2], "w");
    if (!f) {
        printf("%s: could not open '%s'", argv[0], argv[2]);
        return 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            entry entry = (double)rand()/RAND_MAX-0.5 + I*((double)rand()/RAND_MAX-0.5);
            fprintf(f, "(%lf+%lfj) ", creal(entry), cimag(entry));
        }
        fprintf(f, "\n");
    }

    fclose(f);
    return 0;
}