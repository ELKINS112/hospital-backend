from flask import Blueprint, jsonify
from auth import token_required, role_required

accountant_bp = Blueprint('accountant', __name__, url_prefix='/accountant')

@accountant_bp.route('/invoices', methods=['GET'])
@token_required
@role_required('accountant')
def accountant_invoices(current_user):
    return jsonify({'message': 'Accountant Invoices accessed by ' + current_user.email})
