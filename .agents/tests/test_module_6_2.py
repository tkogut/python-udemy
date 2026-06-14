# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import sqlite3
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_6.task_2 import write_to_sql

def test_write_to_sql():
    df = pd.DataFrame({'id': [10, 20], 'name': ['X', 'Y']})
    
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        db_path = tmp.name
        
    try:
        write_to_sql(df, db_path, "target_table")
        
        conn = sqlite3.connect(db_path)
        res = conn.execute("SELECT * FROM target_table").fetchall()
        conn.close()
        
        assert len(res) == 2
        assert res[0] == (10, 'X')
        assert res[1] == (20, 'Y')
    finally:
        if os.path.exists(db_path):
            os.remove(db_path)
