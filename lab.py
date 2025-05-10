from flask import Blueprint, request, jsonify
from models.lab import LabTest, db

lab_bp = Blueprint('lab', __name__)

@lab_bp.route('/api/lab-tests', methods=['POST'])
def create_lab_test():
    data = request.get_json()
    new_test = LabTest(
        patient_id=data['patient_id'],
        test_name=data['test_name'],
        doctor_name=data.get('doctor_name', ''),
        test_date=data.get('test_date'),
        result=data.get('result', ''),
        status=data.get('status', 'Pending')
    )
    db.session.add(new_test)
    db.session.commit()
    return jsonify({'message': 'Lab test created successfully'}), 201

@lab_bp.route('/api/lab-tests', methods=['GET'])
def get_lab_tests():
    tests = LabTest.query.all()
    return jsonify([{
        'id': t.id,
        'patient_id': t.patient_id,
        'test_name': t.test_name,
        'doctor_name': t.doctor_name,
        'test_date': t.test_date,
        'result': t.result,
        'status': t.status
    } for t in tests])
