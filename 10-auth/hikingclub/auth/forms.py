from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    firstName = StringField('First Name: ')
    lastName = StringField('Last Name: ')
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    def checkEmail(self, field):
        # Check if not None for that user email!
        if Member.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')


'''
class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = StringField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')
'''

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired()])
    password = StringField('Password: ')
    submit = SubmitField('Login')
