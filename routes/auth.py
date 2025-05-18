from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models.user import User
from extensions import db
import jwt
import datetime

# ✅ Define Blueprint before using it
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"message": "Missing email or password"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password_hash, data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode(
        {
            "user_id": user.id,
            "role": user.role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        "secret-key",
        algorithm="HS256"
    )

    return jsonify({
    "token": token,
    "role": user.role,
    "name": user.full_name
}), 200

