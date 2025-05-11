from flask import Blueprint, jsonify
from auth import token_required, role_required

patient_bp = Blueprint('patient', __name__, url_prefix='/patient')

@patient_bp.route('/profile', methods=['GET'])
@token_required
@role_required('patient')
def patient_profile(current_user):
    return jsonify({'message': 'Patient Profile accessed by ' + current_user.email})
