from flask import Blueprint, jsonify
from auth import token_required, role_required

nurse_bp = Blueprint('nurse_bp', __name__, url_prefix='/nurse')

@nurse_bp.route('/dashboard')
@token_required
@role_required('nurse')
def nurse_dashboard(current_user):
    return jsonify({'message': 'Welcome Nurse ' + current_user.email})
