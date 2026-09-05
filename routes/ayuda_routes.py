from flask import Blueprint, redirect, flash, url_for
from controllers.ayuda_controller import solicitar_ayuda

ayuda_bp = Blueprint('ayuda', __name__, url_prefix='/ayuda')

@ayuda_bp.route('/enviar', methods=['POST'])
def ruta_ayuda():
    try:
        solicitar_ayuda()
        flash('Se envió el mensaje de ayuda al encargado.', 'success')
    except Exception as e:
        flash(f'Error al enviar el mensaje: {str(e)}', 'danger')
    return redirect(url_for('chat.chat', nohablar=1))