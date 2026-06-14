# -*- coding: utf-8 -*-
import sys
import os
import pytest
from scipy.stats import norm

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_7.task_4 import get_normal_pdf, integrate_normal_density

def test_get_normal_pdf():
    val_0 = get_normal_pdf(0.0)
    assert pytest.approx(val_0, abs=1e-5) == 0.39894
    
    val_1 = get_normal_pdf(1.0)
    assert pytest.approx(val_1, abs=1e-5) == norm.pdf(1.0)

def test_integrate_normal_density():
    # Prawdopodobieństwo w granicach [-1.96, 1.96] dla standardowego rozkładu normalnego wynosi ok. 95%
    p_95 = integrate_normal_density(-1.96, 1.96)
    assert pytest.approx(p_95, abs=1e-2) == 0.95
    
    # Całka w granicach [-1, 1] to ok. 68.27%
    p_68 = integrate_normal_density(-1.0, 1.0)
    assert pytest.approx(p_68, abs=1e-2) == 0.6827
