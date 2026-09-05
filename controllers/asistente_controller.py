from models.asistente import Asistente, db
from werkzeug.security import generate_password_hash, check_password_hash

def registrar_asistente(nombre, correo, contrasena):
    hashed = generate_password_hash(contrasena, method='pbkdf2:sha256', salt_length=16)
    nuevo_asistente = Asistente(nombre=nombre, correo=correo, contrasena=hashed)
    db.session.add(nuevo_asistente)
    db.session.commit()

def verificar_credenciales(correo, contrasena):
    asistente = Asistente.query.filter_by(correo=correo).first()
    print("Asistente:", asistente)
    if asistente:
        print("Hash guardado:", asistente.contrasena)
        print("Contraseña ingresada:", contrasena)
        print("Verifica:", check_password_hash(asistente.contrasena, contrasena))
    if asistente and check_password_hash(asistente.contrasena, contrasena):
        return asistente
    return None