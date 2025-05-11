from flask import Blueprint, jsonify
from auth import token_required, role_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard', methods=['GET'])
@token_required
@role_required('admin')
def admin_dashboard(current_user):
    return jsonify({'message': 'Admin Dashboard accessed by ' + current_user.email})
