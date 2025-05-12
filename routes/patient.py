from flask import Blueprint, jsonify
from auth import token_required, role_required

patient_bp = Blueprint('patient_bp', __name__, url_prefix='/patient')

@patient_bp.route('/dashboard')
@token_required
@role_required('patient')
def patient_dashboard(current_user):
    return jsonify({'message': 'Welcome Patient ' + current_user.email})
