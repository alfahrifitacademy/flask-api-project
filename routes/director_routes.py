from flask import Blueprint
from controllers.director_controller import get_directors, get_director, add_director, update_director, delete_director

director_bp = Blueprint('director_bp', __name__)

director_bp.route('/api/directors', methods=['GET'])(get_directors)
director_bp.route('/api/directors/<int:director_id>', methods=['GET'])(get_director)
director_bp.route('/api/directors', methods=['POST'])(add_director)
director_bp.route('/api/directors/<int:director_id>', methods=['PUT'])(update_director)
director_bp.route('/api/directors/<int:director_id>', methods=['DELETE'])(delete_director)
