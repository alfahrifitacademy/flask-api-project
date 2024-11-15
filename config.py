import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Inisialisasi SQLAlchemy tanpa diikat ke aplikasi
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi database menggunakan variabel lingkungan dari Railway
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+mysqlconnector://{os.getenv('MYSQLUSER')}:{os.getenv('MYSQL_ROOT_PASSWORD')}"
        f"@{os.getenv('MYSQLHOST')}:{os.getenv('MYSQLPORT')}/{os.getenv('MYSQLDATABASE')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inisialisasi SQLAlchemy dengan aplikasi
    db.init_app(app)

    return app
