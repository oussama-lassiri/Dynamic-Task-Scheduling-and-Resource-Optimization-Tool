from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .models import db
from flask_cors import CORS

migrate = Migrate() 
jwt = JWTManager()

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])

    # Configuration settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # SQLite database path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False          # Disable SQLAlchemy event notifications
    app.config['JWT_SECRET_KEY'] = 'ThisIsMySecretKey2@24'
    
    # Initialize Extensions
    from .database import init_db
    init_db(app)
    
    # migrate the changes
    migrate.init_app(app, db)
    
    # initialize the JWT with app
    jwt.init_app(app)

    # Register Blueprints
    from .routes import main  # Import the blueprint from routes.py
    app.register_blueprint(main)
    
   
    return app
