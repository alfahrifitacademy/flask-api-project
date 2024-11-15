from config import db

class Film(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'director_id': self.director_id,
            'genre_id': self.genre_id
        }

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
