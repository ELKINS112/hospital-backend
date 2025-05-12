from flask import Blueprint, jsonify
from auth import token_required, role_required

pharmacist_bp = Blueprint('pharmacist_bp', __name__, url_prefix='/pharmacist')

@pharmacist_bp.route('/dashboard')
@token_required
@role_required('pharmacist')
def pharmacist_dashboard(current_user):
    return jsonify({'message': 'Welcome Pharmacist ' + current_user.email})
