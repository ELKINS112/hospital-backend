
from flask import Blueprint, jsonify

appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointment')

@appointment_bp.route('/')
def index():
    return jsonify({"message": "Appointment API is active"})
