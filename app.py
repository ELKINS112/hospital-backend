from flask import Flask
from flask_cors import CORS
from extensions import db
from models.user import User
from create_all_role_users import create_users

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ✅ FIXED INDENTATION
with app.app_context():
    db.create_all()
    create_users()
