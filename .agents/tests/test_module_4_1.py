# -*- coding: utf-8 -*-
import sys
import os
import pytest
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_4.task_1 import schedule_data_check

def test_schedule_data_check():
    counter = 0
    def dummy_check():
        nonlocal counter
        counter += 1
        return f"run_{counter}"
        
    start_time = time.time()
    results = schedule_data_check(dummy_check, interval_sec=1, max_iterations=3)
    duration = time.time() - start_time
    
    assert results == ["run_1", "run_2", "run_3"]
    # Powinno zająć co najmniej 2 sekundy (opóźnienie między 1-2 i 2-3)
    assert duration >= 1.9
    assert counter == 3
