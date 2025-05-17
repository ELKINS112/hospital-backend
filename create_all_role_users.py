from werkzeug.security import generate_password_hash
from models.user import User
from extensions import db

def create_users():
    users = [
        {"full_name": "Admin User", "email": "admin@example.com", "password": "adminpass", "role": "admin"},
        {"full_name": "Doctor John", "email": "doctor@example.com", "password": "doctorpass", "role": "doctor"},
        {"full_name": "Nurse Joy", "email": "nurse@example.com", "password": "nursepass", "role": "nurse"},
        {"full_name": "Lab Tech", "email": "lab@example.com", "password": "labpass", "role": "lab"},
        {"full_name": "Pharmacist Paul", "email": "pharmacist@example.com", "password": "pharmacistpass", "role": "pharmacist"},
        {"full_name": "Accountant Ann", "email": "accountant@example.com", "password": "accountantpass", "role": "accountant"},
        {"full_name": "Patient Peter", "email": "patient@example.com", "password": "patientpass", "role": "patient"},
    ]
    for u in users:
        if not User.query.filter_by(email=u['email']).first():
            new_user = User(
                full_name=u['full_name'],
                email=u['email'],
                password_hash=generate_password_hash(u['password']),
                role=u['role']
            )
            db.session.add(new_user)

    db.session.commit()
