import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_migrate import Migrate


# Create a login manager object
login_manager = LoginManager()
app = Flask(__name__)

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'hikingclub.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "login"

''''
NOTE! These imports need to come after you've defined db, otherwise you will
get errors in your models.py files.
NOTE:  1.  Import the blueprints defined in the Views
'''
from hikingclub.auth.views import auth_blueprint
from hikingclub.members.views import members_blueprint
from hikingclub.events.views import events_blueprint
from hikingclub.about.views import about_blueprint


'''
NOTE:  2. Register the blueprints.  This prefix sets the link that is produced.
If the templates have the same name, then the first one registered will be
the one that is found.
https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
'''
app.register_blueprint(auth_blueprint,url_prefix="/auth")
app.register_blueprint(events_blueprint,url_prefix="/events")
app.register_blueprint(members_blueprint,url_prefix="/members")
app.register_blueprint(about_blueprint,url_prefix="/about")
