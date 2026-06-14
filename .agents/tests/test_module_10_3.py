# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_10.task_3 import monte_carlo_option_pricing

def test_monte_carlo_option_pricing():
    assert hasattr(monte_carlo_option_pricing, "py_func")
    
    price = monte_carlo_option_pricing(100.0, 100.0, 0.05, 0.2, 1.0, 1000)
    assert isinstance(price, float)
    assert price > 0.0
    assert 5.0 < price < 15.0
