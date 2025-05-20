
from flask import Blueprint, jsonify

billing_bp = Blueprint('billing', __name__, url_prefix='/billing')

@billing_bp.route('/')
def index():
    return jsonify({'message': 'Billing API is active'})
