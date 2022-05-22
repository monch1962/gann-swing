import pytest
from gannswing import GannSwing
import pandas as pd


#@pytest.fixture
def empty_dataframe():
    return pd.DataFrame()

#@pytest.fixture
def zero_bars():
    return pd.DataFrame(columns=['Timestamp', 'Open', 'High', 'Low', 'Close'])

def test_swing_days():
    gs = GannSwing(bars=zero_bars())
    gs.calculate(swing_days=3)
    assert gs != None

def test_swing_days_non_integer():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(TypeError):
        gs.calculate(swing_days=3.5)

def test_swing_days_negative_integer():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(ValueError):
        gs.calculate(swing_days=-1)

def test_inside_down_should_be_bool():
    gs = GannSwing(bars=zero_bars())
    assert isinstance(gs.calculate(inside_down=True), pd.DataFrame)
    gs = GannSwing(bars=zero_bars())
    assert isinstance(gs.calculate(inside_down=False), pd.DataFrame)

def test_inside_down_should_not_be_int():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(TypeError):
        gs.calculate(inside_down=1)

def test_inside_down_should_not_be_string():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(TypeError):
        gs.calculate(inside_down='abc')

def test_inside_down_should_not_be_negative_float():
    gs = GannSwing(bars=zero_bars())    
    with pytest.raises(TypeError):
        gs.calculate(inside_down=-4.9)

def test_ignore_threshold_should_not_be_negative():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(ValueError):
        gs.calculate(ignore_threshold=-1)

def test_ignore_threshold_should_not_be_string():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(TypeError):
        gs.calculate(ignore_threshold='abc')

def test_ignore_threshold_should_not_be_bool():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(TypeError):
        gs.calculate(ignore_threshold=True)

def test_use_close_of_outside_bar_should_be_bool():
    gs = GannSwing(bars=zero_bars())
    assert isinstance(gs.calculate(use_close_of_outside_bar=True),pd.DataFrame)

def test_use_close_of_outside_bar_should_not_be_integer():
    gs = GannSwing(bars=zero_bars())
    with pytest.raises(TypeError):
        gs.calculate(use_close_of_outside_bar=1)