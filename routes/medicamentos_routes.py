from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms.medicamento_form import MedicamentoForm
from controllers.medicamento_controller import(
    registrar_medicamento,
    obtener_medicamentos, 
    obtener_medicamento_por_id,
    eliminar_medicamento_por_id,
    actualizar_medicamento
)

med_bp = Blueprint('medicamentos', __name__, url_prefix='/medicamentos')

@med_bp.route('/', methods=['GET', 'POST'])
def lista_medicamentos():
    form = MedicamentoForm()
    if form.validate_on_submit():
        registrar_medicamento(
            nombre=form.medicamento.data,
            dosis=form.dosis.data,
            hora=form.hora.data
        )
        flash('¡Recordatorio de medicamento registrado con éxito!', 'success')
        return redirect(url_for('medicamentos.lista_medicamentos'))
    
    medicamentos = obtener_medicamentos()
    return render_template('medicamentos.html', form=form, medicamentos=medicamentos)

@med_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_medicamento(id):
    eliminar_medicamento_por_id(id)
    return redirect(url_for('medicamentos.lista_medicamentos'))

@med_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_medicamento(id):
    med = obtener_medicamento_por_id(id)
    form = MedicamentoForm(obj=med)
    if form.validate_on_submit():
        actualizar_medicamento(
            id=med.id,
            nombre=form.medicamento.data,
            dosis=form.dosis.data,
            hora=form.hora.data
        )
        return redirect(url_for('medicamentos.lista_medicamentos'))
    return render_template('editar_medicamento.html', form=form, id=med.id)