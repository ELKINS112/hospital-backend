from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import token_required, role_required
from routes.admin import admin_bp
from routes.doctor import doctor_bp
from routes.nurse import nurse_bp
from routes.lab import lab_bp
from routes.patient import patient_bp
from routes.pharmacist import pharmacist_bp
from routes.accountant import accountant_bp
from create_all_role_users import create_users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
CORS(app)

# Register Blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(doctor_bp, url_prefix='/doctor')
app.register_blueprint(nurse_bp, url_prefix='/nurse')
app.register_blueprint(lab_bp, url_prefix='/lab')
app.register_blueprint(patient_bp, url_prefix='/patient')
app.register_blueprint(pharmacist_bp, url_prefix='/pharmacist')
app.register_blueprint(accountant_bp, url_prefix='/accountant')

with app.app_context():
    db.create_all()
    create_users()

if __name__ == '__main__':
    app.run(debug=True)
