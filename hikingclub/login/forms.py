from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
    email = StringField('Email: ')
    password = StringField('Password: ')
    submit = SubmitField('Login')
