from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import jwt
import datetime

from models.user import db, User
from auth import token_required, role_required

from routes.admin import admin_bp
from routes.doctor import doctor_bp
from routes.nurse import nurse_bp
from routes.pharmacist import pharmacist_bp
from routes.accountant import accountant_bp
from routes.lab import lab_bp
from routes.patient import patient_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SECRET_KEY'] = 'your-secret-key'

db.init_app(app)
CORS(app)

# Register routes
app.register_blueprint(admin_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(nurse_bp)
app.register_blueprint(pharmacist_bp)
app.register_blueprint(accountant_bp)
app.register_blueprint(lab_bp)
app.register_blueprint(patient_bp)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()

    if user and user.check_password(data.get('password')):
        token = jwt.encode({
            'user_id': user.id,
            'role': user.role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401

# Auto-create users on startup
from create_all_role_users import *

if __name__ == '__main__':
    app.run(debug=True)
