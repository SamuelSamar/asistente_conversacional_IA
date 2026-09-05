from flask import Blueprint, jsonify, request
from models.medicamentos import Medicamento
from datetime import datetime
from models import db

medicamento_api = Blueprint('medicamento_api', __name__)

# === Obtener todos los medicamentos (GET /api/medicamentos) ===
@medicamento_api.route('/api/medicamentos', methods=['GET'])
def obtener_medicamentos():
    medicamentos = Medicamento.query.all() # Obtenemos todos los medicamentos de la base de datos
    resultado = []
    for m in medicamentos:
        # Convertimos cada objeto en un diccionario
        resultado.append({
            'id': m.id,
            'nombre': m.medicamento,
            'dosis': m.dosis,
            'hora': m.hora.strftime("%H:%M") # Convertirmos la hora a texto legible
        })
    return jsonify(resultado) # Devolvemos la lista de medicamentos

# === Crear medicamentos (POST /api/medicamentos) ===
@medicamento_api.route('/api/medicamentos', methods=['POST'])
def registrar_medicamento():
    data = request.get_json() # Obtenemos los datos en formato JSON desde el cuerpo del request
    medicamento = data.get('medicamento') # Extraemos el nombre
    dosis = data.get('dosis') # Extraemos la dosis
    hora_str = data.get('hora') # Extraemos la hora como cadena de texto

    # Validamos que todos los campos estén presentes
    if not medicamento or not dosis or not hora_str:
        return jsonify({'error': 'Faltan datos requeridos'})
    
    # Intentamos convertir la hora a formato datetime
    try:
        hora = datetime.strptime(hora_str, "%H:%M").time()
    except ValueError:
        return jsonify({'error': "Formato de hora inválido. Usa HH:MM"})
    
    # Creamos una nueva instancia del medicamento
    nuevo_medicamento = Medicamento(medicamento=medicamento, dosis=dosis, hora=hora)
    # Lo añadimos a la sesión de la base de datos
    db.session.add(nuevo_medicamento)
    db.session.commit() # Confirmamos los cambios en la base de datos

    return jsonify({"mensaje": "Medicamento registrado exitosamente"})

# === Eliminar un medicamento (DELETE /api/medicamentos/<id>)
@medicamento_api.route('/api/medicamentos/<int:id>', methods=['DELETE'])
def eliminar_medicamento(id):
    medicamento = Medicamento.query.get(id) # Buscamos el medicamento por ID
    if not medicamento:
        return jsonify({'error': 'Medicamento no encontrado'})
    
    db.session.delete(medicamento) # Lo eliminamos
    db.session.commit() # Guardamos los cambios

    return jsonify({'mensaje': 'Medicamento eliminado correctamente'})

# === Actualizar medicamento (PUT /api/medicamentos/<id>)
@medicamento_api.route('/api/medicamentos/<int:id>', methods=['PUT'])
def actualizar_medicamento(id):
    # Obtenemos los datos JSON del cuerpo del request
    data = request.get_json()
    medicamento = Medicamento.query.get(id) # Buscamos el medicamento por ID

    if not medicamento:
        return jsonify({'error': 'Medicamento no encontrado'})
    
    # Si bienen datos los actualizamos
    if 'medicamento' in data:
        medicamento.medicamento = data['medicamento']
    if 'dosis' in data:
        medicamento.dosis = data['dosis']
    if 'hora' in data:
        try:
            medicamento.hora = datetime.strptime(data['hora'], '%H:%M').time()
        except ValueError:
            return jsonify({'error': 'Formato de hora inválido. Usa HH:MM'})
    db.session.commit()

    return jsonify({'mensaje': 'Medicamento actualizado correctamente'})