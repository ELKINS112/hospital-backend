from flask import Blueprint, jsonify
from routes.auth import token_required, role_required

lab_bp = Blueprint('lab', __name__)

@lab_bp.route('/lab/dashboard')
@token_required
@role_required('lab')
def dashboard(current_user):
    return jsonify({'message': 'Welcome lab!', 'user': current_user.email})
