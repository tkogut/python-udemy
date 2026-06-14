# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import numpy as np
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_4.task_1 import clean_macro_data

def test_clean_macro_data():
    csv_data = """Kraj,PKB_usd,Inflacja
Polska,"$ 26,000",1.5
Niemcy,"$ 45,000",1.2
USA,,2.1
Francja,"$ 38,000",-999.0
,"$ 10,000",0.5
Wielka Brytania,"$ 40,000",1.8
"""
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False, encoding='utf-8') as f:
        f.write(csv_data)
        temp_csv_path = f.name
        
    try:
        df = clean_macro_data(temp_csv_path)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 4
        assert 'USA' not in df['Kraj'].values
        assert df['Kraj'].isna().sum() == 0
        assert pd.api.types.is_float_dtype(df['PKB_usd'])
        
        expected_pkb = {
            'Polska': 26000.0,
            'Niemcy': 45000.0,
            'Francja': 38000.0,
            'Wielka Brytania': 40000.0
        }
        for kraj, expected_val in expected_pkb.items():
            val = df.loc[df['Kraj'] == kraj, 'PKB_usd'].values[0]
            assert val == expected_val
            
        francja_inflation = df.loc[df['Kraj'] == 'Francja', 'Inflacja'].values[0]
        assert abs(francja_inflation - 1.42) < 1e-5
        assert (df['Inflacja'] == -999.0).sum() == 0
    finally:
        if os.path.exists(temp_csv_path):
            os.remove(temp_csv_path)
