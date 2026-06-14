# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from exercises.module_4.task_2 import delegate_to_subagent

def test_delegate_to_subagent():
    assert delegate_to_subagent("Potrzebuję analizy PKB") == "Delegowano do: Agent Statystyczny"
    assert delegate_to_subagent("Zrób wykres stóp zwrotu") == "Delegowano do: Agent Wizualizacji"
    assert delegate_to_subagent("Jaka jest dzisiejsza inflacja?") == "Delegowano do: General Agent"
    # Case insensitivity test
    assert delegate_to_subagent("WIZUALIZACJA DANYCH") == "Delegowano do: Agent Wizualizacji"
