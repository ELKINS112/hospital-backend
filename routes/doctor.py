from flask import Blueprint

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/')
def doctor_dashboard():
    return "Doctor Dashboard"
