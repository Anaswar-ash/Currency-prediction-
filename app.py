# This is the main entry point for the Flask application.

from backend.currency_prediction import create_app

# Create an instance of the Flask application
app = create_app()

# Run the application
if __name__ == '__main__':
    # The app is run in debug mode for development.
    # In a production environment, this should be run by a production-ready server like Gunicorn or uWSGI.
    app.run(debug=True)
