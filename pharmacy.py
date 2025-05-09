from flask import Blueprint, request, jsonify
from models.pharmacy import Pharmacy, db

pharmacy_bp = Blueprint('pharmacy', __name__)

@pharmacy_bp.route('/api/pharmacy', methods=['GET'])
def get_medicines():
    medicines = Pharmacy.query.all()
    return jsonify([{
        'id': m.id,
        'name': m.name,
        'manufacturer': m.manufacturer,
        'quantity': m.quantity,
        'expiry_date': m.expiry_date,
        'price': m.price,
        'supplier': m.supplier
    } for m in medicines])

@pharmacy_bp.route('/api/pharmacy', methods=['POST'])
def add_medicine():
    data = request.get_json()
    new_medicine = Pharmacy(
        name=data['name'],
        manufacturer=data.get('manufacturer'),
        quantity=data.get('quantity'),
        expiry_date=data.get('expiry_date'),
        price=data.get('price'),
        supplier=data.get('supplier')
    )
    db.session.add(new_medicine)
    db.session.commit()
    return jsonify({'message': 'Medicine added successfully'}), 201
