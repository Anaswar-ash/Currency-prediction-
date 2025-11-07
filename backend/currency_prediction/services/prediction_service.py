# currency_prediction/services/prediction_service.py
# This is where the magic happens! This file contains the core logic for
# training our prediction models and making predictions.

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
from sklearn.linear_model import LinearRegression

def create_lstm_model(input_shape):
    """
    This function creates our LSTM model. LSTM stands for Long Short-Term Memory,
    and it's a type of neural network that's really good at understanding sequences
    of data, like time series data (e.g., stock prices).
    """
    # We're using a Sequential model, which is a simple way to build a neural network
    # by stacking layers on top of each other.
    model = Sequential([
        # We have two LSTM layers here. The first one has `return_sequences=True`
        # because we want it to pass on its output to the next LSTM layer.
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        # We have two Dense layers here. These are our output layers.
        Dense(25),
        Dense(1)
    ])
    # We're compiling the model here. This is where we tell Keras what optimizer
    # and loss function to use. 'adam' is a good general-purpose optimizer, and
    # 'mean_squared_error' is a common loss function for regression problems.
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_and_predict_with_lstm(data, steps=30):
    """
    This function trains our LSTM model and then uses it to predict future values.
    """
    # We're scaling the data here to be between 0 and 1. This is a common practice
    # in machine learning because it helps the model learn more effectively.
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

    # We're creating our training data here. We're using a sliding window approach,
    # where we take a sequence of 60 days of data as our input (X) and the next
    # day's data as our output (y).
    prediction_days = 60
    x_train, y_train = [], []
    for i in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[i-prediction_days:i, 0])
        y_train.append(scaled_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # We're creating and training our LSTM model here.
    # Note: we're only training for 1 epoch here, which is not ideal for a real
    # application. We're doing this to make the prediction faster for this demo.
    # In a real-world scenario, you'd want to train for more epochs to get a
    # more accurate model.
    model = create_lstm_model(input_shape=(x_train.shape[1], 1))
    model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=0)

    # Now we're making our predictions. We're predicting the next `steps` days
    # by feeding the model the last 60 days of data and then using the model's
    # own predictions as input for the next prediction.
    test_inputs = scaled_data[-prediction_days:].reshape(1, -1, 1)
    forecast = []
    current_input = test_inputs

    for _ in range(steps):
        predicted_price = model.predict(current_input)
        forecast.append(predicted_price[0, 0])
        current_input = np.append(current_input[:, 1:, :], [[predicted_price]], axis=1)

    # Finally, we're inverse transforming our predictions to get them back into
    # the original price scale.
    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))
    return forecast.flatten()

def train_and_predict_with_linear_regression(data, steps=30):
    """
    This function trains a Linear Regression model and makes predictions.
    Linear Regression is a much simpler model than LSTM, but it can still be
    effective for some time series problems.
    """
    # We're scaling the data here, just like we did for the LSTM model.
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

    # We're creating our training data here, just like we did for the LSTM model.
    prediction_days = 60
    x_train, y_train = [], []
    for i in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[i-prediction_days:i, 0])
        y_train.append(scaled_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)

    # We're creating and training our Linear Regression model here.
    model = LinearRegression()
    model.fit(x_train, y_train)

    # We're making our predictions here, just like we did for the LSTM model.
    test_inputs = scaled_data[-prediction_days:].flatten()
    forecast = []
    current_input = test_inputs

    for _ in range(steps):
        predicted_price = model.predict([current_input])
        forecast.append(predicted_price[0])
        current_input = np.append(current_input[1:], predicted_price)

    # Finally, we're inverse transforming our predictions to get them back into
    # the original price scale.
    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))
    return forecast.flatten()
