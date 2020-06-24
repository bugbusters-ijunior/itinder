from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])

class CadastroForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    nome = StringField('nome', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])