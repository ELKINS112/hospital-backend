from flask import Blueprint, jsonify
from routes.auth import token_required, role_required

accountant_bp = Blueprint('accountant', __name__)

@accountant_bp.route('/accountant/dashboard')
@token_required
@role_required('accountant')
def dashboard(current_user):
    return jsonify({'message': 'Welcome accountant!', 'user': current_user.email})
