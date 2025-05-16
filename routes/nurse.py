
from flask import Blueprint, jsonify
from auth import token_required, role_required

nurse_bp = Blueprint('nurse', __name__)

@nurse_bp.route('/dashboard', methods=['GET'])
@token_required
@role_required(['nurse'])
def dashboard(current_user):
    return jsonify({
        "message": "Welcome to the Nurse Dashboard",
        "user": current_user.username
    })
