from flask import Blueprint

nurse_bp = Blueprint('nurse', __name__)

@nurse_bp.route('/')
def nurse_dashboard():
    return "Nurse Dashboard"
