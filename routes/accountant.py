
from flask import Blueprint, jsonify
from auth import token_required, role_required

accountant_bp = Blueprint('accountant', __name__)

@accountant_bp.route('/dashboard', methods=['GET'])
@token_required
@role_required(['accountant'])
def dashboard(current_user):
    return jsonify({
        "message": "Welcome to the Accountant Dashboard",
        "user": current_user.username
    })
