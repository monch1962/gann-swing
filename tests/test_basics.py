import pytest
from gannswing import GannSwing
import pandas as pd

@pytest.fixture
def empty_dataframe():
    return pd.DataFrame()

@pytest.fixture
def zero_bars():
    return pd.DataFrame(columns=['Timestamp', 'Open', 'High', 'Low', 'Close'])

def test_class_create_fails_with_no_bars():
    with pytest.raises(TypeError):
        gs = GannSwing()

def test_class_create_success_with_bars():
    bars = pd.DataFrame()
    gs = GannSwing(bars=empty_dataframe)
    assert gs != None

def test_swing_days():
    bars = pd.DataFrame()
    gs = GannSwing(bars=empty_dataframe, swing_days=3)
    assert gs != None