import pytest
from gannswing import GannSwing
import pandas as pd

def test_ticksize():
    bars = pd.read_csv('./tests/data/cba-optuma.csv', delimiter='\t', usecols=['Date', 'Open', 'High', 'Low', 'Close'])
    bars.rename(columns={'Date': 'Timestamp'}, inplace=True)
    gs = GannSwing(bars=bars)
    assert gs.ticksize() == 0.01