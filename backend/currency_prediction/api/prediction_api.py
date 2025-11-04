from flask import Blueprint, request, jsonify
import logging
import requests

from ..services.data_service import get_historical_data
from ..services.prediction_service import train_and_predict_with_lstm, train_and_predict_with_linear_regression

prediction_bp = Blueprint('prediction_bp', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    """Predicts the future exchange rate for a given currency pair."""
    data = request.get_json()
    ticker = data.get('ticker')
    model_name = data.get('model', 'lstm')  # Default to lstm

    if not ticker:
        logging.error("Ticker not provided in request")
        return jsonify({'error': 'Ticker is required'}), 400

    try:
        logging.info(f"Fetching historical data for {ticker}")
        hist = get_historical_data(ticker)

        logging.info(f"Training model '{model_name}' and making predictions for {ticker}")
        if model_name == 'linear_regression':
            forecast = train_and_predict_with_linear_regression(hist)
        else:
            forecast = train_and_predict_with_lstm(hist)

        logging.info(f"Successfully generated prediction for {ticker} using {model_name}")
        return jsonify({'prediction': forecast.tolist()})

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logging.error(f"Ticker not found: {ticker}")
            return jsonify({'error': f'Ticker "{ticker}" not found'}), 404
        else:
            logging.error(f"HTTP error for {ticker}: {e}")
            return jsonify({'error': str(e)}), 500
    except KeyError:
        logging.error(f"Invalid data for ticker: {ticker}")
        return jsonify({'error': f'Invalid data for ticker "{ticker}"'}), 400
    except Exception as e:
        logging.error(f"An unexpected error occurred for {ticker}: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500
