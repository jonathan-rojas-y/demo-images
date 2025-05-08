from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import main  # Import the main module to register routes

    return app