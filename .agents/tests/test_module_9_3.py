# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_9.task_3 import audit_data_quality

def test_audit_data_quality():
    data = {
        "Data": ["2023-01-01", "2023-01-02", "2023-01-03", None],
        "Wartosc": [10.0, -5.0, 15.0, None]
    }
    df = pd.DataFrame(data)
    result = audit_data_quality(df)
    assert result["Completeness"] == 0.75
    assert result["Consistency"] is True
    assert pytest.approx(result["Accuracy"]) == 2 / 3
