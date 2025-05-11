from flask import Blueprint, jsonify
from auth import token_required, role_required

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctor')

@doctor_bp.route('/patients', methods=['GET'])
@token_required
@role_required('doctor')
def doctor_patients(current_user):
    return jsonify({'message': 'Doctor Patients accessed by ' + current_user.email})
