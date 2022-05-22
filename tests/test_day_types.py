import pytest
from gannswing import GannSwing
import numpy as np
import pandas as pd

@pytest.fixture
def gs():
    '''
    We're going to set up a set of bars to test each day type
    '''
    data = [
        [np.nan, np.nan, 5, 1, np.nan],
        [np.nan, np.nan, 6, 2, np.nan], # bar 1 = Up bar vs previous bar
        [np.nan, np.nan, 5, 1, np.nan], # bar 2 = Down bar vs previous bar
        [np.nan, np.nan, 4, 2, np.nan], # bar 3 = Inside bar vs previous bar
        [np.nan, np.nan, 5, 1, np.nan], # bar 4 = Outside bar vs previous bar
        [np.nan, np.nan, 5, 1, np.nan] # bar 5 = Inside day (same as previous bar) vs previous bar
    ]
    bars = pd.DataFrame(data, columns=['Timestamp', 'Open', 'High', 'Low', 'Close'])
    gs = GannSwing(bars=bars)
    return gs

def test_up_day(gs):
    assert gs._up_day(bar=1)
    assert not gs._up_day(bar=2)
    assert not gs._up_day(bar=3)
    assert not gs._up_day(bar=4)
    assert not gs._up_day(bar=5)


def test_down_day(gs):
    assert not gs._down_day(bar=1)
    assert gs._down_day(bar=2)
    assert not gs._down_day(bar=3)
    assert not gs._down_day(bar=4)
    assert not gs._down_day(bar=5)

def test_inside_day(gs):
    assert not gs._inside_day(bar=1)
    assert not gs._inside_day(bar=2)
    assert gs._inside_day(bar=3)
    assert not gs._inside_day(bar=4)
    assert gs._inside_day(bar=5)

def test_outside_day(gs):
    assert not gs._outside_day(bar=1)
    assert not gs._outside_day(bar=2)
    assert not gs._outside_day(bar=3)
    assert gs._outside_day(bar=4)
    assert not gs._outside_day(bar=5)