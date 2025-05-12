from flask import Blueprint, jsonify
from auth import token_required, role_required

lab_bp = Blueprint('lab_bp', __name__, url_prefix='/lab')

@lab_bp.route('/dashboard')
@token_required
@role_required('lab')
def lab_dashboard(current_user):
    return jsonify({'message': 'Welcome Lab Technician ' + current_user.email})
