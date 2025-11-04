import React, { useState } from 'react';
import './App.css';
import PredictionForm from './components/PredictionForm';
import PredictionChart from './components/PredictionChart';
import PredictionResult from './components/PredictionResult';

// This is the main component of the application.
function App() {
    // State variables to store the ticker, prediction data, historical data, error messages, and loading status.
    const [ticker, setTicker] = useState('');
    const [prediction, setPrediction] = useState(null);
    const [historicalData, setHistoricalData] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    // This function is called when the user requests a prediction.
    const handlePredict = async (ticker, model) => {
        // Set the state to indicate that a prediction is in progress.
        setTicker(ticker);
        setLoading(true);
        setError(null);
        setPrediction(null);

        try {
            // Send a POST request to the backend to get the prediction.
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ticker, model }),
            });

            // If the response is not ok, throw an error.
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Something went wrong');
            }

            // Parse the prediction data from the response.
            const data = await response.json();
            setPrediction(data.prediction);

            // In a real application, you would fetch the actual historical data.
            // For now, we'll just use the prediction as the historical data for the chart.
            setHistoricalData(data.prediction);

        } catch (error) {
            // If an error occurs, set the error state and log the error to the console.
            setError(error.message);
            console.error('Error fetching prediction:', error);
        } finally {
            // Set the loading state to false when the prediction is complete.
            setLoading(false);
        }
    };

    // Render the main application component.
    return (
        <div className="App">
            <h1>Currency Prediction</h1>
            {/* The form for submitting a prediction request. */}
            <PredictionForm onPredict={handlePredict} />
            {/* Show a loading message while the prediction is in progress. */}
            {loading && <p>Loading...</p>}
            {/* Show an error message if an error occurs. */}
            {error && <p className="error">Error: {error}</p>}
            {/* Show the prediction chart and result when the prediction is available. */}
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
