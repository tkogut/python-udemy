# -*- coding: utf-8 -*-
import sys
import os
import pytest
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_8.task_3 import build_economic_report

def test_build_economic_report():
    data = {
        'tytul': 'Raport Inflacyjny',
        'autor': 'Antigravity',
        'wynik': 'Wzrost o 2.5%'
    }
    
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
        filepath = tmp.name
        
    try:
        build_economic_report(data, filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        expected = "Raport: Raport Inflacyjny\nAutor: Antigravity\nWynik: Wzrost o 2.5%"
        assert content.strip() == expected.strip()
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
