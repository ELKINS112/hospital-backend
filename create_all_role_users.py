from models.user import db, User
from app import app

with app.app_context():
    users = [
        {"email": "admin@example.com", "password": "admin123", "role": "admin"},
        {"email": "doctor@example.com", "password": "doctor123", "role": "doctor"},
        {"email": "nurse@example.com", "password": "nurse123", "role": "nurse"},
        {"email": "pharmacist@example.com", "password": "pharma123", "role": "pharmacist"},
        {"email": "lab@example.com", "password": "lab123", "role": "lab"},
        {"email": "accountant@example.com", "password": "account123", "role": "accountant"},
        {"email": "patient@example.com", "password": "patient123", "role": "patient"}
    ]

    for u in users:
        if not User.query.filter_by(email=u["email"]).first():
            user = User(email=u["email"], role=u["role"])
            user.set_password(u["password"])
            db.session.add(user)
            print(f"Created user: {u['email']}")

    db.session.commit()
    print("All predefined users added successfully.")
