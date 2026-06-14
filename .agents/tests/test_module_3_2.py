# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_3.task_2 import impute_missing_gdp

def test_impute_missing_gdp():
    df = pd.DataFrame({
        'Kraj': ['Polska', 'Niemcy', 'Czechy', 'Chiny', 'Japonia', 'Indie'],
        'kontynent': ['Europa', 'Europa', 'Europa', 'Azja', 'Azja', 'Azja'],
        'PKB': [100.0, 200.0, np.nan, 300.0, np.nan, 500.0]
    })
    
    result = impute_missing_gdp(df)
    
    assert isinstance(result, pd.DataFrame)
    # Brakujące Czechy powinny mieć średnią Europy: (100 + 200)/2 = 150
    czechy_gdp = result.loc[result['Kraj'] == 'Czechy', 'PKB'].values[0]
    assert czechy_gdp == 150.0
    
    # Brakująca Japonia powinna mieć średnią Azji: (300 + 500)/2 = 400
    japonia_gdp = result.loc[result['Kraj'] == 'Japonia', 'PKB'].values[0]
    assert japonia_gdp == 400.0
    
    # Brak NaN w kolumnie PKB
    assert result['PKB'].isna().sum() == 0
