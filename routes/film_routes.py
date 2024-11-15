from flask import Blueprint
from controllers.film_controller import get_films, get_film, add_film, update_film, delete_film

film_bp = Blueprint('film_bp', __name__)

film_bp.route('/api/films', methods=['GET'])(get_films)
film_bp.route('/api/films/<int:film_id>', methods=['GET'])(get_film)
film_bp.route('/api/films', methods=['POST'])(add_film)
film_bp.route('/api/films/<int:film_id>', methods=['PUT'])(update_film)
film_bp.route('/api/films/<int:film_id>', methods=['DELETE'])(delete_film)
