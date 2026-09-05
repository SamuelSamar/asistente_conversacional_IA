from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class RutinaForm(FlaskForm):
    rutina = StringField('Rutina', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired(), URL()])
    enviar = SubmitField('Agregar')