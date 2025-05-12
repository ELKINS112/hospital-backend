from flask import Blueprint, jsonify
from auth import token_required, role_required

doctor_bp = Blueprint('doctor_bp', __name__, url_prefix='/doctor')

@doctor_bp.route('/dashboard')
@token_required
@role_required('doctor')
def doctor_dashboard(current_user):
    return jsonify({'message': f'Welcome Doctor {current_user.email}'})
