# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_1.task_2 import calculate_gdp

def test_calculate_gdp():
    assert calculate_gdp(1000.0, 200.0, 300.0, 150.0, 100.0) == 1550.0
    assert calculate_gdp(800.5, 150.0, 250.0, 50.0, 80.0) == 1170.5
    assert calculate_gdp(0.0, 0.0, 0.0, 0.0, 0.0) == 0.0
