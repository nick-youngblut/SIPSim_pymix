#!/usr/bin/env python
from setuptools import setup, Extension
import distutils.sysconfig
import numpy.distutils.misc_util
from setuptools import setup, find_packages

# Get the arrayobject.h(numpy) and python.h(python) header file paths:
include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs()
include_dirs.insert(0, distutils.sysconfig.get_python_inc())

setup(name='SIPSim_pymix',
      version="0.1.0",
      description='Python mixture package dependency for SIPSim',
      long_description="See the README",      
      author="Nick Youngblut",
      author_email="nyoungb2@gmail.com",
      url ="https://github.com/nick-youngblut/SIPSim_pymix",
      license='GNU General Public License v2.0',
      packages = find_packages(),
      package_dir = {'SIPSim_pymix' : 'SIPSim_pymix'},
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
