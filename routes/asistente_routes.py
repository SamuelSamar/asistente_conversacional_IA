from flask import Blueprint, render_template, redirect, request, session, url_for, flash
from forms.auth_forms import RegistroForm, LoginForm
from controllers.asistente_controller import registrar_asistente, verificar_credenciales
from models.asistente import Asistente
from flask_login import login_user, logout_user, login_required

asistente_bp = Blueprint('asistentes', __name__, url_prefix='/asistentes')
from models import db

@asistente_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        registrar_asistente(
            nombre=form.nombre.data,
            correo=form.correo.data,
            contrasena=form.contrasena.data
        )
        flash('Registro exitoso.', 'success')
        return redirect(url_for('asistentes.login'))
    else:
        print(form.errors)
    return render_template('registro.html', form=form)

@asistente_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        asistente = verificar_credenciales(
            form.correo.data,
            form.contrasena.data
        )
        if asistente:
            login_user(asistente)
            return redirect(url_for('chat.chat'))
        flash('Credenciales inválidas')
    return render_template('login.html', form=form)

@asistente_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('asistentes.login'))