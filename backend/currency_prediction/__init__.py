from flask import Flask

def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__)

    with app.app_context():
        # Import and register blueprints
        from .api import prediction_api
        app.register_blueprint(prediction_api.prediction_bp)

    return app
