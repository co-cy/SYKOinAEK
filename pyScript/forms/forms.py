from wtforms.fields import SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from pyScript.forms.validators import Length, ComplexPassword
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired("Введите почту"), Length(3, 16)])
    password = PasswordField('Пароль', validators=[DataRequired("Введите пароль"), Length(8, 64)])
    # TODO add recaptcha
    # recaptcha = None
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired("Введите почту"), Length(4, 32)])
    password = PasswordField('Пароль', validators=[DataRequired("Введите пароль"), Length(8, 64), ComplexPassword()])
    repeat_password = PasswordField('Повторный пароль', validators=[DataRequired("Введите повторный пароль"), Length(8, 64), ComplexPassword()])
    # TODO add recaptcha
    # recaptcha = None
    submit = SubmitField('Зарегистрироваться')
