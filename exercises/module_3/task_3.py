# -*- coding: utf-8 -*-
import pandas as pd

def detect_outliers_zscore(df: pd.DataFrame, column: str, threshold: float = 3.0) -> pd.DataFrame:
    """
    Filtruje wiersze, w których wartość w podanej kolumnie odbiega od średniej
    o więcej niż 'threshold' odchyleń standardowych.
    Zwraca DataFrame zawierający wyłącznie te anomalne wiersze (outliers).
    """
    # TWÓJ KOD TUTAJ
    pass
