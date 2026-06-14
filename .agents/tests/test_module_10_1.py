# -*- coding: utf-8 -*-
import sys
import os
import pytest
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_10.task_1 import aggregate_with_polars

def test_aggregate_with_polars():
    content = "Kategoria,Wynik\nA,10.0\nB,20.0\nA,30.0\nB,40.0\n"
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False, mode='w', encoding='utf-8') as tmp:
        tmp.write(content)
        csv_path = tmp.name
        
    try:
        res = aggregate_with_polars(csv_path)
        assert isinstance(res, dict)
        assert pytest.approx(res["A"]) == 20.0
        assert pytest.approx(res["B"]) == 30.0
    finally:
        if os.path.exists(csv_path):
            os.remove(csv_path)
