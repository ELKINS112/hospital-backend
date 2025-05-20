
from flask import Blueprint, jsonify

pharmacy_bp = Blueprint('pharmacy', __name__, url_prefix='/pharmacy')

@pharmacy_bp.route('/')
def index():
    return jsonify({'message': 'Pharmacy API is active'})
