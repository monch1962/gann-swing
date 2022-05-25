import pandas as pd
import numpy as np
from enum import Enum, auto

class GannSwing():
    '''
    Class to perform Gann swing calculations
    '''
    def __init__(self, bars:pd.DataFrame):
        '''
        Parameters:
        - (required) a pandas dataframe containing OHLC data
        - (optional) the number of days required to trigger a swing
        - (optional) should an inside day in a down trend trigger a swing?
        - (optional) what is a small enough swing to ignore
        - (optional) use the close of an outside bar to decide the swing direction
        '''
        self.bars = bars
        self.__validate_bars(bars)
        #self.swing_days = swing_days
        #self.inside_down = inside_down
        #self.ignore_threshold = ignore_threshold
        #self.use_close_of_outside_bar = use_close_of_outside_bar
        #self.__parameter_validation()

    def __validate_bars(self, bars):
        if not isinstance(self.bars, pd.DataFrame):
            raise TypeError('bars should be a Pandas dataframe')
        mandatory_columns = ['Timestamp', 'Open', 'High', 'Low', 'Close']
        columns = list(bars.columns)
        for i in mandatory_columns:
            if i not in columns:
                raise IndexError('bars is missing a column named "%s"' % i)
        

    def __parameter_validation(self):
        '''
        Ensure that the values supplied to GannSwing() are valid
        '''
        if not isinstance(self.swing_days, int):
            raise TypeError('swing_days should be an integer')
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

        

    class Trend(Enum):
        UNKNOWN = np.nan
        UP = 'Up'
        DOWN = 'Down'

    def calculate(self, swing_days:int=1, inside_down:bool=False, ignore_threshold:int=0, use_close_of_outside_bar:bool=False) -> pd.DataFrame:
        self.swing_days = swing_days
        self.inside_down = inside_down
        self.ignore_threshold = ignore_threshold
        self.use_close_of_outside_bar = use_close_of_outside_bar
        self.__parameter_validation()
        results = pd.DataFrame(columns = ['Timestamp', 'SwingStartDate', 'SwingStartPrice', 'SwingEndDate', 'SwingEndPrice', 'TradeableRange', 'Trend'])

        return results

    def _up_day(self, bar:int):
        '''
        Return True if bar is an up day, else False
        '''
        this_bar = self.bars.iloc[bar]
        try:
            previous_bar = self.bars.iloc[bar-1]
            if this_bar['Low'] >= previous_bar['Low'] and this_bar['High'] > previous_bar['High']:
                return True
        except IndexError:
            pass
        return False

    def _down_day(self, bar:int):
        this_bar = self.bars.iloc[bar]
        try:
            previous_bar = self.bars.iloc[bar-1]
            if this_bar['Low'] < previous_bar['Low'] and this_bar['High'] <= previous_bar['High']:
                return True
        except IndexError:
            pass
        return False

    def _inside_day(self, bar:int):
        this_bar = self.bars.iloc[bar]
        try:
            previous_bar = self.bars.iloc[bar-1]
            if this_bar['Low'] >= previous_bar['Low'] and this_bar['High'] <= previous_bar['High']:
                return True
        except IndexError:
            pass
        return False

    def _outside_day(self, bar:int):
        this_bar = self.bars.iloc[bar]
        try:
            previous_bar = self.bars.iloc[bar-1]
            if this_bar['Low'] < previous_bar['Low'] and this_bar['High'] > previous_bar['High']:
                return True
        except IndexError:
            pass
        return False

    def _find_turns(self, swing_days):
        for i in range(swing_days+1, len(self.bars)):
            for j in range(1, swing_days):
                if self.__down_day(i-j) and self.__up_day(i+j):
                    break
            row = pd.DataFrame({'Swing': self.bars.iloc[i]})
        pass

    def visualise(self):
        '''
        Draw an OHLC chart of the bars data. If swings have been calculated, overlay them
        on top of the OHLC chart
        '''
        import plotly.graph_objects as go

        # When you hover over a bar on the chart, you should see the OHLC values
        hovertext=[]
        for i in range(len(bars['Open'])):
            hovertext.append('Open: '+str(bars['Open'][i])+'<br>High: '+str(bars['High'][i])+'<br>Low: '+str(bars['Low'][i])+'<br>Close: '+str(bars['Close'][i]))

        fig = go.Figure(data=go.Ohlc(x=bars['Timestamp'],
            open=bars['Open'],
            high=bars['High'],
            low=bars['Low'],
            close=bars['Close']),
            text=hovertext,
            hoverinfo='text')
        fig.update(layout_xaxis_rangeslider_visible=False)

        if self.swing_days():
            # Overlay a swing chart on top of the bar chart
            # go.update_layout(...)
            pass # Remove this line when the swing charts are working
        fig.show()

    def ticksize(self):
        '''
        Calculate ticksize from the last BARS_TO_USE bars. It's not perfect, but close enough for government work...
        '''
        BARS_TO_USE = 20
        last_N_bars = self.bars.tail(BARS_TO_USE)
        last_N_bars = last_N_bars.drop(columns=['Timestamp'])
        prices = set()

        # Add all the OHLC values from the last BARS_TO_USE bars to a set & sort it
        for _, row in last_N_bars.iterrows():
            prices.add(row['Open'])
            prices.add(row['High'])
            prices.add(row['Low'])
            prices.add(row['Close'])
        p1 = sorted(prices)

        # Find the smallest gap between consecutive items in the set
        ticksize = 10000000
        for first, second in zip(p1, p1[1:]):
            ticksize = min(ticksize, round(second-first, 6))
        return(ticksize)


if __name__ == '__main__':
    gs = GannSwing(bars=pd.DataFrame())