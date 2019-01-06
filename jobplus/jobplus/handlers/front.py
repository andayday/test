from flask import Blueprint, render_template, redirect, url_for
from jobplus.forms import LoginFrom, RegisterForm
from jobplus.models import User
from flask_login import login_user


front = Blueprint('front', __name__, url_prefix = '/')

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		login_user(user, form.remember_me.data)
		next = 'user.profile'
		if user.is_admin:
			next = 'admin.index'	
		else user.is_company:
			next = 'company.profile'
		return redirect(url_for(next))
	return render_template('login.html', form = form)

@front.route('/userregister', methods = ['GET', 'POST'])
def userregister():
	form = RegisterForm()
	if form.validate_on_submit():
		form.create_user()
		flash('register, success!','success')
		return redirect(url_for('.login'))
	return render_template('userregister.html', form = form)

@front.route('/companyregister', methods = ['GET', 'POST'])
	form = RegisterForm()
	form.name.label = u'company label'
	if form.validate_on_submit():
		company_user = form.create_user()
		company_user.role = User.ROLE_COMPANY
		db.session.add(company_user)
		db.session.commit()
		flash('register success, please login in', 'success')
		return redirect(url_for('.login'))

	return render_template('companyregister.html', form = form)
	

