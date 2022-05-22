import pandas as pd
import numpy as np
from enum import Enum, auto

class GannSwing():
    '''
    Class to perform Gann swing calculations
    '''
    def __init__(self, bars: pd.DataFrame):
        '''
        Parameters:
        - (required) a pandas dataframe containing OHLC data
        - (optional) the number of days required to trigger a swing
        - (optional) should an inside day in a down trend trigger a swing?
        - (optional) what is a small enough swing to ignore
        - (optional) use the close of an outside bar to decide the swing direction
        '''
        self.bars = bars
        #self.swing_days = swing_days
        #self.inside_down = inside_down
        #self.ignore_threshold = ignore_threshold
        #self.use_close_of_outside_bar = use_close_of_outside_bar
        #self.__parameter_validation()

    def __parameter_validation(self):
        '''
        Ensure that the values supplied to GannSwing() are valid
        '''
        if not isinstance(self.swing_days, int):
            raise TypeError
        if not self.swing_days > 0:
            raise ValueError('swing_days should be a positive integer')
        if not isinstance(self.inside_down, bool):
            raise TypeError('inside_down should be a boolean')
        if not (isinstance(self.ignore_threshold, float) or isinstance(self.ignore_threshold, int)):
            raise TypeError('ignore_threshold should be a float or int')
        if isinstance(self.ignore_threshold, bool):
            raise TypeError('ignore_threshold should not be a boolean')
        if not self.ignore_threshold >= 0:
            raise ValueError('ignore_threshold should be a positive value')
        if not isinstance(self.use_close_of_outside_bar, bool):
            raise TypeError('use_close_of_outside_bar should be a boolean')
        if not isinstance(self.bars, pd.DataFrame):
            raise TypeError('bars should be a Pandas dataframe')
        

    class Trend(Enum):
        UNKNOWN = np.nan
        UP = 'Up'
        DOWN = 'Down'

    def calculate(self, swing_days: int=1, inside_down: bool=False, ignore_threshold: int=0, use_close_of_outside_bar: bool=False) -> pd.DataFrame:
        self.swing_days = swing_days
        self.inside_down = inside_down
        self.ignore_threshold = ignore_threshold
        self.use_close_of_outside_bar = use_close_of_outside_bar
        self.__parameter_validation()
        return pd.DataFrame(columns = ['Timestamp', 'SwingStartDate', 'SwingStartPrice', 'SwingEndDate', 'SwingEndPrice', 'TradeableRange', 'Trend'])

    def __up_day(self, bar):
        '''
        Return True if bar is an up day, else False
        '''
        this_bar = self.swing_days.loc(bar)
        try:
            previous_bar = self.swing_days.loc(bar-1)
            if this_bar['Low'] >= previous_bar['Low'] and this_bar['High'] > previous_bar['High']:
                return True
        except:
            pass
        return False

    def __down_day(self, bar):
        this_bar = self.swing_days.loc(bar)
        try:
            previous_bar = self.swing_days.loc(bar-1)
            if this_bar['Low'] < previous_bar['Low'] and this_bar['High'] <= previous_bar['High']:
                return True
        except:
            pass
        return False

    def __inside_day(self, bar):
        this_bar = self.swing_days.loc(bar)
        try:
            previous_bar = self.swing_days.loc(bar-1)
            if this_bar['Low'] >= previous_bar['Low'] and this_bar['High'] <= previous_bar['High']:
                return True
        except:
            pass
        return False

    def __outside_day(self, bar):
        this_bar = self.swing_days.loc(bar)
        try:
            previous_bar = self.swing_days.loc(bar-1)
            if this_bar['Low'] < previous_bar['Low'] and this_bar['High'] > previous_bar['High']:
                return True
        except:
            pass
        return False

    def __find_turns(self, swing_days):
        for i in range(swing_days+1, len(self.bars)):
            for j in range(1, swing_days):
                if self.__down_day(i-j) and self.__up_day(i+j):
                    continue
        pass



if __name__ == '__main__':
    gs = GannSwing(bars=pd.DataFrame())