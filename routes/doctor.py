from flask import Blueprint, jsonify
from routes.auth import token_required, role_required

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/doctor/dashboard')
@token_required
@role_required('doctor')
def dashboard(current_user):
    return jsonify({'message': 'Welcome doctor!', 'user': current_user.email})
