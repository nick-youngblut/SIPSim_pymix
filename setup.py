#!/usr/bin/env python
from distutils.core import setup, Extension
import distutils.sysconfig
import numpy.distutils.misc_util

# Get the arrayobject.h(numpy) and python.h(python) header file paths:
include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs()
include_dirs.insert(0, distutils.sysconfig.get_python_inc())

setup(name='SIPSim_pymix',
      version="0.1.0",
      description='Python mixture package dependency for SIPSim',
      long_description="See the README",      
      author="Nick Youngblut",
      author_email="nyoungb2@gmail.com",
      url ="http://www.pymix.org",
      license='GNU General Public License v2.0',
      packages = ['SIPSim_pymix', 'SIPSim_pymix.examples', 'SIPSim_pymix.tests'],
      ext_modules = [Extension('_C_mixextend',
                               ['SIPSim_pymix/C_mixextend.c'],
                               include_dirs = include_dirs,
                               libraries = ['gsl', 'gslcblas' ,'m'],
                               )
                     ],
      requires = [
          'numpy',
      ]
     )

# EOF: setup.py
