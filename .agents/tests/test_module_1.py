# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_1.task_1 import hello_world, get_gdp_value

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_get_gdp_value():
    val = get_gdp_value()
    assert val == 1500.0
    assert isinstance(val, float)
