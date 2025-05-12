from flask import Blueprint, jsonify
from routes.auth import token_required, role_required

nurse_bp = Blueprint('nurse', __name__)

@nurse_bp.route('/nurse/dashboard')
@token_required
@role_required('nurse')
def dashboard(current_user):
    return jsonify({'message': 'Welcome nurse!', 'user': current_user.email})
