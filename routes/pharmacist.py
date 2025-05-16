
from flask import Blueprint, jsonify
from auth import token_required, role_required

pharmacist_bp = Blueprint('pharmacist', __name__)

@pharmacist_bp.route('/dashboard', methods=['GET'])
@token_required
@role_required(['pharmacist'])
def dashboard(current_user):
    return jsonify({
        "message": "Welcome to the Pharmacist Dashboard",
        "user": current_user.username
    })
