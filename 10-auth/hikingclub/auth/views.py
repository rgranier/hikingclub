import sys
from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from hikingclub import db
from hikingclub.models import Member
from hikingclub.auth.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


auth_blueprint = Blueprint('auth',
                              __name__,
                              template_folder='templates/auth')

@auth_blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('index'))

#TODO: for some reason this form is never valid.
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if request.method == 'POST':
        print("Valid Form on Login Submit: ", form.validate_on_submit(), file=sys.stderr)
        # Grab the user from our User Models table
        member = Member.query.filter_by(email=form.email.data).first()
        print(type(member), file=sys.stderr)

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not
        if member is not None:
            isValid = member.checkPassword(form.password.data)
            print("Password Match: ", isValid, file=sys.stderr)

            #If password matches, log in the user
            if (isValid):
                login_user(member)
                flash('Logged in successfully.')
                # If a user was trying to visit a page that requires a login
                # flask saves that URL as 'next'.  Check if that next exists,
                # otherwise we'll go to the welcome page.
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('auth.welcome')
                return redirect(next)
            else:
                return render_template('login.html', form=form)

        else:
            return render_template('login.html', form=form)

    else:
        print("Valid Form on login GET: ", form.validate_on_submit(), file=sys.stderr)
        return render_template('login.html', form=form)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        print("Valid Form on Register Submit: ", form.validate_on_submit(), file=sys.stderr)
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data

        toAdd = Member(firstName, lastName, email, password)
        db.session.add(toAdd)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
