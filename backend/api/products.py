from flask import Blueprint, request, jsonify
from models.product import Product
from api.extensions import mongo


product = Blueprint("product", __name__)


@product.route("/add/", methods=["POST"])
def add_item():
    """Add item to products collection"""
    item = Product.from_dict(request.json)
    id = mongo.db.products.insert_one(item.to_dict()).inserted_id
    print(type(id))

    return f"Item id:{id}"


@product.route("/find/",)
def find_item(name):
    """Find one or more products"""
    name = request.args.get("name")
    result = mongo.db.products.find_many({"name": name})
    return jsonify(result)
