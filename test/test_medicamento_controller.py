import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import time
from flask import Flask
from models import db
from models.medicamentos import Medicamento
from controllers.medicamento_controller import (
    registrar_medicamento,
    obtener_medicamentos,
    eliminar_medicamento_por_id,
    obtener_medicamento_por_id,
    actualizar_medicamento
)

# === Fixture para crear una app flask temporal con una BD en memoria ===

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Base de datos en memoria
    app.config['TESTING'] = True # Modo testing
    db.init_app(app)

    with app.app_context():
        db.create_all() # Crea tablas
        yield app # Devuelve la app lista para usar en los tests
        db.session.remove()
        db.drop_all() # Borra todo al terminar el test

# Prueba para registrar un medicamento
def test_registrar_medicamento(app):
    # Creamos un contexto de aplicación para usar la base de datos con FLask
    with app.app_context():
        # Registramos un medicamento usando la función del controlador
        registrar_medicamento("Paracetamol", "500mg", time(8,0))
        # Obtenemos todos los medicamentos registrados en la base de datos
        medicamentos = obtener_medicamentos()
        # Verificamos que se haya agregado solo un medicamento
        assert len(medicamentos) == 1
        # Verificamos que el nombre del medicamento registrado sea correcto
        assert medicamentos[0].medicamento == "Aspirina"

# Prueba para actualizar un medicamento existente
def test_actualizar_medicamento(app):
    with app.app_context():
        # Primero registramos un medicamento
        registrar_medicamento("Ibuprofeno", "200mg", time(9,0))
        # Obtenemos el primer medicamento para obtener su ID
        medicamento = obtener_medicamentos()[0]
        # Usamos ese ID para actualizar el medicamento
        actualizar_medicamento(medicamento.id, "Ibuprofeno", "400mg", time(10,0))
        # Lo buscamos de nuevo por ID para verificar los cambios
        actualizado = obtener_medicamento_por_id(medicamento.id)
        # Verificamos que la dosis haya cambiado correctamente
        assert actualizado.dosis == "400mg"
        # Verificamos que la hora tmabién haya cambiado
        assert actualizado.hora == time(10, 0)

# Prueba para eliminar un medicamento existente
def test_eliminar_medicamento(app):
    with app.app_context():
        # Registramos un medicamento
        registrar_medicamento("Amoxicilina", "250mg", time(12,0))
        # Obtenemos el prime medicamento recién creado
        med = obtener_medicamentos()[0]
        # Lo eliminamos usando su ID
        eliminar_medicamento_por_id(med.id)
        # Verificamos que la lista de medicamentos esté vacía
        assert obtener_medicamentos() == []