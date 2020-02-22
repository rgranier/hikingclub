from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash
from hikingclub import db
from hikingclub.models import Member
from hikingclub.login.forms import LoginForm
#from hikingclub.owners.forms import AddForm

login_blueprint = Blueprint('login',
                              __name__,
                              template_folder='templates/login')


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    '''
        If entry is found and the password matches, then set status to true, render.
        If entry is found, but passwords don't match, then stays false, render.
        If entry not found, except, status stays as false.
        NOTE:  move the return in once for debug. Create debug code. What are all
        the possible test cases?
    '''

    isloggedin = False
    form = LoginForm()

    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        try:
            member = Member.query.filter_by(email=email).one()
            if password == member.password:
                isloggedin = True

            return render_template('loginstatus.html', isloggedin = isloggedin,
                    email = email, password = password)
        except:
            return render_template('loginstatus.html', isloggedin = isloggedin,
                email = email, password = password)
    else:
        return render_template('login.html', form = form)
