from config import create_app, db
from routes.film_routes import film_bp
from routes.genre_routes import genre_bp
from routes.director_routes import director_bp

# Membuat aplikasi menggunakan create_app
app = create_app()

# Register blueprint
app.register_blueprint(film_bp)
app.register_blueprint(genre_bp)
app.register_blueprint(director_bp)

# Membuat tabel di database jika belum ada
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
