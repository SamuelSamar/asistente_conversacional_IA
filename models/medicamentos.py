from models import db
from datetime import time

class Medicamento(db.Model):
    __tablename__='medicamentos'
    id = db.Column(db.Integer, primary_key=True)
    medicamento = db.Column(db.String(100), nullable=False)
    dosis = db.Column(db.String(50), nullable=False)
    hora = db.Column(db.Time, nullable=False)