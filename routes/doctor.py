
from flask import Blueprint, jsonify
from auth import token_required, role_required

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/dashboard', methods=['GET'])
@token_required
@role_required(['doctor'])
def dashboard(current_user):
    return jsonify({
        "message": "Welcome to the Doctor Dashboard",
        "user": current_user.username
    })
