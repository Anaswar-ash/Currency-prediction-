# currency_prediction/services/data_service.py
# This file is all about fetching the financial data that we need for our predictions.
# We're using the `yfinance` library, which is a great tool for getting data from Yahoo Finance.

import yfinance as yf

def get_historical_data(ticker, period="5y"):
    """
    This function fetches historical market data for a given stock ticker.
    For example, you can pass in 'AAPL' to get data for Apple.
    We're getting 5 years of data by default, but you can change that if you want.
    """
    # We're creating a Ticker object here. This object represents the stock
    # that we want to get data for.
    stock = yf.Ticker(ticker)
    # Here, we're calling the `history` method on the Ticker object to get
    # the historical data. The data is returned as a pandas DataFrame, which
    # is a really convenient format for working with this kind of data.
    hist = stock.history(period=period)
    return hist
