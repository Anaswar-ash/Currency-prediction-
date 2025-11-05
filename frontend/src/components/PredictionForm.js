import React, { useState } from 'react';

const PredictionForm = ({ onPredict }) => {
    const [ticker, setTicker] = useState('GBPINR=X');
    const [model, setModel] = useState('lstm');

    const handleSubmit = (e) => {
        e.preventDefault();
        onPredict(ticker, model);
    };

    return (
        <div className="card">
            <div className="card-body">
                <h5 className="card-title">Select Currency and Model</h5>
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="ticker" className="form-label">Currency Pair</label>
                        <select id="ticker" className="form-select" value={ticker} onChange={(e) => setTicker(e.target.value)}>
                            <option value="GBPINR=X">GBP/INR</option>
                            <option value="EURUSD=X">EUR/USD</option>
                            <option value="USDHKD=X">USD/HKD</option>
                            <option value="USDJPY=X">USD/JPY</option>
                            <option value="AUDUSD=X">AUD/USD</option>
                            <option value="GBPUSD=X">GBP/USD</option>
                        </select>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="model" className="form-label">Prediction Model</label>
                        <select id="model" className="form-select" value={model} onChange={(e) => setModel(e.target.value)}>
                            <option value="lstm">LSTM</option>
                            <option value="linear_regression">Linear Regression</option>
                        </select>
                    </div>
                    <button type="submit" className="btn btn-primary">Predict</button>
                </form>
            </div>
        </div>
    );
};

export default PredictionForm;
