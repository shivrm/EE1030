CC=gcc
CFLAGS=-Wall -fopenmp -Ofast -mavx2 -lm

all: clean gram_schmidt householder generate

clean:
	rm -fr bin	# Remove for real
	mkdir bin

gram_schmidt: src/common.c src/gram_schmidt.c
	$(CC) $(CFLAGS) src/gram_schmidt.c -o bin/gram_schmidt

householder: src/common.c src/householder.c
	$(CC) $(CFLAGS) src/householder.c -o bin/householder

generate: src/common.c src/generate.c
	$(CC) $(CFLAGS) src/generate.c -o bin/generate

.PHONY: clean