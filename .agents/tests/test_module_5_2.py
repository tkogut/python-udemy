# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_5.task_2 import calculate_rolling_mean

def test_calculate_rolling_mean():
    df = pd.DataFrame({'price': [10.0, 12.0, 14.0, 16.0]})
    result = calculate_rolling_mean(df, window=2)
    
    assert isinstance(result, pd.Series)
    assert pd.isna(result.iloc[0])
    assert result.iloc[1] == 11.0  # (10 + 12) / 2
    assert result.iloc[2] == 13.0  # (12 + 14) / 2
    assert result.iloc[3] == 15.0  # (14 + 16) / 2
