import yfinance as yf

def get_historical_data(ticker, period="5y"):
    """Fetches historical data for a given ticker.

    Args:
        ticker (str): The ticker symbol to fetch data for.
        period (str, optional): The period to fetch data for. Defaults to "5y".

    Returns:
        pandas.DataFrame: A DataFrame containing the historical data.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist
