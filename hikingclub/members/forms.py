from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MemberAddForm(FlaskForm):
    firstName = StringField('First Name: ')
    lastName = StringField('Last Name: ')
    email = StringField('Email: ')
    password = StringField('Password: ')
    submit = SubmitField('Add Member')

class MemberEditForm(FlaskForm):
    firstName = StringField('First Name: ')
    lastName = StringField('Last Name: ')
    email = StringField('Email: ')
    password = StringField('Password: ')
    submit = SubmitField('Edit')
