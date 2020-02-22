import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'hikingclub.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.

# NOTE:  1.  Import the blueprints defined in the Views
from hikingclub.registration.views import registration_blueprint
from hikingclub.login.views import login_blueprint
from hikingclub.members.views import members_blueprint
from hikingclub.events.views import events_blueprint
from hikingclub.about.views import about_blueprint

# NOTE:  2. Register the blueprints
app.register_blueprint(registration_blueprint,url_prefix="/registration")
app.register_blueprint(login_blueprint,url_prefix="/login")
app.register_blueprint(events_blueprint,url_prefix="/events")
app.register_blueprint(members_blueprint,url_prefix="/members")
app.register_blueprint(about_blueprint,url_prefix="/about")

# If the templates have the same name, then the first one registered will be
# the one that is found.
#https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
