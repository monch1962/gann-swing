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

def test_bars_column_names_exist():
    '''
    Ensure any missing column in 'bars' is detected and returns an error
    '''
    import itertools

    # Start with a list of all the mandatory columns
    mandatory_columns = ['Timestamp', 'Open', 'High', 'Low', 'Close']

    # Now generate every possible subset of mandatory_columns, except the one that contains all columns...
    for column_count in range(0, len(mandatory_columns)):
        for subset_of_mandatory_columns in itertools.combinations(mandatory_columns, column_count):
            # Every one of these subsets of mandatory_columns should generate an error
            with pytest.raises(IndexError):
                gs = GannSwing(bars = pd.DataFrame(columns = subset_of_mandatory_columns))
