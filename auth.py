from functools import wraps
from flask import request, jsonify, current_app
import jwt
from models.user import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
            token = bearer.split(" ")[1] if " " in bearer else bearer
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid or expired!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def wrapped(current_user, *args, **kwargs):
            if current_user.role != required_role:
                return jsonify({'message': 'Forbidden: Insufficient privileges'}), 403
            return f(current_user, *args, **kwargs)
        return wrapped
    return decorator
