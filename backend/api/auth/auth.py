from flask import Blueprint, request, jsonify, make_response
from api.extensions import mongo
from api.extensions import bcrypt
from flask_jwt_extended import create_access_token


auth = Blueprint("auth", __name__)


@auth.route("/sign_up/", methods=["POST"])
def create_account():
    """Create user's account"""
    pw_hash = bcrypt.generate_password_hash(
        request.json.get('password')).decode('utf-8')

    try:
        if mongo.db.users.find_one({"email": request.json.get('email')}):
            return "Account already exists", 409
        user_data = {"full_name": request.json.get(
            'full_name'), "email": request.json.get('email'), "password": pw_hash}

        inserted_id = mongo.db.users.insert_one(user_data)
    except Exception as e:
        return f"Error: {e}"

    return jsonify(f"Account created successfully {inserted_id}")


@auth.route("/login/", methods=["POST"])
def login():
    """Login to user's account"""
    try:
        # check if user exists
        user = mongo.db.users.find_one_or_404(
            {"email": request.json.get("email")})
        # Check if passwords match
        check_pw = bcrypt.check_password_hash(user.get("password"), request.json.get(
            "password"))

        if check_pw:
            access_token = create_access_token(identity=user.get("email"))
            response = make_response("Login Successful")
            response.set_cookie("access_token", access_token)
            return response
        else:
            return "Incorrect Email or Password", 401
    except Exception as e:
        return f"Error: {e}"
