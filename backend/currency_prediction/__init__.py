# currency_prediction/__init__.py
# This file is like the constructor for our application.
# It's responsible for creating and configuring the Flask app.

from flask import Flask

def create_app():
    """
    This is our application factory. It creates and configures the Flask app.
    Using a factory function is a good practice because it allows us to create
    different instances of the app for different purposes (e.g., one for testing,
    one for production).
    """
    # Create the Flask app instance.
    # `__name__` is a special Python variable that gives the name of the current module.
    # Flask uses this to know where to look for resources like templates and static files.
    app = Flask(__name__)

    # The app_context is a special Flask thing that makes the application instance
    # available to other parts of our code. We need it here to register our blueprint.
    with app.app_context():
        # We're importing our API blueprint here. A blueprint is a way to organize
        # a group of related views and other code. It's like a mini-app within our app.
        from .api import prediction_api
        # We're registering our blueprint with the app here. This makes the API
        # endpoints defined in the blueprint available to our application.
        app.register_blueprint(prediction_api.prediction_bp)

    # Finally, we return the app instance.
    return app
