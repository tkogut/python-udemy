# -*- coding: utf-8 -*-
from numba import jit
import numpy as np

@jit(nopython=True)
def monte_carlo_option_pricing(s0: float, k: float, r: float, sigma: float, t: float, simulations: int) -> float:
    """
    Wycenia opcję call metodą Monte Carlo przy użyciu kompilacji JIT.
    """
    # TWÓJ KOD TUTAJ
    pass
