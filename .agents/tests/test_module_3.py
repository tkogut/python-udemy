# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import numpy as np
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_3.task_1 import clean_macro_data

def test_clean_macro_data():
    # Tworzenie testowego pliku CSV z poprawnie ocytowanymi polami z przecinkami
    csv_data = """Kraj,PKB_usd,Inflacja
Polska,"$ 26,000",1.5
Niemcy,"$ 45,000",1.2
USA,,2.1
Francja,"$ 38,000",-999.0
,"$ 10,000",0.5
Wielka Brytania,"$ 40,000",1.8
"""
    
    # Używamy tempfile do zapisu pliku CSV
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False, encoding='utf-8') as f:
        f.write(csv_data)
        temp_csv_path = f.name
        
    try:
        df = clean_macro_data(temp_csv_path)
        
        # Sprawdzamy typ zwracanego obiektu
        assert isinstance(df, pd.DataFrame)
        
        # Sprawdzamy wymiary
        # Oczekiwane kraje: Polska, Niemcy, Francja, Wielka Brytania
        assert len(df) == 4
        
        # Sprawdzamy, czy wiersze z brakującymi 'Kraj' lub 'PKB_usd' zostały usunięte
        assert 'USA' not in df['Kraj'].values
        assert df['Kraj'].isna().sum() == 0
        
        # Sprawdzamy oczyszczenie kolumny PKB_usd (powinny być typem float)
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
            
        # Sprawdzamy poprawność uzupełnienia braków inflacji
        # Średnia z ważnych wartości inflacji przed czyszczeniem wierszy (1.5, 1.2, 2.1, 0.5, 1.8) wynosi 1.42
        francja_inflation = df.loc[df['Kraj'] == 'Francja', 'Inflacja'].values[0]
        assert abs(francja_inflation - 1.42) < 1e-5
        
        # Upewnijmy się, że nie ma już żadnych wartości -999.0 w ramce
        assert (df['Inflacja'] == -999.0).sum() == 0
        
    finally:
        # Usuwamy plik tymczasowy
        if os.path.exists(temp_csv_path):
            os.remove(temp_csv_path)
