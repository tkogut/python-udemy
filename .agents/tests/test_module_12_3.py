# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_12.task_3 import run_research_pipeline

def test_run_research_pipeline():
    raw_content = "ID,Wartosc\n1,10.0\n2,-5.0\n3,15.0\n"
    
    with tempfile.NamedTemporaryFile(suffix="_raw.csv", delete=False, mode='w', encoding='utf-8') as tmp_raw:
        tmp_raw.write(raw_content)
        raw_path = tmp_raw.name
        
    with tempfile.NamedTemporaryFile(suffix="_clean.csv", delete=False) as tmp_clean:
        clean_path = tmp_clean.name
        
    try:
        success = run_research_pipeline(raw_path, clean_path)
        assert success is True
        
        df_clean = pd.read_csv(clean_path)
        assert len(df_clean) == 2
        assert (df_clean["Wartosc"] >= 0).all()
        assert list(df_clean["ID"]) == [1, 3]
    finally:
        if os.path.exists(raw_path):
            os.remove(raw_path)
        if os.path.exists(clean_path):
            os.remove(clean_path)
