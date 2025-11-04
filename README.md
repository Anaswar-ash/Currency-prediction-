# Currency Prediction Web Application

This web application predicts the exchange rates for the following currency pairs:

*   GBP/INR
*   EUR/USD
*   USD/HKD

## Description

[Provide a more detailed description of your project here. What does it do? What problem does it solve?]

## Features

*   Predicts future exchange rates for GBP, INR, EUR, USD, and HKD.
*   Visualizes historical exchange rate data.
*   [Add more features as needed]

## Supported Currency Pairs

*   GBP/INR
*   EUR/USD
*   USD/HKD
*   USD/JPY
*   AUD/USD
*   GBP/USD

## Technologies Used

*   **Frontend:** React
*   **Backend:** Python
*   **Database:** [e.g., PostgreSQL, MongoDB, SQLite]
*   **Machine Learning:** [e.g., TensorFlow, Keras, Scikit-learn]

## Getting Started

### Prerequisites

*   **Termux**: A terminal emulator for Android.
*   **Node.js**: For running the frontend.
*   **proot-distro**: For running a Linux distribution within Termux.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Anaswar-ash/Currency-prediction-.git
    cd Currency-prediction-
    ```

2.  **Backend Setup (with proot-distro):**

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

3.  **Frontend Setup:**

    a. **Navigate to the frontend directory:**
        ```bash
        cd frontend
        ```

    b. **Install frontend dependencies:**
        ```bash
        npm install
        ```

### Running the Application

1.  **Start the Backend:**

    a. **Log into the Ubuntu environment:**
        ```bash
        proot-distro login ubuntu
        ```

    b. **Navigate to the backend directory and run the Flask app:**
        ```bash
        cd /path/to/Currency-prediction-/backend
        flask run
        ```

2.  **Start the Frontend:**

    a. **Navigate to the frontend directory:**
        ```bash
        cd frontend
        ```

    b. **Start the React development server:**
        ```bash
        npm start
        ```

## Usage

[Explain how to use your application. Provide examples if possible.]

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for details.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
