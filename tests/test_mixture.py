#!/usr/bin/env python
# import
from __future__ import print_function
## batteries
import os
import sys
import pytest
## 3rd party
import numpy as np
## package
from SIPSim_pymix import mixture

# data dir
test_dir = os.path.join(os.path.dirname(__file__))
data_dir = os.path.join(test_dir, 'data')


# UniformDistribution
def test_unif_dist():
    f = mixture.UniformDistribution(0,1)
    x = f.sample()
    assert x >= 0 and x <= 1

def test_unif_dist_fail():
    with pytest.raises(AssertionError):
        f = mixture.UniformDistribution(0,0)
        
# NormalDistrubiont
def test_norm_dist():
    f = mixture.NormalDistribution(1,1)
    x = f.sample()
    assert isinstance(x, float)

def test_norm_dist_zero():
    f = mixture.NormalDistribution(0,0)
    x = f.sample()
    assert isinstance(x, float)
    assert x == 0

def test_norm_dist_pdf():
    f = mixture.NormalDistribution(0,1)
    x = f.pdf(np.array([0,1]))
    assert isinstance(x, np.ndarray)
    assert len(x) == 2


# MixtureModel
def test_mix_model():
    f1 = mixture.NormalDistribution(1,1)
    f2 = mixture.NormalDistribution(2,1)    
    f3 = mixture.MixtureModel(2, [0.5,0.5], [f1,f2])
    x = f3.sample()
    assert isinstance(x, list)
    assert len(x) == 1
