from flask import jsonify, request
from models.models import db, Film

def get_films():
    films = Film.query.all()
    results = [film.to_dict() for film in films]
    return jsonify(results)

def get_film(film_id):
    film = Film.query.get(film_id)
    if not film:
        return jsonify({'message': 'Film not found'}), 404
    return jsonify(film.to_dict())

def add_film():
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'release_year', 'director_id', 'genre_id')):
        return jsonify({'message': 'Invalid data'}), 400
    new_film = Film(title=data['title'], release_year=data['release_year'], director_id=data['director_id'], genre_id=data['genre_id'])
    db.session.add(new_film)
    db.session.commit()
    return jsonify(new_film.to_dict()), 201

def update_film(film_id):
    film = Film.query.get(film_id)
    if not film:
        return jsonify({'message': 'Film not found'}), 404
    data = request.get_json()
    film.title = data.get('title', film.title)
    film.release_year = data.get('release_year', film.release_year)
    film.director_id = data.get('director_id', film.director_id)
    film.genre_id = data.get('genre_id', film.genre_id)
    db.session.commit()
    return jsonify(film.to_dict())

def delete_film(film_id):
    film = Film.query.get(film_id)
    if not film:
        return jsonify({'message': 'Film not found'}), 404
    db.session.delete(film)
    db.session.commit()
    return jsonify({'message': 'Film deleted successfully'})
