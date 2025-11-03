import React, { useState } from 'react';
import './App.css';
import PredictionForm from './components/PredictionForm';
import PredictionChart from './components/PredictionChart';
import PredictionResult from './components/PredictionResult';

function App() {
    const [ticker, setTicker] = useState('');
    const [prediction, setPrediction] = useState(null);
    const [historicalData, setHistoricalData] = useState([]);

    const handlePredict = async (ticker) => {
        setTicker(ticker);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ticker }),
            });

            const data = await response.json();
            setPrediction(data.prediction);

            // For now, we'll just use the prediction as the historical data
            // In a real application, you would fetch the actual historical data
            setHistoricalData(data.prediction);

        } catch (error) {
            console.error('Error fetching prediction:', error);
        }
    };

    return (
        <div className="App">
            <h1>Currency Prediction</h1>
            <PredictionForm onPredict={handlePredict} />
            {prediction && (
                <>
                    <PredictionChart historicalData={historicalData} prediction={prediction} />
                    <PredictionResult prediction={prediction} />
                </>
            )}
        </div>
    );
}

export default App;
