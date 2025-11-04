import React, { useState } from 'react';

// This component renders the form for submitting a prediction request.
const PredictionForm = ({ onPredict }) => {
    // State variables to store the selected ticker and model.
    const [ticker, setTicker] = useState('GBPINR=X');
    const [model, setModel] = useState('lstm');

    // This function is called when the form is submitted.
    const handleSubmit = (e) => {
        e.preventDefault();
        // Call the onPredict function passed from the parent component.
        onPredict(ticker, model);
    };

    // Render the prediction form.
    return (
        <form onSubmit={handleSubmit}>
            {/* Dropdown for selecting the currency pair. */}
            <select value={ticker} onChange={(e) => setTicker(e.target.value)}>
                <option value="GBPINR=X">GBP/INR</option>
                <option value="EURUSD=X">EUR/USD</option>
                <option value="USDHKD=X">USD/HKD</option>
                <option value="USDJPY=X">USD/JPY</option>
                <option value="AUDUSD=X">AUD/USD</option>
                <option value="GBPUSD=X">GBP/USD</option>
            </select>
            {/* Dropdown for selecting the prediction model. */}
            <select value={model} onChange={(e) => setModel(e.target.value)}>
                <option value="lstm">LSTM</option>
                <option value="linear_regression">Linear Regression</option>
            </select>
            {/* Button to submit the form. */}
            <button type="submit">Predict</button>
        </form>
    );
};

export default PredictionForm;
