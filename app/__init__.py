from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])

    # Configuration settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # SQLite database path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False          # Disable SQLAlchemy event notifications

    # Register Blueprints
    from .routes import main  # Import the blueprint from routes.py
    app.register_blueprint(main)

    # Initialize Extensions
    from .database import init_db
    init_db(app)

    return app
