# Currency Prediction Web Application

This web application predicts the exchange rates for various currency pairs using different machine learning models.

## Description

This project is a web application that allows users to select a currency pair and a machine learning model to predict future exchange rates. The application displays the historical data and the prediction in an interactive chart.

## Features

*   Predicts future exchange rates for various currency pairs.
*   Supports multiple machine learning models (LSTM and Linear Regression).
*   Visualizes historical and predicted exchange rate data in an interactive chart.
*   Modern and responsive user interface built with React and Bootstrap.

## Supported Currency Pairs

*   GBP/INR
*   EUR/USD
*   USD/HKD
*   USD/JPY
*   AUD/USD
*   GBP/USD

## Technologies Used

*   **Frontend:** React, Bootstrap, Recharts
*   **Backend:** Python, Flask, TensorFlow, Keras, Scikit-learn

## Getting Started

### Prerequisites (Termux)

*   **Termux**: A terminal emulator for Android.
*   **Node.js**: For running the frontend.
*   **proot-distro**: For running a Linux distribution within Termux.

### Prerequisites (Windows)

*   **Python**: For running the backend.
*   **Node.js**: For running the frontend.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Anaswar-ash/Currency-prediction-.git
    cd Currency-prediction-
    ```

2.  **Backend Setup (Termux with proot-distro):**

    The backend requires `tensorflow`, which cannot be installed directly on Termux. We will use `proot-distro` to create an Ubuntu environment.

    a. **Install `proot-distro`:**
        ```bash
        pkg install proot-distro -y
        ```

    b. **Install Ubuntu:**
        ```bash
        proot-distro install ubuntu
        ```

    c. **Log into Ubuntu:**
        ```bash
        proot-distro login ubuntu
        ```

    d. **Inside the Ubuntu environment, install backend dependencies:**
        ```bash
        # Update package lists
        apt update && apt upgrade -y

        # Install Python and pip
        apt install python3 python3-pip -y

        # Navigate to the backend directory and install dependencies
        cd /path/to/Currency-prediction-/backend 
        pip3 install -r requirements.txt
        ```
        *(Note: You will need to replace `/path/to/Currency-prediction-` with the actual path to the repository within your Termux environment)*

3.  **Backend Setup (Windows):**

    a. **Create a virtual environment:**
        ```bash
        cd backend
        python -m venv venv
        ```

    b. **Activate the virtual environment:**
        ```bash
        .\venv\Scripts\activate
        ```

    c. **Install backend dependencies:**
        ```bash
        pip install -r requirements.txt
        ```

4.  **Frontend Setup:**

    a. **Navigate to the frontend directory:**
        ```bash
        cd frontend
        ```

    b. **Install frontend dependencies:**
        ```bash
        npm install
        ```

### Running the Application

1.  **Start the Backend (Termux):**

    a. **Log into the Ubuntu environment:**
        ```bash
        proot-distro login ubuntu
        ```

    b. **Navigate to the backend directory and run the Flask app:**
        ```bash
        cd /path/to/Currency-prediction-/backend
        flask run
        ```

2.  **Start the Backend (Windows):**

    a. **Navigate to the backend directory and activate the virtual environment:**
        ```bash
        cd backend
        .\venv\Scripts\activate
        ```

    b. **Run the Flask app:**
        ```bash
        flask run
        ```

3.  **Start the Frontend:**

    a. **Navigate to the frontend directory:**
        ```bash
        cd frontend
        ```

    b. **Start the React development server:**
        ```bash
        npm start
        ```

## Usage

1.  Open your web browser and navigate to `http://localhost:3000`.
2.  Select a currency pair and a prediction model from the dropdown menus.
3.  Click the "Predict" button to see the prediction.

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for details.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
