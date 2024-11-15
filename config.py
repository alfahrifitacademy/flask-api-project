from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Inisialisasi SQLAlchemy tanpa diikat ke aplikasi
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi database (gunakan nama db_movie)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dbmovie_condition:3e8298c113c4e068502e9b52853c33f80e3b9dea@e6-t9.h.filess.io:3307/dbmovie_condition'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inisialisasi SQLAlchemy dengan aplikasi
    db.init_app(app)

    return app
