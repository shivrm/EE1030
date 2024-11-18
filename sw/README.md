# Software Assignment: Eigenvalue Calculation

## What's here

 - `report/` has the files for the report
 - `src/` has the actual C code
 - `data/` has some collected data (described in the report)
 - `figs/` has figures used in the report
 - `Makefile` is used to build the project
 - `plot.py` plots the figures in `figs/` using the data in `data/`
 - `compare.sh` and `householder250.sh` are scripts used for generating the data in `data/`

## How to use

Build using
```
make all
```

This should create a directory called bin with three executables: `gram_schmidt`, `householder`, and `generate`.
 - Run `./bin/generate 50 matrix.txt` to generate a 50x50 matrix and put it in `matrix.txt`
 - Run `./bin/gram_schmidt 50 matrix.txt` to find the eigenvalues of a 50x50 matrix stored in `matrix.txt` using Gram-Schmidt orthogonalization.
 - Run `./bin/householder 50 matrix.txt` to find the eigenvalues of a 50x50 matrix stored in `matrix.txt` using Householder transformations.

To build the report run
```
cd report
pdflatex main.tex
```
