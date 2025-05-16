from flask import Blueprint

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/')
def patient_dashboard():
    return "Patient Dashboard"
