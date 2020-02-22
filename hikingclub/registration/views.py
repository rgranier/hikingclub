from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash
from hikingclub import db
from hikingclub.models import Member
from hikingclub.registration.forms import RegistrationForm
#from hikingclub.owners.forms import AddForm

registration_blueprint = Blueprint('registration',
                              __name__,
                              template_folder='templates/registration')


@registration_blueprint.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if request.method == 'POST':
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data

        toAdd = Member(firstName, lastName, email, password)
        db.session.add(toAdd)
        db.session.commit()
        return render_template('thankyou.html', toAdd = toAdd)
    else:
        return render_template('register.html', form = form)
