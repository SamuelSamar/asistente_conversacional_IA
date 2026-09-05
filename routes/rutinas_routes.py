from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms.rutina_form import RutinaForm
from controllers.rutina_controller import(
    registrar_rutina,
    obtener_rutina_por_id,
    obtener_rutinas,
    eliminar_rutina_por_id,
    actualizar_rutina
)

rut_bp = Blueprint('rutinas', __name__, url_prefix='/rutinas')

@rut_bp.route('/', methods=['GET', 'POST'])
def lista_rutinas():
    form = RutinaForm()
    if form.validate_on_submit():
        registrar_rutina(
            nombre=form.rutina.data,
            url=form.url.data
        )
        flash('¡Rutina recreativa registrada con éxito!', 'success')
        return redirect(url_for('rutinas.lista_rutinas'))
    
    rutinas = obtener_rutinas()
    return render_template('rutinas.html', form=form, rutinas=rutinas)

@rut_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_rutina(id):
    eliminar_rutina_por_id(id)
    return redirect(url_for('rutinas.lista_rutinas'))

@rut_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_rutina(id):
    rut = obtener_rutina_por_id(id)
    form = RutinaForm(obj=rut)
    if form.validate_on_submit():
        actualizar_rutina(
            id=rut.id,
            nombre=form.rutina.data,
            url=form.url.data
        )
        return redirect(url_for('rutinas.lista_rutinas'))
    return render_template('editar_rutina.html', form=form, id=rut.id)