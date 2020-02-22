from hikingclub import db

class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, first, last, email, password):
        self.firstName = first
        self.lastName = last
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Email: {self.email}"

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
