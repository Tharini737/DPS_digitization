import pytest
from model.prediction import data_prep, predictions
import pandas as pd

# Intergration tests for the functions

raw_data = r"data/raw_data.csv"

def test_data_prep_to_prediction():
    prepared_data = data_prep(raw_data)
    category = 'Alkoholunfälle'
    accident_type = 'insgesamt'
    year = 2021
    month = 1
    prediction_result = predictions(category, accident_type, year, month, prepared_data)
    assert prediction_result is not None
   
