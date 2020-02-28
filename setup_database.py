'''
    This version requires that we do db.create_all() to set up the database
    before we do anything else.  The creation of the account is optional.
    How can we create the db dynamically using Flask-SQLAlchemy?
'''

# Import database info
from hikingclub import db
from hikingclub.models import Member, Event

# Create the tables in the database
# (Usually won't do it this way!)
db.create_all()

member = Member('Test', 'Account', 'foo@bar.com', 'password')
db.session.add(member)
db.session.commit()

event = Event('Hiking in Glacier National Park', 'Kalispel, MT', '11/1/19')
db.session.add(event)
db.session.commit()
