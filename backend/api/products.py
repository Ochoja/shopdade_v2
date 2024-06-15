from flask import Blueprint, request, jsonify
from models.product import Product
from api.extensions import mongo
from bson.json_util import dumps
import re


product = Blueprint("product", __name__)


@product.route("/add/", methods=["POST"])
def add_item() -> str:
    """Add item to products collection"""
    item = Product.from_dict(request.json)
    id = mongo.db.products.insert_one(item.to_dict()).inserted_id

    return f"Item id:{id}"


@product.route("/products/")
def show_products() -> list[dict]:
    """Returns a list of products based on offset and limit"""
    offset = request.args.get("offset")  # number of documents to be skipped
    limit = request.args.get("limit")  # number of items to be displayed

    if limit and not offset:
        results = mongo.db.products.find().limit(limit)
        res = [result for result in results]
        return dumps(res)
    if offset and limit:
        results = mongo.db.products.find().skip(offset).limit(limit)
        res = [result for result in results]
        return dumps(res)
    else:
        results = mongo.db.products.find().limit(10)
        res = [result for result in results]
        return dumps(res)


@product.route("/search/<query>")
def find_product(query: str) -> list[dict]:
    """Find one or more products"""
    offset = request.args.get("offset")
    words = query.split("-")
    regex_pattern = "|".join([re.escape(word) for word in words])
    query = {
        "$or": [
            {"name": {"$regex": regex_pattern, "$options": "i"}},
            {"description": {"$regex": regex_pattern, "$options": "i"}}
        ]
    }

    results = mongo.db.products.find(query).offset(offset).limit(
        10) if offset else mongo.db.products.find(query).limit(10)
    res = [result for result in results]

    return dumps(res)


@product.route("/search/<category>/<query>/")
def find_by_category(category: str, query: str) -> list[dict]:
    """Find products in a category"""
    offset = request.args.get("offset")
    words = query.split("-")
    regex_pattern = "|".join([re.escape(word) for word in words])
    query = {
        "$or": [
            {"name": {"$regex": regex_pattern, "$options": "i"}},
            {"description": {"$regex": regex_pattern, "$options": "i"}}
        ],
        "category": category
    }

    results = mongo.db.products.find(query).limit(10).offset(
        offset) if offset else mongo.db.products.find(query).limit(10)
    res = [result for result in results]

    return (dumps(res))
