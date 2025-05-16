from flask import Blueprint

lab_bp = Blueprint('lab', __name__)

@lab_bp.route('/')
def lab_dashboard():
    return "Lab Dashboard"
