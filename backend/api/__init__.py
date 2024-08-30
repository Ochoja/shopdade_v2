from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from api.products import product
from api.extensions import mongo
from api.extensions import bcrypt
from api.extensions import jwt
from api.auth.auth import auth
import os

# Get current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct path to .env file in the root directory
env_path = os.path.join(current_directory, '..', '.env')

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("mongo_uri")
    app.config["JWT_SECRET_KEY"] = os.getenv("jwt_secret_key")
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_SAMESITE'] = 'None'
    app.config['JWT_COOKIE_SECURE'] = True
    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app, supports_credentials=True)

    # blueprints
    app.register_blueprint(product, url_prefix="/api")
    app.register_blueprint(auth, url_prefix="/api")

    return app
