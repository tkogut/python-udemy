# -*- coding: utf-8 -*-
import sys
import os
import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_11.task_2 import fit_garch_model

def test_fit_garch_model():
    np.random.seed(42)
    returns = np.random.normal(0, 0.02, 500).tolist()
    
    omega, alpha, beta = fit_garch_model(returns)
    assert isinstance(omega, float)
    assert isinstance(alpha, float)
    assert isinstance(beta, float)
    assert omega > 0
    assert alpha >= 0
    assert beta >= 0
