import pytest
from gannswing import GannSwing
import numpy as np
import pandas as pd

@pytest.fixture
def gs():
    '''
    We're going to set up a set of bars to test each type of swing
    '''
    data = [
        [0, np.nan, 5, 1, np.nan],
        [1, np.nan, 6, 2, np.nan], # bar 1 = Up bar vs previous bar
        [2, np.nan, 5, 1, np.nan], # bar 2 = Down bar vs previous bar
        [3, np.nan, 4, 2, np.nan], # bar 3 = Inside bar vs previous bar
        [4, np.nan, 5, 1, np.nan], # bar 4 = Outside bar vs previous bar
        [5, np.nan, 5, 1, np.nan] # bar 5 = Inside day (same as previous bar) vs previous bar
    ]
    bars = pd.DataFrame(data, columns=['Timestamp', 'Open', 'High', 'Low', 'Close'])
    gs = GannSwing(bars=bars)
    return gs

@pytest.fixture
def expected_swing_column_names():
    return ['Timestamp', 'SwingStartDate', 'SwingStartPrice', 'SwingEndDate', 'SwingEndPrice', 'TradeableRange', 'Trend']


def test_swing_column_names_are_correct(gs, expected_swing_column_names):
    '''
    Check that the set of columns returned by the calculate() function is correct
    '''
    expected = expected_swing_column_names.sort()
    actual_column_names = gs.calculate().columns.values.tolist().sort()
    # Now we've sorted expected... and actual..., they're easy to compare
    assert expected == actual_column_names

def test_1_day_swing_timestamps(gs):
    '''
    Check that the correct set of 1 day swings are detected
    '''
    swings_found = gs.calculate(swing_days=1)
    correct_swings = [1, 4, 17] # These are the swing timestamps that should be detected

    # First confirm that the number of swings we found is correct
    assert len(swings_found) == len(correct_swings) 

    # Now check each swing that gets returned
    for i in range(0, len(swings_found)-1):
        if i in correct_swings:
            # We should have a swing returned for this timestamp
            assert swings.loc[i]['Timestamp'] == i
        else:
            # We shouldn't have a swing returned for this timestamp
            assert not swings.loc[i]['Timestamp'] == i