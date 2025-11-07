# app.py
# This is the heart of our Flask backend.
# It's the first file that gets run and it's responsible for starting up the whole application.

from currency_prediction import create_app

# We're creating an instance of our Flask app here.
# The `create_app` function is a factory that builds our app,
# which is a nice way to keep our code organized.
app = create_app()

# This is a standard Python thing. It means that the code inside this block
# will only run when you execute this file directly (e.g., `python app.py`).
# It won't run if you import this file into another file.
if __name__ == '__main__':
    # We're running the app in debug mode here.
    # This is great for development because it gives us helpful error messages
    # and automatically reloads the server when we make changes.
    # For a real, live application, we'd want to use a more robust server.
    app.run(debug=True)
