import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const PredictionChart = ({ historicalData, prediction }) => {
    const data = historicalData.map((item, index) => ({
        name: index,
        historical: item,
        prediction: prediction && prediction[index] ? prediction[index] : null,
    }));

    return (
        <ResponsiveContainer width="100%" height={400}>
            <LineChart
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
                <Line type="monotone" dataKey="historical" stroke="#8884d8" activeDot={{ r: 8 }} />
                {prediction && Array.isArray(prediction) && <Line type="monotone" dataKey="prediction" stroke="#82ca9d" />}
            </LineChart>
        </ResponsiveContainer>
    );
};

export default PredictionChart;
