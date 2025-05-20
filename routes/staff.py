
from flask import Blueprint, jsonify

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

@staff_bp.route('/')
def index():
    return jsonify({"message": "Staff API is active"})
