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

    const handlePredict = async (ticker, model) => {
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
                body: JSON.stringify({ ticker, model }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Something went wrong');
            }

            const data = await response.json();
            setPrediction(data.prediction);
            setHistoricalData(data.prediction);

        } catch (error) {
            setError(error.message);
            console.error('Error fetching prediction:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">Currency Prediction</a>
                </div>
            </nav>
            <div className="container mt-4">
                <div className="row">
                    <div className="col-md-4">
                        <PredictionForm onPredict={handlePredict} />
                    </div>
                    <div className="col-md-8">
                        {loading && <div className="d-flex justify-content-center"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>}
                        {error && <div className="alert alert-danger">Error: {error}</div>}
                        {prediction && !error && (
                            <div className="card">
                                <div className="card-body">
                                    <h5 className="card-title">Prediction for {ticker}</h5>
                                    <PredictionChart historicalData={historicalData} prediction={prediction} />
                                    <PredictionResult prediction={prediction} />
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default App;
