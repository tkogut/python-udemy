# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_3.task_1 import analyze_stock_returns

def test_analyze_stock_returns():
    prices = [100.0, 105.0, 102.0, 108.0]
    df, mean_ret, vol = analyze_stock_returns(prices)
    
    assert isinstance(df, pd.DataFrame)
    assert 'price' in df.columns
    assert 'simple_return' in df.columns
    assert 'log_return' in df.columns
    
    assert len(df) == 4
    assert list(df['price']) == prices
    assert pd.isna(df['simple_return'].iloc[0])
    assert pd.isna(df['log_return'].iloc[0])
    
    expected_simple = [np.nan, 0.05, (102.0 - 105.0) / 105.0, (108.0 - 102.0) / 102.0]
    np.testing.assert_allclose(df['simple_return'].fillna(-999).values[1:], expected_simple[1:], rtol=1e-5)
    
    expected_log = [np.nan, np.log(105.0 / 100.0), np.log(102.0 / 105.0), np.log(108.0 / 102.0)]
    np.testing.assert_allclose(df['log_return'].fillna(-999).values[1:], expected_log[1:], rtol=1e-5)
    
    valid_simple = df['simple_return'].dropna()
    assert abs(mean_ret - valid_simple.mean()) < 1e-6
    assert abs(vol - valid_simple.std()) < 1e-6
