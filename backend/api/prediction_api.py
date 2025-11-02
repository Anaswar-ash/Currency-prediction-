from flask import Blueprint, request, jsonify

from ..services.data_service import get_historical_data
from ..services.prediction_service import train_and_predict_with_lstm

prediction_bp = Blueprint('prediction_bp', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    """Predicts the future exchange rate for a given currency pair."""
    data = request.get_json()
    ticker = data.get('ticker')

    if not ticker:
        return jsonify({'error': 'Ticker is required'}), 400

    try:
        # Fetch historical data
        hist = get_historical_data(ticker)

        # Train the model and make predictions
        forecast = train_and_predict_with_lstm(hist)

        return jsonify({'prediction': forecast.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
