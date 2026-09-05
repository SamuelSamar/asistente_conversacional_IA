from flask import Blueprint, render_template, request, redirect
from controllers.chat_controller import procesar_mensaje
from controllers.clima_controller import obtener_clima
from models.mensajes import Mensaje
from models.mensajes import db
from forms.chat_form import ChatForm
from flask import url_for
from models.medicamentos import Medicamento

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/', methods=['GET', 'POST'])
def chat():
    form = ChatForm()

    if form.validate_on_submit():
        mensaje_usuario = form.mensaje.data
        # Si se pregunta por el clima
        if "clima" in mensaje_usuario.lower():
            datos_clima = obtener_clima()
            if "error" in datos_clima:
                respuesta_bot = "Lo siento, no pude obtener el clima en este momento."
            else:
                respuesta_bot = (
                    f'El clima actual en {datos_clima['ciudad']} es {datos_clima['temperatura']}°C, '
                    f'{datos_clima['descripcion']} y {datos_clima['humedad']}% de humedad.'
                )
            nuevo_mensaje = Mensaje(mensaje_usuario=mensaje_usuario, respuesta_bot=respuesta_bot)
            db.session.add(nuevo_mensaje)
            db.session.commit()
        else:
            procesar_mensaje(mensaje_usuario)
        return redirect(url_for('chat.chat'))
    
    historial = Mensaje.query.order_by(Mensaje.fecha_hora.asc()).all()

    medicamentos = Medicamento.query.all()
    medicamentos_json=[
        {
            "id":m.id,
            "medicamento":m.medicamento,
            "dosis":m.dosis,
            "hora":m.hora.strftime("%H:%M")
        } for m in medicamentos
    ]

    return render_template('chat.html', historial=historial, form=form, medicamentos_json=medicamentos_json)