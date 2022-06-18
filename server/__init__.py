# Modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Blueprints
from blueprints.main import main
from blueprints.auth import auth

BLUEPRINTS = [main, auth]

# Initialise SQLALCHEMY
db = SQLAlchemy()

def get_secret_key():
    with open("secrets/secret.key", "r") as f:
        return f.read()

def create_app():
    # Create flask app instance
    app = Flask(__name__)
    
    # Set config, namely secret key
    app.config['SECRET_KEY'] = get_secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.sqlite'

    db.init_app(app)
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
    
