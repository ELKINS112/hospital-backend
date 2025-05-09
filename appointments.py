from flask import Blueprint, request, jsonify
from models.appointment import Appointment, db

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/api/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{
        'id': a.id,
        'patient_id': a.patient_id,
        'doctor_name': a.doctor_name,
        'date': a.date,
        'time': a.time
    } for a in appointments])

@appointments_bp.route('/api/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    new_appointment = Appointment(
        patient_id=data['patient_id'],
        doctor_name=data['doctor_name'],
        date=data['date'],
        time=data['time']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment created'}), 201
