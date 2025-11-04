# This file contains functions for fetching financial data.

import yfinance as yf

def get_historical_data(ticker, period="5y"):
    """Fetches historical data for a given ticker from Yahoo Finance.

    Args:
        ticker (str): The ticker symbol to fetch data for (e.g., 'AAPL').
        period (str, optional): The period to fetch data for. Defaults to "5y".

    Returns:
        pandas.DataFrame: A DataFrame containing the historical data, including
                          Open, High, Low, Close, Volume, and Dividends.
    """
    # Create a Ticker object for the given ticker symbol
    stock = yf.Ticker(ticker)
    # Fetch the historical data for the specified period
    hist = stock.history(period=period)
    return hist
