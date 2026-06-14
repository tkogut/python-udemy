# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import sqlite3
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_6.task_1 import read_sql_data

def test_read_sql_data():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        db_path = tmp.name
        
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("CREATE TABLE test_table (id INT, val TEXT)")
        conn.execute("INSERT INTO test_table VALUES (1, 'A'), (2, 'B')")
        conn.commit()
        conn.close()
        
        df = read_sql_data(db_path, "SELECT * FROM test_table")
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 2
        assert list(df['val']) == ['A', 'B']
    finally:
        if os.path.exists(db_path):
            os.remove(db_path)
