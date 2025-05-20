from flask import Blueprint

accountant_bp = Blueprint('accountant', __name__)

@accountant_bp.route('/')
def accountant_dashboard():
    return "Accountant Dashboard"
