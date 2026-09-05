from models import db

class Rutina(db.Model):
    __tablename__ = 'rutinas'
    id = db.Column(db.Integer, primary_key=True)
    rutina = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)