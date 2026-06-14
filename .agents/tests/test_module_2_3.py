# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_2.task_3 import aggregate_portfolio

def test_aggregate_portfolio():
    portfolio = pd.DataFrame({
        'aktywo': ['Akcje A', 'Akcje B', 'Obligacje A', 'Obligacje B'],
        'sektor': ['Finanse', 'Technologia', 'Finanse', 'Technologia'],
        'wartosc': [1000, 2000, 1500, 500],
        'stopa_zwrotu': [0.05, 0.12, 0.02, 0.04]
    })
    
    result = aggregate_portfolio(portfolio)
    
    assert isinstance(result, pd.DataFrame)
    # Powinny być dwa sektory w indeksie/kolumnie
    assert len(result) == 2
    assert 'wartosc' in result.columns
    assert 'stopa_zwrotu' in result.columns
    
    # Finanse sum: 1000 + 1500 = 2500, mean: (0.05 + 0.02) / 2 = 0.035
    assert result.loc['Finanse', 'wartosc'] == 2500
    assert abs(result.loc['Finanse', 'stopa_zwrotu'] - 0.035) < 1e-6
    
    # Technologia sum: 2000 + 500 = 2500, mean: (0.12 + 0.04) / 2 = 0.08
    assert result.loc['Technologia', 'wartosc'] == 2500
    assert abs(result.loc['Technologia', 'stopa_zwrotu'] - 0.08) < 1e-6
