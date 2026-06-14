# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_3.task_2 import merge_macro_micro

def test_merge_macro_micro():
    micro_df = pd.DataFrame({
        'data': ['2026-06-01', '2026-06-02', '2026-06-03'],
        'cena_akcji': [100.0, 102.5, 101.0]
    })
    macro_df = pd.DataFrame({
        'data': ['2026-06-01', '2026-06-02', '2026-06-04'],
        'stopa_procentowa': [0.05, 0.0525, 0.055]
    })
    
    result = merge_macro_micro(micro_df, macro_df)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3
    assert 'cena_akcji' in result.columns
    assert 'stopa_procentowa' in result.columns
    assert result.loc[result['data'] == '2026-06-01', 'stopa_procentowa'].values[0] == 0.05
    assert pd.isna(result.loc[result['data'] == '2026-06-03', 'stopa_procentowa'].values[0])
