import React, { useState } from 'react';

const PredictionForm = ({ onPredict }) => {
    const [ticker, setTicker] = useState('GBPINR=X');
    const [model, setModel] = useState('lstm');

    const handleSubmit = (e) => {
        e.preventDefault();
        onPredict(ticker, model);
    };

    return (
        <form onSubmit={handleSubmit}>
            <select value={ticker} onChange={(e) => setTicker(e.target.value)}>
                <option value="GBPINR=X">GBP/INR</option>
                <option value="EURUSD=X">EUR/USD</option>
                <option value="USDHKD=X">USD/HKD</option>
                <option value="USDJPY=X">USD/JPY</option>
                <option value="AUDUSD=X">AUD/USD</option>
                <option value="GBPUSD=X">GBP/USD</option>
            </select>
            <select value={model} onChange={(e) => setModel(e.target.value)}>
                <option value="lstm">LSTM</option>
                <option value="linear_regression">Linear Regression</option>
            </select>
            <button type="submit">Predict</button>
        </form>
    );
};

export default PredictionForm;
