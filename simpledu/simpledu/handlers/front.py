from flask import flash, redirect, url_for, request, current_app
from flask import Blueprint, render_template
from simpledu.models import Course
from simpledu.models import User
from simpledu.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
    page = request.args.get('page', default = 1, type = int)
    pagination = Course.query.paginate(
            page = page,
            per_page = current_app.config['INDEX_PER_PAGE'],
            error_out = False,
            )
    return render_template('index.html', pagination = pagination)

@front.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html', form = form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have logout', 'success')
    return redirect(url_for('.index'))

@front.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('register success', 'success')
        return redirect(url_for('.login'))

    return render_template('register.html', form = form)
