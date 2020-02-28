from flask import Blueprint, render_template, redirect, url_for
from hikingclub import db
from hikingclub.models import Event


events_blueprint = Blueprint('events',
                              __name__,
                              template_folder='templates/events')

# https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
# You must call directory/file.html
@events_blueprint.route('/')
def list():
    eventList = db.session.query(Event)
    return render_template('eventlist.html', eventList = eventList)
