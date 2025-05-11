from flask import Blueprint, jsonify
from auth import token_required, role_required

pharmacist_bp = Blueprint('pharmacist', __name__, url_prefix='/pharmacist')

@pharmacist_bp.route('/inventory', methods=['GET'])
@token_required
@role_required('pharmacist')
def pharmacist_inventory(current_user):
    return jsonify({'message': 'Pharmacist Inventory accessed by ' + current_user.email})
