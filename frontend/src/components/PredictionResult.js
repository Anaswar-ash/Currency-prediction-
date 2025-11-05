import React from 'react';

const PredictionResult = ({ prediction }) => {
    if (!prediction) {
        return null;
    }

    return (
        <div className="mt-4">
            <h5>Prediction Result</h5>
            <p>The predicted currency value is: <strong>{prediction}</strong></p>
        </div>
    );
};

export default PredictionResult;
