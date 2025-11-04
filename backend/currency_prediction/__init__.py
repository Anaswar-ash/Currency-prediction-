# This file is responsible for creating and configuring the Flask application.

from flask import Flask

def create_app():
    """Creates and configures an instance of the Flask application."""
    # Create the Flask app instance
    app = Flask(__name__)

    # The app_context is used to make the application instance available
    # to the blueprints and other parts of the application.
    with app.app_context():
        # Import and register the prediction API blueprint
        from .api import prediction_api
        app.register_blueprint(prediction_api.prediction_bp)

    return app
