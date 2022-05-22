import pytest
from gannswing import GannSwing
import pandas as pd

#@pytest.fixture
def empty_dataframe():
    return pd.DataFrame()

#@pytest.fixture
def zero_bars():
    return pd.DataFrame(columns=['Timestamp', 'Open', 'High', 'Low', 'Close'])

def test_class_create_fails_with_no_bars():
    with pytest.raises(TypeError):
        gs = GannSwing()

def test_class_create_success_with_bars():
    gs = GannSwing(bars=zero_bars())
    assert gs != None

