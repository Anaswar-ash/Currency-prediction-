import React, { useState } from 'react';

const PredictionForm = ({ onPredict }) => {
    const [ticker, setTicker] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onPredict(ticker);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={ticker}
                onChange={(e) => setTicker(e.target.value)}
                placeholder="Enter currency ticker (e.g., GBPINR=X)"
            />
            <button type="submit">Predict</button>
        </form>
    );
};

export default PredictionForm;
