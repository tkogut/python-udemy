# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_2.task_1 import classify_income

def test_classify_income():
    assert classify_income(20000) == "Niski"
    assert classify_income(30000) == "Średni"
    assert classify_income(50000) == "Średni"
    assert classify_income(85000) == "Wysoki"
    assert classify_income(100000) == "Wysoki"
