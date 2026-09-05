from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ChatForm(FlaskForm):
    mensaje = StringField('Mensaje', validators=[DataRequired(), Length(min=1, max=500)],
                          render_kw={"placeholder":"Escribe tu mensaje..."}
    )
    enviar = SubmitField('Enviar')