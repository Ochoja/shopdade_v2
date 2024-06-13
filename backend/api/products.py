from flask import Blueprint, request, jsonify
from models.product import Product
from api.extensions import mongo
from bson.json_util import dumps
import re


product = Blueprint("product", __name__)


@product.route("/add/", methods=["POST"])
def add_item():
    """Add item to products collection"""
    item = Product.from_dict(request.json)
    id = mongo.db.products.insert_one(item.to_dict()).inserted_id

    return f"Item id:{id}"


@product.route("/search/<query>")
def find_product(query: str) -> list[dict]:
    """Find one or more products"""
    print(query)
    words = query.split("_")
    regex_pattern = "|".join([re.escape(word) for word in words])
    print(regex_pattern)
    query = {
        "$or": [
            {"name": {"$regex": regex_pattern, "$options": "i"}},
            {"description": {"$regex": regex_pattern, "$options": "i"}}
        ]
    }
    results = mongo.db.products.find(query)

    for result in results:
        print(result)
    return jsonify({"result": "successful"})


@product.route("/search/<category>/<query>/")
def find_by_category(category: str, query: str) -> list[dict]:
    """Find products in a category"""
    words = query.split("_")
    regex_pattern = "|".join([re.escape(word) for word in words])
    query = {
        "$or": [
            {"name": {"$regex": regex_pattern, "$options": "i"}},
            {"description": {"$regex": regex_pattern, "$options": "i"}}
        ],
        "category": category
    }

    results = mongo.db.products.find(query)

    res = [result for result in results]

    return (dumps(res))
