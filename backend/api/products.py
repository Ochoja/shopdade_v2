from flask import Blueprint, request, jsonify
from models.product import Product
from api.extensions import mongo
import re


product = Blueprint("product", __name__)


@product.route("/add/", methods=["POST"])
def add_item():
    """Add item to products collection"""
    item = Product.from_dict(request.json)
    id = mongo.db.products.insert_one(item.to_dict()).inserted_id
    print(type(id))

    return f"Item id:{id}"


@product.route("/search/<query>/",)
def find_product(query: str) -> list[dict]:
    """Find one or more products"""
    query = request.args.get("query")
    words = query.split()
    regex_pattern = "|".join([re.escape(word) for word in words])
    query = {
        "$or": [
            {"name": {"$regex": regex_pattern}, "$options": "i"},
            {"description": {"$regex": regex_pattern, "$options": "i"}}
        ]
    }
    result = mongo.db.products.find_many(query)
    return jsonify(result)


@product.route("/search/<category>/<query>/")
def find_by_category(category: str, query: str) -> list[dict]:
    """Find products in a category"""
    category = request.args.get("category")
    query = request.args.get("query")
    words = query.split()
    regex_pattern = "|".join([re.escape(word) for word in words])
    query = {
        "$or": [
            {"name": {"$regex": regex_pattern}, "$options": "i"},
            {"description": {"$regex": regex_pattern, "$options": "i"}}
        ],
        "category": category
    }

    result = mongo.db.products.find_many(query)
    return jsonify(result)
