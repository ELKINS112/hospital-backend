from flask import Blueprint, jsonify
from auth import token_required, role_required

nurse_bp = Blueprint('nurse', __name__, url_prefix='/nurse')

@nurse_bp.route('/appointments', methods=['GET'])
@token_required
@role_required('nurse')
def nurse_appointments(current_user):
    return jsonify({'message': 'Nurse Appointments accessed by ' + current_user.email})
