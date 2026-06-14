# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_5.task_1 import filter_by_date

def test_filter_by_date():
    df = pd.DataFrame({
        'data': ['2026-06-01', '2026-06-02', '2026-06-03', '2026-06-04'],
        'price': [10.0, 11.0, 12.0, 13.0]
    })
    
    result = filter_by_date(df, '2026-06-02', '2026-06-03')
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert isinstance(result.index, pd.DatetimeIndex)
    assert list(result['price']) == [11.0, 12.0]
