import numpy as np
import pandas as pd
import alpaca_trade_api as tradeapi
import time

with open("keys.txt") as keys_file:
    public_key = keys_file.readline().strip()
    secret_key = keys_file.readline().strip()
api = tradeapi.REST(public_key, secret_key)

symbols_frame = pd.read_csv("data/companylist.csv")
# print(symbols_frame.head())
# print(symbols_frame["Symbol"].head())

# TODO figure out how to put this result in a dataframe or also in a csv file
for symbol in symbols_frame["Symbol"]:
    # Add sleep to avoid rate limits
    time.sleep(0.25)

    # Get daily price data for each symbol over the last 5 trading days.
    barset = api.get_barset(symbol, 'day', limit=5)
    bars = barset[symbol]

    # See how much AAPL moved in that timeframe.
    if len(bars) > 0:
        week_open = bars[0].o
        week_close = bars[-1].c
        percent_change = (week_close - week_open) / week_open * 100
        print('{} moved {}% over the last 5 days'.format(symbol, percent_change))