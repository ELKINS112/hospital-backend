from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LabTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(100), nullable=False)
    test_name = db.Column(db.String(100), nullable=False)
    doctor_name = db.Column(db.String(100))
    test_date = db.Column(db.String(50))
    result = db.Column(db.Text)
    status = db.Column(db.String(50), default="Pending")
