# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_12.task_2 import estimate_causal_effect

def test_estimate_causal_effect():
    np.random.seed(42)
    n = 200
    W = np.random.normal(0, 1, n)
    p_T = 1 / (1 + np.exp(-W))
    T = np.random.binomial(1, p_T)
    Y = 3.0 * T + 2.0 * W + np.random.normal(0, 0.05, n)
    
    df = pd.DataFrame({'T': T, 'W': W, 'Y': Y})
    
    effect = estimate_causal_effect(df)
    assert isinstance(effect, float)
    assert pytest.approx(effect, abs=0.25) == 3.0
