
from flask import Blueprint, jsonify
from auth import token_required, role_required

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/dashboard', methods=['GET'])
@token_required
@role_required(['patient'])
def dashboard(current_user):
    return jsonify({
        "message": "Welcome to the Patient Dashboard",
        "user": current_user.username
    })
