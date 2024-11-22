from flask import Flask

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

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
