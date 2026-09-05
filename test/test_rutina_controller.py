import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask import Flask
from models import db
from models.rutinas import Rutina
from controllers.rutina_controller import (
    registrar_rutina,
    obtener_rutinas,
    eliminar_rutina_por_id,
    obtener_rutina_por_id,
    actualizar_rutina,
    transformar_a_embed
)

# === Fixture para crear una app flask temporal con una BD en memoria ===

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria
    app.config['TESTING'] = True  # Modo testing
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app  # Devuelve la app lista para usar en los tests
        db.session.remove()
        db.drop_all()  # Borra todo al terminar el test

# Prueba para registrar una rutina
def test_registrar_rutina(app):
    # Creamos un contexto de aplicación para usar la base de datos con FLask
    with app.app_context():
        # Registramos una rutina usando la función del controlador
        registrar_rutina("Estiramiento", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        # Obtenemos todos las rutinas registradas en la base de datos
        rutinas = obtener_rutinas()
        # Verificamos que se haya agregado solo una rutina
        assert len(rutinas) == 1
        # Verificamos que el nombre de la rutina registrada sea correcto
        assert rutinas[0].rutina == "Estiramiento"

# Prueba para actualizar una rutina existente
def test_actualizar_rutina(app):
    # Creamos un contexto de aplicación para usar la base de datos con FLask
    with app.app_context():
        # Primero registramos una rutina
        registrar_rutina("Cardio", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        # Obtenemos la primera rutina para obtener su ID
        rutina = obtener_rutinas()[0]
        # Usamos ese ID para actualizar la rutina
        actualizar_rutina(rutina.id, "Cardio Avanzado", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        # Lo buscamos de nuevo por ID para verificar los cambios
        actualizado = obtener_rutina_por_id(rutina.id)
        # Verificamos que el nombre y la URL hayan cambiado correctamente
        assert actualizado.rutina == "Cardio Avanzado"
        assert actualizado.url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Prueba para eliminar una rutina existente
def test_eliminar_rutina(app):
    # Creamos un contexto de aplicación para usar la base de datos con FLask
    with app.app_context():
        # Primero registramos una rutina
        registrar_rutina("Yoga", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        # Obtenemos la primera rutina para obtener su ID
        rut = obtener_rutinas()[0]
        # Usamos ese ID para eliminar la rutina
        eliminar_rutina_por_id(rut.id)
        # Verificamos que la rutina ya no exista
        assert obtener_rutinas() == []

# Prueba para transformar URLs a formato embed
def test_transformar_a_embed(app):
    # Creamos un contexto de aplicación para usar la base de datos con FLask
    with app.app_context():
        # Probamos varias URLs de YouTube
        url1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        url2 = "https://youtu.be/dQw4w9WgXcQ"
        # Verificamos que la transformación a embed funcione correctamente
        assert transformar_a_embed(url1) == "https://www.youtube.com/embed/dQw4w9WgXcQ"
        assert transformar_a_embed(url2) == "https://www.youtube.com/embed/dQw4w9WgXcQ"
