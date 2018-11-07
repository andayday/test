from flask import Blueprint, render_template
from simpledu.models import User

user = Blueprint('user', __name__, url_prefix = '/users')

@user.route('/<username>')
def index(username):
    userinfo = User.query.filter_by(username = username).first()
    return render_template('user.html', userinfo = userinfo)


