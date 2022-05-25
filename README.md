# gann-swing
Python module to calculate Gann swings

# Why?
I've gotten sick of waiting for someone to write a robust, correct Python module to calculate Gann swings so thought I may as well take it on myself

# To use it

(add in later)

## To-do list

Quite a long list, but it gives me a task list to prioritise and work to:
- work out the structure of the Pandas dataframe to deliver results
- package it into a proper Python module that I can install using `pip install`
- implement support for 1-bar, 2-bar, 3-bar, ... swings
- can draw a quick chart of swings overlaid on top of a bar chart
- build a huge test suite that covers all the functionality. Tests should be able to confirm that it e.g. calculates swings correctly when it gets 17 outside days in a row...
- work out the trend as well as the swings
- calculate the days and points between successive swings
- option to create a swing for inside days in a down trend 
- option to filter out tiny swings 
- option to compare the open & close on outside days to determine whether where to put a swing in the daily chart without waiting for the next up or down day
- build in support for consuming OHLC data from a range of common data sources
