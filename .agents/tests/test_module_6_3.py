# -*- coding: utf-8 -*-
import sys
import os
import pytest
import sqlite3
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_6.task_3 import get_total_sales_by_product

def test_get_total_sales_by_product():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        db_path = tmp.name
        
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("CREATE TABLE sales (product TEXT, quantity INT, price REAL)")
        conn.execute("INSERT INTO sales VALUES ('Chleb', 2, 4.0), ('Mleko', 1, 3.5), ('Chleb', 3, 4.0)")
        conn.commit()
        conn.close()
        
        results = get_total_sales_by_product(db_path)
        
        assert isinstance(results, list)
        assert len(results) == 2
        
        # Słownik dla łatwiejszej asercji
        res_dict = dict(results)
        # Chleb: 2*4.0 + 3*4.0 = 20.0
        # Mleko: 1*3.5 = 3.5
        assert res_dict['Chleb'] == 20.0
        assert res_dict['Mleko'] == 3.5
    finally:
        if os.path.exists(db_path):
            os.remove(db_path)
