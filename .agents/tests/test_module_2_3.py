# -*- coding: utf-8 -*-
import sys
import os
import pytest
import json
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_2.task_3 import serialize_and_save

def test_serialize_and_save():
    data = {"PKB": 1500, "Kraj": "Polska"}
    
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        filepath = tmp.name
        
    try:
        serialize_and_save(data, filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            loaded = json.load(f)
        assert loaded == data
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
