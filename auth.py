from flask import request, jsonify
import jwt
from functools import wraps
from models import User
from app import app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['user_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated(user, *args, **kwargs):
            if user.role != role:
                return jsonify({'message': 'Access Denied'}), 403
            return f(user, *args, **kwargs)
        return decorated
    return wrapper
