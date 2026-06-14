# -*- coding: utf-8 -*-
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_9.task_1 import get_dbnomics_series

def test_get_dbnomics_series_success():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "_meta": {},
        "series": {
            "docs": [
                {"period": "2021", "value": 68.5},
                {"period": "2022", "value": "NA"},
                {"period": "2023", "value": None},
                {"period": "2024", "value": 72.1}
            ]
        }
    }
    
    with patch('requests.get', return_value=mock_response) as mock_get:
        result = get_dbnomics_series("AMECO/UDGG/DEU.1.1.0.0.UDGG")
        assert len(result) == 4
        assert result[0] == {"period": "2021", "value": 68.5}
        assert result[1] == {"period": "2022", "value": None}
        assert result[2] == {"period": "2023", "value": None}
        assert result[3] == {"period": "2024", "value": 72.1}
        mock_get.assert_called_once_with("https://api.dbnomics.world/v22/series/AMECO/UDGG/DEU.1.1.0.0.UDGG?format=json")

def test_get_dbnomics_series_failure():
    with patch('requests.get', side_effect=requests.exceptions.RequestException("Connection error")):
        result = get_dbnomics_series("AMECO/UDGG/DEU.1.1.0.0.UDGG")
        assert result == []
