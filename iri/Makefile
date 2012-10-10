#!/bin/bash
MODULE := iriFort

all:
	f2py --overwrite-signature irisub.for -m ${MODULE} -h iri.pyf
	gfortran -w -O2 -fbacktrace -fno-automatic -fPIC -c *.for
	f2py --f77flags="-w" -c iri.pyf *.for

clean:
	find . -type f -name "*.o" | xargs rm -f
	find . -type f -name "*.so" | xargs rm -f
	find  -type f -name "*.pyf" | xargs rm -f
