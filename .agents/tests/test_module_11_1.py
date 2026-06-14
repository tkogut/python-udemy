# -*- coding: utf-8 -*-
import sys
import os
import pytest
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_11.task_1 import estimate_panel_ols

def test_estimate_panel_ols():
    entities = ["Firma_A", "Firma_B", "Firma_C"]
    years = [2020, 2021, 2022, 2023, 2024]
    
    index = pd.MultiIndex.from_product([entities, years], names=["entity", "time"])
    df = pd.DataFrame(index=index)
    
    np.random.seed(42)
    df["X"] = np.random.randn(len(df))
    eff = {"Firma_A": 5.0, "Firma_B": 10.0, "Firma_C": -3.0}
    df["eff"] = [eff[ent] for ent, yr in df.index]
    df["Y"] = 2.5 * df["X"] + df["eff"] + np.random.randn(len(df)) * 0.05
    
    coeff = estimate_panel_ols(df)
    assert isinstance(coeff, float)
    assert pytest.approx(coeff, abs=0.1) == 2.5
