# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_7.task_3 import run_t_test

def test_run_t_test():
    sample1 = [10, 12, 11, 9, 13]
    sample2 = [100, 102, 101, 99, 103] # zupełnie różne próbki
    
    t_stat, p_val = run_t_test(sample1, sample2)
    
    assert p_val < 0.05
    assert t_stat != 0.0
