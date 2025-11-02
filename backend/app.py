from flask import Flask

from api.prediction_api import prediction_bp

app = Flask(__name__)

app.register_blueprint(prediction_bp)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
