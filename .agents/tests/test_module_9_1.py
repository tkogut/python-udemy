# -*- coding: utf-8 -*-
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_9.task_1 import get_nbp_exchange_rate

def test_get_nbp_exchange_rate_success():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "table": "A",
        "currency": "euro",
        "code": "EUR",
        "rates": [{"no": "208/A/NBP/2023", "effectiveDate": "2023-10-25", "mid": 4.5823}]
    }
    
    with patch('requests.get', return_value=mock_response) as mock_get:
        rate = get_nbp_exchange_rate("EUR", "2023-10-25")
        assert rate == 4.5823
        mock_get.assert_called_once_with("http://api.nbp.pl/api/exchangerates/rates/a/EUR/2023-10-25/?format=json")

def test_get_nbp_exchange_rate_failure():
    with patch('requests.get', side_effect=requests.exceptions.HTTPError("404 Client Error")):
        rate = get_nbp_exchange_rate("EUR", "2023-10-25")
        assert rate == -1.0
