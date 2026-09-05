from models.mensajes import db, Mensaje
from datetime import datetime
# from utils.ia import responder_consulta
from utils.respuestas_predefinidas import responder_predefinido

def procesar_mensaje(mensaje_usuario):
    # respuesta = responder_consulta(mensaje_usuario)
    respuesta = responder_predefinido(mensaje_usuario)
    nuevo_mensaje = Mensaje(
        mensaje_usuario = mensaje_usuario,
        respuesta_bot=respuesta,
        fecha_hora = datetime.utcnow()
    )

    db.session.add(nuevo_mensaje)
    db.session.commit()

    return nuevo_mensaje
        