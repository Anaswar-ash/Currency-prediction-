# This file contains the core logic for training the prediction models and making predictions.

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
from sklearn.linear_model import LinearRegression

def create_lstm_model(input_shape):
    """Creates and compiles a simple LSTM model.

    Args:
        input_shape (tuple): The shape of the input data for the first LSTM layer.

    Returns:
        tensorflow.keras.models.Sequential: The compiled LSTM model.
    """
    # Define the LSTM model architecture
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        Dense(25),
        Dense(1)
    ])
    # Compile the model with an Adam optimizer and mean squared error loss function
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_and_predict_with_lstm(data, steps=30):
    """Trains an LSTM model on the provided data and predicts future values.

    Args:
        data (pandas.DataFrame): The historical data to train the model on.
        steps (int, optional): The number of future steps to predict. Defaults to 30.

    Returns:
        numpy.ndarray: An array of predicted values.
    """
    # Scale the closing prices to be between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

    # Create the training data
    prediction_days = 60
    x_train, y_train = [], []
    for i in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[i-prediction_days:i, 0])
        y_train.append(scaled_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Create and train the LSTM model
    model = create_lstm_model(input_shape=(x_train.shape[1], 1))
    model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=0)

    # Make predictions for the next 'steps' days
    test_inputs = scaled_data[-prediction_days:].reshape(1, -1, 1)
    forecast = []
    current_input = test_inputs

    for _ in range(steps):
        predicted_price = model.predict(current_input)
        forecast.append(predicted_price[0, 0])
        current_input = np.append(current_input[:, 1:, :], [[predicted_price]], axis=1)

    # Inverse transform the predictions to get the actual price values
    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))
    return forecast.flatten()

def train_and_predict_with_linear_regression(data, steps=30):
    """Trains a Linear Regression model and makes predictions.

    Args:
        data (pandas.DataFrame): The historical data to train the model on.
        steps (int, optional): The number of future steps to predict. Defaults to 30.

    Returns:
        numpy.ndarray: An array of predicted values.
    """
    # Scale the closing prices to be between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

    # Create the training data
    prediction_days = 60
    x_train, y_train = [], []
    for i in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[i-prediction_days:i, 0])
        y_train.append(scaled_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)

    # Create and train the Linear Regression model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Make predictions for the next 'steps' days
    test_inputs = scaled_data[-prediction_days:].flatten()
    forecast = []
    current_input = test_inputs

    for _ in range(steps):
        predicted_price = model.predict([current_input])
        forecast.append(predicted_price[0])
        current_input = np.append(current_input[1:], predicted_price)

    # Inverse transform the predictions to get the actual price values
    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))
    return forecast.flatten()
