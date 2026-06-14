# -*- coding: utf-8 -*-
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from exercises.module_12.task_1 import calculate_sentiment_score

def test_calculate_sentiment_score():
    text = "Wzrost gospodarczy był silny, ale inflacja i ryzyko geopolityczne budzą niepokój."
    pos = ["silny", "wzrost", "dobry"]
    neg = ["ryzyko", "inflacja", "niepokój"]
    
    score = calculate_sentiment_score(text, pos, neg)
    assert pytest.approx(score) == -0.2
