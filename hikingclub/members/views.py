from flask import Blueprint, request, render_template, redirect, url_for
from hikingclub import db
from hikingclub.models import Member
from hikingclub.members.forms import MemberAddForm, MemberEditForm

members_blueprint = Blueprint('members',
                              __name__,
                              template_folder='templates/members')


# https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
# You must call directory/file.html
@members_blueprint.route('/')
def list():
    memberList = db.session.query(Member)
    return render_template('memberlist.html', memberList = memberList)

# TODO:  Change the forms so that it's clear that it's an admin forms
# and not a registration form.
@members_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = MemberAddForm()
    if request.method == 'POST':
        first = form.firstName.data
        last = form.lastName.data
        email = form.email.data
        password = form.password.data

        toAdd = Member(first, last, email, password)
        db.session.add(toAdd)
        db.session.commit()
        return redirect(url_for('members.list'))
    else:
        return render_template('memberadd.html', form = form)

@members_blueprint.route('/<int:memberId>/edit', methods=['GET', 'POST'])
def edit(memberId):

    # Pass in the toEdit object with the form.
    toEdit = Member.query.get(memberId)
    form = MemberEditForm(obj=toEdit)

    if request.method == 'POST':
        if form.firstName.data:
            toEdit.firstName = form.firstName.data
        if form.lastName.data:
            toEdit.lastName = form.lastName.data
        if form.email.data:
            toEdit.email = form.email.data
        if form.password.data:
            toEdit.password = form.password.data

        db.session.add(toEdit)
        db.session.commit()

        return redirect(url_for('members.list'))
    else:
        return render_template('memberedit.html', form = form, member = toEdit)

# Same deal as edit where we need the object from the DB to display in the form.
@members_blueprint.route('/<int:memberId>/delete', methods=['GET', 'POST'])
def delete(memberId):
    toDelete = Member.query.get(memberId)

    if request.method == 'POST':
        db.session.delete(toDelete)
        db.session.commit()
        return redirect(url_for('members.list'))
    else:
        return render_template('memberdelete.html', member = toDelete)
