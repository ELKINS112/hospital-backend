from flask import Blueprint, jsonify
from routes.auth import token_required, role_required

pharmacist_bp = Blueprint('pharmacist', __name__)

@pharmacist_bp.route('/pharmacist/dashboard')
@token_required
@role_required('pharmacist')
def dashboard(current_user):
    return jsonify({'message': 'Welcome pharmacist!', 'user': current_user.email})
