from flask import Blueprint, jsonify, request
from models.rutinas import Rutina
from models import db

rutina_api = Blueprint('rutina_api', __name__)

@rutina_api.route('/api/rutinas', methods=['GET'])
def obtener_rutinas():
    rutinas = Rutina.query.all()
    resultado = []
    for r in rutinas:
        resultado.append({
            'id': r.id,
            'rutina': r.rutina,
            'url': r.url
        })
    return jsonify(resultado)

@rutina_api.route('/api/rutinas', methods=['POST'])
def registrar_rutina():
    data = request.get_json()
    rutina = data.get('rutina')
    url = data.get('url')

    if not rutina or not url:
        return jsonify({'error': 'Faltan datos requeridos'})
    
    nueva_rutina = Rutina(rutina=rutina, url=url)
    db.session.add(nueva_rutina)
    db.session.commit()

    return jsonify({'mensaje': "Rutina registrado exitosamente"})

@rutina_api.route('/api/rutinas/<int:id>', methods=['DELETE'])
def eliminar_rutina(id):
    rutina = Rutina.query.get(id)
    if not rutina:
        return jsonify({'error': 'Rutina no encontrada'})
    db.session.delete(rutina)
    db.session.commit()

    return jsonify({'mensaje': 'Rutina eliminada correctamente'})

@rutina_api.route('/api/rutinas/<int:id>', methods=['PUT'])
def actualizar_rutina(id):
    data = request.get_json()
    rutina = Rutina.query.get(id)

    if not rutina:
        return jsonify({'error': 'Rutina no encontrada'})
    
    if 'rutina' in data:
        rutina.rutina = data['rutina']
    if 'url' in data:
        rutina.url = data['url']
    db.session.commit()

    return jsonify({'mensaje': 'Rutina actualizada correctamente'})