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
        self.use_close_of_outside_bar = use_close_of_outside_bar
        self.__check_input_values()

    def __check_input_values(self):
        '''
        Ensure that the values supplied to GannSwing() are valid
        '''
        if not isinstance(self.swing_days, int):
            raise ValueError
        if not self.swing_days > 0:
            raise ValueError
        if not isinstance(self.inside_down, bool):
            raise ValueError
        if not (isinstance(self.ignore_threshold, float) or isinstance(self.ignore_threshold, int)):
            raise ValueError
        if isinstance(self.ignore_threshold, bool):
            raise ValueError
        if not self.ignore_threshold >= 0:
            raise ValueError
        if not isinstance(self.use_close_of_outside_bar, bool):
            raise ValueError
        


if __name__ == '__main__':
    gs = GannSwing(bars=pd.DataFrame())