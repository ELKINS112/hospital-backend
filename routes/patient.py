from flask import Blueprint, jsonify
from routes.auth import token_required, role_required

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/patient/dashboard')
@token_required
@role_required('patient')
def dashboard(current_user):
    return jsonify({'message': 'Welcome patient!', 'user': current_user.email})
