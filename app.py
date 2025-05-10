import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from models.pharmacy import db
from routes.pharmacy import pharmacy_bp
from routes.billing import billing_bp
from routes.appointments import appointments_bp
from routes.lab import lab_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(pharmacy_bp)
app.register_blueprint(billing_bp)
app.register_blueprint(appointments_bp)
app.register_blueprint(lab_bp)

@app.route('/')
def home():
    return {'message': 'Hospital Management Full Backend Running'}

if __name__ == '__main__':
    app.run(debug=True)
