from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Optional


class FormAgregarTareas(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class FormEditarTareas (FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    actualizar = SubmitField('Actualizar')
# Eliminar por ID
class FormEliminarTarea(FlaskForm):
    id_tarea = IntegerField('ID a eliminar', validators=[Optional()])
    eliminar = SubmitField('Eliminar')
