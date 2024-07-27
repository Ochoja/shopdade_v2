from flask import Blueprint, request, jsonify
from api.extensions import mongo
from api.extensions import bcrypt


auth = Blueprint("auth", __name__)


@auth.route("/sign_up/", methods=["POST"])
def create_account():
    """Create user's account"""
    pw_hash = bcrypt.generate_password_hash(
        request.form.get('password')).decode('utf-8')

    try:
        if mongo.db.users.find_one({"email": request.form.get('email')}):
            return "Account already exists", 409
        user_data = {"full_name": request.form.get(
            'full_name'), "email": request.form.get('email'), "password": pw_hash}

        inserted_id = mongo.db.users.insert_one(user_data)
    except Exception as e:
        return f"Error: {e}"

    return jsonify(f"Account created successfully {inserted_id}")
