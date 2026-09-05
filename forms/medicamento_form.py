from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SubmitField
from wtforms.validators import DataRequired

class MedicamentoForm(FlaskForm):
    medicamento = StringField('Medicamento', validators=[DataRequired()])
    dosis = StringField('Dosis', validators=[DataRequired()])
    hora = TimeField('Hora', validators=[DataRequired()])
    enviar = SubmitField('Agregar')
