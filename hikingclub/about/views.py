from flask import Blueprint,render_template,redirect,url_for

about_blueprint = Blueprint('about',
                              __name__,
                              template_folder='templates/about')


@about_blueprint.route('/about')
def about():
    return render_template('about.html')
