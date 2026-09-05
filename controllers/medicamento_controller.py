from models.medicamentos import Medicamento
from models import db

def registrar_medicamento(nombre, dosis, hora):
    nuevo_medicamento = Medicamento(medicamento=nombre, dosis=dosis, hora=hora)
    db.session.add(nuevo_medicamento)
    db.session.commit()

def obtener_medicamentos():
    return Medicamento.query.order_by(Medicamento.hora.asc()).all()

def eliminar_medicamento_por_id(id):
    med = Medicamento.query.get_or_404(id)
    db.session.delete(med)
    db.session.commit()

def obtener_medicamento_por_id(id):
    return Medicamento.query.get_or_404(id)

def actualizar_medicamento(id, nombre, dosis, hora):
    med = Medicamento.query.get_or_404(id)
    med.medicamento = nombre
    med.dosis = dosis
    med.hora = hora
    db.session.commit()    