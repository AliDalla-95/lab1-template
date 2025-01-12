from flask import Blueprint, jsonify, request, url_for
from .models import Person
from .schemas import PersonRequestSchema, PersonResponseSchema
from . import db

person_bp = Blueprint('person', __name__, url_prefix='/api/v1')
person_request_schema = PersonRequestSchema()
person_response_schema = PersonResponseSchema()

@person_bp.route('/persons', methods=['GET'])
def list_persons():
    persons = Person.query.all()
    return jsonify(person_response_schema.dump(persons, many=True)), 200

@person_bp.route('/persons', methods=['POST'])
def create_person():
    data = request.json
    errors = person_request_schema.validate(data)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    new_person = Person(**data)
    db.session.add(new_person)
    db.session.commit()

    return jsonify(person_response_schema.dump(new_person)), 201, {'Location': url_for('person.get_person', id=new_person.id)}

@person_bp.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get_or_404(id)
    return jsonify(person_response_schema.dump(person)), 200

@person_bp.route('/persons/<int:id>', methods=['PATCH'])
def edit_person(id):
    person = Person.query.get_or_404(id)
    data = request.json
    errors = person_request_schema.validate(data, partial=True)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    for key, value in data.items():
        setattr(person, key, value)

    db.session.commit()
    return jsonify(person_response_schema.dump(person)), 200

@person_bp.route('/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return '', 204