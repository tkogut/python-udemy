# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_9.task_2 import parse_fred_vintage

def test_parse_fred_vintage():
    vintage_data = {
        "2023-01-01": {
            "2023-01-15": 1.2,
            "2023-02-15": 1.3,
            "2023-03-15": 1.25
        }
    }
    # Publikacja przed lub równo z 2023-01-14 (brak)
    val1 = parse_fred_vintage(vintage_data, "2023-01-01", "2023-01-14")
    assert val1 is None
    
    # Publikacja przed lub równo z 2023-01-16 (jest 1.2)
    val2 = parse_fred_vintage(vintage_data, "2023-01-01", "2023-01-16")
    assert val2 == 1.2
    
    # Publikacja przed lub równo z 2023-02-28 (najnowsza do tej daty to 1.3 opublikowana 2023-02-15)
    val3 = parse_fred_vintage(vintage_data, "2023-01-01", "2023-02-28")
    assert val3 == 1.3
    
    # Publikacja przed lub równo z 2023-04-01 (najnowsza to 1.25 opublikowana 2023-03-15)
    val4 = parse_fred_vintage(vintage_data, "2023-01-01", "2023-04-01")
    assert val4 == 1.25
