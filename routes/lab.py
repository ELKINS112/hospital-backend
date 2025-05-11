from flask import Blueprint, jsonify
from auth import token_required, role_required

lab_bp = Blueprint('lab', __name__, url_prefix='/lab')

@lab_bp.route('/results', methods=['GET'])
@token_required
@role_required('lab')
def lab_results(current_user):
    return jsonify({'message': 'Lab Results accessed by ' + current_user.email})
