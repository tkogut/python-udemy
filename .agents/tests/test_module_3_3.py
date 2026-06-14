# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_3.task_3 import aggregate_portfolio

def test_aggregate_portfolio():
    portfolio = pd.DataFrame({
        'aktywo': ['Akcje A', 'Akcje B', 'Obligacje A', 'Obligacje B'],
        'sektor': ['Finanse', 'Technologia', 'Finanse', 'Technologia'],
        'wartosc': [1000, 2000, 1500, 500],
        'stopa_zwrotu': [0.05, 0.12, 0.02, 0.04]
    })
    
    result = aggregate_portfolio(portfolio)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert 'wartosc' in result.columns
    assert 'stopa_zwrotu' in result.columns
    assert result.loc['Finanse', 'wartosc'] == 2500
    assert abs(result.loc['Finanse', 'stopa_zwrotu'] - 0.035) < 1e-6
    assert result.loc['Technologia', 'wartosc'] == 2500
    assert abs(result.loc['Technologia', 'stopa_zwrotu'] - 0.08) < 1e-6
