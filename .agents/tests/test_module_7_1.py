# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_7.task_1 import get_correlations

def test_get_correlations():
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1], # ujemna korelacja (-1)
        'C': [1, 2, 1, 2, 1]
    })
    
    result = get_correlations(df)
    
    assert isinstance(result, pd.DataFrame)
    assert result.loc['A', 'A'] == 1.0
    assert abs(result.loc['A', 'B'] - (-1.0)) < 1e-6
