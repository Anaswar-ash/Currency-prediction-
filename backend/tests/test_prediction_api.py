import pytest
from backend.currency_prediction import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_predict_endpoint(client, mocker):
    # Mock the services
    mocker.patch('backend.currency_prediction.api.prediction_api.get_historical_data', return_value=None)
    mocker.patch('backend.currency_prediction.api.prediction_api.train_and_predict_with_lstm', return_value=[1, 2, 3])

    response = client.post('/predict', json={'ticker': 'GBPINR=X'})
    assert response.status_code == 200
    assert response.json == {'prediction': [1, 2, 3]}

def test_predict_endpoint_no_ticker(client):
    response = client.post('/predict', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Ticker is required'}
