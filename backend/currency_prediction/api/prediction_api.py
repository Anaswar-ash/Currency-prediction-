# currency_prediction/api/prediction_api.py
# This is where we define the API endpoints for our currency prediction service.
# An API endpoint is like a specific URL that our frontend can send a request to,
# and our backend will respond with some data.

from flask import Blueprint, request, jsonify
import logging
import requests

from ..services.data_service import get_historical_data
from ..services.prediction_service import train_and_predict_with_lstm, train_and_predict_with_linear_regression

# A Blueprint is a way to organize a group of related views and other code.
# It's like a mini-app within our app. We're creating one here for our prediction API.
prediction_bp = Blueprint('prediction_bp', __name__)

# We're setting up logging here so we can see what's happening in our application.
# This is really helpful for debugging.
logging.basicConfig(level=logging.INFO)

# This is the main endpoint for our API. It's a POST request because the frontend
# will be sending us some data (the ticker and the model name).
@prediction_bp.route('/predict', methods=['POST'])
def predict():
    """
    This function handles the prediction request. It takes a currency ticker
    and a model name, fetches the historical data, trains a model, and then
    returns the prediction.
    """
    # We're getting the data that the frontend sent us. It's in JSON format.
    data = request.get_json()
    ticker = data.get('ticker')
    model_name = data.get('model', 'lstm')  # We'll default to 'lstm' if no model is specified.

    # It's always a good idea to validate the input we receive.
    # Here, we're making sure that a ticker was actually provided.
    if not ticker:
        logging.error("Ticker not provided in request")
        return jsonify({'error': 'Ticker is required'}), 400

    try:
        # We're calling our data service to get the historical data for the ticker.
        logging.info(f"Fetching historical data for {ticker}")
        hist = get_historical_data(ticker)

        # Now we're training the selected model and making a prediction.
        logging.info(f"Training model '{model_name}' and making predictions for {ticker}")
        if model_name == 'linear_regression':
            forecast = train_and_predict_with_linear_regression(hist)
        else:
            forecast = train_and_predict_with_lstm(hist)

        # Finally, we're sending the prediction back to the frontend as a JSON response.
        logging.info(f"Successfully generated prediction for {ticker} using {model_name}")
        return jsonify({'prediction': forecast.tolist()})

    except requests.exceptions.HTTPError as e:
        # This is our error handling. We're catching specific errors that might happen
        # and returning a helpful error message to the frontend.
        if e.response.status_code == 404:
            logging.error(f"Ticker not found: {ticker}")
            return jsonify({'error': f'Ticker "{ticker}" not found'}), 404
        else:
            logging.error(f"HTTP error for {ticker}: {e}")
            return jsonify({'error': str(e)}), 500
    except KeyError:
        # This handles cases where the data for the ticker is invalid.
        logging.error(f"Invalid data for ticker: {ticker}")
        return jsonify({'error': f'Invalid data for ticker "{ticker}"'}), 400
    except Exception as e:
        # This is a catch-all for any other unexpected errors.
        logging.error(f"An unexpected error occurred for {ticker}: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500
