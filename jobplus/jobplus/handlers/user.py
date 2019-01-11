from flask import Blueprint, render_template, redirect
from flask_login import login_required

user = Blueprint('user', __name__, url_prefix = '/user')

@user.route('/profile', methods = ['GET', 'POST'])
def profile():
    return render_template('index.html')


