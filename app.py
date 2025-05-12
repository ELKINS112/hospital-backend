from flask import Flask
from flask_cors import CORS
from models.user import db
from routes.admin import admin_bp
from routes.doctor import doctor_bp
from routes.nurse import nurse_bp
from routes.lab import lab_bp
from routes.pharmacist import pharmacist_bp
from routes.accountant import accountant_bp
from routes.patient import patient_bp
from auth import token_required, role_required
from auth_routes import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'super-secret'
CORS(app)
db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(nurse_bp)
app.register_blueprint(lab_bp)
app.register_blueprint(pharmacist_bp)
app.register_blueprint(accountant_bp)
app.register_blueprint(patient_bp)

with app.app_context():
    db.create_all()  # ✅ Create tables first
    from create_all_role_users import *  # ✅ Then insert predefined users

if __name__ == "__main__":
    app.run(debug=True)
