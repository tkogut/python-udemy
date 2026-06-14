# -*- coding: utf-8 -*-
import sys
import os
import pytest
import duckdb

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_10.task_2 import duckdb_query_and_regression

def test_duckdb_query_and_regression():
    db_path = "test_duck.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        
    con = duckdb.connect(db_path)
    con.execute("CREATE TABLE ekonomia (X DOUBLE, Y DOUBLE)")
    # Y = 2 * X + 5
    con.execute("INSERT INTO ekonomia VALUES (1, 7), (2, 9), (3, 11), (4, 13)")
    con.close()
    
    try:
        slope, intercept = duckdb_query_and_regression(db_path)
        assert pytest.approx(slope) == 2.0
        assert pytest.approx(intercept) == 5.0
    finally:
        if os.path.exists(db_path):
            os.remove(db_path)
