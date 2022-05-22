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

def test_swing_days():
    gs = GannSwing(bars=zero_bars(), swing_days=3)
    assert gs != None

def test_swing_days_non_integer():
    with pytest.raises(TypeError):
        gs = GannSwing(bars=zero_bars(), swing_days=3.5)

def test_swing_days_negative_integer():
    with pytest.raises(ValueError):
        gs = GannSwing(bars=zero_bars(), swing_days=-1)

def test_inside_down_should_be_bool():
    gs = GannSwing(bars=zero_bars(), inside_down=True)
    assert gs != None
    gs = GannSwing(bars=zero_bars(), inside_down=False)
    assert gs != None

def test_inside_down_should_not_be_int():
    with pytest.raises(TypeError):
        gs = GannSwing(bars=zero_bars(), inside_down=1)

def test_inside_down_should_not_be_string():
    with pytest.raises(TypeError):
        gs = GannSwing(bars=zero_bars(), inside_down='abc')

def test_inside_down_should_not_be_negative_float():
    with pytest.raises(TypeError):
        gs = GannSwing(bars=zero_bars(), inside_down=-4.9)

def test_ignore_threshold_should_not_be_negative():
    with pytest.raises(ValueError):
        gs = GannSwing(bars=zero_bars(), ignore_threshold=-1)

def test_ignore_threshold_should_not_be_string():
    with pytest.raises(TypeError):
        gs = GannSwing(bars=zero_bars(), ignore_threshold='abc')

def test_ignore_threshold_should_not_be_bool():
    with pytest.raises(TypeError):
        gs = GannSwing(bars=zero_bars(), ignore_threshold=True)

def test_use_close_of_outside_bar_should_be_bool():
    gs = GannSwing(bars=zero_bars(), use_close_of_outside_bar=True)
    assert gs != None

def test_use_close_of_outside_bar_should_not_be_integer():
    with pytest.raises(TypeError):
        gs = GannSwing(bars=zero_bars(), use_close_of_outside_bar=1)