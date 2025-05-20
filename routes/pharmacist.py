from flask import Blueprint

pharmacist_bp = Blueprint('pharmacist', __name__)

@pharmacist_bp.route('/')
def pharmacist_dashboard():
    return "Pharmacist Dashboard"
