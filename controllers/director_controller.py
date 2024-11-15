from flask import jsonify, request
from models.models import db, Director

def get_directors():
    directors = Director.query.all()
    results = [director.to_dict() for director in directors]
    return jsonify(results)

def get_director(director_id):
    director = Director.query.get(director_id)
    if not director:
        return jsonify({'message': 'Director not found'}), 404
    return jsonify(director.to_dict())

def add_director():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'message': 'Invalid data'}), 400
    new_director = Director(name=data['name'])
    db.session.add(new_director)
    db.session.commit()
    return jsonify(new_director.to_dict()), 201

def update_director(director_id):
    director = Director.query.get(director_id)
    if not director:
        return jsonify({'message': 'Director not found'}), 404
    data = request.get_json()
    director.name = data.get('name', director.name)
    db.session.commit()
    return jsonify(director.to_dict())

def delete_director(director_id):
    director = Director.query.get(director_id)
    if not director:
        return jsonify({'message': 'Director not found'}), 404
    db.session.delete(director)
    db.session.commit()
    return jsonify({'message': 'Director deleted successfully'})
