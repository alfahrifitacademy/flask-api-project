from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Inisialisasi SQLAlchemy tanpa diikat ke aplikasi
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi database (gunakan nama db_movie)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://alfahri:alfahri123@localhost/db_movie'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inisialisasi SQLAlchemy dengan aplikasi
    db.init_app(app)

    return app
