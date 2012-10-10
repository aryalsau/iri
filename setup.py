#!/usr/bin/env python
from numpy.distutils.core import setup, Extension

ext = Extension('iri.iriFort',
  sources=['iri/iri.pyf', 'iri/irisub.for', 'iri/irifun.for', 'iri/iriflip.for', 'iri/iritec.for', 'iri/igrf.for', 'iri/cira.for', 'iri/iridreg.for'])

setup (name = "IRI-2012",
       version = "0.1",
       description = "Wrapper to call fortran routines from the International Reference Ionosphere (2012)",
       author = "Sebastien de Larquier",
       author_email = "sdelarquier@vt.edu",
       url = "",
       long_description =
        """
For more information on the International Reference Ionosphere, go to 
http://iri.gsfc.nasa.gov/
        """,
       packages = ['iri'],
       ext_modules = [ext],
       keywords=['Scientific/Space'],
       classifiers=[
                   "Programming Language :: Python/Fortran"
                   ]
        )

