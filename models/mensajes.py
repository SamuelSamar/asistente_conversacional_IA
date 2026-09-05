from models import db
from datetime import datetime

class Mensaje(db.Model):
    __tablename__ = 'mensajes'

    id = db.Column(db.Integer, primary_key=True)
    mensaje_usuario = db.Column(db.Text, nullable=False)
    respuesta_bot = db.Column(db.Text, nullable=False)
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow)