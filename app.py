from flask import Flask
from flask_cors import CORS
from extensions import db
from models.user import User
from create_all_role_users import create_users

from routes.admin import admin_bp
from routes.doctor import doctor_bp
from routes.nurse import nurse_bp
from routes.lab import lab_bp
from routes.pharmacist import pharmacist_bp
from routes.accountant import accountant_bp
from routes.patient import patient_bp
from routes.auth import auth_bp
from routes.pharmacy import pharmacy_bp
from routes.billing import billing_bp
from routes.medical_record import medical_record_bp
from routes.staff import staff_bp
from routes.appointment import appointment_bp
from routes.user import user_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    create_users()

app.register_blueprint(admin_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(nurse_bp)
app.register_blueprint(lab_bp)
app.register_blueprint(pharmacist_bp)
app.register_blueprint(accountant_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(pharmacy_bp)
app.register_blueprint(billing_bp)
app.register_blueprint(medical_record_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(user_bp)
