from flask import Flask
from api.products import product
from api.extensions import mongo


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/shopDADE"
    mongo.init_app(app)

    # blueprints
    app.register_blueprint(product, url_prefix="/api")

    return app
