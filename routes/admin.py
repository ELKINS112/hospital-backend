from flask import Blueprint, jsonify
from auth import token_required, role_required

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@token_required
@role_required('admin')
def admin_dashboard(current_user):
    return jsonify({'message': f'Welcome Admin {current_user.email}'})
