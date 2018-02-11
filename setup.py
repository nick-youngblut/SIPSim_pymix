#!/usr/bin/env python
from distutils.core import setup, Extension
import distutils.sysconfig
import numpy.distutils.misc_util
import os

# Get the arrayobject.h(numpy) and python.h(python) header file paths:
include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs()
include_dirs.insert(0, distutils.sysconfig.get_python_inc())
## including conda include/ dir if found
try:
    conda_include = os.path.join(os.environ['CONDA_PREFIX'], 'include')
    include_dirs.insert(0, conda_include)
except KeyError:
    pass

# c module that requires gsl
module1 = Extension('_C_mixextend',
                    ['SIPSim_pymix/C_mixextend.c'],
                    include_dirs = include_dirs,
                    libraries = ['gsl', 'gslcblas' ,'m'])

# setup
setup(name='SIPSim_pymix',
      version="0.1.0",
      description='Python mixture package dependency for SIPSim',
      long_description="See the README",      
      author="Nick Youngblut",
      author_email="nyoungb2@gmail.com",
      url ="https://github.com/nick-youngblut/SIPSim_pymix",
      license='GNU General Public License v2.0',
      packages = ['SIPSim_pymix'],
      package_dir = {'SIPSim_pymix' : 'SIPSim_pymix'},
      ext_modules = [module1],
      requires = ['numpy']
     )
