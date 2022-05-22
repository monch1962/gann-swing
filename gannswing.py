import pandas as pd
import numpy as np

class GannSwing():
    '''
    Class to perform Gann swing calculations
    '''
    def __init__(self, bars, swing_days=1, inside_down=False, ignore_threshold=0, use_close_of_outside_bar=False):
        '''
        Parameters:
        - (required) a pandas dataframe containing OHLC data
        - (optional) the number of days required to trigger a swing
        - (optional) should an inside day in a down trend trigger a swing?
        - (optional) what is a small enough swing to ignore
        - (optional) use the close of an outside bar to decide the swing direction
        '''
        self.swing_days = swing_days
        self.inside_down = inside_down
        self.ignore_threshold = ignore_threshold

if __name__ == '__main__':
    gs = GannSwing(bars=pd.DataFrame())