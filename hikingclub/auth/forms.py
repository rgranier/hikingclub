from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from hikingclub.models import Member

#TODO:  Explore error propagation.  Where does the ValidationError go?
# https://wtforms.readthedocs.io/en/stable/validators.html
class RegistrationForm(FlaskForm):
    '''
        Added validators DataRequired(), Email() EqualTo()
    '''
    firstName = StringField('First Name: ')
    lastName = StringField('Last Name: ')
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    # Custom validator
    def checkEmail(self, email):
        # Check if not None for that user email!
        if Member.query.filter_by(email=email).first():
            raise ValidationError('Your email has been registered already!')

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')
