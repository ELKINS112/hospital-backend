from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models.user import User
from extensions import db
import jwt, datetime
from flask import current_app as app

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        'user_id': user.id,
        'role': user.role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, 'secret_key', algorithm='HS256')

    return jsonify({'token': token, 'role': user.role})
