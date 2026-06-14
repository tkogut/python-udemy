# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_7.task_2 import run_regression

def test_run_regression():
    df = pd.DataFrame({
        'y': [2.0, 4.0, 6.0, 8.0, 10.0],
        'x': [1.0, 2.0, 3.0, 4.0, 5.0] # y = 2x (dokładnie dopasowany model)
    })
    
    r2, pvalues = run_regression(df, 'y', 'x')
    
    assert abs(r2 - 1.0) < 1e-6
    # wyraz wolny (const) oraz x powinny mieć p-value bliskie zero (lub małe)
    assert 'const' in pvalues.index
    assert 'x' in pvalues.index
