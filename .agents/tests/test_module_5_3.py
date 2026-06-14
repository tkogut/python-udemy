# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_5.task_3 import resample_to_monthly

def test_resample_to_monthly():
    # Dane dzienne dla dwóch miesięcy
    dates = pd.date_range(start='2026-01-01', end='2026-02-28', freq='D')
    df = pd.DataFrame({'price': [10.0] * len(dates)}, index=dates)
    
    result = resample_to_monthly(df)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2  # Styczeń i Luty
    assert result.index[0].month == 1
    assert result.index[1].month == 2
    assert result['price'].iloc[0] == 10.0
