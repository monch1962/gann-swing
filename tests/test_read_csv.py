import pytest
from gannswing import GannSwing
import pandas as pd

@pytest.fixture
def csv_with_extra_headers():
    return "./tests/data/apple-YYYY-MM-DD.csv"

def test_read_csv_with_headers(csv_with_extra_headers):
    '''
    Confirm we can handle a CSV data file that contains extra headers
    '''
    bars = pd.read_csv(csv_with_extra_headers)
    gs = GannSwing(bars=bars)
    assert gs != None
