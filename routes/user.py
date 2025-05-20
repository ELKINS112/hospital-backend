
from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'error': 'User already exists'}), 400
    new_user = User(
        full_name=data['full_name'],
        email=data['email'],
        password=generate_password_hash(data['password']),
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([
        {
            'id': u.id,
            'full_name': u.full_name,
            'email': u.email,
            'role': u.role
        } for u in users
    ])

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
