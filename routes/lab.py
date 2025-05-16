
from flask import Blueprint, jsonify
from auth import token_required, role_required

lab_bp = Blueprint('lab', __name__)

@lab_bp.route('/dashboard', methods=['GET'])
@token_required
@role_required(['lab'])
def dashboard(current_user):
    return jsonify({
        "message": "Welcome to the Lab Dashboard",
        "user": current_user.username
    })
