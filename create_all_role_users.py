from models import User, db
from werkzeug.security import generate_password_hash

def create_users():
    users = [
        {"email": "admin@example.com", "password": "admin123", "role": "admin"},
        {"email": "doctor@example.com", "password": "doctor123", "role": "doctor"},
        {"email": "nurse@example.com", "password": "nurse123", "role": "nurse"},
        {"email": "lab@example.com", "password": "lab123", "role": "lab"},
        {"email": "patient@example.com", "password": "patient123", "role": "patient"},
        {"email": "pharmacist@example.com", "password": "pharm123", "role": "pharmacist"},
        {"email": "accountant@example.com", "password": "acct123", "role": "accountant"},
    ]

    for u in users:
        if not User.query.filter_by(email=u["email"]).first():
            user = User(email=u["email"], password_hash=generate_password_hash(u["password"]), role=u["role"])
            db.session.add(user)
    db.session.commit()
