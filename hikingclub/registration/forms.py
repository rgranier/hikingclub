from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#TODO:  Should we create a delete form for consistancy?
class RegistrationForm(FlaskForm):
    firstName = StringField('First Name: ')
    lastName = StringField('Last Name: ')
    email = StringField('Email: ')
    password = StringField('Password: ')
    submit = SubmitField('Register')
