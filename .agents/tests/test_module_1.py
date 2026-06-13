# -*- coding: utf-8 -*-
import sys
import os
import pytest

# Dodaj główny katalog do ścieżki wyszukiwania modułów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_1.task_1 import calculate_fv, calculate_pv, calculate_npv

def test_calculate_fv():
    assert round(calculate_fv(1000, 0.05, 5), 2) == 1276.28
    assert round(calculate_fv(100, 0.10, 1), 2) == 110.00
    assert round(calculate_fv(500, 0.0, 10), 2) == 500.00

def test_calculate_pv():
    assert round(calculate_pv(1276.28, 0.05, 5), 2) == 1000.00
    assert round(calculate_pv(110, 0.10, 1), 2) == 100.00
    assert round(calculate_pv(500, 0.0, 10), 2) == 500.00

def test_calculate_npv():
    cash_flows = [-1000, 300, 400, 500]
    r = 0.08
    expected_npv = -1000 + (300 / 1.08**1) + (400 / 1.08**2) + (500 / 1.08**3)
    assert abs(calculate_npv(cash_flows, r) - expected_npv) < 1e-2
    
    # Próg rentowności / zero stopa dyskontowa
    assert calculate_npv([-1000, 500, 500], 0.0) == 0.0
