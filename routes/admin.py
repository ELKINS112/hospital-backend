from flask import Blueprint, jsonify
from routes.auth import token_required, role_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/dashboard')
@token_required
@role_required('admin')
def dashboard(current_user):
    return jsonify({'message': 'Welcome admin!', 'user': current_user.email})
