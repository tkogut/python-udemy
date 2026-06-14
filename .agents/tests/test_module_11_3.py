# -*- coding: utf-8 -*-
import sys
import os
import pytest
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_11.task_3 import decompose_macro_series

def test_decompose_macro_series():
    np.random.seed(42)
    t = np.linspace(0, 10, 100)
    trend_true = 2 * t
    cycle_true = np.sin(2 * np.pi * t)
    series = (trend_true + cycle_true).tolist()
    
    trend, cycle = decompose_macro_series(series, 1600.0)
    assert isinstance(trend, list)
    assert isinstance(cycle, list)
    assert len(trend) == 100
    assert len(cycle) == 100
    for i in range(100):
        assert pytest.approx(trend[i] + cycle[i]) == series[i]
