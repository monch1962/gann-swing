# gann-swing
Python module to calculate Gann swings

## Why?
I've gotten sick of waiting for someone to write a robust, correct Python module to calculate Gann swings with all the variations and optional parameters I want, so thought I may as well take it on myself

## To run all test cases & confirm everything is working OK

`$ pytest -v`

## To use it

(add in later)

## Consuming data from different data sources

GannSwing is expecting data to be provided in a Pandas dataframe with the following set of column headings:
- Timestamp
- Open
- High
- Low
- Close

All these columns are mandatory; any other columns in the dataframe are ignored.

### Optuma

Optuma lets you copy/paste data in a CSV, tab-limited format. Here's an example of how to consume this data format

```
$ ipython
> from gannswing import GannSwing
> from pandas import pd
> bars = pd.read_csv('./tests/data/optuma.csv', delimiter='\t', usecols=['Date', 'Open', 'High', 'Low', 'Close'])
> bars.rename(columns={'Date': 'Timestamp'}, inplace=True)
> gs = GannSwing(bars=bars)
```

### ProfitSource

(add later)

### Yahoo Finance

(add later)

## To-do list

Quite a long list, but it gives me a task list to prioritise and work to:
- ~~calculate ticksize~~
- ~~work out the structure of the Pandas dataframe to deliver results~~
- package it into a proper Python module that I can install using `pip install gann-swings`
- implement support for 1-bar, 2-bar, 3-bar, ... swings
- be able to draw a quick chart of swings overlaid on top of a bar chart as a visual reference point
- build a huge test suite that covers all the functionality. Tests should be able to confirm that it e.g. calculates swings correctly when it gets 17 outside days in a row...
- work out the trend as well as the swings
- calculate the days and price difference between successive swings
- option to create a swing for inside days in a down trend 
- option to filter out tiny swings 
- option to compare the open & close on outside days to determine whether where to put a swing in the daily chart without waiting for the next up or down day
- ~~build in support for consuming OHLC data from a range of common data sources~~
