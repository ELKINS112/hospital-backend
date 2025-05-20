
from flask import Blueprint, jsonify

medical_record_bp = Blueprint('medical_record', __name__, url_prefix='/medical_record')

@medical_record_bp.route('/')
def index():
    return jsonify({"message": "Medical Record API is active"})
