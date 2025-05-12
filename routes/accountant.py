from flask import Blueprint, jsonify
from auth import token_required, role_required

accountant_bp = Blueprint('accountant_bp', __name__, url_prefix='/accountant')

@accountant_bp.route('/dashboard')
@token_required
@role_required('accountant')
def accountant_dashboard(current_user):
    return jsonify({'message': 'Welcome Accountant ' + current_user.email})
