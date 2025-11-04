import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

// This component renders the chart for displaying historical and predicted data.
const PredictionChart = ({ historicalData, prediction }) => {
    // Combine the historical and prediction data into a single array for the chart.
    const data = historicalData.map((item, index) => ({
        name: index, // Use the index as the x-axis label.
        historical: item, // The historical data point.
        prediction: prediction && prediction[index] ? prediction[index] : null, // The predicted data point.
    }));

    // Render the line chart using the recharts library.
    return (
        <LineChart
            width={800}
            height={400}
            data={data}
            margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
            }}
        >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            {/* Line for the historical data. */}
            <Line type="monotone" dataKey="historical" stroke="#8884d8" activeDot={{ r: 8 }} />
            {/* Line for the predicted data, only rendered if prediction data is available. */}
            {prediction && Array.isArray(prediction) && <Line type="monotone" dataKey="prediction" stroke="#82ca9d" />}
        </LineChart>
    );
};

export default PredictionChart;
