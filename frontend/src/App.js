import React, { useState } from 'react';
import './App.css';
import PredictionForm from './components/PredictionForm';
import PredictionChart from './components/PredictionChart';
import PredictionResult from './components/PredictionResult';

function App() {
    const [ticker, setTicker] = useState('');
    const [prediction, setPrediction] = useState(null);
    const [historicalData, setHistoricalData] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handlePredict = async (ticker) => {
        setTicker(ticker);
        setLoading(true);
        setError(null);
        setPrediction(null);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ticker }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Something went wrong');
            }

            const data = await response.json();
            setPrediction(data.prediction);

            // For now, we'll just use the prediction as the historical data
            // In a real application, you would fetch the actual historical data
            setHistoricalData(data.prediction);

        } catch (error) {
            setError(error.message);
            console.error('Error fetching prediction:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="App">
            <h1>Currency Prediction</h1>
            <PredictionForm onPredict={handlePredict} />
            {loading && <p>Loading...</p>}
            {error && <p className="error">Error: {error}</p>}
            {prediction && !error && (
                <>
                    <PredictionChart historicalData={historicalData} prediction={prediction} />
                    <PredictionResult prediction={prediction} />
                </>
            )}
        </div>
    );
}

export default App;
