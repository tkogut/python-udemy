# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_4.task_3 import detect_outliers_zscore

def test_detect_outliers_zscore():
    data = [9.5, 10.2, 9.8, 10.5, 9.9, 10.1, 100.0]
    df = pd.DataFrame({'inflacja': data})
    outliers = detect_outliers_zscore(df, 'inflacja', threshold=2.0)
    
    assert isinstance(outliers, pd.DataFrame)
    assert len(outliers) == 1
    assert outliers['inflacja'].values[0] == 100.0
