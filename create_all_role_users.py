from models.user import db, User
from app import app

with app.app_context():
    db.create_all()
    roles = {
        'admin@example.com': 'admin',
        'nurse@example.com': 'nurse',
        'doctor@example.com': 'doctor',
        'pharmacist@example.com': 'pharmacist',
        'accountant@example.com': 'accountant',
        'patient@example.com': 'patient',
        'lab@example.com': 'lab'
    }

    for email, role in roles.items():
        if not User.query.filter_by(email=email).first():
            user = User(email=email, role=role)
            user.set_password('secret')
            db.session.add(user)

    db.session.commit()
    print("All role-based demo users created.")
