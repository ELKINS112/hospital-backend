from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100))
    quantity = db.Column(db.Integer, default=0)
    expiry_date = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    supplier = db.Column(db.String(100))
