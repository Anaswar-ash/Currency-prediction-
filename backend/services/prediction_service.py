from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(data):
    """Trains an ARIMA model on the given data.

    Args:
        data (pandas.DataFrame): A DataFrame containing the historical data.

    Returns:
        statsmodels.tsa.arima.model.ARIMAResultsWrapper: The trained ARIMA model.
    """
    model = ARIMA(data['Close'], order=(5,1,0))
    model_fit = model.fit()
    return model_fit

def predict_with_arima(model, steps=30):
    """Makes predictions with a trained ARIMA model.

    Args:
        model (statsmodels.tsa.arima.model.ARIMAResultsWrapper): The trained ARIMA model.
        steps (int, optional): The number of steps to predict. Defaults to 30.

    Returns:
        pandas.Series: A Series containing the predicted values.
    """
    forecast = model.forecast(steps=steps)
    return forecast
