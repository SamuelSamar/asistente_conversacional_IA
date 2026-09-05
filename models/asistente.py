from models import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Asistente(UserMixin, db.Model):
    __tablename__='asistente'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)
