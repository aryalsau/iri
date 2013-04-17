# International Reference Ionosphere: Python wrappers

## Licence

Though edits had to be made to the fortran code to accomodate f2py compilation, I do not claim any intellectual contributions to said files.
Please visit <http://iri.gsfc.nasa.gov/> for more details on IRI itself and its principal contributors.

My only contribution was to optimized the fortran code in order to wrap it with f2py, making it useable from Python. 
In the future, I will add higher level Python wrappers to abstract the calls to fortran routines.

## Installation

To install the IRI python module, from this repository run:

    cd iri
    make clean
    make
    cd ..
    sudo python setup.py install

## Use

To use this module:

    import iri
