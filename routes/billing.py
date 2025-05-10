from flask import Blueprint, request, jsonify
from models.bill import Bill, db

billing_bp = Blueprint('billing', __name__)

@billing_bp.route('/api/billing', methods=['POST'])
def create_bill():
    data = request.get_json()
    new_bill = Bill(
        patient_id=data['patient_id'],
        items=",".join(data['items']),
        total_amount=data['total_amount'],
        payment_method=data['payment_method'],
        status=data.get('status', 'Unpaid')
    )
    db.session.add(new_bill)
    db.session.commit()
    return jsonify({'message': 'Bill created'}), 201

@billing_bp.route('/api/billing', methods=['GET'])
def get_bills():
    bills = Bill.query.all()
    return jsonify([{
        'id': b.id,
        'patient_id': b.patient_id,
        'items': b.items.split(","),
        'total_amount': b.total_amount,
        'payment_method': b.payment_method,
        'status': b.status
    } for b in bills])
