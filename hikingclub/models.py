from hikingclub import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
'''
By inheriting the UserMixin we get access to a lot of built-in attributes
which we will be able to call in our views!
is_authenticated(), is_active(), is_anonymous(), get_id()

We will inherit from both db.Model and UserMixin
'''
# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(memberId):
    return Member.query.get(memberId)

class Member(db.Model, UserMixin):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    email = db.Column(db.String(64), unique=True, index=True)
    passwordHash = db.Column(db.String(128))

    def __init__(self, firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.passwordHash, password)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    date = db.Column(db.Text)

    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date

    def __repr__(self):
        return f"Event Name: {self.name}"
