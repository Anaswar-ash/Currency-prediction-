import React from 'react';

// This component renders the prediction result.
const PredictionResult = ({ prediction }) => {
    // If there is no prediction data, render nothing.
    if (!prediction) {
        return null;
    }

    // Render the prediction result.
    return (
        <div>
            <h2>Prediction</h2>
            {/* Display the prediction data. */}
            <p>{prediction}</p>
        </div>
    );
};

export default PredictionResult;
